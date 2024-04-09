$(document).ready(function () {
  const checkedAmenities = [];

  function updateAmenities () {
    const amenitiesText = checkedAmenities.join(', ');

    $('.amenities h4').text(amenitiesText);
  }

  $('.amenities input[type="checkbox"]').change(function () {
    const amenityId = $(this).data('id');

    if ($(this).is(':checked')) {
      checkedAmenities.push(amenityId);
    } else {
      const index = checkedAmenities.indexOf(amenityId);
      if (index !== -1) {
        checkedAmenities.splice(index, 1);
      }
    }
    updateAmenities();
  });
});
