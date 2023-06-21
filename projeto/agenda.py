import sys
import psycopg2
import calendar
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QTableWidget, QTableWidgetItem, QPushButton, QLineEdit

class AgendaApp(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Agenda")
        self.setGeometry(100, 100, 500, 400)

        self.central_widget = QWidget(self)
        self.setCentralWidget(self.central_widget)

        self.layout = QVBoxLayout(self.central_widget)

        self.table_widget = QTableWidget()
        self.table_widget.setColumnCount(5)
        self.table_widget.setHorizontalHeaderLabels(['Código', 'Nome', 'Telefone', 'Data', 'Evento'])
        
        
        
        self.layout.addWidget(self.table_widget)

        self.input_codigo   = QLineEdit()
        self.input_nome     = QLineEdit()
        self.input_telefone = QLineEdit()
        self.input_data     = QLineEdit()
        self.input_evento   = QLineEdit()
        self.btn_add = QPushButton("Adicionar Evento")

        self.layout.addWidget(self.input_codigo)
        self.layout.addWidget(self.input_nome)
        self.layout.addWidget(self.input_telefone)
        self.layout.addWidget(self.input_data)
        self.layout.addWidget(self.input_evento)
        self.layout.addWidget(self.btn_add)

        self.btn_add.clicked.connect(self.add_event)
        
        self.db_connection = psycopg2.connect(
            host="localhost",
            port="5432",
            database="Projeto",
            user="postgres",
            password="89iokl,."
        )

    def add_event(self):
        
        codigo   = self.input_codigo.text()
        nome     = self.input_nome.text()
        telefone = self.input_telefone.text()
        data     = self.input_data.text()
        evento   = self.input_evento.text()
        
        
        row_count = self.table_widget.rowCount()
        self.table_widget.insertRow(row_count)

        cursor = self.db_connection.cursor()
        cursor.execute("INSERT INTO public.contatos(codigo, nome, telefone, data, evento)VALUES (%s, %s, %s,%s,%s)", (codigo, nome, telefone, data, evento))
        self.db_connection.commit()
        cursor.close()

        row_count = self.table_widget.rowCount()
        self.table_widget.insertRow(row_count)
        
        self.table_widget.setItem(row_count, 1, QTableWidgetItem(codigo))
        self.table_widget.setItem(row_count, 2, QTableWidgetItem(nome))
        self.table_widget.setItem(row_count, 3, QTableWidgetItem(telefone))
        self.table_widget.setItem(row_count, 4, QTableWidgetItem(data))
        self.table_widget.setItem(row_count, 5, QTableWidgetItem(evento))
 
        self.input_codigo.clear()
        self.input_nome.clear()
        self.input_telefone.clear()
        self.input_data.clear()
        self.input_evento.clear()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    agenda = AgendaApp()
    agenda.show()
    sys.exit(app.exec_())
