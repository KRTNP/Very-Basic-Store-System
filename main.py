class Handkerchief:
    def __init__(self, style, color, quantity):
        self.style = style
        self.color = color
        self.quantity = quantity

    def calculate_price(self):
        style_prices = {"Plain": 5, "Printed": 7, "Embroidered": 10}
        base_price = style_prices[self.style]
        if len(self.color) == 2:
            base_price += 3  # Additional charge for pairing colors
        return base_price * self.quantity


def main():
    styles = ["Plain", "Printed", "Embroidered"]
    colors = ["Red", "Blue", "Green", "Yellow", "Black", "White", "Pink", "Orange", "Purple", "Brown", "Gray", "Cyan"]

    while True:
        print("Welcome to the Handkerchief Shop!")
        print("Choose a style:")
        for i, style in enumerate(styles):
            print(f"{i + 1}. {style}")
        
        style_choice = int(input("Enter the number corresponding to your choice: "))
        selected_style = styles[style_choice - 1]

        print("Choose a color:")
        for i, color in enumerate(colors):
            print(f"{i + 1}. {color}")

        color_choice1 = int(input("Enter the number corresponding to your first color choice: "))
        color_choice2 = int(input("Enter the number corresponding to your second color choice (optional, enter 0 to skip): "))
        selected_color1 = colors[color_choice1 - 1]
        selected_color2 = None if color_choice2 == 0 else colors[color_choice2 - 1]
        selected_color = [selected_color1]
        if selected_color2:
            selected_color.append(selected_color2)

        quantity = int(input("Enter the quantity: "))

        handkerchief = Handkerchief(selected_style, selected_color, quantity)
        total_price = handkerchief.calculate_price()
        print(f"Total price for {quantity} {selected_style} handkerchief(s) with color(s) {', '.join(selected_color)}: ${total_price}")

        buy_again = input("Do you want to buy anything else? (y/n): ")
        if buy_again.lower() != 'y':
            print("Thank you for shopping with us!")
            break


if __name__ == "__main__":
    main()
