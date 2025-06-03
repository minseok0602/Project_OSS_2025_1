import datetime
import csv
from expense import Expense

class Budget:
    def __init__(self):
        self.expenses = []

    def add_expense(self, category, description, amount):
        today = datetime.date.today().isoformat()
        expense = Expense(today, category, description, amount)
        self.expenses.append(expense)
        print("지출이 추가되었습니다.\n")

    def list_expenses(self):
        if not self.expenses:
            print("지출 내역이 없습니다.\n")
            return
        print("\n[지출 목록]")
        for idx, e in enumerate(self.expenses, 1):
            print(f"{idx}. {e}")
        print()

    def total_spent(self):
        total = sum(e.amount for e in self.expenses)
        print(f"총 지출: {total}원\n")

    def export_to_csv(self, filename="expenses.csv"):
        if not self.expenses:
            print("지출 내역이 없어 파일을 저장할 수 없습니다.\n")
            return

        with open(filename, mode="w", newline='', encoding="utf-8") as file:
            writer = csv.writer(file)
            writer.writerow(["날짜", "카테고리", "설명", "금액"])
            for e in self.expenses:
                writer.writerow([e.date, e.category, e.description, e.amount])

        print(f"지출 내역이 CSV 파일 '{filename}'로 저장되었습니다.\n")


