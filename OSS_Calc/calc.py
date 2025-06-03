import tkinter as tk
from tkinter import simpledialog, messagebox


class Calculator:
    def __init__(self, root):
        self.root = root
        self.root.title("계산기")
        self.root.geometry("300x450")

        self.expression = ""

        # 입력창
        self.entry = tk.Entry(root, font=("Arial", 24), justify="right")
        self.entry.pack(fill="both", ipadx=8, ipady=15, padx=10, pady=10)

        # 버튼 생성
        buttons = [
            ['7', '8', '9', '/'],
            ['4', '5', '6', '*'],
            ['1', '2', '3', '-'],
            ['0', '.', 'BMI', '+'],
            ['C', '=']
        ]

        for row in buttons:
            frame = tk.Frame(root)
            frame.pack(expand=True, fill="both")
            for char in row:
                btn = tk.Button(
                    frame,
                    text=char,
                    font=("Arial", 18),
                    command=lambda ch=char: self.on_click(ch)
                )
                btn.pack(side="left", expand=True, fill="both")

    def on_click(self, char):
        if char == 'C':
            self.expression = ""
        elif char == '=':
            try:
                self.expression = str(eval(self.expression))
            except Exception:
                self.expression = "에러"
        elif char == 'BMI':
            self.calculate_bmi()
        else:
            self.expression += str(char)

        self.entry.delete(0, tk.END)
        self.entry.insert(tk.END, self.expression)

    def calculate_bmi(self):
        try:
            height_cm = simpledialog.askfloat("BMI 계산", "키(cm)를 입력하세요:")
            if height_cm is None:
                return
            weight_kg = simpledialog.askfloat("BMI 계산", "몸무게(kg)를 입력하세요:")
            if weight_kg is None:
                return

            height_m = height_cm / 100
            bmi = weight_kg / (height_m ** 2)
            bmi = round(bmi, 2)

            result = f"당신의 BMI는 {bmi}입니다."

            # 간단한 분류
            if bmi < 18.5:
                result += " (저체중)"
            elif bmi < 23:
                result += " (정상)"
            elif bmi < 25:
                result += " (과체중)"
            else:
                result += " (비만)"

            messagebox.showinfo("BMI 결과", result)
        except Exception as e:
            messagebox.showerror("오류", f"BMI 계산 중 오류 발생: {e}")
