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
        row.id = response.data[i];
        let name = document.createElement("td");
        let select = document.createElement("td");
        let cycles = document.createElement("td");
        cycles.classList.add("d-flex", "justify-content-center");
        let deleteRoute = document.createElement("td");
        let trackName = response.data[i];
        name.innerHTML = trackName;
        select.innerHTML = `<button class="btn btn-primary" onclick="selectRoute('${trackName}')">Selecionar</button>`;
        // select numbers of cycles
        cycles.innerHTML = `<input type="number" id="cycles${trackName}" class="form-control w-50" name="cycles" min="1" max="10" value="1">`;
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

function magnetRecord(){
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
  $("#toastText").text("Adicionando posição, por favor aguarde...");
  $('.toast').toast('show');
  let xhttp = new XMLHttpRequest();
  xhttp.open("GET", "http://localhost:5000/add_position_dobot2", true);
  xhttp.send();
  xhttp.onreadystatechange = function() {
    if (this.readyState == 4 && this.status == 200) {
      let response = JSON.parse(this.responseText);
      track.push([response.x, response.y, response.z, response.r, order, magnetStatus()]);
      order++;
      console.log(track);
      $("#toastText").text("Posição adicionada com sucesso!");
      // fade out toast
      setTimeout(function() {
        $('.toast').toast('hide');
      }, 1000);
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

function sendPostRoute(){
  let xhttp = new XMLHttpRequest();
  xhttp.open("POST", "http://localhost:5000/add_track", true);
  xhttp.setRequestHeader("Content-type", "application/json");
  xhttp.send(JSON.stringify(mkArray()));
  xhttp.onreadystatechange = function() {
    if (this.readyState == 4 && this.status == 200) {
      console.log(this.responseText);
    }
  }
}

function getCycles(track){
  let cycles = document.getElementById(`cycles${track}`).value;
  if (cycles == 0){
    cycles = 1;
    document.getElementById("cycles").value = 1;
    alert("O número de ciclos foi alterado para 1 (mínimo permitido)")
  }
  else if (cycles > 10){
    cycles = 10;
    document.getElementById("cycles").value = 10;
    alert("O número de ciclos foi alterado para 10 (máximo permitido)")
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

async function postRotaPadrao(test) {
  axios
    .post("http://localhost:5000/robot", test)
    .then(function (response) {
      console.log("It says: " + response.data);
    })
    .catch(function (error) {
      console.log(error);
    });
}

// Função que altera o botão de ligar/desligar imã e envia o comando para o raspberry
// function magnetonoff() {
//   const magnetButton = document.getElementById("magnetButton");
//   if (magnetButton.innerHTML == "Ligar Imã") {
//     magnetButton.innerHTML = "Desligar Imã";
//     axios.get("http://localhost:5000/magnet_on").then(function (response) {
//       console.log(response.data);
//     });
//   } else {
//     magnetButton.innerHTML = "Ligar Imã";
//     axios.get("http://localhost:5000/magnet_off").then(function (response) {
//       console.log(response.data);
//     });
//   }
// }

// {"data": [array]}