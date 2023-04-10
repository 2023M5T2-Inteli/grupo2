// Variáveis globais
var track = []; // Tupla que salva as tracks do banco de dados 
var order = 0; // Variável que salva a ordem das posições da track atual

// ----------------- Funções de interface e manipulação de objetos -----------------

// Função para facilitar a criação de toasts, com os parâmetros msg, time e type
// msg: mensagem a ser exibida
// time: tempo que o toast deve ficar visível
// type: tipo do toast, pode ser "good" ou "bad", o que altera sua cor
function toastShowFade(msg, time, type) {
  if (type == "good") {
    $('.toast').removeClass("toastBgBad");
    $('.toast').addClass("toastBgGood");
  } else if (type == "bad") {
    $('.toast').removeClass("toastBgGood");
    $('.toast').addClass("toastBgBad");
  }
  $("#toastText").text(msg);
  $('.toast').toast('show');
  if (time != 0)
    setTimeout(function() {
      $('.toast').toast('hide');
    }, time);
}

// Função que muda o status do imã quando o respectivo botão é clicado
function magnetRecordChange(){
  const magnetButtonRecord = document.getElementById("magnetButtonRecord");
  if (magnetButtonRecord.innerHTML == "Imã Ligado") {
    magnetButtonRecord.innerHTML = "Imã Desligado";
    magnetButtonRecord.classList.remove("greenbg");
    magnetButtonRecord.classList.add("redbg");
  }
  else{
    magnetButtonRecord.innerHTML = "Imã Ligado";
    magnetButtonRecord.classList.remove("redbg");
    magnetButtonRecord.classList.add("greenbg");
  }
}

// Função que retorna o status do imã, quando é chamado pela função addNodePost()
function magnetStatus(){
  const magnetButtonRecord = document.getElementById("magnetButtonRecord");
  if (magnetButtonRecord.innerHTML == "Imã Ligado") {
    return true;
  }
  else{
    return false;
  }
}

// Função que retora o número de ciclos da track da tabela que foi selecionada, quando é chamada pela função selectRoute()
function getCycles(track){
  let cycles = document.getElementById(`cycles${track}`).value;
  // Prefere o valor do input, mas se for inválido, retorna 1 ou 10, dependendo do caso
  if (cycles == 0){ // 1 é o mínimo permitido
    cycles = 1;
    document.getElementById(`cycles${track}`).value = 1;
    toastShowFade("O número de ciclos foi alterado para 1 (mínimo permitido)", 2000, "bad");
  }
  else if (cycles > 10){ // 10 é o máximo permitido, o que é suficiente para a maioria dos casos
    cycles = 10;
    document.getElementById(`cycles${track}`).value = 10;
    toastShowFade("O número de ciclos foi alterado para 10 (máximo permitido)", 2000, "bad");
  }
  return cycles;
}

// Função que adiciona o nome da track no array track, cria um objeto json e retorna ele, quando chamado pela função sendPostTrack()
function mkJSON(){
  for(let i = 0; i < track.length; i++){
    // Adiciona o nome da track no array track
    const name = document.getElementById("trackName").value;
    track[i].push(name);
  }
  // console.log(track);
  let trackPost = {"data": track} 
  // Limpa o array track e a variável order para receber novos inputs de posição
  order = 0
  track = []
  // console.log(trackPost)
  return trackPost
}

// ----------------- Funções HTTP request -----------------

// Quando a página é carregada, chama a função getTracks que popula a tabela com as tracks
getTracks = () => {
  axios
    .get("http://localhost:5000/get_tracks") // Requisição GET para o servidor
    .then(function (response) {
      // console.log(response.data);
      let tracksTable = document.getElementById("tracksTable");
      // Cria os elementos da tabela para cada track
      for (let i = 0; i < response.data.length; i++) {
        let row = document.createElement("tr");
        row.classList.add("text-center", "justify-content-center");
        row.id = response.data[i];
        let name = document.createElement("td");
        name.classList.add("text-center");
        let select = document.createElement("td");
        let cycles = document.createElement("td");
        let deleteRoute = document.createElement("td");
        let trackName = response.data[i];
        name.innerHTML = trackName;
        select.innerHTML = `<button class="btn btn-primary" onclick="selectRoute('${trackName}')">Selecionar</button>`;
        cycles.innerHTML = `<input type="number" id="cycles${trackName}" class="w-50 cyclesInput" name="cycles" min="1" max="10" value="1">`;
        deleteRoute.innerHTML = `<button class="btn btn-danger" onclick="deleteRoute('${trackName}')">Deletar</button>`;
        // Utiliza o método appendChild para adicionar os elementos na tabela
        row.appendChild(name);
        row.appendChild(select);
        row.appendChild(cycles);
        row.appendChild(deleteRoute);
        tracksTable.appendChild(row);
      }
    })
    .catch(function (error) {
      // console.log(error);
    });
};

