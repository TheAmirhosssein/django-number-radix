function encrypt() {
    var number = $('#numberInput').val();
    var radix = $('#radixInput').val();
    $.get('/encrypt/operation/', {
        number: number,
        radix: radix,
    }).then(res => {
        $('#resultArea').html(res);
    });
}


function decrypt() {
    var number = $('#numberInput').val();
    var radix = $('#radixInput').val();
    $.get('/decrypt/operation/', {
        number: number,
        radix: radix,
    }).then(res => {
        $('#resultArea').html(res);
    });
}