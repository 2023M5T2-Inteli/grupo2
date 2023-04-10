// Este arquivo é responsável por fazer o setup de todo o sistema
// antes de executar a interface gráfica.

// São processos python que executam em sequencia.

const { app, BrowserWindow } = require("electron");
const { spawn } = require("child_process");

const {
  py_connectDobot,
  py_installLibs,
  py_models,
  py_runServer,
  py_connectRasp
} = require("./startup/startupScript");

// Configura a janela do Electron
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

// quando o electron está pronto, executa essa função
// cada uma dessas funções está em "startup/startupScript.js"
app.whenReady().then(async () => {
  console.log("--------------INSTALANDO LIBS NECESSARIAS--------------");
  await py_installLibs();

  console.log("--------------SCRIPT DE CONEXÃO DO ROBO-----------------");
  dobotPort = await py_connectDobot();

  console.log("--------------SCRIPT DE CONEXÃO DO RASPBERRY-----------------");
  raspPort = await py_connectRasp();

  console.log("--------------RODANDO MODELOS-----------------------");
  await py_models();

  console.log("--------------INICIANDO SERVIDOR-----------------------");
  py_runServer(dobotPort, raspPort);
  setTimeout(() => {
    createWindow();
  }, 2000);
});
