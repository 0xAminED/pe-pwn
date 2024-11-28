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
