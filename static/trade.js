
if (document.getElementById('tradepage')!=null) {
	// if on the trade page
	var unitPrice = document.getElementById('pricecheck').innerText;
	var distance = document.getElementById('distance').innerText;
	var fuelCost = document.getElementById('fuelcost');
	var totalPriceElement = document.getElementById('totalprice');
	// find elements that contain trade data relevant to the total price and fuel cost
	document.getElementById('id_amount').oninput=function() {
	    totalPriceElement.innerText = this.value * unitPrice;
	    fuelcost.innerText = Math.round(distance / 5000 * this.value); 
	}
	// calculate fuel cost and total price as amount is entered.
}

if (document.getElementById('shipbuypage')!=null) {
	// if on the trade page
	var unitPrice = document.getElementById('pricecheck').innerText;
	var totalPriceElement = document.getElementById('totalprice');
	// find elements that contain trade data relevant to the total price and fuel cost
	document.getElementById('id_amount').oninput=function() {
	    totalPriceElement.innerText = this.value * unitPrice;
	}
	// calculate fuel cost and total price as amount is entered.
}

if (document.getElementById('minebuypage')!=null) {
	// if on the trade page
	var unitPrice = document.getElementById('pricecheck').innerText;
	var totalPriceElement = document.getElementById('totalprice');
	// find elements that contain trade data relevant to the total price and fuel cost
	document.getElementById('id_amount').oninput=function() {
	    totalPriceElement.innerText = this.value * unitPrice;
	}
	// calculate fuel cost and total price as amount is entered.
}

