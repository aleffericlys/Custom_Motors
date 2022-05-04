$(document).ready(function() {
	
	///busca
	var searchBtn = $('#search-btn')
	var searchForm = $('#search-form')
	
	$(searchBtn).on('click', function () {
		
		searchForm.submit();
	});

	//nosso projeto
	$('.filter-btn').on('click',function() {

		let type = $(this).attr('id');
		let boxes = $('.project-box');

		$('.main-btn').removeClass('active');
		$(this).addClass('active');
		
		if(type == 'mot-btn'){
			eachBoxes('mot', boxes)
		} else if (type == 'pec-btn') {
			eachBoxes('pec', boxes);
		} else if (type == 'fer-btn') {
			eachBoxes('fer', boxes);
		} else {
			eachBoxes('all', boxes);
		}

	});
	
	function eachBoxes(type, boxes) {
		if(type == 'all') {
			$(boxes).fadeIn();
		} else {
			$(boxes).each(function() {
				if(!$(this).hasClass(type)) {
					$(this).fadeOut('slow');
				} else {
					$(this).fadeIn();
				}
			});
		}
	}

});


