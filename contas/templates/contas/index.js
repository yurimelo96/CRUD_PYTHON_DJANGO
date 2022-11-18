var dados = []

$(function () {
    dados = localStorage.getItem("{% for transacao in transacoes %}{{transacao.descricao}}{% endfor %}")
})