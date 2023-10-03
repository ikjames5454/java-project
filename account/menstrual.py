from datetime import datetime, timedelta


class Menstrual:

    def check_next_flow_date(self, last_period, cycle_duration):
        specified_date = self.parse_date(last_period)
        specific_date = datetime.strptime(specified_date, "%Y-%m-%d")
        return specific_date + timedelta(days=cycle_duration + 1)

    def check_end_of_menstrual_cycle(self, last_period, cycle_duration):
        specified_date = self.parse_date(last_period)
        specific_date = datetime.strptime(specified_date, "%Y-%m-%d")
        return specific_date + timedelta(days=cycle_duration)

    def ovulation_date(self, last_period, menstrual_cycle_duration):
        specified_date = self.parse_date(last_period)
        specific_date = datetime.strptime(specified_date, "%Y-%m-%d")
        return specific_date + timedelta(days=menstrual_cycle_duration // 2)

    def next_safe_date(self, last_period, menstrual_cycle_duration):
        specified_date = self.parse_date(last_period)
        specific_date = datetime.strptime(specified_date, "%Y-%m-%d")
        return specific_date + timedelta(days=menstrual_cycle_duration - 7)

    @staticmethod
    def parse_date(date):
        try:
            datetime.strptime(date, "%Y-%m-%d")
            return date
        except ValueError:
            raise ValueError("Invalid Date Format")
