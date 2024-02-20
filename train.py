def upcoming_birthdays(address_book, days):
        current_date = datetime.now().date()
        upcoming_date = current_date + timedelta(days=days)

        upcoming_birthdays_list = []

        for contact in address_book.values():
            birthday_date = contact.get_birthday_date()

            if birthday_date:
                birthday_date = birthday_date.replace(year=upcoming_date.year)

            if birthday_date == upcoming_date:
                upcoming_birthdays_list.append(contact)

        return upcoming_birthdays_list


  def save_to_file(self, filename = 'cash.bin'):
        with open (filename, 'wb') as file:
            pickle.dump(self.data, file)

    def open_from_file(self, filename = 'cash.bin'):
        try: 
            with open (filename, 'rb') as file:
                self.data = pickle.load(file)
        except FileNotFoundError:
            print('Cash not found. Create new Address Book')