var track = []; // Tupla que salva as tracks do banco de dados
var order = 0; // Variável que salva a ordem das posições

// Quando a página é carregada, chama a função getTracks que popula a tabela com as tracks
getTracks = () => {
  axios
    .get("http://localhost:5000/get_tracks")
    .then(function (response) {
      console.log(response.data);
      let tracksTable = document.getElementById("tracksTable");
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
        // select numbers of cycles
        cycles.innerHTML = `<input type="number" id="cycles${trackName}" class="w-50 cyclesInput" name="cycles" min="1" max="10" value="1">`;
        deleteRoute.innerHTML = `<button class="btn btn-danger" onclick="deleteRoute('${trackName}')">Deletar</button>`;
        row.appendChild(name);
        row.appendChild(select);
        row.appendChild(cycles);
        row.appendChild(deleteRoute);
        tracksTable.appendChild(row);
      }
    })
    .catch(function (error) {
      console.log(error);
    });
};

function toastShowFade(msg, time, type) {
  // add class to toast
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

// Função que retorna o status do imã
function magnetStatus(){
  const magnetButtonRecord = document.getElementById("magnetButtonRecord");
  if (magnetButtonRecord.innerHTML == "Imã Ligado") {
    return true;
  }
  else{
    return false;
  }
}

// Pega a posição atual do robô e insere no array track
function addNodePost(){
  // toast notification
  toastShowFade("Adicionando posição, por favor aguarde...", 0, "good");
  let xhttp = new XMLHttpRequest();
  xhttp.open("GET", "http://localhost:5000/add_position_dobot2", true);
  xhttp.send();
  xhttp.onreadystatechange = function() {
    if (this.readyState == 4 && this.status == 200) {
      let response = JSON.parse(this.responseText);
      track.push([response.j1, response.j2, response.j3, response.j4, order, magnetStatus()]);
      order++;
      console.log(track);
      toastShowFade("Posição adicionada com sucesso!", 1000, "good");
    }
    // if error show toast
    else if (this.readyState == 4 && this.status != 200){
      toastShowFade("Erro ao adicionar posição!", 1000, "bad");
    }
  }
}

function mkArray(){
  for(let i = 0; i < track.length; i++){
    // add name in track for each position
    const name = document.getElementById("trackName").value;
    track[i].push(name);
  }
  console.log(track);
  let trackPost = {"data": track}
  order = 0
  track = []
  console.log(trackPost)
  // make trackPost a json with the "data:" object
  return trackPost
}

function sendPostTrack(){
  if (track.length == 0){
    // alert("Não há posições para adicionar à rota!"); toast
    toastShowFade("Não há posições para adicionar à rota!", 1000, "bad");
    return;
  }
  else if (document.getElementById("trackName").value == ""){
    // alert("O nome da rota não pode ser vazio!"); toast 
    toastShowFade("O nome da rota não pode ser vazio!", 1000, "bad");
    return;
  }
  let xhttp = new XMLHttpRequest();
  xhttp.open("POST", "http://localhost:5000/add_track", true);
  xhttp.setRequestHeader("Content-type", "application/json");
  xhttp.send(JSON.stringify(mkArray()));
  xhttp.onreadystatechange = function() {
    if (this.readyState == 4 && this.status == 200) {
      console.log(this.responseText);
      toastShowFade("Rota adicionada com sucesso!", 1000, "good");
      // reload window
      window.location.reload();
    }
  }
}

function getCycles(track){
  let cycles = document.getElementById(`cycles${track}`).value;
  if (cycles == 0){
    cycles = 1;
    document.getElementById(`cycles${track}`).value = 1;
    toastShowFade("O número de ciclos foi alterado para 1 (mínimo permitido)", 2000, "bad");
  }
  else if (cycles > 10){
    cycles = 10;
    document.getElementById(`cycles${track}`).value = 10;
    toastShowFade("O número de ciclos foi alterado para 10 (máximo permitido)", 2000, "bad");
  }
  return cycles;
}

function selectRoute(track){
  let xhttp = new XMLHttpRequest();
  xhttp.open("POST", "http://localhost:5000/run_track", true);
  xhttp.setRequestHeader("Content-type", "application/json");
  xhttp.send(JSON.stringify({"track": track, "cycles": getCycles(track)}));
  console.log(JSON.stringify({"track": track, "cycles": getCycles(track)}));
  xhttp.onreadystatechange = function() {
    if (this.readyState == 4 && this.status == 200) {
      // toast 
      toastShowFade(`Rota executada com o tempo de ${this.responseText}'s`, 2000, "good");
      console.log(this.responseText);
    }
  };
}

function deleteRoute(track){
  let xhttp = new XMLHttpRequest();
  xhttp.open("DELETE", "http://localhost:5000/delete_track", true);
  xhttp.setRequestHeader("Content-type", "application/json");
  xhttp.send(JSON.stringify({"track": track}));
  xhttp.onreadystatechange = function() {
    if (this.readyState == 4 && this.status == 200) {
      let tracksTable = document.getElementById("tracksTable");
      // delete rows with the track name 
      for (let i = 0; i < tracksTable.rows.length; i++) {
        if (tracksTable.rows[i].id == track){
          tracksTable.deleteRow(i);
        }
      }
    }
  };
}
