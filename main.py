from PIL import Image, ImageDraw, ImageFont

class Wallet:
    def __init__(self, name, money, logs: list = []):
        self.name = name
        self.money = money
        self.logs = logs
        
    def add_money(self, source, amount):
        self.logs.append((source, amount))
        self.money += amount
        
    def spend_money(self, reason, amount):
        self.logs.append((reason, -(amount))),
        self.money -= amount
        
    def display_logs(self):
        print(self.logs)
        
    def export_logs_to_png(self):
        FONT_SIZE = 30
        image = Image.new("RGB", (500, 500), color="white")
        draw = ImageDraw.Draw(image)
        font = ImageFont.load_default(size=FONT_SIZE)
        
        next_y_coordinate_available = 0
                
        for log in self.logs:
            draw.text((0, next_y_coordinate_available), f"{log[0]}: {log[1]}", fill="black", font=font)
            next_y_coordinate_available += FONT_SIZE

        image.save("output.png")
        
