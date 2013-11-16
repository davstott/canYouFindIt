import math, ngramQuery

cipher = "AWVLI QIQVT QOSQO ELGCV IIQWD LCUQE EOENN WWOAO LTDNU QTGAW TSMDO QTLAO QSDCH PQQIQ DQQTQ OOTUD BNIQH BHHTD UTEET FDUEA UMORE SQEQE MLTME TIREC LICAI QATUN QRALT ENEIN RKG".replace(" ", "").replace("Q"," ")

for key in range(1,15):
  plain = ""
  rowLength = int(math.ceil(float(len(cipher)) / key))
  for i in range(rowLength):
    while (i < len(cipher)):
      plain = plain + cipher[i]
      i += rowLength
  print key, int(ngramQuery.getProb(plain, (2,))), plain[:60]
