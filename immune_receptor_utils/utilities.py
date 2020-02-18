from immune_receptor_utils.enums import ImmuneReceptorType


def extract_tcr_gene_string(text, immuneReceptorType=ImmuneReceptorType.TCR):
    if immuneReceptorType == ImmuneReceptorType.TCR:
        start = text.find('TR')
        tmp = text.rfind('TR')
        if start == tmp:
            a_i = text[start:].find('*')
            if a_i == -1:
                space_i = text[start:].find(' ')
                if (space_i == -1) or (space_i > start + 13): raise ValueError('Immune receptor strings not found')
                end = space_i
            elif (a_i > 0) and (a_i < start + 13):
                end = start+a_i + 3
            else:
                raise ValueError('Immune receptor strings not found')
            out = text[start: end]
        else:
            raise ValueError('Multiple immune receptor strings found')
    else:
        raise NotImplementedError()
    return out
