const { app, BrowserWindow } = require("electron");
// const path = require("path");
const { spawn } = require("child_process");

const createWindow = () => {
  const win = new BrowserWindow({
    width: 800,
    height: 600,
    webPreferences: {
      nodeIntegration: true,
    },
  });
  // launch flask server

  win.loadFile("index.html");
};

app.on("window-all-closed", () => {
  if (process.platform !== "darwin") app.quit();
});

const py_installLibs = () => {
  return new Promise((resolve, reject)=>{
    const pythonProcess = spawn("python", ["./startup/install_libs.py"]);
  
    pythonProcess.stdout.on("data",(data)=>{
      console.log(data.toString())
    })
    pythonProcess.stderr.on("data",(data)=>{
      console.log(data.toString())
    })
    pythonProcess.on("close", (code) => {
      console.log(`child process exited with code ${code}`);
      resolve()
    });
  })
}
const py_connectDobot = () => {
  return new Promise((resolve, reject)=>{
    const pythonProcess = spawn("python", ["./startup/connect_dobot.py"]);
  
    pythonProcess.stdout.on("data",(data)=>{
      console.log(data.toString())
      if (data.includes("PORT==")) {
        let port = data.toString()
        port = port.replace("PORT==", "")
        port = port.replace("==","")
        console.log("A PORTA DO DOBOT É", Number(port))
        resolve(Number(port))
      }
    })
    pythonProcess.on("close", (code) => {
      console.log(`child process exited with code ${code}`);
    });
  })
}
const py_runServer = (dobotPort) => {
  return new Promise((resolve, reject)=>{
    const pythonProcess = spawn("python", ["./startup/server.py", dobotPort]);
  
    pythonProcess.stdout.on("data",(data)=>{
      console.log(data.toString())
    })
    pythonProcess.on("close", (code) => {
      console.log(`child process exited with code ${code}`);
      resolve()
    });
  })
}

app.whenReady().then(async () =>  {
  console.log("--------------INSTALANDO LIBS NECESSARIAS--------------")
  await py_installLibs()

  console.log("--------------EXECUTANDO SCRIPT PYTHON-----------------")
  dobotPort = await py_connectDobot()

  console.log("--------------INICIANDO SERVIDOR-----------------------")
  await py_runServer(dobotPort)

  createWindow();
});

// const create_window2 = () => {
//   const win = new BrowserWindow({
//     width: 800,
//     height: 600,
//   });

//   win.loadFile("ensaios.html");
// };
