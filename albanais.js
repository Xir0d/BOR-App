/**
 * This file is loaded via the <script> tag in the index.html file and will
 * be executed in the renderer process for that window. No Node.js APIs are
 * available in this process because `nodeIntegration` is turned off and
 * `contextIsolation` is turned on. Use the contextBridge API in `preload.js`
 * to expose Node.js functionality from the main process.
 */

//CODE

prompt({
  title: 'Variable',
  label: 'Voici votre variable:',
  value: myVariable,
  inputAttrs: { // désactive l'édition du champ de saisie
    readOnly: true
  },
  type: 'input'
}).then((r) => {
  if (r === null) {
    console.log('La fenêtre de dialogue a été fermée sans entrée.');
  } else {
    // Copie de la variable dans le presse-papiers
    clipboard.writeText(myVariable);
    console.log('La variable a été copiée dans le presse-papiers.');
  }
}).catch(console.error);