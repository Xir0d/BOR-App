//SELECTION DES OPTIONS CRYPTER OU DECRYPTER VIA MENU DEROULANT:

// Definition des éléments nécessaires:
const menuDeroulant = document.querySelector('.selectionOption');
const spanDecryptInputs = document.querySelector('.decryptButtons');
const divChamps = document.querySelector('.champs');
const boutonCrypt = document.querySelector('.crypt');
const boutonDecrypt = document.querySelector('.decrypt');
var scryptALancer = 'code/crypt.py'; //Car en arrivant sur la page, par defaut on est sur le menu crypt
scryptCrypt = 0; 
scryptDecrypt = 0;

// Ajoutez un écouteur d'événement pour détecter le changement de sélection
menuDeroulant.addEventListener("change", function() {
  // Vérifiez quelle option est sélectionnée
  var optionSelectionnee = menuDeroulant.value;
  // Affichage des nouveaux champs indicatifs et du bouton CRYPT ou DECRYPT en fonction de l'option sélectionnée:
  if (optionSelectionnee === "decrypt") {
    spanDecryptInputs.style.display = 'inline';
    divChamps.style.marginLeft = '35vh';
    divChamps.style.marginRight = '35vh';
    boutonDecrypt.style.display = 'inline';
    boutonCrypt.style.display = 'none';
    var scryptDecrypt = 1;
    var scryptCrypt = 0;
  } else {
    spanDecryptInputs.style.display = 'none';
    divChamps.style.marginLeft = '50vh';
    divChamps.style.marginRight = '50vh';
    boutonDecrypt.style.display = 'none';
    boutonCrypt.style.display = 'inline';
    var scryptDecrypt = 0;
    var scryptCrypt = 1;
  }
  //Choix du scrypt à lancer selon la selection actuelle du menu deroulant:
  if (scryptDecrypt === 1) {
    scryptALancer = 'code/decrypt.py';
  } else {
    scryptALancer = 'code/crypt.py';
  }
  if (scryptCrypt === 1) {
    scryptALancer = 'code/crypt.py';
  } else {
    scryptALancer = 'code/decrypt.py';
  }
});

//Obligation d'ecriture en majuscule dans le champs pour saisir la clé:
let myInputs = document.getElementsByClassName("inputCle");
for (let i = 0; i < myInputs.length; i++) {
  myInputs[i].addEventListener("input", function() {
    this.value = this.value.toUpperCase();
  });
}


// Les variables à stocker dans le fichier
let cleDeChiffrement = "";
let message = "";
indicatif1 = "";
indicatif2 = "";

//OUVERTURE page clé de chiffrement:
const boutonCle = document.querySelectorAll('.cle');
const divInputs = document.querySelector('.inputs');
const inputCle = document.querySelector(' .inputCle');
const inputMessage = document.querySelector('.inputMessage');
const indicatif1Input = document.querySelector('.indicatif1Input');
const indicatif2Input = document.querySelector('.indicatif2Input');

boutonCle.forEach(function(bouton) {
  bouton.addEventListener('click', function() {
    divInputs.style.display = 'inline';
    inputCle.style.display = 'inline';
    inputMessage.style.display = 'none';
    indicatif1Input.style.display = 'none';
    indicatif2Input.style.display = 'none';
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
    divInputs.style.display = 'inline';
    inputCle.style.display = 'none';
    inputMessage.style.display = 'inline';
    indicatif1Input.style.display = 'none';
    indicatif2Input.style.display = 'none';
    //Ecriture automatique dans la zone au chargement:
    inputMessage.focus();
    //Validation par touche  entree:
    inputMessage.addEventListener("keyup", function(event) {
      if (event.key === "Enter") {
        message = inputMessage.value;
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

//Ouverture Page Indicatifs:
const boutonIndicatif = document.querySelectorAll('.indicatifButton');

boutonIndicatif.forEach(function(boutonindicatif) {
  boutonindicatif.addEventListener('click', function() {
    divInputs.style.display = 'inline';
    inputCle.style.display = 'none';
    inputMessage.style.display = 'none';
    indicatif1Input.style.display = 'inline';
    indicatif2Input.style.display = 'inline';
    //Ecriture automatique dans la zone au chargement:
    indicatif1Input.focus();
    //Validation par touche  entree:
    indicatif1Input.addEventListener("keyup", function(event) {
      if (event.key === "Enter") {
        indicatif1 = indicatif1Input.value;
        indicatif2Input.focus();
      }
    });
    indicatif2Input.addEventListener("keyup", function(event) {
      if (event.key === "Enter") {
        indicatif2 = indicatif2Input.value;
        indicatif1 = indicatif1Input.value;
        divInputs.style.display = 'none';
        console.log(indicatif1+indicatif2);
      }
    });
  });
});

//Envoie des variables dans le fichier json AVEC LE BOUTON VALIDER:
//BOUTON VALIDER LANCE LE FICHIER CRYPT ET DECRYPT
var exportButton = document.querySelector('.export');

exportButton.addEventListener('click', function() {
  // Écrire les données dans le fichier
  window.fs.fsWrite('code/data.json', cleDeChiffrement, message, indicatif1, indicatif2)
  window.pythonShell.launch(scryptALancer);
});

//AFFICHAGE DES RESULTATS DU BOUTON CRYPT:
var cryptButton = document.querySelector('.crypt');
cryptButton.addEventListener('click', function() {

  //CREATION DE LA FONCTION CALLBACK:
  function fsReadResult(data) {
    resultat = data;
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


//PopUp indiquant qu'il n'y a pas de problemes avec les indicatifs -> utiliser les variables verif_indicatif dans data.json

//PopuP indiquant la bonne validation avec le bouton "Valider"