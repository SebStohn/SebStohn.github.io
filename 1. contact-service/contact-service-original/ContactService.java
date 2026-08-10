package contact;

import java.util.HashMap;
import java.util.Map;

public class ContactService {
	private Map<String, Contact> contacts = new HashMap<String, Contact>();
	
	public void addContact(Contact contact) {
		String id = contact.getId();
		
		if (contacts.containsKey(id)) {
			throw new IllegalArgumentException("Id already in use");
		}
		
		contacts.put(id, contact);
	}
	
	public void deleteContact(String id) {
		if (!contacts.containsKey(id)) {
			throw new IllegalArgumentException("Id not found");
		}
		
		contacts.remove(id);
	}
	
	public void updateFirstName(String id, String firstName) {
		if (!contacts.containsKey(id)) {
			throw new IllegalArgumentException("Id not found");
		}
		
		Contact contact = contacts.get(id);
		
		contact.setFirstName(firstName);
	}
	
	public void updateLastName(String id, String lastName) {
		if (!contacts.containsKey(id)) {
			throw new IllegalArgumentException("Id not found");
		}
		
		Contact contact = contacts.get(id);
		
		contact.setLastName(lastName);
	}
	
	public void updatePhone(String id, String phone) {
		if (!contacts.containsKey(id)) {
			throw new IllegalArgumentException("Id not found");
		}
		
		Contact contact = contacts.get(id);
		
		contact.setPhone(phone);
	}
	
	public void updateAddress(String id, String address) {
		if (!contacts.containsKey(id)) {
			throw new IllegalArgumentException("Id not found");
		}
		
		Contact contact = contacts.get(id);
		
		contact.setAddress(address);
	}
	
	public Contact getContact(String id) {
		if (!contacts.containsKey(id)) {
			throw new IllegalArgumentException("Id not found");
		}
		
		return contacts.get(id);
	}
}
