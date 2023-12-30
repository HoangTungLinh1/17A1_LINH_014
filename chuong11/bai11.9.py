def party_late(arrivals, name):
    so_khach_den=arrivals.index(name)
    so_luong_toi_da_khach_muon=len(arrivals)//2
    if so_khach_den>=so_luong_toi_da_khach_muon and so_khach_den !=len(arrivals) - 1:
        return True
    else:
        return False
arrivals = ['Adela', 'Fleda', 'Owen', 'May', 'Mona', 'Gilbert', 'Ford']
print(party_late(arrivals,name='Gilbert'))
print(party_late(arrivals,name='Ford'))
print(party_late(arrivals,name='Mona'))