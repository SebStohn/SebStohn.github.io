package contact;

import java.util.Collection;
import org.springframework.web.bind.annotation.DeleteMapping;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.PutMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

/**
 * ContactController class for HTTP request routing and and API end points.
 *
 * @author Sebastian Stohn
 * @since 2026-08-03
 */
@RestController
@RequestMapping("/contacts")
public class ContactController {
	private final ContactService contactService; // Service instance
	
	/**
	 * Initialize controller with service instance.
	 *
	 * @param cs Contact service instance.
	 */
	public ContactController(ContactService cs) {
        this.contactService = cs;
    }
	
	/**
	 * Request routing for addContact.
	 *
	 * @param contact Newly created contact.
	 */
	@PostMapping
    public void addContact(@RequestBody Contact contact) {
        contactService.addContact(contact);
    }
	
	/**
	 * Request routing for deleteContact.
	 *
	 * @param id Selected contact's id.
	 */
	@DeleteMapping("/{id}")
    public void deleteContact(@PathVariable String id) {
        contactService.deleteContact(id);
    }
	
	/**
	 * Request routing for updateFirstName.
	 *
	 * @param id Selected contact's id.
	 * @param firstName New first name.
	 */
	@PutMapping("/{id}/firstname")
    public void updateFirstName(@PathVariable String id, @RequestBody String firstName) {
        contactService.updateFirstName(id, firstName);
    }

	/**
	 * Request routing for updateLastName.
	 *
	 * @param id Selected contact's id.
	 * @param lastName New last name.
	 */
    @PutMapping("/{id}/lastname")
    public void updateLastName(@PathVariable String id, @RequestBody String lastName) {
        contactService.updateLastName(id, lastName);
    }

    /**
	 * Request routing for updatePhone.
	 *
	 * @param id Selected contact's id.
	 * @param phone New phone number.
	 */
    @PutMapping("/{id}/phone")
    public void updatePhone(@PathVariable String id, @RequestBody String phone) {
        contactService.updatePhone(id, phone);
    }

    /**
	 * Request routing for updateAddress.
	 *
	 * @param id Selected contact's id.
	 * @param address New address.
	 */
    @PutMapping("/{id}/address")
    public void updateAddress(@PathVariable String id, @RequestBody String address) {
        contactService.updateAddress(id, address);
    }
    
    /**
	 * Request routing for getContact.
	 *
	 * @param id Selected contact's id.
	 * @return Contact with passed id.
	 */
    @GetMapping("/{id}")
    public Contact getContact(@PathVariable String id) {
        return contactService.getContact(id);
    }
    
    /**
	 * Request routing for getAllContacts.
	 *
	 * @return Contact collection.
	 */
    @GetMapping
    public Collection<Contact> getAllContacts() {
    	return contactService.getAllContacts();
    }
}