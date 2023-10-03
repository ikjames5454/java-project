from menstrual import Menstrual


class MenstrualApp:
    menstrual = Menstrual()

    def menu(self):
        try:
            self.output("WELCOME TO SIMPLE MENSTRUAL APP")
            option = self.inputFunction("Enter one to continue: ")
            if option == "1":
                self.menstrualMenu()
            else:
                self.menu()
        except (ValueError,KeyboardInterrupt):
            self.output("wrong action")
            self.menu()

    def menstrualMenu(self):
        option = self.inputFunction("""
         My beautiful ladies una don land, oya choose option
                1. Check beginning of flow date
                2. Check end of menstrual circle
                3. Check ovulation Date
                4. Check next safe Date
                5. exit
        Enter any of the option number:         
        """)
        match option:
            case "1":
                self.beginningOfDate()
            case "2":
                self.endOfMenstrualCircle()
            case "3":
                self.ovulationDate()
            case "4":
                self.safeDate()
            case "5":
                self.exit()
            case _:
                self.menstrualMenu()

    def beginningOfDate(self):
        try:
            lastPeriod = self.inputFunction("Enter the last date of period in this format: YY-MM-DD: ")
            circleDuration = int(self.inputFunction("Enter the duration of your circle: "))
            display = self.menstrual.check_next_flow_date(lastPeriod, circleDuration)
            self.output("your next flow date start: ")
            self.output(display)
            self.menstrualMenu()
        except Exception as e:
            self.output(e)
            self.beginningOfDate()

    def endOfMenstrualCircle(self):
        try:
            lastPeriod = self.inputFunction("Enter the last date of period in this format: YY-MM-DD: ")
            circleDuration = int(self.inputFunction("Enter the duration of your circle: "))
            display = self.menstrual.check_end_of_menstrual_cycle(lastPeriod, circleDuration)
            self.output("your menstrual circle ends at: ")
            self.output(display)
            self.output("so your period start a day after the end of your circle")
            self.menstrualMenu()
        except Exception as e:
            self.output(e)
            self.endOfMenstrualCircle()

    def ovulationDate(self):
        try:
            lastPeriod = self.inputFunction("Enter the last date of period in this format: YY-MM-DD: ")
            circleDuration = int(self.inputFunction("Enter the duration of your circle: "))
            display = self.menstrual.ovulation_date(lastPeriod, circleDuration)
            self.output("your ovulation date start at: ")
            self.output(display)
            self.output(
                "which last for a period of 24 hours, it start in between your circle that is half of your circle \n" +
                " duration, so you have a high percentage chance of getting pregnant, so thread carefully if you are not married and also if you are married \n"
                + "and tying to get pregnant, you can meet your husband now for steady intercourse")
            self.menstrualMenu()
        except Exception as e:
            self.output(e)
            self.ovulationDate()

    def safeDate(self):
        try:
            lastPeriod = self.inputFunction("Enter the last date of period in this format: YY-MM-DD: ")
            circleDuration = int(self.inputFunction("Enter the duration of your circle: "))
            display = self.menstrual.next_safe_date(lastPeriod, circleDuration)
            self.output("your safe date is: ")
            self.output(display)
            self.output("your safe date start 7 days before the end of your menstrual circle \n " +
                        "not hundred percent guaranteed, you fit still get belle, is not a reliable contraception \n," +
                        "Sperm can survive inside the female reproductive tract for a few days,");
            self.menstrualMenu()
        except Exception as e:
            self.output(e)
            self.safeDate()

    def output(self, output):
        print(output)

    def inputFunction(self, enter):
        entry = input(enter)
        return entry

    def main(self):
        self.menu()

    def exit(self):
        pass


if __name__ == "__main__":
    menstrual = MenstrualApp()
    menstrual.main()
