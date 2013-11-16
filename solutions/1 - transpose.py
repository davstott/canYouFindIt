# turing
# turing.metro.co.uk or metro.co.uk/turing
import math
cipher = "WDVFEIELASRERCEEEOD"
key = 5


cipher = "AWVLI QIQVT QOSQO ELGCV IIQWD LCUQE EOENN WWOAO LTDNU QTGAW TSMDO QTLAO QSDCH PQQIQ DQQTQ OOTUD BNIQH BHHTD UTEET FDUEA UMORE SQEQE MLTME TIREC LICAI QATUN QRALT ENEIN RKG"
cipher = cipher.replace(" ", "")
cipher = cipher.replace("Q", " ")
key = 11


plain = ""
rowLength = int(math.ceil(float(len(cipher)) / key))
for i in range(rowLength):
  while (i < len(cipher)):
    plain = plain + cipher[i]
    i += rowLength

print plain