// Função que retorna o robô à posição inicial, e para isso acessa a rota /home do servidor
function goToHome() {
  let xhttp = new XMLHttpRequest();
  xhttp.open("GET", "http://localhost:5000/home", true);
  xhttp.send();
  xhttp.onreadystatechange = function() {
    if (this.readyState == 4 && this.status == 200) {
      toastShowFade("Retornado à posição incial!", 2000, "good");
    }
  }
}

// Pega a posição atual do robô e insere no array track
function addNodePost(){
  toastShowFade("Adicionando posição, por favor aguarde...", 0, "good");
  let xhttp = new XMLHttpRequest();
  xhttp.open("GET", "http://localhost:5000/add_position_dobot", true); // Requisição que pega a posição atual do robô
  xhttp.send();
  xhttp.onreadystatechange = function() {
    if (this.readyState == 4 && this.status == 200) {
      let response = JSON.parse(this.responseText);
      track.push([response.j1, response.j2, response.j3, response.j4, order, magnetStatus()]); // Adiciona a posição atual do robô, sua ordem e o status do imã no array track
      order++;
      // console.log(track);
      toastShowFade("Posição adicionada com sucesso!", 1000, "good");
    }
    // Se falhar ao adicionar a posição, mostra um toast com a mensagem de erro
    else if (this.readyState == 4 && this.status != 200){
      toastShowFade("Erro ao adicionar posição!", 1000, "bad");
    }
  }
}

// Após todos os pontos serem adicionados, envia o JSON de tracks para o servidor
function sendPostTrack(){
  // Verifica se há posições para adicionar à rota
  if (track.length == 0){
    toastShowFade("Não há posições para adicionar à rota!", 1000, "bad");
    return;
  }
  // Verifica se o nome da rota não está vazio
  else if (document.getElementById("trackName").value == ""){
    toastShowFade("O nome da rota não pode ser vazio!", 1000, "bad");
    return;
  }
  let xhttp = new XMLHttpRequest();
  xhttp.open("POST", "http://localhost:5000/add_track", true);
  xhttp.setRequestHeader("Content-type", "application/json");
  xhttp.send(JSON.stringify(mkJSON()));
  xhttp.onreadystatechange = function() {
    if (this.readyState == 4 && this.status == 200) {
      // console.log(this.responseText);
      toastShowFade("Rota adicionada com sucesso!", 1000, "good");
      window.location.reload(); // Recarrega a página para atualizar a tabela
    }
  }
}

// Função que envia a rota selecionada na tabela para o servidor, para que seja executada pelo robô
function selectRoute(track){ // O parâmetro track é enviado diretamente do frontend
  let xhttp = new XMLHttpRequest();
  xhttp.open("POST", "http://localhost:5000/run_track", true);
  xhttp.setRequestHeader("Content-type", "application/json");
  xhttp.send(JSON.stringify({"track": track, "cycles": getCycles(track)})); // Envia o nome da rota e o número de ciclos
  // console.log(JSON.stringify({"track": track, "cycles": getCycles(track)}));
  xhttp.onreadystatechange = function() {
    if (this.readyState == 4 && this.status == 200) {
      toastShowFade(`Rota executada com o tempo de ${this.responseText}'s`, 2000, "good");
      // console.log(this.responseText);
    }
  };
}

// Função que deleta a rota selecionada na tabela do banco de dados
function deleteRoute(track){
  let xhttp = new XMLHttpRequest();
  xhttp.open("DELETE", "http://localhost:5000/delete_track", true);
  xhttp.setRequestHeader("Content-type", "application/json");
  xhttp.send(JSON.stringify({"track": track}));
  xhttp.onreadystatechange = function() {
    if (this.readyState == 4 && this.status == 200) {
      let tracksTable = document.getElementById("tracksTable");
      // Deleta no front end a rota selecionada
      for (let i = 0; i < tracksTable.rows.length; i++) {
        if (tracksTable.rows[i].id == track){
          tracksTable.deleteRow(i);
        }
      }
    }
  };
}

// Todos os console.log() foram comentados, mas podem ser descomentados para debugar o código