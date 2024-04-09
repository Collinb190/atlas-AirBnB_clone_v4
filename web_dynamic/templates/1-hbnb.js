// 1-hbnb.js
$(document).ready(function () {
    $('input[type=checkbox]').change(function () {
        var checkedAmenities = [];
        $('input[type=checkbox]').each(function () {
            if ($(this).is(':checked')) {
                checkedAmenities.push($(this).attr('data-id'));
            }
        });
        $('#amenities').text(checkedAmenities.join(', '));
    });
});