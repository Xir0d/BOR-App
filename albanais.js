var fs = require('fs-extra');

//Obligation d'ecriture en majuscule dans le champs pour saisir la clé:
let myInputs = document.getElementsByClassName("inputCle");
for (let i = 0; i < myInputs.length; i++) {
  myInputs[i].addEventListener("input", function() {
    this.value = this.value.toUpperCase();
  });
}


// Les variables à stocker dans le fichier
let cléDeChiffrement = "";
let messageAChiffrer = "";

//OUVERTURE page clé de chiffrement:
const boutonCle = document.querySelectorAll('.cle');
const divInputs = document.querySelector('.inputs');
const inputCle = document.querySelector(' .inputCle');
const inputMessage = document.querySelector('.inputMessage');

boutonCle.forEach(function(bouton) {
  bouton.addEventListener('click', function() {
    divInputs.style.display = 'block';
    inputCle.style.display = 'block';
    inputMessage.style.display = 'none';
    inputCle.addEventListener("keyup", function(event) {
      if (event.key === "Enter") {
        cléDeChiffrement = inputCle.value;
        divInputs.style.display = 'none';
      }
    });
  });
});

//OUVERTURE page message:
var boutonMessage = document.querySelectorAll('.message');

boutonMessage.forEach(function(bouton) {
  bouton.addEventListener('click', function() {
    divInputs.style.display = 'block';
    inputCle.style.display = 'none';
    inputMessage.style.display = 'block';
    inputMessage.addEventListener("keyup", function(event) {
      if (event.key === "Enter") {
        messageAChiffrer = inputMessage.value;
        divInputs.style.display = 'none';
      }
    });
  });
});

//Envoie des variables dans le fichier json AVEC LE BOUTON VALIDER:
var exportButton = document.querySelector('.export');

exportButton.addEventListener('click', function() {
  const dataExport = {
    'cléDeChiffrement': cléDeChiffrement,
    'messageAChiffrer': messageAChiffrer
  };
  const jsonData = JSON.stringify(dataExport);
  fs.writeFile('code/data.json', jsonData, function(err) {
    if (err) {
      console.error('Erreur lors de l\'écriture du fichier : ', err);
    } else {
      console.log('Fichier JSON créé avec succès.');
    }
  });
});





// Convertir les variables en chaîne JSON


// Écrire les données dans le fichier


//Lancement du scrypt pour crypter:


//Lancement du scrypt pour décrypter:

//Easter Egg BOR SYSTEM:
