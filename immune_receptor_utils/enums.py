from enum import Enum


class SequenceType(Enum):
    RNA = 0
    DNA = 1
    Protein = 2


class ProteinRegion(Enum):
    FR1 = 0
    CDR1 = 1
    FR2 = 2
    CDR2 = 3
    FR3 = 4
    CDR3 = 5
    FR4 = 6


class GeneLevel(Enum):
    Allele = 0
    Gene = 1
    Subgroup = 2


class GeneSegment(Enum):
    TRV = 0
    TRD = 1
    TRJ = 2

    @staticmethod
    def __str_abbreviated__(geneSegment):
        s = str(geneSegment)
        i = s.index('.')
        return s[i+1:]

    @staticmethod
    def get_tra_gene(geneSegment):
        if geneSegment == GeneSegment.TRV:
            return GeneChainSegment.TRAV
        elif geneSegment == GeneSegment.TRD:
            return None
        elif geneSegment == GeneSegment.TRJ:
            return GeneChainSegment.TRAJ
        else:
            raise NotImplementedError()

    @staticmethod
    def get_trb_gene(geneSegment):
        if geneSegment == GeneSegment.TRV:
            return GeneChainSegment.TRBV
        elif geneSegment == GeneSegment.TRD:
            return GeneChainSegment.TRBD
        elif geneSegment == GeneSegment.TRJ:
            return GeneChainSegment.TRBJ
        else:
            raise NotImplementedError()

    @staticmethod
    def get_trg_gene(geneSegment):
        if geneSegment == GeneSegment.TRV:
            return GeneChainSegment.TRGV
        elif geneSegment == GeneSegment.TRD:
            return None
        elif geneSegment == GeneSegment.TRJ:
            return GeneChainSegment.TRGJ
        else:
            raise NotImplementedError()

    @staticmethod
    def get_trd_gene(geneSegment):
        if geneSegment == GeneSegment.TRV:
            return GeneChainSegment.TRDV
        elif geneSegment == GeneSegment.TRD:
            return GeneChainSegment.TRDD
        if geneSegment == GeneSegment.TRJ:
            return GeneChainSegment.TRDJ
        else:
            raise NotImplementedError()


class GeneChainSegment(Enum):
    TRAV = 0
    TRAJ = 1
    TRBV = 2
    TRBD = 3
    TRBJ = 4
    TRGV = 5
    TRGJ = 6
    TRDV = 7
    TRDD = 8
    TRDJ = 9

    @staticmethod
    def __str_abbreviated__(geneChainSegment):
        s = str(geneChainSegment)
        i = s.index('.')
        return s[i+1:]

    @staticmethod
    def get_gene_segment(geneChainSegment):
        if (geneChainSegment == GeneChainSegment.TRAV) or (geneChainSegment == GeneChainSegment.TRBV) or \
                (geneChainSegment == GeneChainSegment.TRGV) or (geneChainSegment == GeneChainSegment.TRDV):
            return GeneSegment.TRV
        elif (geneChainSegment == GeneChainSegment.TRAJ) or (geneChainSegment == GeneChainSegment.TRBJ) or \
                (geneChainSegment == GeneChainSegment.TRGJ) or (geneChainSegment == GeneChainSegment.TRDJ):
            return GeneSegment.TRJ
        elif (geneChainSegment == GeneChainSegment.TRBD) or (geneChainSegment == GeneChainSegment.TRDD):
            return GeneSegment.TRD
        else:
            raise NotImplementedError()

    @staticmethod
    def get_chain(geneChainSegment):
        if (geneChainSegment == GeneChainSegment.TRAV) or (geneChainSegment == GeneChainSegment.TRAJ):
            return Chain.TRA
        elif (geneChainSegment == GeneChainSegment.TRBV) or (geneChainSegment == GeneChainSegment.TRBJ) or \
                (geneChainSegment == GeneChainSegment.TRBD):
            return Chain.TRB
        elif (geneChainSegment == GeneChainSegment.TRGV) or (geneChainSegment == GeneChainSegment.TRGJ):
            return Chain.TRG
        elif (geneChainSegment == GeneChainSegment.TRDV) or (geneChainSegment == GeneChainSegment.TRDJ) or \
                (geneChainSegment == GeneChainSegment.TRDD):
            return Chain.TRD
        else:
            raise NotImplementedError()


class TCellType(Enum):
    AB = 0
    GD = 1


class ChainCopy(Enum):
    First = 1
    Second = 2


class Chain(Enum):
    TRA = 0
    TRB = 1
    TRG = 2
    TRD = 3

    @staticmethod
    def __str_abbreviated__(chain):
        s = str(chain)
        i = s.index('.')
        return s[i+1:]

    @staticmethod
    def get_tcell_type(chain):
        if chain == Chain.TRA or chain == Chain.TRB:
            return TCellType.AB
        elif chain == Chain.TRG or chain == Chain.TRD:
            return TCellType.GD
        else:
            raise NotImplementedError()

    @staticmethod
    def get_v_gene(chain):
        if chain == Chain.TRA:
            return GeneChainSegment.TRAV
        elif chain == Chain.TRB:
            return GeneChainSegment.TRBV
        elif chain == Chain.TRG:
            return GeneChainSegment.TRGV
        elif chain == Chain.TRD:
            return GeneChainSegment.TRDV
        else:
            raise NotImplementedError()

    @staticmethod
    def get_j_gene(chain):
        if chain == Chain.TRA:
            return GeneChainSegment.TRAJ
        elif chain == Chain.TRB:
            return GeneChainSegment.TRBJ
        elif chain == Chain.TRG:
            return GeneChainSegment.TRGJ
        elif chain == Chain.TRD:
            return GeneChainSegment.TRDJ
        else:
            raise NotImplementedError()


class IMGTSequenceGaps(Enum):
    No = 0
    Yes = 1


class ImmuneReceptorType(Enum):
    TCR = 0
    BCR = 1

