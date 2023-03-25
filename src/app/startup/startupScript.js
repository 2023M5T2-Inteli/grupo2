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
        console.log(`child process exited with code ${code}`);
        resolve();
      });
    });
  };
  const py_connectDobot = () => {
    return new Promise((resolve, reject) => {
      const pythonProcess = spawn("python", ["./startup/connect_dobot.py"]);
  
      pythonProcess.stdout.on("data", (data) => {
        console.log(data.toString());
        if (data.includes("PORT==")) {
          let port = data.toString();
          port = port.replace("PORT==", "");
          port = port.replace("==", "");
          console.log("A PORTA DO DOBOT É", Number(port));
          resolve(Number(port));
        }
      });
      pythonProcess.on("close", (code) => {
        console.log(`child process exited with code ${code}`);
      });
    });
  };
  const py_runServer = (dobotPort) => {
    return new Promise((resolve, reject) => {
      const pythonProcess = spawn("python", [
        "./api/app.py",
        dobotPort,
      ]);
  
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

module.exports = {py_connectDobot, py_installLibs, py_runServer}
