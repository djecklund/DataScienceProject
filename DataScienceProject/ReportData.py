class CityStatePayments():
    def __init__(self, provider_city, provider_state, avg_total_payment, num_payments):
        self.provider_city = provider_city
        self.provider_state = provider_state
        self.avg_total_payment = avg_total_payment
        self.num_payments = num_payments

class ProviderPayments():
    def __init__(self, provider_name, provider_city, provider_state, avg_total_payment, num_payments):
        self.provider_name = provider_name
        self.provider_city = provider_city
        self.provider_state = provider_state
        self.avg_total_payment = avg_total_payment
        self.num_payments = num_payments

class StatePayments():
    def __init__(self, provider_state, avg_total_payment, num_payments):
        self.provider_state = provider_state
        self.avg_total_payment = avg_total_payment
        self.num_payments = num_payments

class DRGDefPayments():
    def __init__(self, drg_definition, avg_total_payment, num_payments):
        self.drg_definition = drg_definition
        self.avg_total_payment = avg_total_payment
        self.num_payments = num_payments
