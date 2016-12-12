$(document).ready(function() {
    $('#sort-by-price').click(function() {
        var $this = $(this);
        var asc = $this.attr('data-asc');
        if (asc == 'true') {
            $this.attr('data-asc', false);
            $this.children('span').removeClass('glyphicon-sort-by-attributes-alt');
            $this.children('span').addClass('glyphicon-sort-by-attributes');
            $.get('/sort-by-price/asc', function(data) {
                $('.catalog').html('');
                $('.catalog').replaceWith(data);
            });
        } else {
            $this.attr('data-asc', true);
            $this.children('span').removeClass('glyphicon-sort-by-attributes');
            $this.children('span').addClass('glyphicon-sort-by-attributes-alt');
            $.get('/sort-by-price/desc', function(data) {
                $('.catalog').html('');
                $('.catalog').replaceWith(data);
            });
        }
    });
    $('.product .inner .btn').click(function(e) {
        e.preventDefault();
        $(this).parent().parent().children('.product-popup').fadeIn();
        $(this).parent().parent().children('.product-popup-bg').fadeIn();
    });
    $('.product-popup-bg').click(function() {
        $(this).fadeOut();
        $(this).parent().children('.product-popup').fadeOut();
    });
    $(".image").click(function() {
        var image = $(this).attr("rel");
        $('#image').hide();
        $('#image').fadeIn('slow');
        $('#image').html('<img src="' + image + '"/>');
        return false;
    });
});