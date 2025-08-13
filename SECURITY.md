
# Security Overview

## Encryption

- All files are encrypted using AES (CBC mode) with a static key (for demo purposes).
- IV is randomly generated for each file and prepended to the ciphertext.
- Decryption occurs on download, ensuring files are never stored or transmitted in plaintext.

## Key Management

- The encryption key is hardcoded for demonstration. In production, use environment variables or a secure key vault.
- Never commit real keys to version control.

## File Handling

- Uploaded files are stored in a protected directory (`media/encrypted_files/`).
- File access is managed via UUIDs to prevent enumeration.

## Recommendations

- Use HTTPS in production to secure data in transit.
- Rotate encryption keys periodically.
- Implement user authentication and access controls.
- Validate and sanitize all file uploads.

## Dependencies

- Django (web framework)
- PyCryptodome (cryptography)

## Threat Model

- Protects against unauthorized access to files at rest.
- Mitigates risks of file interception during download/upload.

## Limitations

- Demo uses a static key; production should use secure key management.
- No user authentication implemented (add for real-world use).