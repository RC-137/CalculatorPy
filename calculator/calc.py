import webview

class CalculatorAPI:
    def __init__(self):
        self.expression = "0"
        self.lastPoint = False

    def press(self, value):
        # Clear button
        if value == "C":
            self.expression = "0"
            return self.expression
        
        elif value == "=":
            if value == '.':
                last_number = self.expression.split('+')[-1].split('-')[-1].split('*')[-1].split('/')[-1]
                if '.' in last_number:
                 return self.expression
                
            while self.expression and self.expression[-1] in "+-*/":
                self.expression = self.expression[:-1]

            if not self.expression:
                self.expression = "0"
                return self.expression

            try:
                result = str(eval(self.expression))
                self.expression = result
                return result
            
            except:
                self.expression = "0"
                return self.expression

        else:
         if value == '.':
                last_number = self.expression.split('+')[-1].split('-')[-1].split('*')[-1].split('/')[-1]
                if '.' in last_number:
                    return self.expression

                if self.expression == "0" and value != '.':
                 self.expression = value
                else:
                 self.expression += value
                return self.expression

         if self.expression == "0" and value != '.':
           self.expression = value
         else:
          self.expression += value
        return self.expression



if __name__ == "__main__":
    webview.create_window(
        "Calculator",
        "calc.html", 
        js_api=CalculatorAPI(),
        width=350,
        height=500
    )
    webview.start()
