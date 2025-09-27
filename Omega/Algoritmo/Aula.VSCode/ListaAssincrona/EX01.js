new Promise(function(entregarResultado, informarErro){
    if(1 == 1) {
        entregarResultado("Sua Pizza Chegou!")
    } else {
        informarErro("Acabou a Pizza de Musarrela!")
    }
});

var pedirPizza = new Promise(function(entregarResultado, informarErro){
    setTimeout(function() {
    }
    })
    if(1 == 2) {
        entregarResultado("Sua Pizza Chegou!")
    } else {
        informarErro("Acabou a Pizza de Musarrela!")
    }
});

var pedirPizza = new Promise(function(entregarResultado, informarErro){
    setTimeout(function() {
        entregarResultado("Sua Pizza Chegou!")
    }, 5000);
});

pedirPizza
    .then(function(resultado) {
    console.log(resultado);
    })
    .cath(function(erro){
    console.log(erro);
    });