// Aqui estão as funções que spawnam processos python para fazer o setup do programa.
// Todas as funções devem ser executadas sem erros para que a interface gráfica abra.
// cada um dos scripts python está nessa mesma pasta
const { spawn } = require("child_process");

// Spawna o processo responsável por instalar
// todas as bibliotecas python necessárias no computador do usuário
const py_installLibs = () => {

  // Criamos promisses para possibilitar o sincronismo necessário para o setup:
  // as libs tem que ser instaladas antes de executar o servidor e assim por diante 
  return new Promise((resolve, reject) => {
    // Inicia o processo python
    const pythonProcess = spawn("python", ["./startup/install_libs.py"]);

    // Repassa as informações do console do processo python para o console do node
    pythonProcess.stdout.on("data", (data) => {
      console.log(data.toString());
    });
    // Repassa os erros do processo python para o console do node
    pythonProcess.stderr.on("data", (data) => {
      console.log(data.toString());
    });
    // Quando o processo termina, recebemos um código. O código 0 significa que o processo finalizou sem erros
    pythonProcess.on("close", (code) => {
      if (code == 0) {
        console.log(`script finalizado`);
        resolve();
        // Caso o processo finalize com um erro, matamos o node para evitar que o processo continue e a interface abra.
      } else {
        console.error("erro na execução do script");
        process.exit();
      }
    });
  });
};

// Spawna o processo que confere se o Dobot esta devidamente conectado ao computador
const py_connectDobot = () => {
  return new Promise((resolve, reject) => {
    const pythonProcess = spawn("python", ["./startup/connect_dobot.py"]);
    
    pythonProcess.stdout.on("data", (data) => {
      console.log(data.toString());
      
    });
    pythonProcess.stderr.on("data", (data) => {
      console.log(data.toString());
    });
    // Nesse caso, o código de finalização do script corresponde a porta onde o dobot está conectado
    pythonProcess.on("close", (code) => {
      // Se o código for 0 ou 2, significa que tivemos algum problema no processo python
      // Caso contrário, o código é a porta do Dobot e será devolvido como o resolve da promisse
      if (code && code != 2) {
        console.log(`script finalizado`);
        dobotPort = "COM" + code.toString();
        console.log("!!!", dobotPort);
        resolve(dobotPort);
      } else {
        console.error("erro na execucao do script");
        process.exit();
      }
    });
  });
};

// Spawna o processo que confere se o Raspberry esta devidamente conectado ao computador
// Segue exatamente a mesma lógica de py_connectDobot
const py_connectRasp = () => {
  return new Promise((resolve, reject) => {
    const pythonProcess = spawn("python", ["./startup/connect_rasp.py"]);
    
    pythonProcess.stdout.on("data", (data) => {
      console.log(data.toString());

    });
    pythonProcess.stderr.on("data", (data) => {
      console.log(data.toString());
    });
    pythonProcess.on("close", (code) => {
      if (code && code != 2) {
        console.log(`script finalizado`);
        raspPort = "COM" + code.toString();
        console.log("!!!", raspPort);
        resolve(raspPort);
      } else {
        console.error("erro na execucao do script");
        process.exit();
      }
    });
  });
};

// Spawna o processo que cria os modelos de banco de dados necessários
const py_models = () => {
  return new Promise((resolve, reject) => {
    const pythonProcess = spawn("python", ["../app/api/models.py"]);

    pythonProcess.stdout.on("data", (data) => {
      console.log(data.toString());
    });
    pythonProcess.stderr.on("data", (data) => {
      console.log(data.toString());
    });
    pythonProcess.on("close", (code) => {
      // Se o código é 0, o script foi realizado sem problemas
      if (code == 0) {
        console.log(`script finalizado`);
        resolve();
      } else {
        console.error("erro na execução do script");
        process.exit();
      }
    });
  });
};

// Spawna o processo do servidor. Esse processo não tem um fim
// programado e será finalizado só quando o usuário fechar o programa
const py_runServer = (dobotPort, raspPort) => {
  return new Promise((resolve, reject) => {
    const pythonProcess = spawn("python", ["./api/app.py", dobotPort, raspPort]);

    pythonProcess.stdout.on("data", (data) => {
      console.log(data.toString());
    });
    pythonProcess.stderr.on("data", (data) => {
      console.log(data.toString());
    });
    pythonProcess.on("close", (code) => {
      console.log(`child process exited with code ${code}`);
      resolve();
    });
  });
};

module.exports = { py_installLibs, py_runServer, py_models, py_connectDobot, py_connectRasp };
