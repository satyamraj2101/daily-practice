from datetime import datetime
import tkinter as tk
from tkinter import ttk

class Note:

    def __init__(self, memo, tags=''):
        self.memo = memo
        self.tags = tags
        self.creation_date = datetime.now()
    
    def match(self, filter):
        return filter in self.memo or filter in self.tags

class Notebook:

    def __init__(self):
        self.notes = []

    def new_note(self, memo, tags=''):
        self.notes.append(Note(memo, tags))

    def _find_note(self, note_id):
        for note in self.notes:
            if note.id == note_id:
                return note
        return None

    def modify_memo(self, note_id, memo):
        note = self._find_note(note_id)
        if note:
            note.memo = memo
            return True
        return False

    def modify_tags(self, note_id, tags):
        note = self._find_note(note_id)
        if note:
            note.tags = tags
            return True
        return False

    def search(self, filter):
        return [note for note in self.notes if note.match(filter)]

class NoteApp:

    def __init__(self, master):
        self.master = master
        master.title('Notes')

        # Create notebook object
        self.notebook = Notebook()

        # Create GUI elements
        self.frm_notes = ttk.Frame(master)
        self.txt_note = ttk.Entry(self.frm_notes)
        self.btn_add = ttk.Button(self.frm_notes, text="Add Note", command=self.add_note)

        self.frm_notes.grid(row=0, column=0)
        self.txt_note.grid(row=0, column=0)
        self.btn_add.grid(row=0, column=1)

    def add_note(self):
        memo = self.txt_note.get()
        self.notebook.new_note(memo)
        self.txt_note.delete(0, 'end')

root = tk.Tk()
app = NoteApp(root)
root.mainloop()
notebook = Notebook()
notebook.new_note("hello world")
notebook.new_note("hello again")

print(notebook.search("hello"))