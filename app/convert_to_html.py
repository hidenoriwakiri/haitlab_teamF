import csv

tab = "  "
with open("bill.csv", "r") as f:
    with open("table.html", "w") as g:
        reader = csv.reader(f)
        g.write("<!DOCTYPE html>\n<html>\n")
        g.write("<head>\n")
        g.write(tab+'<meta charset="utf-8">\n')
        g.write("</head>\n")
            
        g.write("<body>\n")
        g.write(tab+"<table width = '1000' height = '500'>\n") #tableのwidthとheightを設定できます
        for row in reader:
            g.write(tab+tab+"<tr>\n")
            count = 1
            
            for x in row:
                if count == 1:
                    g.write(tab+tab+tab+"<th>"+x+"</th>\n")
                else:
                    g.write(tab+tab+tab+"<td>"+x+"</td>\n")
                count += 1
                
            g.write(tab+tab+"</tr>\n")
        
        g.write(tab+"</table>\n")
        
        g.write("</body>\n")