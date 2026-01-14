from datetime import date, datetime
def calculate_age(self):
    
    if isinstance(self.birthday, str):
        #Kiểm tra chuỗi có đúng định dạng ngày tháng không
        try:
            birthday = datetime.strptime(self.birthday, "%d/%m/%Y").date()
        except ValueError:
            raise ValueError("Invalid date format. Please use DD/MM/YYYY.")
    elif isinstance(self.birthday, date):
         birthday = self.birthday
    else:
        raise TypeError("Birthday must be a string in DD/MM/YYYY format or a date object.")
    today = date.today()
    age = today.year - birthday.year - ((today.month, today.day) < (birthday.month, birthday.day))
    return age