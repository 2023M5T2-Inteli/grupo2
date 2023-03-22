const { app, BrowserWindow } = require("electron");
// const path = require("path");

const createWindow = () => {
  const win = new BrowserWindow({
    width: 800,
    height: 600,
    webPreferences: {
      nodeIntegration: true,
    },
  });
  // launch flask server
  const { spawn } = require("child_process");
  const pythonProcess = spawn("flask", ["run"]);
  pythonProcess.stdout.on("data", (data) => {
    console.log(data.toString());
  });
  pythonProcess.stderr.on("data", (data) => {
    console.log(data.toString());
  });
  pythonProcess.on("close", (code) => {
    console.log(`child process exited with code ${code}`);
  });

  win.loadFile("index.html");
};

app.on("window-all-closed", () => {
  if (process.platform !== "darwin") app.quit();
});

app.whenReady().then(() => {
  createWindow();
});

// const create_window2 = () => {
//   const win = new BrowserWindow({
//     width: 800,
//     height: 600,
//   });

//   win.loadFile("ensaios.html");
// };
