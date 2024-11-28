import pefile
import sys

def analyze_pe(file_path):
    try:
        # Load the PE file
        pe = pefile.PE(file_path)

        print("\n====== PE File Analysis ======")
        print(f"File: {file_path}\n")

        # Display the DOS header
        print("== DOS Header ==")
        print(pe.DOS_HEADER)

        # Display the NT headers
        print("\n== NT Headers ==")
        print(pe.NT_HEADERS)

        # Display the file header
        print("\n== File Header ==")
        print(pe.FILE_HEADER)

        # Display the optional header
        print("\n== Optional Header ==")
        print(pe.OPTIONAL_HEADER)

        # Display sections
        print("\n== Sections ==")
        for section in pe.sections:
            print(f"Name: {section.Name.decode().strip()}")
            print(f"  Virtual Address: 0x{section.VirtualAddress:08X}")
            print(f"  Virtual Size: 0x{section.Misc_VirtualSize:08X}")
            print(f"  Raw Size: 0x{section.SizeOfRawData:08X}")
            print(f"  Characteristics: {section.Characteristics}\n")

        # Display imported functions
        if hasattr(pe, 'DIRECTORY_ENTRY_IMPORT'):
            print("\n== Imported Functions ==")
            for entry in pe.DIRECTORY_ENTRY_IMPORT:
                print(f"Library: {entry.dll.decode()}")
                for imp in entry.imports:
                    print(f"  {imp.name.decode() if imp.name else 'None'} at 0x{imp.address:08X}")
        else:
            print("\nNo imported functions found.")

        # Display exported functions
        if hasattr(pe, 'DIRECTORY_ENTRY_EXPORT'):
            print("\n== Exported Functions ==")
            for exp in pe.DIRECTORY_ENTRY_EXPORT.symbols:
                print(f"  {exp.name.decode() if exp.name else 'None'} at 0x{exp.address:08X}")
        else:
            print("\nNo exported functions found.")

        # Display resources
        if hasattr(pe, 'DIRECTORY_ENTRY_RESOURCE'):
            print("\n== Resources ==")
            for resource in pe.DIRECTORY_ENTRY_RESOURCE.entries:
                print(f"  Resource Type: {resource.struct.Id} (ID or type)")
        else:
            print("\nNo resources found.")

    except FileNotFoundError:
        print(f"Error: File not found: {file_path}")
    except pefile.PEFormatError as e:
        print(f"Error: {e}")

# Main program
if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python pe_explorer.py <path_to_pe_file>")
    else:
        analyze_pe(sys.argv[1])
