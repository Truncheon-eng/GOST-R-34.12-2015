# GOST R 34.12-2015 Encryption Tool

This application implements encryption and decryption using the GOST R 34.12-2015 algorithm (Kuznyechik or Magma).

## Usage

The application requires four parameters:

```
options:
  -h, --help            Show this help message and exit.
  -i INPUT, --input INPUT
                        Specify the path to the input file.
  -o OUTPUT, --output OUTPUT
                        Specify the path to the output file.
  -k KEY, --key KEY     Specify the encryption key in Base64 format.
  -m {0,1}, --mode {0,1}
                        0 - encryption; 1 - decryption.
```

## Installation

Ensure that the application binary is executable:

```bash
chmod +x your_application_name
```

## Examples

### Encrypt a file

```bash
./your_application_name -i plaintext.txt -o encrypted.txt -k SGVsbG9Xb3JsZA== -m 0
```

### Decrypt a file

```bash
./your_application_name -i encrypted.txt -o decrypted.txt -k SGVsbG9Xb3JsZA== -m 1
```

## Notes
- The encryption key must be provided in Base64 format.
- Ensure that the correct mode (`-m 0` for encryption, `-m 1` for decryption) is selected.
- If you need help, run:

```bash
./your_application_name -h
```

