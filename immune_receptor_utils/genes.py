from immune_receptor_utils.gene import Gene


class Genes(object):
    def __init__(self):
        self._items=[]

    def __iter__(self):
        return iter(self._items)

    def add_gene(self, gene):
        self._items.append(gene)

    def __len__(self):
        return len(self._items)

    def __getitem__(self, i):
        return self._items.__getitem__(i)

    def get_tcr_chain(self):
        out = None
        possibilities = set()
        for gene in self._items:
            if 'TRA' in str(gene):
                out=TCRChain.TRA
                possibilities.add('TRA')
            elif 'TRB' in str(gene):
                out=TCRChain.TRB
                possibilities.add('TRB')
            elif 'TRD' in str(gene):
                out = TCRChain.TRD
                possibilities.add('TRD')
            elif 'TRG' in str(gene):
                out=TCRChain.TRG
                possibilities.add('TRG')
            if len(possibilities)>1:
                return None
        return out


class GenePossibilities(Genes):
    def __init__(self, genes_text=None, assume_01_allele=True):
        self._items=[]
        if genes_text is not None:
            self._parse(genes_text, assume_01_allele)

    def _parse(self, text, assume_01_allele):
        parts=text.split('|')
        for part in parts:
            part = part.strip()
            g = Gene(part, assume_01_allele)
            self._items.append(g)

    def overlap_exists(self, gene_possibilites, include_allele):
        for gene in gene_possibilites:
            found = self.has_gene(gene, include_allele)
            if found:
                return True
        return False

    def add_gene(self, gene, also_check_allele=True):
        if not self.has_gene(gene, also_check_allele):
            super(GenePossibilities, self).add_gene(gene)

    def has_gene(self, gene, include_allele):
        for my_gene in self._items:
            if my_gene.equals(gene, include_allele):
                return True
        return False

    def get_distinct_genes(self):
        out = GenePossibilities()
        distinct_genes=[]
        for gene in self._items:
            gene_only = gene.get_gene_text()
            if gene_only not in distinct_genes:
                distinct_genes.append(gene_only)
                out.add_gene(gene)
        return out

    def __str__(self):
        out=''
        for gene in self._items:
            if len(out)!=0:
                out+='|'
            out+=str(gene)
        return out
