$(document).ready(function() {
    $('#tweet-form').on('submit', function(e) {
        e.preventDefault();
        $.ajax({
            url: '/predict',
            method: 'POST',
            contentType: 'application/json',
            data: JSON.stringify({ tweet: $('#tweet').val() }),
            success: function(data) {
                $('#result').text('Sentiment: ' + data.prediction);
            }
        });
    });
});