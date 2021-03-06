import astropy.io.fits as fits
import numpy

class FitsHandler(object):
    """docstring for FitsHandler.
    fitsデータのオープンや変換，書き出しなどを担う∊"""

    def __init__(self, FitsPath):
        self.FitsPath = FitsPath

    def open_fits(self):
        hdulist = fits.open(self.FitsPath)
        # オープンした結果は中身が1つのリスト形式であるため
        self.hdulist = hdulist[0]


    def header(self):
        header = fits.getheader(self.FitsPath)
        self.header = header
        return header

    def data(self):
        data = fits.getdata(self.FitsPath)
        self.data = data
        return data
