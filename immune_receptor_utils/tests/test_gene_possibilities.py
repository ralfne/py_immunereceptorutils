from immune_receptor_utils.genes import GenePossibilities
import pytest
from immune_receptor_utils.gene import Gene


def test_get_distinct_genes():
    gp = GenePossibilities()
    g1 = Gene('TRAV26-1*01')
    gp.add_gene(g1)
    g2 = Gene('TRAV26-1*02')
    gp.add_gene(g2)
    g3 = Gene('TRAV26-1*03')
    gp.add_gene(g3)
    distinct_genes = gp.get_distinct_genes()
    assert (distinct_genes is not None)
