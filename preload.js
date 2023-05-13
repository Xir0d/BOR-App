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

contextBridge.exposeInMainWorld('fs', {
    fsWrite: function fsWrite(path, jsonData) { 
        fs.writeFile(path, jsonData, function(err) {
        if (err) {
            console.error('Erreur lors de l\'écriture du fichier : ', err);
        } else {
            console.log('Fichier JSON créé avec succès.');
        }
    })}
})

contextBridge.exposeInMainWorld('fs', {
  fsWrite: function fsWrite(path, jsonData) { 
      fs.writeFile(path, jsonData, function(err) {
      if (err) {
          console.error('Erreur lors de l\'écriture du fichier : ', err);
      } else {
          console.log('Fichier JSON créé avec succès.');
      }
  })}
})