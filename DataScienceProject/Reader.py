from ReportData import *
import xlrd
import xlsxwriter

class Reader():

    def read(self):
        file = ("Input/Data Science Report.xlsx")
        wb = xlrd.open_workbook(file)
        sheet = wb.sheet_by_index(0)

        cityStatePayments = []
        providerPayments = []
        statePayments = []
        drgDefPayments = []

        for i in range(sheet.nrows):
            if sheet.cell_value(i,0).startswith('189') or sheet.cell_value(i,0).startswith('207') or sheet.cell_value(i,0).startswith('208') \
                    or sheet.cell_value(i,0).startswith('312') or sheet.cell_value(i,0).startswith('313')\
                    or sheet.cell_value(i,0).startswith('885'):
                drg_definition = sheet.cell_value(i,0)
                provider_name = sheet.cell_value(i,2)
                provider_city = sheet.cell_value(i,4)
                provider_state = sheet.cell_value(i,5)
                avg_total_payment = float(sheet.cell_value(i,10))

                if cityStatePayments.__len__() == 0:
                    cityStatePayments.append(CityStatePayments(provider_city, provider_state, float(avg_total_payment), 1))
                else:
                    check = False
                    for x in range(0,cityStatePayments.__len__()):
                        if provider_city == cityStatePayments[x].provider_city and provider_state == cityStatePayments[x].provider_state:
                            cityStatePayments[x].avg_total_payment = cityStatePayments[x].avg_total_payment + avg_total_payment
                            cityStatePayments[x].num_payments = cityStatePayments[x].num_payments + 1
                            check = True
                            break

                    if not check:
                        cityStatePayments.append(CityStatePayments(provider_city, provider_state, float(avg_total_payment), 1))


                if providerPayments.__len__() == 0:
                    providerPayments.append(ProviderPayments(provider_name, provider_city, provider_state, float(avg_total_payment), 1))
                else:
                    check = False
                    for x in range(0,providerPayments.__len__()):
                        if provider_name == providerPayments[x].provider_name and provider_city == providerPayments[x].provider_city and provider_state == providerPayments[x].provider_state:
                            providerPayments[x].avg_total_payment = providerPayments[x].avg_total_payment + avg_total_payment
                            providerPayments[x].num_payments = providerPayments[x].num_payments + 1
                            check = True
                            break

                    if not check:
                        providerPayments.append(ProviderPayments(provider_name, provider_city, provider_state, float(avg_total_payment), 1))


                if statePayments.__len__() == 0:
                    statePayments.append(StatePayments(provider_state, float(avg_total_payment), 1))
                else:
                    check = False
                    for x in range(0,statePayments.__len__()):
                        if provider_state == statePayments[x].provider_state:
                            statePayments[x].avg_total_payment = statePayments[x].avg_total_payment + avg_total_payment
                            statePayments[x].num_payments = statePayments[x].num_payments + 1
                            check = True
                            break

                    if not check:
                        statePayments.append(StatePayments(provider_state, float(avg_total_payment), 1))


                if drgDefPayments.__len__() == 0:
                    drgDefPayments.append(DRGDefPayments(drg_definition, float(avg_total_payment), 1))
                else:
                    check = False
                    for x in range(0,drgDefPayments.__len__()):
                        if drg_definition == drgDefPayments[x].drg_definition:
                            drgDefPayments[x].avg_total_payment = drgDefPayments[x].avg_total_payment + avg_total_payment
                            drgDefPayments[x].num_payments = drgDefPayments[x].num_payments + 1
                            check = True
                            break

                    if not check:
                        drgDefPayments.append(DRGDefPayments(drg_definition, float(avg_total_payment), 1))

        for x in range(0,cityStatePayments.__len__()):
            cityStatePayments[x].avg_total_payment = cityStatePayments[x].avg_total_payment / cityStatePayments[x].num_payments

        for x in range(0,providerPayments.__len__()):
            providerPayments[x].avg_total_payment = providerPayments[x].avg_total_payment / providerPayments[x].num_payments

        for x in range(0,statePayments.__len__()):
            statePayments[x].avg_total_payment = statePayments[x].avg_total_payment / statePayments[x].num_payments

        for x in range(0,drgDefPayments.__len__()):
            drgDefPayments[x].avg_total_payment = drgDefPayments[x].avg_total_payment / drgDefPayments[x].num_payments

        cityStatePayments.sort(key=lambda x: x.avg_total_payment, reverse=True)
        providerPayments.sort(key=lambda x: x.avg_total_payment, reverse=True)
        statePayments.sort(key=lambda x: x.avg_total_payment, reverse=True)
        drgDefPayments.sort(key=lambda x: x.avg_total_payment, reverse=True)

        # workbook for CityState
        workbook = xlsxwriter.Workbook("./Output/Research Summary.xlsx")
        cityStateSheet = workbook.add_worksheet("City State Summary")
        providerSheet = workbook.add_worksheet("Provider Summary")
        stateSheet = workbook.add_worksheet("State Summary")
        drgDefSheet = workbook.add_worksheet("DRGDefPayments Summary")

        bold = workbook.add_format({'bold': True})
        cityStateSheet.write(0,0,"Provider City", bold)
        cityStateSheet.write(0,1,"Provider State", bold)
        cityStateSheet.write(0,2,"Provider Average Medicare Payment", bold)

        for x in range(0,cityStatePayments.__len__()):
            cityStateSheet.write(x+1, 0, cityStatePayments[x].provider_city)
            cityStateSheet.write(x+1, 1, cityStatePayments[x].provider_state)
            cityStateSheet.write(x+1, 2, '${:,.2f}'.format(cityStatePayments[x].avg_total_payment))

        providerSheet.write(0,0,"Provider Name", bold)
        providerSheet.write(0,1,"Provider City", bold)
        providerSheet.write(0,2,"Provider State", bold)
        providerSheet.write(0,3,"Provider Average Medicare Payment", bold)

        for x in range(0,providerPayments.__len__()):
            providerSheet.write(x+1, 0, providerPayments[x].provider_name)
            providerSheet.write(x+1, 1, providerPayments[x].provider_city)
            providerSheet.write(x+1, 2, providerPayments[x].provider_state)
            providerSheet.write(x+1, 3, '${:,.2f}'.format(providerPayments[x].avg_total_payment))

        stateSheet.write(0,0,"Provider State", bold)
        stateSheet.write(0,1,"Provider Average Medicare Payment", bold)

        for x in range(0,statePayments.__len__()):
            stateSheet.write(x+1, 0, statePayments[x].provider_state)
            stateSheet.write(x+1, 1, '${:,.2f}'.format(statePayments[x].avg_total_payment))

        drgDefSheet.write(0,0,"Diagnosis", bold)
        drgDefSheet.write(0,1,"Provider Average Medicare Payment", bold)

        for x in range(0,drgDefPayments.__len__()):
            drgDefSheet.write(x+1, 0, drgDefPayments[x].drg_definition)
            drgDefSheet.write(x+1, 1, '${:,.2f}'.format(drgDefPayments[x].avg_total_payment))

        workbook.close()
