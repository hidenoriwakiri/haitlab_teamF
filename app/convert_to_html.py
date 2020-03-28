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
        g.write(tab+"<table width = '800' height = '350'>\n") #tableのwidthとheightを設定できます
        for row in reader:
            if row[0] == "計":
                 g.write(tab+tab+"<tr class='total'>\n")
            else:
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
        
        g.write("<style>\n")
        g.write("table {\n")
        g.write(tab+"text-align: center;\n")
        g.write("}\n")
        g.write("td, th { border: 2px solid #CCC; }\n")
        g.write(".total{\n")
        g.write(tab+"background-color: #F1F1F1;\n")
        g.write("}\n")
        g.write("</style>\n")
        
        g.write("</html>")