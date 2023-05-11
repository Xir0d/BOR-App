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
const inputCle = document.querySelector('.inputCle');
const inputMessage = document.querySelector('.inputMessage');

boutonCle.forEach(function(bouton) {
  bouton.addEventListener('click', function() {
    divInputs.style.display = 'block';
    inputCle.style.display = 'block';
    inputMessage.style.display = 'none';
    inputCle.addEventListener("keyup", function(event) {
      if (event.key === "Enter") {
        cléDeChiffrement = inputCle.value;
        console.log(cléDeChiffrement);
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
        console.log(messageAChiffrer);
        divInputs.style.display = 'none';
      }
    });
  });
});

//Envoie des variables dans le fichier json:





// Convertir les variables en chaîne JSON


// Écrire les données dans le fichier


//Lancement du scrypt pour crypter:


//Lancement du scrypt pour décrypter:

//Easter Egg BOR SYSTEM:
