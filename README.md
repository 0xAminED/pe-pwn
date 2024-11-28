# PE-PWN

A Python script for analyzing **Portable Executable (PE)** files. This tool extracts detailed information about PE file structures such as headers, sections, imports, exports, and resources. It is useful for malware analysis, reverse engineering, and exploring PE file internals.

---

## Features

- **DOS Header**: Displays basic information such as the magic number and address of the NT header.
- **NT Headers**: Provides metadata about the PE file structure.
- **File Header**: Details about the machine type, number of sections, timestamp, and more.
- **Optional Header**: Information about the entry point, image base, and other execution-related data.
- **Sections**: Displays details about sections like `.text`, `.data`, and `.rsrc`.
- **Imports**: Lists all libraries and functions imported by the PE file.
- **Exports**: Displays functions and symbols exported by the PE file.
- **Resources**: Extracts embedded resources such as icons, version info, and other assets.

---

## Requirements

- Python 3.x
- `pefile` library

You can install the required library using pip:

```bash
pip install pefile
```
OR
```bash
pip install -r requirements.txt
```
## Usage

### 1. Clone the Repository
First, clone the repository to your local machine:

```bash
git clone https://github.com/0xAminED/pe-pwn.git
cd pe-pwn
```
### 2. Run the Script
Use the following command to analyze a PE file. Replace <path_to_pe_file> with the path to the PE file you want to analyze.
```bash
python pe_pwn.py <path_to_pe_file>
```
Example:
```bash
python pe_pwn.py C:\path\to\file.exe
```
### 3. Output
The script will display detailed information about the PE file, including headers, sections, imports, exports, and resources. Here is an example of the output format:

```bash
====== PE File Analysis ======
File: C:\path\to\file.exe

== DOS Header ==
{
  'e_magic': 23117, 
  'e_cblp': 0, 
  'e_cp': 0, 
  ...
}

== NT Headers ==
{
  'Signature': b'PE\0\0',
  'FileHeader': { ... },
  'OptionalHeader': { ... }
}

== File Header ==
{
  'Machine': 332, 
  'NumberOfSections': 5, 
  'TimeDateStamp': 1390763812, 
  ...
}

== Sections ==
Name: .text
  Virtual Address: 0x1000
  Virtual Size: 0x2000
  Raw Size: 0x4000
  Characteristics: 0x60000020

...

== Imported Functions ==
Library: user32.dll
  MessageBoxW at 0x12345678

...

== Exported Functions ==
  MyFunction at 0x10001234

== Resources ==
  Resource Type: 0x1 (RT_ICON)

```


## Supported File Formats
This tool works with the following Windows PE file formats:
- **Executable files (.exe)**
- **Dynamic-Link Libraries (.dll)**
- **Driver files (.sys)**
- **Control Panel files (.cpl)**
- **Screensaver files (.scr)**
- **Legacy .com files (if they are in PE format)**

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- Thanks to the contributors for their valuable feedback and improvements.

