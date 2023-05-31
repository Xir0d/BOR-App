var boutonEncodage = document.querySelector('.crypt');
var boutonDecodage = document.querySelector('.decrypt');

boutonEncodage.addEventListener('click', function() {
    window.childProcess.startCmd('C:/Users/pacom/AppData/Local/Programs/Python/Python311/python.exe c:/Users/pacom/Documents/GitHub/BOR-App/code/encodage.py');
});

boutonDecodage.addEventListener('click', function() {
    window.childProcess.startCmd('C:/Users/pacom/AppData/Local/Programs/Python/Python311/python.exe c:/Users/pacom/Documents/GitHub/BOR-App/code/decodage.py');
});