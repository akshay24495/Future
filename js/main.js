;(function () {
	
	'use strict';

	var contentWayPoint = function() {
		var i = 0;
		$('.animate-box').waypoint( function( direction ) {

			if( direction === 'down' && !$(this.element).hasClass('animated-fast') ) {
				
				i++;

				$(this.element).addClass('item-animate');
				setTimeout(function(){

					$('body .animate-box.item-animate').each(function(k){
						var el = $(this);
						setTimeout( function () {
							var effect = el.data('animate-effect');
							if ( effect === 'fadeIn') {
								el.addClass('fadeIn animated-fast');
							} else if ( effect === 'fadeInLeft') {
								el.addClass('fadeInLeft animated-fast');
							} else if ( effect === 'fadeInRight') {
								el.addClass('fadeInRight animated-fast');
							} else {
								el.addClass('fadeInUp animated-fast');
							}

							el.removeClass('item-animate');
						},  k * 200, 'easeInOutExpo' );
					});
					
				}, 100);
				
			}

		} , { offset: '85%' } );
	};

	// Loading page
	var loaderPage = function() {
		$(".fh5co-loader").fadeOut("slow");
	};

	var counter = function() {
		$('.js-counter').countTo({
			 formatter: function (value, options) {
	      return value.toFixed(options.decimals);
	    },
		});
	};
	
	$(function(){
	//	mobileMenuOutsideClick();
	//	offcanvasMenu();
	//	burgerMenu();
		contentWayPoint();
	//	dropdown();
	//	goToTop();
		loaderPage();
	//	counterWayPoint();

	});


}());

function showFuture() {
	$.ajax(
		{
			type:"POST",
			url:"https://storiwall.com/future",
			dataType:"data",
			success: function(msg) {
				console.log("hello");
			},
			error:function(xhr,status,error) {
				console.log(error)
			}
		}
	);
}
