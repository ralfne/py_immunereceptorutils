
class GeneParsingException(Exception):
    def __init__(self, error):
        super(GeneParsingException, self).__init__(error)


class Gene:
    def __init__(self, gene_text, assume_01_allele=True):
        self._gene = ''
        self._allele = 1
        self._parse(gene_text, assume_01_allele)

    def _parse(self, text, assume_01_allele=True):
        parts=text.split('*')
        if len(parts)==1:
            self._gene=text
            if assume_01_allele:
                self._allele=1
            else:
                self._allele = -1
        elif len(parts)==2:
            self._gene = parts[0]
            self._allele = int(parts[1])
        else:
            raise ValueError('Could not parse gene text')

    def get_gene_text(self):
        return self._gene

    def get_subgroup_text(self):
        if '-' in self._gene:
            out = self._gene
            out = out[:out.index('-')]
        else:
            out = None
        return out

    def get_allele_text(self):
        if self._allele == -1:
            out = None
        else:
            out = str(self._allele)
        return out

    def equals(self, other, include_allele=True):
        if include_allele:
            my_def = str(self)
            other_def = str(other)
        else:
            my_def = self.get_gene_text()
            other_def = other.get_gene_text()
        return my_def==other_def

    def __str__(self):
        out = ''
        if self._allele==-1:
            out = self._gene
        else:
            out = self._gene + '*' + "%02d" % (self._allele,)
        return out
