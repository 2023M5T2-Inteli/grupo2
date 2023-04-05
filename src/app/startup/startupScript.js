const { spawn } = require("child_process");

const py_installLibs = () => {
  return new Promise((resolve, reject) => {
    const pythonProcess = spawn("python", ["./startup/install_libs.py"]);

    pythonProcess.stdout.on("data", (data) => {
      console.log(data.toString());
    });
    pythonProcess.stderr.on("data", (data) => {
      console.log(data.toString());
    });
    pythonProcess.on("close", (code) => {
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
const py_connectDobot = () => {
  return new Promise((resolve, reject) => {
    const pythonProcess = spawn("python", ["./startup/connect_dobot.py"]);

    pythonProcess.stdout.on("data", (data) => {
      console.log(data.toString());

    });
    pythonProcess.stderr.on("data", (data) => {
      console.log(data.toString());
    });
    pythonProcess.on("close", (code) => {
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
