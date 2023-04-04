var track = [[1,true],[2,false]];
var order = 0;

// body onload get all routes from database
getRoutes = () => {
  console.log("getRoutes");
  axios
    .get("http://localhost:5000/get_tracks")
    .then(function (response) {
      console.log(response.data);
      // populate the table with the routes
      let routes = document.getElementById("routes");
      for (let i = 0; i < response.data.length; i++) {
        let route = response.data[i];
        let row = document.createElement("tr");
        let name = document.createElement("td");
        let description = document.createElement("td");
        let select = document.createElement("td");

        let deleteRoute = document.createElement("td");
        name.innerHTML = route.track;
        description.innerHTML = route.description;
        select.innerHTML =
          '<button class="btn btn-primary">Selecionar</button>';
        deleteRoute.innerHTML =
          '<button class="btn btn-primary">Excluir</button>';
        row.appendChild(name);
        row.appendChild(description);
        row.appendChild(select);
        row.appendChild(deleteRoute);
        routes.appendChild(row);
      }
    })
    .catch(function (error) {
      console.log(error);
    });
};

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
  axios
    .get("http://localhost:5000/add_position_dobot")
    .then(function (response) {
      // apeend into track response and order
      track.push(response.x, response.y, response.z, response.r, order, magnetStatus());
      order++;
      console.log(track);
    }
    )
    .catch(function (error) {
      console.log(error);
    }
    );
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
  // make trackPost a json with the "data:" object
  return trackPost
}

function sendPostRoute(){
  axios
    .post("http://localhost:5000/add_track", mkArray())
    .then(function (response) {
      console.log(response.data);
    })
    .catch(function (error) {
      console.log(error);
    });
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

// {"data": [array]}