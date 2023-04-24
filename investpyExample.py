import investpy

calendar = investpy.economic_calendar(
    countries=['united states'],
    importances=['high'],
    from_date='01/01/2022',
    to_date='30/01/2022'
)

for event in calendar['Event'].values:
    if 'EUR/USD' in event:
        print('Title:', event['title'])
        print('Forecast:', event['forecast'])
        print('Actual:', event['actual'])
        print()

