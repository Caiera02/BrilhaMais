async function BuscaCep() {

    let cep1 = document.getElementById('cep').value
    // let url = `https://viacep.com.br/ws/${cep1}/json/`
    let url = 'https://viacep.com.br/ws/' + cep1 + '/json/'

    await fetch(url).then((response) => {
        // Transforma JSON em OBJ
        return response.json();

    }).then((response) => {
        document.getElementById('cep').value = response.cep
        document.getElementById('logradouro').value = response.logradouro
        document.getElementById('bairro').value = response.bairro
        document.getElementById('numero').value = response.complemento
        document.getElementById('estado').value = response.estado

    })
}

async function Salvar() {
    alert('Cadastro realizado com sucesso !! \n \n Seja Bem vindo !!');
}