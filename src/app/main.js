const { app, BrowserWindow } = require("electron");
const { spawn } = require("child_process");

const {py_connectDobot, py_installLibs, py_runServer} = require("./startup/startupScript")

const createWindow = () => {
  const win = new BrowserWindow({
    width: 800,
    height: 600,
    webPreferences: {
      nodeIntegration: true,
    },
  });
  win.loadFile("pages/index.html");
};

app.on("window-all-closed", () => {
  if (process.platform !== "darwin") app.quit();
});

app.whenReady().then( async () => {

  console.log("--------------INSTALANDO LIBS NECESSARIAS--------------");
  await py_installLibs();

  console.log("--------------EXECUTANDO SCRIPT PYTHON-----------------");
  dobotPort = await py_connectDobot();

  console.log("--------------INICIANDO SERVIDOR-----------------------");
  py_runServer(dobotPort);
  setTimeout(()=>{
    createWindow();
  }, 5000)

});
