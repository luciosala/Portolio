def convert(seg, minu, hor):
    segundosTotales = 0
    segundosTotales += hor * 60 * 60
    segundosTotales += minu * 60
    segundosTotales += seg
    return segundosTotales
print(convert(100,1,3))