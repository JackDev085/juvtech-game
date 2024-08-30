function validateForm() {
    // Obtém todos os inputs de rádio dentro do formulário
    const radios = document.querySelectorAll('input[type="radio"]');
    let radioSelected = false;

    // Verifica se algum dos inputs de rádio está selecionado
    for (var i = 0; i < radios.length; i++) {
        if (radios[i].checked) {
            radioSelected = true;
            break;
        }
    }

    // Se nenhum input de rádio estiver selecionado, exibe um alerta e retorna false para cancelar o envio
    if (!radioSelected) {
        alert('Por favor, selecione uma opção.');
        return false;
    }

    // Se algum input de rádio estiver selecionado, permite o envio do formulário
    return true;
}