"""
CEL datatype sniffer for Command Console version 1 format (binary files).
http://media.affymetrix.com/support/developer/powertools/changelog/gcos-agcc/cel.html#calvin
http://media.affymetrix.com/support/developer/powertools/changelog/gcos-agcc/generic.html

"""
import data
from galaxy.datatypes.binary import Binary

class CelCc1( Binary ):
    file_ext = "celcc1"

    def sniff(self, filename):
        # Determine if the file is in CEL Command Console version 1 format.
        # Filename is in the format 'upload_file_data_jqRiCG', therefore we must check the header bytes.
        # Get the first 2 'UBYTE' (8bit unsigned). First is magic number 59, second is version number (always 1).

        with open(filename, "rb") as f:
            byte = f.read(2)

        try:
            if byte[0:2] == b'\x3B\x01':
                return True
            else:
                return False
        except IndexError:
            return False

Binary.register_sniffable_binary_format("celcc1", "celcc1", CelCc1)

