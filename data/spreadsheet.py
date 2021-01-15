import xlsxwriter

class ExcelWriter():
    def __init__(self, filename):
        self.workbook = xlsxwriter.Workbook(filename)
        self.worksheet = self.workbook.add_worksheet()
        self.current_row = 0

    def write_headers(self, headers):
        for i in range(0, len(headers)):
            self.worksheet.write(self.current_row, i, headers[i])
        self.current_row = self.current_row + 1

    def write_model(self, model):
        cols = model.to_array()
        for i in range(0, len(cols)):
            self.worksheet.write(self.current_row, i, cols[i])
            self.current_row = self.current_row + 1

    def write_models(self, models):
        for model in models:
            self.write_model(model)

    def close(self):
        self.workbook.close()