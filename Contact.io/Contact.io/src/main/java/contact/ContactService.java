package contact;

import java.util.Map;
import java.util.HashMap;
import java.util.Collection;
import org.springframework.stereotype.Service;

/**
 * ContactService class handling contact storage and business operations.
 *
 * @author Sebastian Stohn
 * @since 2026-08-03
 */
@Service
public class ContactService {
	private Map<String, Contact> contacts = new HashMap<String, Contact>(); // Storage HashMap
	
	/**
	 * Helper method to return a contact by id.
	 *
	 * @param id Selected contact's id.
	 * @return Contact with passed id.
	 * @throws IllegalArgumentException If contact is null (not found).
	 */
	private Contact getExistingContact(String id) {
        Contact contact = contacts.get(id); // Retrieve contact
        if (contact == null) {
            throw new IllegalArgumentException("Id not found");
        }
        return contact;
    }
	
	/**
	 * Method to add a new contact.
	 *
	 * @param contact Newly created contact to add.
	 * @throws IllegalArgumentException If duplicate found.
	 */
	public void addContact(Contact contact) {
		String id = contact.getId(); // Isolate id
		if (contacts.containsKey(id)) {
			throw new IllegalArgumentException("Id already in use");
		}
		contacts.put(id, contact);
	}
	
	/**
	 * Method to delete an existing contact.
	 *
	 * @param id Selected contact's id.
	 * @throws IllegalArgumentException If no contact found.
	 */
	public void deleteContact(String id) {
		if (!contacts.containsKey(id)) {
			throw new IllegalArgumentException("Id not found");
		}
		contacts.remove(id);
	}
	
	/**
	 * Method to update a contact's first name.
	 *
	 * @param id Selected contact's id.
	 * @param firstName New first name.
	 */
	public void updateFirstName(String id, String firstName) {
		Contact contact = getExistingContact(id);
		contact.setFirstName(firstName);
	}
	
	/**
	 * Method to update a contact's last name.
	 *
	 * @param id Selected contact's id.
	 * @param lastName New last name.
	 */
	public void updateLastName(String id, String lastName) {
		Contact contact = getExistingContact(id);
		contact.setLastName(lastName);
	}
	
	/**
	 * Method to update a contact's phone number.
	 *
	 * @param id Selected contact's id.
	 * @param phone New phone number.
	 */
	public void updatePhone(String id, String phone) {
		Contact contact = getExistingContact(id);
		contact.setPhone(phone);
	}
	
	/**
	 * Method to update a contact's address.
	 *
	 * @param id Selected contact's id.
	 * @param address New address.
	 */
	public void updateAddress(String id, String address) {
		Contact contact = getExistingContact(id);
		contact.setAddress(address);
	}
	
	/**
	 * Method to retrieve a contact.
	 *
	 * @param id Selected contact's id.
	 * @return result of getExistingContact().
	 */
	public Contact getContact(String id) {
		return getExistingContact(id);
	}
	
	/**
	 * Method to retrieve all contacts.
	 *
	 * @return Collection of all contacts.
	 */
	public Collection<Contact> getAllContacts() {
		return contacts.values();
	}
}