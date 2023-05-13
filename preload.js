/**
 * The preload script runs before. It has access to web APIs
 * as well as Electron's renderer process modules and some
 * polyfilled Node.js functions.
 * 
 * https://www.electronjs.org/docs/latest/tutorial/sandbox
 */
window.addEventListener('DOMContentLoaded', () => {
    const replaceText = (selector, text) => {
      const element = document.getElementById(selector)
      if (element) element.innerText = text
    }
  
    for (const type of ['chrome', 'node', 'electron']) {
      replaceText(`${type}-version`, process.versions[type])
    }
  })

//AJOUT DU MODULE FS ET DES FONCTIONS ISOLEES:
const { contextBridge } = require('electron')
const fs = require('fs')
const { PythonShell } = require('python-shell');

//ECRIRE ET LIRE DANS FICHIER JSON:
contextBridge.exposeInMainWorld('fs', {
    fsWrite: function fsWrite(path, jsonData) {
      const contenuFichier = fs.readFileSync(path, 'utf-8');
      const data = JSON.parse(contenuFichier);
      data.nouvelleVariable = 'Valeur de la nouvelle variable';
      const nouvelleContenuFichier = JSON.stringify(data);
      fs.writeFileSync('data.json', nouvelleContenuFichier, 'utf-8');
    },
    fsRead: function fsRead(path, callback) {
      fs.readFile(path, 'utf8', (error, data) => {
        if (error) {
          console.error('Erreur lors de la lecture du fichier JSON:', error);
          return;
        }
        callback(data);
      });
    }
})

//LANCER SCRYPT PYTHON:
contextBridge.exposeInMainWorld('pythonShell', {
  launch: function launch(filePath) { 
    PythonShell.run(filePath, null).then(messages=>{
    });
  }
})

/*fs.writeFile(path, jsonData, function(err) {
  if (err) {
      console.error('Erreur lors de l\'écriture du fichier : ', err);
  } else {
      console.log('Fichier JSON créé avec succès.');
  }
})}*/