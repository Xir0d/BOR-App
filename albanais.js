const fs = require('fs');

//Obligation d'ecriture en majuscule dans le champs pour saisir la clé:
let myInput = document.getElementById("key");
myInput.addEventListener("input", function() {
  this.value = this.value.toUpperCase();
});


//Envoie des variables dans le fichier json:
let exportButton = document.getElementById("export");
exportButton.addEventListener("click", function() {
  

// Les variables à stocker dans le fichier
  const data = {
    name: "John Doe",
    age: 30,
    city: "Paris"
};

// Convertir les variables en chaîne JSON
  const jsonData = JSON.stringify(data);

// Écrire les données dans le fichier
  fs.writeFile('./code/data.json', jsonData, 'utf8', (err) => {
    if (err) {
      console.error(err);
      return;
    }
    console.log("Les données ont été écrites dans le fichier !");
  });

});

//Lancement du scrypt pour crypter:


//Lancement du scrypt pour décrypter:

//Easter Egg BOR SYSTEM:
