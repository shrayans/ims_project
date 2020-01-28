$('.form .stages label').click(function() {
	var radioButtons = $('.form input:radio');
	var selectedIndex = radioButtons.index(radioButtons.filter(':checked'));
	selectedIndex = selectedIndex + 1;
});

$('.form .gg label').click(function() {
	var radioButtons = $('.form input:radio');
	var selectedIndex = radioButtons.index(radioButtons.filter(':checked'));
	selectedIndex = selectedIndex + 1;
});



$('.form button').click(function() {
	var radioButtons = $('.form input:radio');
	var selectedIndex = radioButtons.index(radioButtons.filter(':checked'));

	selectedIndex = selectedIndex + 2;

	$('.form input[type="radio"]:nth-of-type(' + selectedIndex + ')').prop('checked', true);

	if (selectedIndex == 4) {
		$('button').html('Submit');
	}

  if (selectedIndex == 1) {
		$('button').html('Next').prop;
	}

});
