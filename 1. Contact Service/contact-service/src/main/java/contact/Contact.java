package contact;

/**
 * Contact class containing business logic for the creation of contact objects.
 *
 * @author Sebastian Stohn
 * @since 2026-08-03
 */
public class Contact {
	private final String id;	// Holds contact id
	private String firstName;	// Holds contact first name
	private String lastName;	// Holds contact last name
	private String phone;		// Holds contact phone number
	private String address;		// Holds contact address
	
	/**
	 * Initialize new contact from user input values.
	 *
	 * @param id User selected id.
	 * @param firstName User selected first name.
	 * @param lastName User selected last name.
	 * @param phone User selected phone number.
	 * @param address User selected address.
	 * @throws IllegalArgumentException If id is null, empty, or greater than 10 characters.
	 */
	public Contact(String id, String firstName, String lastName, String phone, String address) {
		if (id == null || id.trim().isEmpty() || id.length() > 10) {
			throw new IllegalArgumentException("Invalid id");
		}
		this.id = id;				// Initialize id
		setFirstName(firstName);	// Call function to initialize value
		setLastName(lastName);		// Call function to initialize value
		setPhone(phone);			// Call function to initialize value
		setAddress(address);		// Call function to initialize value
	}
	
	/**
	 * Set this contact's first name.
	 *
	 * @param firstName User selected first name.
	 * @throws IllegalArgumentException If name is null, empty, or greater than 10 characters.
	 */
	public void setFirstName(String firstName) {
		if (firstName == null || firstName.trim().isEmpty() || firstName.length() > 10) {
			throw new IllegalArgumentException("Invalid first name");
		}
		this.firstName = firstName; // Initialize first name
	}
	
	/**
	 * Set this contact's last name.
	 *
	 * @param lastName User selected last name.
	 * @throws IllegalArgumentException If name is null, empty, or greater than 10 characters.
	 */
	public void setLastName(String lastName) {
		if (lastName == null || lastName.trim().isEmpty() || lastName.length() > 10) {
			throw new IllegalArgumentException("Invalid last name");
		}
		this.lastName = lastName; // Initialize last name
	}
	
	/**
	 * Set this contact's number.
	 *
	 * @param phone User selected phone number.
	 * @throws IllegalArgumentException If number is null or not 10 digits.
	 */
	public void setPhone(String phone) {
		if (phone == null || !phone.matches("\\d{10}")) {
			throw new IllegalArgumentException("Invalid number");
		}
		this.phone = phone; // Initialize phone number
	}
	
	/**
	 * Set this contact's address.
	 *
	 * @param address User selected address.
	 * @throws IllegalArgumentException If address is null, empty, or greater than 30 characters.
	 */
	public void setAddress(String address) {
		if (address == null || address.trim().isEmpty() || address.length() > 30) {
			throw new IllegalArgumentException("Invalid address");
		}
		this.address = address; //Initialize address
	}
	
	/**
	 * @return This contact's id.
	 */
	public String getId() {
		return id;
	}
	
	/**
	 * @return This contact's first name.
	 */
	public String getFirstName() {
		return firstName;
	}
	
	/**
	 * @return This contact's last name.
	 */
	public String getLastName() {
		return lastName;
	}
	
	/**
	 * @return This contact's phone number.
	 */
	public String getPhone() {
		return phone;
	}
	
	/**
	 * @return This contact's address.
	 */
	public String getAddress() {
		return address;
	}
}