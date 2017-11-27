$(document).ready(function() {
	$('#pagewrapper').removeClass("pageout").addClass("pagein");
	// IF USER OPENS/RESIZES WINDOW AND #ISMOBILE IS/BECOMES ACTIVE (ON A SMALL SCREEN)
	// REMOVE MENU UNTIL USER CLICKS.
	if($('#ismobile').is(':visible')) {
		$(".link").addClass("noclick"); // remove pointer to links if pageloads on mobile
	} 
	$( window ).resize(function() {
	// IF USER MOVES OUTSIDE MOBILE SIZE, MENU STYLE IS CHANGED BACK TO TABLET++
		if($('#isntmobile').is(':visible')) {
			$('#pagewrapper').addClass("lighten").removeClass("darken") // return screen to normal brightness
			$(".fa-angle-double-up").addClass("fadeout").removeClass("fadein");
			$(".fa-angle-double-down").removeClass("fadeout").addClass("fadein"); // change icons			
			$("#linkbar").removeClass("transition"); // remove transition class (prevents menu appearing when resizing)
			$("#linkbar").removeClass("mobilevisible").addClass("mobilehidden"); // remove mobile meny styling
			$(".link").removeClass("noclick"); // add click functions back in
		}
		else {
			$(".link").addClass("noclick"); // remove click functions until menu button is pressed
		}
	});
	// TOGGLES VISIBILITY OF LINKBAR WHEN NAVBUTTON IS CLCIKED
	$(".navbutton").on("click", function(){ // if navbutton clicked
		$("#linkbar").addClass("transition"); // add transition class (prevents menu appearing when resizing)		
		if($('#ismobile').is(':visible')) { // if on mobile
			if ($('#linkbar').hasClass('mobilevisible')) { // and the menu has been opened
				$('#pagewrapper').addClass("lighten").removeClass("darken") // return screen to normal brightness 
				$(".fa-angle-double-up").addClass("fadeout").removeClass("fadein");
				$(".fa-angle-double-down").removeClass("fadeout").addClass("fadein"); // change icons
				$("#linkbar").removeClass("mobilevisible").addClass("mobilehidden"); // close menu
				$(".link").addClass("noclick"); // and remove click functionality from links
			}
			else { // otherwise
				$('#pagewrapper').addClass("darken").removeClass("lighten")
				$("#linkbar").addClass("mobilevisible").removeClass("mobilehidden"); // open the menu
				$(".fa-angle-double-down").addClass("fadeout").removeClass("fadein");
				$(".fa-angle-double-up").removeClass("fadeout").addClass("fadein"); // change icons
				$(".link").removeClass("noclick");	// and return click functionality to links.		
			}
		}
	});
	$("#pagewrapper").on("click", function(){ // if anywhere but navbar is clicked.
		if($('#ismobile').is(':visible')) { // if on mobile
			if ($('#linkbar').hasClass('mobilevisible')) { // and the menu has been opened
				$('#pagewrapper').addClass("lighten").removeClass("darken"); // darken rest of screen 
				$(".fa-angle-double-up").addClass("fadeout").removeClass("fadein");
				$(".fa-angle-double-down").removeClass("fadeout").addClass("fadein"); // change icons
				$("#linkbar").removeClass("mobilevisible").addClass("mobilehidden"); // close menu
				$(".link").addClass("noclick"); // and remove click functionality from links
			}
		}
	});
				
});