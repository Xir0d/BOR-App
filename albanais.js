//Obligation d'ecriture en majuscule dans le champs pour saisir la clé:
let myInputs = document.getElementsByClassName("inputCle");
for (let i = 0; i < myInputs.length; i++) {
  myInputs[i].addEventListener("input", function() {
    this.value = this.value.toUpperCase();
  });
}


// Les variables à stocker dans le fichier
let cleDeChiffrement = "";
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
    //Ecriture automatique dans la zone au chargement:
    inputCle.focus();
    //Validation par touche  entree:
    inputCle.addEventListener("keyup", function(event) {
      if (event.key === "Enter") {
        cleDeChiffrement = inputCle.value;
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
    //Ecriture automatique dans la zone au chargement:
    inputMessage.focus();
    //Validation par touche  entree:
    inputMessage.addEventListener("keyup", function(event) {
      if (event.key === "Enter") {
        messageAChiffrer = inputMessage.value;
        divInputs.style.display = 'none';
      }
    });
  });
});
//Empechement du retour à la ligne avec la TOUCHE ENTREE (sinon probleme avec valeur json du msg):
inputMessage.addEventListener('keydown', function(event) {
  if (event.key === 'Enter') {
    event.preventDefault();
  }
});

//Envoie des variables dans le fichier json AVEC LE BOUTON VALIDER:
//BOUTON VALIDER LANCE LE FICHIER CRYPT ET DECRYPT
var exportButton = document.querySelector('.export');

exportButton.addEventListener('click', function() {
  // Écrire les données dans le fichier
  window.fs.fsWrite('code/data.json', cleDeChiffrement, messageAChiffrer)
  window.pythonShell.launch('code/crypt.py')
  window.pythonShell.launch('code/decrypt.py')
});

//AFFICHAGE DES RESULTATS DU BOUTON CRYPT:
var cryptButton = document.querySelector('.crypt');
cryptButton.addEventListener('click', function() {

  //CREATION DE LA FONCTION CALLBACK:
  function fsReadResult(data) {
    resultat = data;
    console.log(resultat);
    const jsonData = JSON.parse(resultat);
    const indicatif1Resultat = jsonData.indicatif1;
    const indicatif2Resultat = jsonData.indicatif2;
    const messageChiffreResultat = jsonData.messageCrypte;
    //Affichage des résultats:
    var indicatif1Div = document.querySelector('.indicatif1');
    var indicatif2Div = document.querySelector('.indicatif2');
    var messageChiffreDiv = document.querySelector('.messageChiffreArea');

    indicatif1Div.textContent = ' ' + indicatif1Resultat;
    indicatif2Div.textContent = ' ' + indicatif2Resultat;
    messageChiffreDiv.textContent = ' ' + messageChiffreResultat;
  }
  //RECUPERATION des DONNEES AU PRES DE DATA.JSON
  window.fs.fsRead('code/data.json', fsReadResult);
});


//AFFICHAGE DES RESULTATS DU BOUTON CRYPT:
var decryptButton = document.querySelector('.decrypt');

decryptButton.addEventListener('click', function() {
});

//LE BOUTON CRYPT OU DECRYPT AFFICHE SEULEMENT LE RESULTAT EN ALLANT CHERCHER LES VARIABLES SOUHAITEES
//faire apparition et disparition des divs en haut 

//Input message pour decrypt = meme input que pour crypt

//Au moment de decrypt, verifier les indicatifs

//Valider les indicatifs via des variables dans le fichier python.

//exemple: verif_indicatif1 = 0 pas d'erreur = 1 erreur.
