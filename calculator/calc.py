import webview
import tkinter as tk

class CalculatorAPI:
    def __init__(self):
        self.expression = "0"
        self.lastPoint = False

    def press(self, value):
        total_chars = len(self.expression.replace('\n', ''))
        max_chars = 50
        if total_chars >= max_chars:
            self.expression = "Can't enter more than 50 characters"
            return self.expression

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
    root = tk.Tk()
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    root.destroy()
    win_width = int(screen_width / 3)
    win_height = int(screen_height / 1.3)

    webview.create_window(
        "Calculator",
        "calc.html",
        js_api=CalculatorAPI(),
        width=win_width,
        height=win_height,
        resizable=True  
    )
    webview.start()
