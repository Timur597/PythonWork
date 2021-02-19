txt='Ботнет IPStorm , в который ранее входили лишь Windows-машины, увеличился до 13 500 зараженных систем'
txt1=len(txt)
lower_case=txt.lower()
upper_case=txt.upper()
cut_len=txt1-(txt1//2)
printlen=lower_case[: cut_len]+upper_case[cut_len:]
print(printlen)