/**
 * @fileoverview	Handles client-side functions and UI updates for contact service.
 * @author			Sebastian Stohn
 * @date			2026-08-03
 */


/**
 * Function to create and add new contact based on contact form fields.
 */
async function addContact() {
	// Create contact from contact form
	const contact = {
	    id: document.getElementById("contactId").value,
	    firstName: document.getElementById("contactFirst").value,
	    lastName: document.getElementById("contactLast").value,
	    phone: document.getElementById("contactPhone").value,
	    address: document.getElementById("contactAddress").value
	};
	
	// Send POST request
	const response = await fetch("/contacts", {
		method: "POST",
		headers: {"Content-Type": "application/json"},
		body: JSON.stringify(contact)
	});
	
	// Validate request success
	if (response.ok) {
		clearResult();
		alert("Contact sucessfully added");
	}
	else {
		clearResult();
		alert(await response.text());
	}
}


/**
 * Function to retreive contact by id.
 */
async function findContact() {
	// Extract contact id and send GET request
    const id = document.getElementById("findContact").value;
    const response = await fetch(`/contacts/${id}`);

	// Validate request success
    if (!response.ok) {
		clearResult();
        alert("Contact not found");
        return;
    }

	// Convert json and display retreived contact
    const contact = await response.json();
	displayContact(contact);
}


/**
 * Function to retreive and display all contacts.
 */
async function displayAllContacts() {
	// Send GET request
	const response = await fetch("/contacts");
	
	// Validate request success
	if (!response.ok) {
		clearResult();
		alert(await response.text());
		return;
	}
	
	// Convert json
	const contacts = await response.json();
	
	// Case for no contacts
	if (contacts.length === 0) {
		document.getElementById("contactBook").innerHTML = "No contacts found";
		return;
	}
	
	// Display each contact
	document.getElementById("contactBook").innerHTML = contacts.map(contact =>
		`ID: ${contact.id}<br>
		${contact.firstName} ${contact.lastName}<br>
		${contact.phone}<br>
		${contact.address}`
	).join("<hr>");
}


/**
 * Function to delete a contact.
 */
async function deleteContact() {
	// Extract id
	const id = document.getElementById("findContact").value;
	
	// Validate id input
	if (id === "") {
		clearResult();
		alert("Invalid id");
	    return;
	}
	
	// Send DELETE request
    const response = await fetch(`/contacts/${id}`, {
        method: "DELETE"
    });

	// Validate request success
	if (response.ok) {
		clearResult();
		alert("Contact sucessfully deleted");
	}
	else {
		clearResult();
		alert(await response.text());
	}
}


/**
 * Function to update a contact's first name.
 */
async function updateFirstName() {
	// Extract id and first name
    const id = document.getElementById("findContact").value
    const firstName = document.getElementById("editFirst").value
	document.getElementById("contactBook").innerHTML = "Select show all contacts";

	// Validate inputs
    if (id === "" || firstName === "") {
        alert("Fill in both fields");
        return;
    }

	// Send PUT request
    const response = await fetch(`/contacts/${id}/firstname`, {
        method: "PUT",
        headers: {"Content-Type": "text/plain"},
        body: firstName
    });

	// Validate request success
    if (response.ok) {
		const response = await fetch(`/contacts/${id}`);	// Send GET request
		const contact = await response.json();				// Convert json
		displayContact(contact);							// Display updated contact
        alert("First name updated");
    }
	else {
        alert(await response.text());
    }
}


/**
 * Function to update a contact's last name.
 */
async function updateLastName() {
	// Extract id and last name
    const id = document.getElementById("findContact").value
    const lastName = document.getElementById("editLast").value
	document.getElementById("contactBook").innerHTML = "Select show all contacts";

	// Validate inputs
    if (id === "" || lastName === "") {
        alert("Fill in both fields");
        return;
    }

	// Send PUT request
    const response = await fetch(`/contacts/${id}/lastname`, {
        method: "PUT",
        headers: {"Content-Type": "text/plain"},
        body: lastName
    });

	// Validate request success
    if (response.ok) {
		const response = await fetch(`/contacts/${id}`);	// Send GET request
		const contact = await response.json();				// Convert json
		displayContact(contact);							// Display updated contact
        alert("Last name updated");
    }
	else {
        alert(await response.text());
    }
}


/**
 * Function to update a contact's phone number.
 */
async function updatePhone() {
	// Extract id and phone number
    const id = document.getElementById("findContact").value
    const phone = document.getElementById("editPhone").value
	document.getElementById("contactBook").innerHTML = "Select show all contacts";

	// Validate inputs
    if (id === "" || phone === "") {
        alert("Fill in both fields");
        return;
    }

	// Send PUT request
    const response = await fetch(`/contacts/${id}/phone`, {
        method: "PUT",
        headers: {"Content-Type": "text/plain"},
        body: phone
    });

	// Validate request success
    if (response.ok) {
		const response = await fetch(`/contacts/${id}`);	// Send GET request
		const contact = await response.json();				// Convert json
		displayContact(contact);							// Display updated contact
        alert("Phone number updated");
    }
	else {
        alert(await response.text());
    }
}


/**
 * Function to update a contact's address.
 */
async function updateAddress() {
	// Extract id and address
    const id = document.getElementById("findContact").value
    const address = document.getElementById("editAddress").value
	document.getElementById("contactBook").innerHTML = "Select show all contacts";

	// Validate inputs
    if (id === "" || address === "") {
        alert("Fill in both fields");
        return;
    }

	// Send PUT request
    const response = await fetch(`/contacts/${id}/address`, {
        method: "PUT",
        headers: {"Content-Type": "text/plain"},
        body: address
    });

	// Validate request success
    if (response.ok) {
		const response = await fetch(`/contacts/${id}`);	// Send GET request
		const contact = await response.json();				// Convert json
		displayContact(contact);							// Display updated contact
        alert("Address updated");
    }
	else {
        alert(await response.text());
    }
}


/**
 * Helper function to clear html fields and hide update options.
 */
function clearResult() {
	document.getElementById("result").innerHTML = "None";
	document.getElementById("hidden").style.display = "none";
	document.getElementById("contactBook").innerHTML = "Select show all contacts";
}


/**
 * Helper function to display a given contact.
 * @param contact - Contact to display.
 */
function displayContact(contact) {
	document.getElementById("result").innerHTML =
	`${contact.firstName} ${contact.lastName}<br>
	${contact.phone}<br>
	${contact.address}`;
	document.getElementById("hidden").style.display = "block";
}