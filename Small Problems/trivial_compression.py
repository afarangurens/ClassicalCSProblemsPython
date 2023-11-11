"""
    If the number of possible different values that a type is meant to represent is less than
    then the number of values that the bits being used to store it can represent, it can likely
    be more efficiently stored.

    I.E: Consider the nucleotides(A, C, G, T) that form a gene in DNA. If they're stored as str
         which can be thought as a collection of Unicode characters, each nucleotide will be
         represented by a character which generally requires 8 bits of storage. 

         This can be reduced to 2 bits, since you can represent 4 states with only two bits:
         00, 01, 10, 11, these bits can then be mapped to A, C, G, T respectively. This implies
         a reduction of 75% (from 8 bits to 2 bits) These are called bit strings.
"""

class CompressedGenes:
    def __init__(self, gene: str) -> None:
        self._compress(gene)

    def _compress(self, gene: str) -> None:  # Since python has no concept of truly private methods or variables
        self.bit_string: int = 1             # underscore naming functions are to be treated as such, just a formality

        for nucleotide in gene.upper():
            self.bit_string <<= 2

            if nucleotide == "A":
                self.bit_string |= 0b00
            elif nucleotide == "C":
                self.bit_string |= 0b01
            elif nucleotide == "G":
                self.bit_string |= 0b10
            elif nucleotide == "T":
                self.bit_string |= 0b11
            else:
                raise ValueError("Invalid Nucleotide: {}".format(nucleotide))
    
    def decompress(self) -> str:
        gene: str = ""
        for i in range(0, self.bit_string.bit_length() - 1, 2):
            bits: int = self.bit_string >> i & 0b11

            if bits == 0b00: gene += "A"
            elif bits == 0b01: gene += "C"
            elif bits == 0b10: gene += "G"
            elif bits == 0b11: gene += "T"
            else:
                raise ValueError("Invalid bits: {}".format(bits))
        return gene[::-1]
    
    def __str__(self) -> str:
        return self.decompress()

if __name__ == '__main__':
    from sys import getsizeof

    original: str = "TAGGGATTAACCGTTATATATATATAGCCATGGATCGATTATATAGGGATTAACCGTTATATATATATAGCCATGGATCGATTATA" * 100
    print("Original is {} bytes".format(getsizeof(original)))

    compressed: CompressedGenes = CompressedGenes(original)
    print("Compressed is {} bytes".format(getsizeof(compressed)))

    print(compressed)
    print("Original and decompressed ar the same: {}".format(original == compressed.decompress()))