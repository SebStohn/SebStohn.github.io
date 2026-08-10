package contact;

import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.ExceptionHandler;
import org.springframework.web.bind.annotation.RestControllerAdvice;

/**
 * ContactException class returning logical exceptions.
 *
 * @author Sebastian Stohn
 * @since 2026-08-03
 */
@RestControllerAdvice
public class ContactExceptions {
	 @ExceptionHandler(IllegalArgumentException.class)
	 public ResponseEntity<String> handleException(IllegalArgumentException e) {
		 return ResponseEntity.badRequest().body(e.getMessage());
	 }
}