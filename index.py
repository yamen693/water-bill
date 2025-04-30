class WaterBill:
    def __init__(self, person_names, initial_bills):
        self.persons = {name: {'unpaid': initial_bills.get(name, 0), 'bill': 0} for name in person_names}
        self.total_bill = 0
        self.individual_share = 0
        self.remaining_after_old = 0

    def show_old_bills(self):
        print("\n📌 Old unpaid bills per person:")
        for name, info in self.persons.items():
            print(f"{name}: {info['unpaid']} EGP")

    def total_unpaid_amount(self):
        return sum(info['unpaid'] for info in self.persons.values())

    def set_total_bill(self, total_amount):
        self.total_bill = total_amount

        
        total_old_unpaid = self.total_unpaid_amount()
        print(f"\n📊 Total unpaid from previous bills: {total_old_unpaid:.2f} EGP")

        
        self.remaining_after_old = abs(total_amount - total_old_unpaid)
        print(f"🧮 Difference between new bill and unpaid total: {self.remaining_after_old:.2f} EGP")


        self.individual_share = self.remaining_after_old / len(self.persons)

    def display_amounts_due(self):
        print("\n💧 Each person should pay this amount from the new bill (after adjustment):")
        for name in self.persons:
            print(f"{name}: {self.individual_share:.2f} EGP")

        print("\n📌 Total amount each person should pay (new share + old unpaid):")
        for name, info in self.persons.items():
            total_due = info['unpaid'] + self.individual_share
            print(f"{name}: {total_due:.2f} EGP")


persons = ["Abdelmged", "Ahmed Saeed", "Mohamed Senary", "Mohamed Ahmed", "Om Omar", "Hossam Kassem"]
initial_bills = {
    "Abdelmged": 1420,
    "Ahmed Saeed": 1420,
    "Mohamed Senary": 0,
    "Mohamed Ahmed": 770,
    "Om Omar": 770,
    "Hossam Kassem": 0,
}


water_bill = WaterBill(persons, initial_bills)

water_bill.show_old_bills()

total_amount = float(input("\n💰 Enter the new total water bill amount: "))
water_bill.set_total_bill(total_amount)


water_bill.display_amounts_due()
