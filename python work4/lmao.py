txt="Ботнет IPStorm в который ранее входили лишь Windows-машины, увеличился до 13 500 зараженных систем"
txt1=len(txt)
lower=txt.lower()
upper=txt.upper()
cut_len=txt1-(txt1//2)
println=lower[:cut_len]+upper[cut_len:]
print(println)