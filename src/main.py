from functions import FitsHandler


handler = FitsHandler("../sample_datas/sample.fits")
handler.open_fits()
print(handler.header())
