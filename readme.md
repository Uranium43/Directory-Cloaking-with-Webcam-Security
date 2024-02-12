# Directory Cloaking with Webcam Security

## Overview
Directory Cloaking with Webcam Security is a Python-based project aimed at providing enhanced security for sensitive files within a directory. This project utilizes encryption techniques to lock files, requiring a password for access. Additionally, it incorporates webcam functionality to capture photos of unauthorized users attempting to access locked files.

## Features
### File Locking
Encrypts files within a specified directory to prevent unauthorized access.

### Password Protection
Requires a password to unlock and decrypt files.

### Webcam Security
Captures photos of unauthorized users attempting to access locked files.

### User-Friendly Interface
Provides a simple command-line interface for locking, unlocking, and managing files.

## Installation
1. Clone the repository to your local machine:
git clone https://github.com/yourusername/directory-cloaking.git

2. Install the required dependencies:
pip install -r requirements.txt

## Usage
1. **Locking Files**:
python app.py

Follow the prompts to specify the file path and set a password for locking.

2. **Unlocking Files**:
python decrypt.py

Enter the path to the encrypted file and provide the password to unlock and decrypt it.

## Security Considerations
- **Secure Password Management**: Avoid storing passwords in plain text files for better security. Consider using a more secure method such as key management systems.
- **Encryption**: Ensure that strong encryption algorithms are used to protect sensitive data.
- **Error Handling**: Implement robust error handling to handle potential exceptions and errors gracefully.
- **Dependency Management**: Regularly update dependencies to mitigate security vulnerabilities.

## Contributing
Contributions are welcome! If you'd like to contribute to this project, please fork the repository, make your changes, and submit a pull request.

## License
This project is licensed under the [MIT License](LICENSE).

## Acknowledgments
- This project utilizes the [cryptography](https://cryptography.io/en/latest/) library for encryption.
- Webcam functionality is implemented using [OpenCV](https://opencv.org/).

## Contact
For questions or feedback, feel free to contact the project maintainer at ajinkyamahalpure43@gmail.com