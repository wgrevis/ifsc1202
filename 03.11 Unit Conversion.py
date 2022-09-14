fromvalue = float(input("Enter From Value: "))
fromunit = (input("Enter From Unit (in, ft, yd, mi): "))
tounit = (input("Enter To Unit (in, ft, yd, mi): "))
if fromunit != "in" and fromunit != "ft" and formunit != "yd" and fromunit != "mi" :
    print("From Unit is not valid. ")
else :
    if tounit != "in" and tounit != "ft" and tounit != "yd" and tounit != "mi" :
        print("To Unit is not valid. ")
    else:
        if fromunit == "in" and tounit == "in" :
            multiplier = 1.0
        if fromunit == "in" and tounit == "ft" : 
            multiplier = 0.08333333333333
        if fromunit == "in" and tounit == "yd" :
            multiplier = 0.02777777777778
        if fromunit == "in" and tounit == "mi" :
            mulitplier = 0.00001578282828283 

        if fromunit == "ft" and tounit == "in" :
            multiplier = 12.0
        if fromunit == "ft" and tounit == "ft" : 
            multiplier = 1.0
        if fromunit == "ft" and tounit == "yd" :
            multiplier = 0.3333333333333
        if fromunit == "ft" and tounit == "mi" :
            mulitplier = 0.0001893939393939 
        
        if fromunit == "yd" and tounit == "in" :
            multiplier = 36.0 
        if fromunit == "yd" and tounit == "ft" : 
            multiplier = 3.0
        if fromunit == "yd" and tounit == "yd" :
            multiplier = 1.0
        if fromunit == "yd" and tounit == "mi" :
            mulitplier = 0.0005681818181818 

        if fromunit == "mi" and tounit == "in" :
            multiplier = 63360.0
        if fromunit == "mi" and tounit == "ft" : 
            multiplier = 5280.0
        if fromunit == "mi" and tounit == "yd" :
            multiplier = 1760.0
        if fromunit == "mi" and tounit == "mi" :
            mulitplier = 1.0

        tovalue = round(fromvalue * multiplier , 7)
        print(fromvalue, fromunit, tovalue, tounit)