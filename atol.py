from libfptr10 import IFptr
#try to find atol dll at default path

#SetSettings For ATOL DEVICE

class ConnectDevice():
    def __init__(self):
        self.state = 0
        self.fptr = IFptr("")
        self.model = IFptr.LIBFPTR_MODEL_ATOL_AUTO
        self.port = IFptr.LIBFPTR_PORT_COM
        self.path = "auto"
        self.baudrate = IFptr.LIBFPTR_PORT_BR_115200

        self.settings = {
        self.fptr.LIBFPTR_SETTING_MODEL: self.model,
        self.fptr.LIBFPTR_SETTING_PORT: self.port,
        self.fptr.LIBFPTR_SETTING_USB_DEVICE_PATH: self.path,
        self.fptr.LIBFPTR_SETTING_BAUDRATE: self.baudrate
            }

#0 Already opened
#-1 Port zanyat
#1
    def opendevice(self):
        self.fptr.open()
        self.state = self.fptr.isOpened()
        if self.state == 1:
           print('Connected') 
           return self.state
        elif self.state == -1:
            print('port zanyat')
            return self.state
        else: 
           print('Disconnected')
           return self.state
          

class PrintReports(ConnectDevice):
    def authorization(self, cashiername='Администратор', inn='12345678'):
        self.cashiername = cashiername
        self.inn = inn
    def xreport(self):
         print(self.state) 
         print(self.fptr.isOpened())
         self.fptr.setParam(IFptr.LIBFPTR_PARAM_REPORT_TYPE, IFptr.LIBFPTR_RT_X)
         self.fptr.report()
         print('X-REPORT COMPLETED')
         return ('Успешно распечатан Х отчёт') 
    
    def zreport(self):
            self.fptr.setParam(1021, self.cashiername)
            self.fptr.setParam(1203, self.inn)
            self.fptr.operatorLogin()
            self.fptr.setParam(IFptr.LIBFPTR_PARAM_REPORT_TYPE, IFptr.LIBFPTR_RT_CLOSE_SHIFT)
            self.fptr.report()
            self.fptr.checkDocumentClosed()
            print('Shift is closed')
            return('Смена закрыта')

    def openshift(self):
            self.fptr.setParam(1021, self.cashiername)
            self.fptr.setParam(1203, self.inn)
            self.fptr.operatorLogin()
            self.fptr.openShift()
            print('Shift is opened')
            return('Смена успешно открыта')


class FN(ConnectDevice):

    def dayfn(self):
        self.fptr.setParam(IFptr.LIBFPTR_PARAM_FN_DATA_TYPE, IFptr.LIBFPTR_FNDT_VALIDITY)
        self.fptr.fnQueryData()
        dateTime            = self.fptr.getParamDateTime(IFptr.LIBFPTR_PARAM_DATE_TIME)     
        s = dateTime
        return s

# f = PrintReports()
# f.opendevice()
