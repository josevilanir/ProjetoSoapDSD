const soap = require('soap');

const url = 'http://localhost:8000/?wsdl';

soap.createClient(url, (err, client) => {
    if (err) {
        console.error(err);
    } else {
        // Chama o método remoto do serviço
        const params = {
            num1: 5.0,
            num2: 7.0
        };

        client.calcularMedia(params, (err, result) => {
            if (err) {
                console.error(err);
            } else {
                console.log('Média calculada:', result);
            }
        });
    }
});

