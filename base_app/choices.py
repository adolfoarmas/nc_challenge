
CREDIT_CARD = 'CC'
DEBT_CARD = 'DC'
CASH = 'CS'

PAYMENT_METHOD = (
    ('CC', 'Credit Card'),
    ('DC', 'Debt Card'),
    ('CS', 'Cash')
)

PAID = 'PD'
PENDING = 'PG'
IN_CLAIM = 'IC'

PAYMENT_STATUS = (
        (PAID, 'Paid'),
        (PENDING, 'Pending'),
        (IN_CLAIM, 'In Claim'),
    )

GAS = 'FAS'
ELECTRIC_SERVICE = 'ELE'
COMMUNICATIONS_SERVICE = 'COM'
TOLL_SERVCE = 'TLL'


SERVICE_TYPE = (
        (GAS, 'Gas Service'),
        (ELECTRIC_SERVICE, 'Electric Energy Service'),
        (COMMUNICATIONS_SERVICE, 'TV/Phone/Internet'),
        (TOLL_SERVCE, 'Toll Service')
    )

"""
CURRENCY = (
    ('USD', 'US Dolars'),
    ('ARS', 'Argentinian Pesos'),
    ('MX', 'Mexican Pesos'),
)
"""
