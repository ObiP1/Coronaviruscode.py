import requests
CountryPercentages = {'China': 0.0000560951, 'South Korea': 0.0001434, 'Italy': 0.00012194, 'Iran': 0.0000809, 'France': 0.00001852, 'Germany': 0.00001241, 'Spain': 0.00001442, 'USA': 0.00000167, 'United States': 0.00000167, 'United States of America': 0.00000167, 'Japan': 0.00000397, 'Switzerland': 0.00003836, 'UK': 0.0000041, 'United Kingdom': 0.0000041, 'Netherlands': 0.00001547, 'Sweden': 0.0000201, 'Belgium': 0.00001726, 'Norway': 0.00003246, 'Singapore': 0.00002564, 'Hong Kong': 0.00001533, 'Austria': 0.00001154, 'Malaysia': 0.00000306, 'Australia': 0.00000365, 'Bahrain': 0.00005, 'Greece': 0.000007, 'Canada': 0.00000175, 'Kuwait': 0.00001499, 'Iraq': 0.00000149, 'Iceland': 0.00016997, 'Egypt': 0.00000054, 'Thailand': 0.00000072, 'Taiwan': 0.00000189, 'UAE': 0.00000455, 'United Arab Emirates': 0.00000455, 'India': 0.000000028985415, 'Israel': 0.00000451, 'San Marino': 0.00106167, 'Denmark': 0.00000604, 'Czechia': 0.00000299, 'Czech Republic': 0.00000299, 'Lebanon': 0.00000469, 'Portugal': 0.00000294, 'Vietnam': 0.00000031, 'Brazil': 0.00000012, 'Finland': 0.00000451, 'Ireland': 0.00000425, 'Algeria': 0.00000046, 'Palestine': 0.00000376, 'Russia': 0.00000012, 'Oman': 0.00000313, 'Slovenia': 0.0000077, 'Ecuador': 0.00000085, 'Georgia': 0.00000376, 'Qatar': 0.00000521, 'Romania': 0.00000078, 'Saudi Arabia': 0.00000043, 'Argentina': 0.00000027, 'Croatia': 0.00000292, 'Macao': 0.0000154, 'Estonia': 0.00000753, 'Chile': 0.00000052, 'Azerbaijan': 0.00000089, 'Costa Rica': 0.00000177, 'Hungary': 0.00000093, 'Slovakia': 0.00000147, 'Mexico': 0.00000005, 'Pakistan': 0.00000003, 'Peru': 0.00000021, 'South Africa': 0.00000012, 'Belarus': 0.00000063, 'Latvia': 0.00000318, 'Dominican Republic': 0.00000046, 'Luxembourg': 0.00000799, 'New Zealand': 0.00000104, 'Tunisia': 0.00000042, 'French Guiana': 0.0000168, 'Afghanistan': 0.0000001, 'North Macedonia': 0.00000192, 'Senegal': 0.00000024, 'Bulagaria': 0.00000058, 'Maldives': 0.0000074, 'Bangladesh': 0.00000002, 'Bosnia and Herzegovnia': 0.00000091, 'Bosnia Herzegovnia': 0.00000091, 'Colombia': 0.00000006, 'Malta': 0.00000679, 'Cambodia': 0.00000012, 'Morocco': 0.00000005, 'Nigeria': 0.0000000097, 'Albania': 0.00000069, 'Cameroon': 0.00000008, 'Faeroe Islands': 0.00004098, 'Martinique': 0.00000533}
print("Welcome! There is a global epidemic of a disease called Coronavirus. We want to inform you of your proabability of contracting the virus.")
Response1 = input("Would you like to know your proabability of contracting the virus? (Enter Y for yes and N for no): ")
Answer = ""

def question_prompt():
  print(Response1)
  if Response1 == "Y" or Response1 == "y":
    Answer = input("Which country do you reside in?(Capitalize your first letter of each word): ")
  return Answer

if Response1 == "Y" or Response1 == "y":
  Answer = question_prompt()
  print("{:.7%}".format(CountryPercentages[Answer]))

print("Thanks for running the program! Please remember to wash your hands")