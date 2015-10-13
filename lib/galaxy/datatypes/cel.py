"""
CEL datatype sniffer for v4 (binary files).
http://media.affymetrix.com/support/developer/powertools/changelog/gcos-agcc/cel.html

"""
import data
from galaxy.datatypes.binary import Binary

class Cel( Binary ):
    file_ext = "cel"

    def sniff(self, filename):
        # Determine if the file is in CEL v4 format.
        # Filename is in the format 'upload_file_data_jqRiCG', therefore we must check the header bytes.
        # Get the first 2 integers (32bit). First is magic number 64, second is version number (always 4).

        with open(filename, "rb") as f:
            byte = f.read(8)

        try:
            if byte[0:8] == b'\x40\x00\x00\x00\x04\x00\x00\x00':
                return True
            else:
                return False
        except IndexError:
            return False

Binary.register_sniffable_binary_format("cel", "cel", Cel)

