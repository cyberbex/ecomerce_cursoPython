def formata_preco(val):
    if val:
        return f'R$ {val:.2f}'.replace('.',',')
    return 'none'