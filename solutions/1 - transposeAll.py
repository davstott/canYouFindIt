# turing
# turing.metro.co.uk or metro.co.uk/turing
import math

cipher = "AWVLI QIQVT QOSQO ELGCV IIQWD LCUQE EOENN WWOAO LTDNU QTGAW TSMDO QTLAO QSDCH PQQIQ DQQTQ OOTUD BNIQH BHHTD UTEET FDUEA UMORE SQEQE MLTME TIREC LICAI QATUN QRALT ENEIN RKG"
cipher = cipher.replace(" ", "")
#cipher = cipher.replace("Q", " ")
plain = []
plain.append("")
for key in range(1,20):
  plain.append("")
  rowLength = int(math.ceil(float(len(cipher)) / key))
  for i in range(rowLength):
    while (i < len(cipher)):
      plain[key] = plain[key] + cipher[i]
      i += rowLength
  print key, plain[key][:60]
