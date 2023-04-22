#начни тут создавать приложение с умными заметками
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QInputDialog, QPushButton, QLabel, QVBoxLayout, QRadioButton, QButtonGroup, QHBoxLayout, QMessageBox, QGroupBox, QListWidget, QTextEdit, QLineEdit
import json
#типа умные заметки
app = QApplication([])
window = QWidget()
window.setWindowTitle('Заметки')
window.resize(800, 600)
#тут йа все кнопочки делаю
btn_create_note = QPushButton('Создать заметку')
btn_del_note = QPushButton('Удалить заметку')
btn_save_note= QPushButton('Сохранить заметку')
btn_add_tag= QPushButton('Добавить к заметке')
btn_del_fromtag = QPushButton('Открепить от заметки')
btn_find_tag = QPushButton('Искать по тегу')
#а тут какие то лэйбли и что то про что я уже забы
input_text = QTextEdit()
list_notes = QListWidget()
list_notes_name = QLabel('Список заметок')
list_tags = QListWidget()
list_tags_name = QLabel('Список тегов')
field_tag = QLineEdit()
notes = {'бе бе бе бе бе': 'Это самое лучшее приложение для заметок!'}
with open('notes_data.json', 'w') as file:
    json.dump(notes, file)
#тут просто сделал лэйауты
layout_line_V1 = QVBoxLayout()
layout_line_V2 = QVBoxLayout()
layout_line_H1 = QHBoxLayout()
layout_line_H2 = QHBoxLayout()
#тут добавил всякие виджеты
layout_line_V2.addWidget(list_notes_name)
layout_line_V2.addWidget(list_notes, stretch=2)
layout_line_V1.addWidget(input_text, stretch=2)
layout_line_V2.addLayout(layout_line_H1, stretch=2)
layout_line_H1.addWidget(btn_create_note, stretch=2)
layout_line_H1.addWidget(btn_del_note ,stretch=2)
layout_line_V2.addWidget(btn_save_note, stretch=2)
layout_line_V2.addWidget(list_tags_name, stretch=1)
layout_line_V2.addWidget(list_tags, stretch=2)
layout_line_V2.addWidget(field_tag, stretch=2)
layout_line_V2.addLayout(layout_line_H2, stretch=2)
layout_line_H2.addWidget(btn_add_tag, stretch=2)
layout_line_H2.addWidget(btn_del_fromtag, stretch=2)
layout_line_V2.addWidget(btn_find_tag, stretch=2)
#а тут все в 1 лэйаут сделал
layout_card = QHBoxLayout()
layout_card.addLayout(layout_line_V1, stretch=5)
layout_card.addLayout(layout_line_V2, stretch=3)

def show_note():
    name = list_notes.selectedItems()[0].text()
    field_text.setText(notes[name]['текст'])
    list_tags.clear()
    list_tags.addItems(notes[name]['теги'])
def add_notes():
    note_name, ok = QInputDialog.getText(window, 'Добавить заметку', 'Название заметки:')
    if ok and note_name != '':
        notes[note_name] = {'текст' : '', 'теги':[]}
        list_notes.addItem(note_name)
def save_note():
    if list_notes.SelectItems():
        key = list_notes.SelectItems()[0].text()
        notes[key]['текст'] = field_text.toPlaint.text
        with open('notes_data.json', 'w') as file:
            json.dump(notes, file, sort_keys = True )
        print(notes)
#ну и обычная концовка что бы "это" вообще открылась
window.setLayout(layout_card)
btn_create_note.clicked.connect(add_notes)
btn_save_note.clicked.connect(save_note)
with open('notes_data.json', 'r') as file:
    notes = json.load(file)
list_notes.addItems(notes)
window.show()
app.exec()