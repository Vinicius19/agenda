import sys
import psycopg2
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QTableWidget, QTableWidgetItem, QDialog, QLabel, QVBoxLayout, QPushButton, QMenu, QAction, QLineEdit, QListWidget, QInputDialog


class EventDialog(QDialog):
    def __init__(self, date, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Inserir Evento")
        
        layout = QVBoxLayout(self)
        
        label = QLabel(f"Data: {date}")
        layout.addWidget(label)
        
        self.event_list = QListWidget()
        layout.addWidget(self.event_list)
        
        self.event_input = QLineEdit()
        layout.addWidget(self.event_input)
        
        button_layout = QHBoxLayout()
        
        add_button = QPushButton("Adicionar")
        add_button.clicked.connect(self.add_event)
        button_layout.addWidget(add_button)
        
        remove_button = QPushButton("Remover")
        remove_button.clicked.connect(self.remove_event)
        button_layout.addWidget(remove_button)
        
        layout.addLayout(button_layout)
        
        self.date = date
        self.load_events()
    
    def load_events(self):
        self.event_list.clear()
        
        try:
            conn = psycopg2.connect(
                host="localhost",
                port="5432",
                database="Projeto",
                user="postgres",
                password="89iokl,."
            )
            
            cursor = conn.cursor()
            cursor.execute("SELECT contatos FROM public.contatos WHERE data = %s", (self.date,))
            
            events = cursor.fetchall()
            
            for event in events:
                self.event_list.addItem(event[0])
            
            cursor.close()
            conn.close()
        
        except psycopg2.Error as e:
            print("Erro ao carregar contatos:", e)
    
    def add_event(self):
        event = self.event_input.text()
        if event:
            try:
                conn = psycopg2.connect(
                    host="localhost",
                    port="5432",
                    database="Projeto",
                    user="postgres",
                    password="89iokl,."
                )
                
                cursor = conn.cursor()
                cursor.execute("INSERT INTO public.contatos (codigo, nome, telefone, data, evento) VALUES (%s, %s, %s, %s, %s)", (self.codigo, nome, telefone, data, evento))
                conn.commit()
                cursor.close()
                conn.close()
                
                self.event_list.addItem(event)
                self.event_input.clear()
            
            except psycopg2.Error as e:
                print("Erro ao adicionar evento:", e)
    
    def remove_event(self):
        selected_items = self.event_list.selectedItems()
        
        if not selected_items:
            return
        
        event = selected_items[0].text()
        
        try:
            conn = psycopg2.connect(
                host="localhost",
                port="5432",
                database="Projeto",
                user="postgres",
                password="89iokl,."
            )
            
            cursor = conn.cursor()
            cursor.execute("DELETE FROM public.contatos WHERE data = %s AND evento = %s", (self.data, evento))
            conn.commit()
            cursor.close()
            conn.close()
            
            self.event_list.takeItem(self.event_list.row(selected_items[0]))
        
        except psycopg2.Error as e:
            print("Erro ao remover evento:", e)


class CalendarApp(QMainWindow):
    def __init__(self):
        super().__init__()
        
        self.setWindowTitle("Calendário")
        self.setGeometry(100, 100, 600, 500)
        
        self.central_widget = QWidget(self)
        self.setCentralWidget(self.central_widget)
        
        layout = QVBoxLayout(self.central_widget)
        
        self.table_widget = Q