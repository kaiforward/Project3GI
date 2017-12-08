
if (document.getElementById('tradepage')!=null) {
	// if on the trade page
	var unitPrice = document.getElementById('pricecheck').innerText;
	var distance = document.getElementById('distance').innerText;
	var fuelCost = document.getElementById('fuelcost');
	var totalPriceElement = document.getElementById('totalprice');
	// find elements that contain trade data relevant to the total price and fuel cost
	document.getElementById('id_amount').oninput=function() {
	    totalPrice = this.value * unitPrice
	    totalPriceElement.innerText = totalPrice.toLocaleString();
	    readableFuelCost = Math.round(distance / 100 * this.value)
	    fuelcost.innerText = readableFuelCost.toLocaleString(); 
	}
	// calculate fuel cost and total price as amount is entered.
}

if (document.getElementById('shipbuypage')!=null) {
	// if on the trade page
	var unitPrice = document.getElementById('pricecheck').innerText;
	var totalPriceElement = document.getElementById('totalprice');
	// find elements that contain trade data relevant to the total price and fuel cost
	document.getElementById('id_amount').oninput=function() {
		totalPrice = this.value * unitPrice
	    totalPriceElement.innerText = totalPrice.toLocaleString();
	}
	// calculate fuel cost and total price as amount is entered.
}

if (document.getElementById('minebuypage')!=null) {
	// if on the trade page
	var unitPrice = document.getElementById('pricecheck').innerText;
	var totalPriceElement = document.getElementById('totalprice');
	// find elements that contain trade data relevant to the total price and fuel cost
	document.getElementById('id_amount').oninput=function() {
		totalPrice = this.value * unitPrice
	    totalPriceElement.innerText = totalPrice.toLocaleString();
	}
	// calculate fuel cost and total price as amount is entered.
}

$(document).ready(function() {
	$(".el").on("tap click", function(){ // if element is clicked on show details
		$('.el').removeClass("fadeout noclick").addClass("fadein");
		$(this).addClass("fadeout noclick").removeClass("fadein");
	});				
});


