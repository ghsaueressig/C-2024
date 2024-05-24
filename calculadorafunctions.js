function addOperation() {
    var inputs = document.querySelectorAll('.number.form-control');
    var input1 = parseFloat(inputs[inputs.length - 2].value); // Último input
    var input2 = parseFloat(inputs[inputs.length - 1].value); // Penúltimo input
    var operacao = document.getElementById('operacao').value;
    var resultado;

    switch (operacao) {
        case 'soma':
            resultado = input1 + input2;
            operationString = input1 + ' + ' + input2 + ' = ' + resultado;
            break;
        case 'subtracao':
            resultado = input1 - input2;
            operationString = input1 + ' - ' + input2 + ' = ' + resultado;
            break;
        case 'multiplicacao':
            resultado = input1 * input2;
            operationString = input1 + ' * ' + input2 + ' = ' + resultado;
            break;
        case 'divisao':
            resultado = input1 / input2;
            operationString = input1 + ' / ' + input2 + ' = ' + resultado;
            break;
        case 'exponenciacao':
            resultado = Math.pow(input1, input2);
            operationString = input1 + ' ^ '  + input2 + ' = ' + resultado;
            break;
        case 'raiz':
            var indice = parseFloat(inputs[inputs.length - 1].value);
            if (!isNaN(indice) && indice !== 2) {
                resultado = Math.pow(input1, 1 / indice);
                operationString = indice + '√' + input1 + ' = ' + resultado;
            } else {
                resultado = Math.sqrt(input1);
                operationString = '√' + input1 + ' = ' + resultado;
            }
            break;
        case 'media':
            resultado = (input1 + input2) / 2;
            operationString = 'Média de ' + input1 + ' e ' + input2 + ' = ' + resultado;
            break;
        case 'porcentagem':
            resultado = (input1 / input2) * 100;
            operationString = input1 + ' é ' + resultado + '% de ' + input2;
            break;
        default:
            resultado = NaN; // Caso a operação não seja reconhecida
            operationString = 'Operação inválida';
    }

    // Atualiza o primeiro input com o resultado da operação
    inputs[0].value = resultado;

    // Redefine o valor dos demais inputs para vazio
    for (var i = 1; i < inputs.length; i++) {
        inputs[i].value = "";
    }
        
    var operationList = document.getElementById('lista-operacoes');
    var listItem = document.createElement('li');
    listItem.textContent = operationString;
    operationList.appendChild(listItem);
    document.getElementById('input2').value = "";
    }

function limparInputs(inputs) {
    for (var i = 1; i < inputs.length; i++) {
        inputs[i].value = "";
    }
}

function resetCalculatorPartial() {
    var inputs = document.querySelectorAll('.number.form-control');
    inputs.forEach(function(input) {
        input.value = "";
    });
    document.getElementById('operacao').selectedIndex = 0;
    
}

function resetCalculatorFull() {
    resetCalculatorPartial(); // Chama a função parcial para limpar os valores dos inputs e redefinir o seletor de operações
    
    // Limpa o histórico da calculadora
    var operationList = document.getElementById('lista-operacoes');
    operationList.innerHTML = ""; // Remove todos os elementos dentro da lista
    
    // Remove inputs extras além dos dois primeiros
    var inputsContainer = document.getElementById('inputs-container');
    var inputs = inputsContainer.querySelectorAll('.number.form-control');
    for (var i = inputs.length - 1; i >= 2; i--) {
        inputs[i].parentNode.parentNode.remove();
    }
    
    alert("Calculadora completamente redefinida.");
}

function toggleOperations() {
    var operationsDiv = document.getElementById('operacoes');
    if (operationsDiv.style.display === 'none') {
        operationsDiv.style.display = 'block';
    } else {
        operationsDiv.style.display = 'none';
    }
}

function addInput() {
    var inputsContainer = document.getElementById('inputs-container');

    var newRow = document.createElement('div');
    newRow.className = 'row mb-2 ms-5';

    var newInputDiv = document.createElement('div');
    newInputDiv.className = 'col-3';

    var newInput = document.createElement('input');
    newInput.className = 'number form-control';
    newInput.setAttribute('name', 'input[]');
    newInput.setAttribute('placeholder', 'Input');
    newInput.setAttribute('type', 'number');

    newInputDiv.appendChild(newInput);
    newRow.appendChild(newInputDiv);
    inputsContainer.appendChild(newRow);
}

function removeLastInput() {
    var inputsContainer = document.getElementById('inputs-container');
    var inputs = inputsContainer.querySelectorAll('.number.form-control');

    // Verifica se há pelo menos 2 inputs antes de remover
    if (inputs.length > 2) {
        var lastInputRow = inputs[inputs.length - 1].parentNode.parentNode;
        lastInputRow.parentNode.removeChild(lastInputRow);
    } else {
        alert("Não é possível remover mais inputs.");
    }
}

function swapInputs() {
    var inputsContainer = document.getElementById('inputs-container');
    var inputs = inputsContainer.querySelectorAll('.number.form-control');

    // Verifica se há pelo menos 2 inputs antes de trocar
    if (inputs.length >= 2) {
        var lastInputValue = inputs[inputs.length - 1].value;

        // Move os valores dos inputs uma posição para frente
        for (var i = inputs.length - 1; i > 0; i--) {
            inputs[i].value = inputs[i - 1].value;
        }

        // Coloca o valor do último input no primeiro input
        inputs[0].value = lastInputValue;
    } else {
        alert("Não há inputs suficientes para trocar.");
    }
}

function arredondarNumeros() {
    var inputs = document.querySelectorAll('.number.form-control');
    inputs.forEach(function(input) {
        input.value = Math.round(parseFloat(input.value)); // Arredonda cada valor para o inteiro mais próximo
    });
}

function invertSignals() {
    var inputs = document.querySelectorAll('.number.form-control');

    inputs.forEach(function(input) {
        var value = parseFloat(input.value);

        // Verifica se o valor é um número válido antes de inverter o sinal
        if (!isNaN(value)) {
            input.value = -value; // Inverte o sinal do valor
        }
    });
}

document.addEventListener('keydown', function(event) {
    var operacaoSelecionada = document.getElementById('operacao');
    
    // Verifica se a tecla pressionada é o sinal de adição (+)
    if (event.key === '+') {
        operacaoSelecionada.value = 'soma';
    }
    
    // Verifica se a tecla pressionada é o sinal de subtração (-)
    if (event.key === '-') {
        operacaoSelecionada.value = 'subtracao';
    }
    
    // Verifica se a tecla pressionada é o asterisco (*)
    if ((event.key === '*') || (event.key === 'x')){
        operacaoSelecionada.value = 'multiplicacao';
    }

    // Verifica se a tecla pressionada é o e (e)
    if (event.key === 'e'){
        operacaoSelecionada.value = 'exponenciacao';
    }
    
    // Verifica se a tecla pressionada é a barra (/)
    if (event.key === '/') {
        operacaoSelecionada.value = 'divisao';
    }

    // Verifica se a tecla pressionada é a M (m)
    if (event.key === 'm') {
        operacaoSelecionada.value = 'media';
    }

    // Verifica se a tecla pressionada é a P (p)
    if (event.key === 'p') {
        operacaoSelecionada.value = 'porcentagem';
    }

});
