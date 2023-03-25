
    // body onload get all routes from database
    getRoutes = () => {
        console.log("getRoutes")
        axios.get('http://localhost:5000/robot/getroutes')
        .then(function (response) {
            console.log(response.data);
            // populate the table with the routes
            let routes = document.getElementById('routes');
            for (let i = 0; i < response.data.length; i++) {
                let route = response.data[i];
                let row = document.createElement('tr');
                let name = document.createElement('td');
                let description = document.createElement('td');
                let select = document.createElement('td');

                let deleteRoute = document.createElement('td');
                name.innerHTML = route.name;
                description.innerHTML = route.description;
                select.innerHTML = '<button class="btn btn-primary">Selecionar</button>';
                deleteRoute.innerHTML = '<button class="btn btn-primary">Excluir</button>';
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
    }

    // Função que altera o botão de ligar/desligar imã e envia o comando para o raspberry
    function magnetonoff(){
        const magnetButton = document.getElementById('magnetButton');
        if(magnetButton.innerHTML == "Ligar Imã"){
            magnetButton.innerHTML = "Desligar Imã";
            axios.get("http://localhost:5000/magnet_on").then(function (response) {
                console.log(response.data);
            })

        }else{
            magnetButton.innerHTML = "Ligar Imã";
            axios.get("http://localhost:5000/magnet_off").then(function (response) {
                console.log(response.data);
            })
        }
    }


    async function makePostRequest(test) {
    axios.post('http://localhost:5000/robot', test)
    .then(function (response) {
    console.log("It says: " + response.data);
    })
    .catch(function (error) {
    console.log(error);
    });
    }
