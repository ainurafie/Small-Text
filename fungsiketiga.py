def fungsiketiga(msg):
  from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
 
  analyzer = SentimentIntensityAnalyzer()
  # text_input = str(input("Masukkan Teks     : "))
  analisis = analyzer.polarity_scores(msg) 
  # print(analisis)
  if analisis['compound'] >= 0.05:
    return "Teks ini bersifat Positif"
  elif analisis['compound'] <= -0.05:
    return "Teks ini bersifat Negatif"
  else:
    return "Teks ini bersifat Netral"
 
# fungsiketiga()