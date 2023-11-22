$(document).ready(function () {
    // Init
    $('.image-section').hide();
    $('.loader').hide();
    $('#result').hide();
    $('#details').hide();
    $('#instd_det').hide();
    $('#rec').hide();

    // Upload Preview
    function readURL(input) {
        if (input.files && input.files[0]) {
            var reader = new FileReader();
            reader.onload = function (e) {
                $('#imagePreview').css('background-image', 'url(' + e.target.result + ')');
                $('#imagePreview').hide();
                $('#imagePreview').fadeIn(650);
            }
            reader.readAsDataURL(input.files[0]);
        }
    }
    $("#imageUpload").change(function () {
        $('.image-section').show();
        $('#btn-predict').show();
        $('#result').text('');
        $('#result').hide();
        $('#details').text('');
        $('#details').hide();
        $('#instd_det').text('');
        $('#instd_det').hide();
        $('#rec').text('');
        $('#rec').hide();
        readURL(this);
    });

    // Predict
    $('#btn-predict').click(function () {
        var form_data = new FormData($('#upload-file')[0]);

        // Show loading animation
        $(this).hide();
        $('.loader').show();

        // Make prediction by calling api /predict
        $.ajax({
            type: 'POST',
            url: '/predict',
            data: form_data,
            contentType: false,
            cache: false,
            processData: false,
            async: true,
            success: function (data) {
                // Get and display the result
                $('.loader').hide();
                $('html, body').animate({
                    scrollTop: $('#sec4').offset().top
                }, 200);
                // location.hash = '#sec4';
                $('#result').fadeIn(600);
                $('#result').text(data.insect_name);
                $('#details').fadeIn(600);
                $('#details').text(data.details);
                $('#instd_det').fadeIn(600);
                $('#instd_det').text(data.pesticides);
                $('#rec').fadeIn(600);
                $('#rec').text("Insecticides Recommended");
                console.log('Success!');

                $('html, body').animate({
                    scrollTop: $('#sec4').offset().top
                }, 600);

            
            },
        });
    });

});
