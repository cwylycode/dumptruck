#Oh look...something actually useful
def convert_temperature(temp=0,from_scale="C",to_scale="F",rounding=1):
    """Convert and return the supplied temperature in a different scale.
    \n'C','F','K','R' = Celsius,Fahrenheit,Kelvin,Rakine
    \n'A' = All temperature conversions as a list (only used with 'to_scale')
    \n'rounding' = Round all temperatures to the nearest decimal place"""

    scales = ["C","F","K","R","A"]
    if from_scale not in scales[:-1] or to_scale not in scales:return "Invalid scale input"
    if from_scale == "C":temps = [temp,(9/5)*temp+32,temp+273.15,(9/5)*(temp+273.15)]
    if from_scale == "F":temps = [(temp-32)*(5/9),temp,(temp+459.67)*(5/9),temp+459.67]
    if from_scale == "K":temps = [temp-273.15,(temp*(9/5)-459.67),temp,temp*(9/5)]
    if from_scale == "R":temps = [(temp-491.67)*(5/9),temp-459.67,temp*(5/9),temp]
    temps = list(map(lambda x:round(float(x),int(rounding)),temps))

    for i,scale in enumerate(scales):
        if to_scale == "A":return temps
        if to_scale == scale:return temps[i]