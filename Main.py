import tkinter as tk
from tkinter import messagebox,ttk
import mysql.connector
import os
from dotenv import load_dotenv

load_dotenv()

# --- Database Connection (Fixed) ---
def get_db_connection():
    try:
        conn = mysql.connector.connect(
            host=os.getenv("DB_HOST"),  # Default to localhost if not set
            user=os.getenv("DB_USER"),        # Apna MySQL user check karein
            password=os.getenv("DB_PASSWORD"), # Apna MySQL password sahi likhein
            database=os.getenv("DB_NAME")
        )
        return conn
    except mysql.connector.Error as err:
        # Agar DB nahi mila ya password galat hua to yahan error dikhayega
        print(f"Error: {err}")
        return None
# ==========================================
# 0. Login DASHBOARD CLASS
# ==========================================
class LoginPage:
    def __init__(self, root):
        self.root = root
        self.root.title("University Portal Login")
        self.root.geometry("450x600")
        self.root.configure(bg="#121212")
        self.root.resizable(False, False)

        # Container Frame (Taake packing issues na hon)
        self.main_frame = tk.Frame(self.root, bg="#121212")
        self.main_frame.pack(expand=True, fill="both")

        # --- Login Card ---
        self.card = tk.Frame(self.main_frame, bg="#1E1E2E", padx=20, pady=20)
        self.card.place(relx=0.5, rely=0.5, anchor="center", width=350, height=450)

        # Header
        tk.Label(self.card, text="LOGIN", font=("Helvetica", 24, "bold"),bg="#1E1E2E", fg="#FFFFFF").pack(pady=(20, 30))

        # Username Input
        tk.Label(self.card, text="Username", bg="#1E1E2E", font=("Arial", 10, "bold"),fg="#FFFFFF" ).pack(anchor="w", padx=25)
        self.username_ent = tk.Entry(self.card, font=("Arial", 12),fg="#FFFFFF",insertbackground="#FFFFFF", bg="#27272A", bd=0)
        self.username_ent.pack(fill="x", padx=25, ipady=8, pady=(5, 20))

        # Password Input
        tk.Label(self.card, text="Password", bg="#1E1E2E", font=("Arial", 10, "bold"),fg="#FFFFFF").pack(anchor="w", padx=25)
        self.password_ent = tk.Entry(self.card, font=("Arial", 12), bg="#27272A",insertbackground="#FFFFFF",fg="#FFFFFF", bd=0, show="*")
        self.password_ent.pack(fill="x", padx=25, ipady=8, pady=(5, 30))

        # Login Button
        self.login_btn = tk.Button(self.card, text="LOG IN", font=("Arial", 12, "bold"),activebackground="#60A5FA", bg="#3B82F6", fg="white", bd=0,relief="flat", cursor="hand2",command=self.validate_login)
        self.login_btn.pack(fill="x", padx=25, ipady=10)

    def validate_login(self):
        user = self.username_ent.get()
        pwd = self.password_ent.get()

        if not user or not pwd:
            messagebox.showwarning("Empty Fields", "Please enter both username and password")
            return

        conn = get_db_connection()
        if conn:
            try:
                cursor = conn.cursor(dictionary=True)
                # SQL Query
                query = "SELECT role FROM Users WHERE username = %s AND password = %s"
                cursor.execute(query, (user, pwd))
                result = cursor.fetchone()

                if result:
                    role = result['role']
                    messagebox.showinfo("Success", f"Login Successful! Role: {role}")
                    if role == "admin":
                        self.root.destroy()
                        admin_root = tk.Tk()
                        AdminDashboard(admin_root, user)
                        admin_root.mainloop()
                    elif role == "student":
                        self.root.destroy()
                        student_root = tk.Tk()
                        r=self.current_user_id = user[0]
                        StudentDashboard(student_root, user, r)
                        student_root.mainloop() 
                else:
                    messagebox.showerror("Login Failed", "Invalid Username or Password")
            except Exception as e:
                messagebox.showerror("Query Error", f"Something went wrong: {e}")
            finally:
                conn.close()
        else:
            messagebox.showerror("DB Connection", "Could not connect to Database. Check MySQL Service.")
    def get_user_id(self, username, conn):
        cursor = conn.cursor()
        cursor.execute("SELECT id FROM Users WHERE username = %s", (username))
        user = cursor.fetchone()
        return user[0] if user else None
    
# ==========================================
# 1. Admin DASHBOARD CLASS
# ==========================================
class AdminDashboard:
    def __init__(self, root, username):
        self.root = root
        self.username = username
        self.root.title("Admin Panel - University Event Manager")
        self.root.geometry("1000x600")
        self.root.configure(bg="#121212")
        self.conn = get_db_connection()
        self.cursor = self.conn.cursor() if self.conn else None

        # Sidebar
        self.side = tk.Frame(self.root, bg="#1E1E2E", width=220)
        self.side.pack(side="left", fill="y")
        
        tk.Label(self.side, text="ADMIN PRO", font=("Segoe UI", 26, "bold"), bg="#2D2D44", fg="#2DD4BF", pady=30).pack()
        
        # Navigation Buttons
        tk.Button(self.side, text="Add New Event", bg="#2D2D44", activebackground="#3B82F6", fg="white", bd=0, pady=15, command=self.draw_add_event_ui).pack(fill="x")
        tk.Button(self.side, text="View All Events", bg="#2D2D44", activebackground="#3B82F6", fg="white", bd=0, pady=15, command=self.show_all_events).pack(fill="x")
        tk.Button(self.side, text="View Registrations", bg="#2D2D44", activebackground="#3B82F6", fg="white", bd=0, pady=15, command=self.draw_registrations_ui).pack(fill="x")
        tk.Button(self.side, text="Update Event", bg="#2D2D44", activebackground="#3B82F6", fg="white", bd=0, pady=15, command=self.update_event).pack(fill="x")
        tk.Button(self.side, text="Delete Event", bg="#2D2D44", activebackground="#3B82F6", fg="white", bd=0, pady=15, command=self.delete_event).pack(fill="x")
        tk.Button(self.side, text="Logout", bg="#EF4444", fg="white", bd=0, pady=10, command=self.root.quit).pack(side="bottom", fill="x")

        # Main Content Area
        self.content = tk.Frame(self.root, bg="#121212", padx=30, pady=30)
        self.content.pack(side="right", fill="both", expand=True)
        
        self.draw_add_event_ui() # Default View
    
    def show_all_events(self):
        self.clear_content()
        tk.Label(self.content, text="All Events", font=("Arial", 22, "bold"), bg="#121212", fg="#FFFFFF").pack(anchor="w", pady=(0,20))

        # Treeview Setup
        columns = ('ID', 'Title', 'Venue', 'Date', 'Description')
        tree = ttk.Treeview(self.content, columns=columns, show='headings', height=15)
        
        # Headings Setup
        for col in columns:
            tree.heading(col, text=col)

        # Width Setup
        tree.column("ID", width=50, anchor='center')
        tree.column("Title", width=150, anchor='center')
        tree.column("Venue", width=150, anchor='center')
        tree.column("Date", width=100, anchor='center')
        tree.column("Description", width=300, anchor='w')
        
        tree.pack(pady=10, fill='both', expand=True)

        # SQL Logic to fetch events
        try:
            self.cursor.execute("SELECT * FROM Events ORDER BY id DESC")
            records = self.cursor.fetchall()

            for row in records:
                tree.insert('', tk.END, values=row)

        except Exception as e:
            messagebox.showerror("Database Error", f"Error fetching data: {e}")


    def update_event(self):
        self.clear_content()
        tk.Label(self.content, text="Update an Event", font=("Arial", 22, "bold"), bg="#121212", fg="#FFFFFF").pack(anchor="w", pady=(0,20))

        card = tk.Frame(self.content, bg="#121212", padx=30, pady=30, relief="solid", bd=1)
        card.pack(fill="x")

        tk.Label(card, text="Event ID to Update:", bg="#121212", fg="#FFFFFF").pack(anchor="w")
        event_id_ent = tk.Entry(card, font=("Arial", 12))
        event_id_ent.pack(fill="x", pady=(5, 15))

        tk.Label(card, text="New Venue:", bg="#121212", fg="#FFFFFF").pack(anchor="w")
        venue_ent = tk.Entry(card, font=("Arial", 12))
        venue_ent.pack(fill="x", pady=(5, 15))

        tk.Label(card, text="New Date (YYYY-MM-DD):", bg="#121212", fg="#FFFFFF").pack(anchor="w")
        date_ent = tk.Entry(card, font=("Arial", 12))
        date_ent.pack(fill="x", pady=(5, 15))


        def confirm_update():
            conn = get_db_connection()
            if conn:
                cursor = conn.cursor()
                cursor.execute("UPDATE Events SET venue = %s, date = %s WHERE id = %s", (venue_ent.get(), date_ent.get(), event_id_ent.get()))
                conn.commit()
                conn.close()
                messagebox.showinfo("Success", "Event Updated Successfully!")
                event_id_ent.delete(0, tk.END)
                venue_ent.delete(0, tk.END)
                date_ent.delete(0, tk.END)
            else:
                messagebox.showerror("DB Connection", "Could not connect to Database.")

        tk.Button(card, text="Update Event", bg="#F59E0B",activebackground="#D97706", fg="white", font=("Arial", 10, "bold"), pady=10, command=confirm_update).pack(fill="x")

    def delete_event(self):
        self.clear_content()
        tk.Label(self.content, text="Delete an Event", font=("Arial", 32, "bold"),fg="#FFFFFF",bg="#121212").pack(anchor="w", pady=(10,25))

        card = tk.Frame(self.content, bg="#121212", padx=30, pady=30, relief="solid", bd=1)
        card.pack(fill="x")

        tk.Label(card, text="Event ID to Delete:", fg="#FFFFFF", bg="#121212", padx=5).pack(anchor="w")
        event_id_ent = tk.Entry(card, font=("Arial", 12))
        event_id_ent.pack(fill="x", pady=(5, 15))


        def confirm_delete():
            conn = get_db_connection()
            if conn:
                cursor = conn.cursor(buffered =True)
                cursor.execute("SELECT * FROM Registrations WHERE event_id = %s", (event_id_ent.get(),))
                cursor.execute("DELETE FROM Events WHERE id = %s", (event_id_ent.get()))
                conn.commit()
                conn.close()
                messagebox.showinfo("Success", "Event Deleted Successfully!")
                event_id_ent.delete(0, tk.END)
            else:
                messagebox.showerror("DB Connection", "Could not connect to Database.")

        tk.Button(card, text="Delete Event", bg="#EF4444", fg="white", font=("Arial", 10, "bold"), pady=10, command=confirm_delete,cursor="hand2").pack(fill="x")

    def clear_content(self):
        for widget in self.content.winfo_children(): widget.destroy()

    def draw_add_event_ui(self):
        self.clear_content()
        tk.Label(self.content, text="Post a New Event", font=("Arial", 22, "bold"), bg="#121212", fg="#FFFFFF").pack(anchor="w", pady=(0,20))

        card = tk.Frame(self.content, bg="#121212", padx=30, pady=30, relief="solid", bd=1)
        card.pack(fill="x")

        tk.Label(card, text="Event Title:", bg="#121212", fg="#FFFFFF").pack(anchor="w")
        title_ent = tk.Entry(card, font=("Arial", 12))
        title_ent.pack(fill="x", pady=(5, 15))

        tk.Label(card, text="Venue:", bg="#121212", fg="#FFFFFF").pack(anchor="w")
        venue_ent = tk.Entry(card, font=("Arial", 12))
        venue_ent.pack(fill="x", pady=(5, 15))

        tk.Label(card, text="Event Date (YYYY-MM-DD):", bg="#121212", fg="#FFFFFF").pack(anchor="w")
        date_ent = tk.Entry(card, font=("Arial", 12), bd=2, relief="groove")
        date_ent.insert(0, "YYYY-MM-DD") # Placeholder date
        date_ent.pack(fill="x", pady=(5, 15))

        # --- Description Input ---
        tk.Label(card, text="Description:", bg="#121212", font=("Arial", 10, "bold"), fg="#FFFFFF").pack(anchor="w")
        # Description ke liye Entry ki jagah Text behtar hai (multi-line ke liye)
        desc_txt = tk.Text(card, font=("Arial", 11), height=4, bd=2, relief="groove")
        desc_txt.pack(fill="x", pady=(5, 15))

        def save_event():
            conn = get_db_connection()
            if not title_ent.get().strip() or not venue_ent.get().strip() or not date_ent.get().strip() or not desc_txt.get("1.0", tk.END).strip():
                messagebox.showwarning("Input Error", "All Fields Must Be Filled!")
                return
            if conn:
                cursor = conn.cursor()
                cursor.execute("INSERT INTO Events (name, venue, date, description) VALUES (%s, %s, %s, %s)", (title_ent.get(), venue_ent.get(), date_ent.get(), desc_txt.get("1.0", tk.END).strip()))
                conn.commit()
                conn.close()
                messagebox.showinfo("Success", "Event Published Successfully!")
                title_ent.delete(0, tk.END)
                venue_ent.delete(0, tk.END)
                date_ent.delete(0, tk.END)
                date_ent.insert(0, "YYYY-MM-DD") # Optional: Date ka format wapas likh dein
                desc_txt.delete("1.0", tk.END)

        tk.Button(card, text="Publish Event", bg="#22C55E",activebackground="#16A34A", fg="white", font=("Arial", 10, "bold"), pady=10, command=save_event).pack(fill="x")
    
    def draw_registrations_ui(self):
        self.clear_content()

        tk.Label(self.content, text="All Registrations", font=("Arial", 22, "bold"), bg="#121212", fg="#FFFFFF").pack(anchor="w", pady=(0,20))

        # Treeview Setup
        columns = ('Reg ID', 'Student Name', 'Event Name', 'Event Date')
        tree = ttk.Treeview(self.content, columns=columns, show='headings', height=10)
        
        # Headings Setup
        for col in columns:
            tree.heading(col, text=col)
        # Width Setup
        tree.column("Reg ID", width=50, anchor='center')
        tree.column("Student Name", width=150, anchor='center')
        tree.column("Event Name", width=200, anchor='center')
        tree.column("Event Date", width=100, anchor='center')
        tree.pack(pady=10, fill='both', expand=True)

        # tk.Label(self.root, text="All Registered Students", font=("Arial", 20, "bold"), fg="#333").pack(pady=20)

        # Treeview Setup (Isme errors fixed hain)
        # columns = ('Reg ID', 'Student Name', 'Event Name', 'Event Date')
        # tree = ttk.Treeview(self.root, columns=columns, show='headings', height=15)
        
        # # Headings Setup
        # tree.heading('Reg ID', text='ID')
        # tree.heading('Student Name', text='Student Name')
        # tree.heading('Event Name', text='Event Name')
        # tree.heading('Event Date', text='Date')

        # # Width Setup
        # tree.column("Reg ID", width=50, anchor='center')
        # tree.column("Student Name", width=150, anchor='center')
        # tree.column("Event Name", width=200, anchor='center')
        # tree.column("Event Date", width=100, anchor='center')
        
        # tree.pack(pady=10, padx=20, fill='both', expand=True)

        # SQL Logic with JOIN
        try:
            query = """
            SELECT registrations.id, users.username, events.name, events.date 
            FROM registrations
            JOIN users ON registrations.student_id = users.id
            JOIN events ON registrations.event_id = events.id
            ORDER BY registrations.id DESC
            """
            self.cursor.execute(query)
            records = self.cursor.fetchall()

            for row in records:
                tree.insert('', tk.END, values=row)

        except Exception as e:
            # Fix: tk.messagebox ki jagah direct messagebox use karein
            messagebox.showerror("Database Error", f"Error fetching data: {e}")

        # Back Button
        # tk.Button(self.root, text="Back to Dashboard", command=self.show_admin_panel, bg="gray", fg="white", width=20).pack(pady=20)
    
    def show_admin_panel(self):
        self.clear_screen()
        self.__init__(self.root, self.username)
    
    def clear_screen(self):
        
        for widget in self.root.winfo_children():
            widget.destroy()
# ==========================================
# 2. STUDENT DASHBOARD CLASS
# ==========================================
class StudentDashboard:
    def __init__(self, root, username, user_id):
        self.root = root
        self.username = username
        self.user_id = user_id
        self.root.title("Student Panel - University Event Manager")
        self.root.geometry("1000x600")
        self.root.configure(bg="#121212")
        self.conn = get_db_connection()
        self.cursor = self.conn.cursor() if self.conn else None

        # Sidebar
        self.side = tk.Frame(self.root, bg="#1E1E2E", width=220)
        self.side.pack(side="left", fill="y")
        
        tk.Label(self.side, text=f"Welcome {username} ", font=("Segoe UI", 26, "bold"), bg="#2D2D44", fg="#2DD4BF", pady=30).pack()
        
        # Navigation Buttons
        tk.Button(self.side, text="Register New Event", bg="#2D2D44", activebackground="#3B82F6", fg="white", bd=0, pady=15, command=self.register_event).pack(fill="x")
        tk.Button(self.side, text="View All Events", bg="#2D2D44", activebackground="#3B82F6", fg="white", bd=0, pady=15, command=self.show_all_events).pack(fill="x")
        tk.Button(self.side, text="View Registrations", bg="#2D2D44", activebackground="#3B82F6", fg="white", bd=0, pady=15, command=self.registrations).pack(fill="x")
        tk.Button(self.side, text="Delete Registration", bg="#2D2D44", activebackground="#3B82F6", fg="white", bd=0, pady=15, command=self.delete_reg).pack(fill="x")

        tk.Button(self.side, text="Logout", bg="#EF4444", fg="white", bd=0, pady=10, command=self.root.quit).pack(side="bottom", fill="x")

        # Main Content Area
        self.content = tk.Frame(self.root, bg="#121212", padx=30, pady=30)
        self.content.pack(side="right", fill="both", expand=True)
        



        self.show_all_events() # Default View


    def delete_reg(self):
        self.clear_content()
        tk.Label(self.content, text="Delete a Registration", font=("Arial", 32, "bold"),fg="#FFFFFF",bg="#121212").pack(anchor="w", pady=(10,25))

        card = tk.Frame(self.content, bg="#121212", padx=30, pady=30, relief="solid", bd=1)
        card.pack(fill="x")

        tk.Label(card, text="Registration ID to Delete:", fg="#FFFFFF", bg="#121212", padx=5).pack(anchor="w")
        event_id_ent = tk.Entry(card, font=("Arial", 12))
        event_id_ent.pack(fill="x", pady=(5, 15))


        def confirm_delete():
            conn = get_db_connection()
            if conn:
                cursor = conn.cursor(buffered =True)
                cursor.execute("DELETE FROM Registrations WHERE id = %s AND student_id = %s", (event_id_ent.get(), self.user_id))
                conn.commit()
                conn.close()
                messagebox.showinfo("Success", "Registration Deleted Successfully!")
                event_id_ent.delete(0, tk.END)
            else:
                messagebox.showerror("DB Connection", "Could not connect to Database.")

        tk.Button(card, text="Delete Registration", bg="#EF4444", fg="white", font=("Arial", 10, "bold"), pady=10, command=confirm_delete,cursor="hand2").pack(fill="x")

    def register_event(self):
        self.clear_content()
        tk.Label(self.content, text="Register for an Event", font=("Arial", 22, "bold"), bg="#121212", fg="#FFFFFF").pack(anchor="w", pady=(0,20))

        card = tk.Frame(self.content, bg="#121212", padx=30, pady=30, relief="solid", bd=1)
        card.pack(fill="x")

        tk.Label(card, text="Event ID to Register:", bg="#121212", fg="#FFFFFF").pack(anchor="w")
        event_id_ent = tk.Entry(card, font=("Arial", 12))
        event_id_ent.pack(fill="x", pady=(5, 15))


        def confirm_registration():
            conn = get_db_connection()
            if conn:
                cursor = conn.cursor()
                cursor.execute("INSERT INTO Registrations (student_id, event_id) VALUES (%s, %s)", (self.user_id, event_id_ent.get()))
                conn.commit()
                conn.close()
                messagebox.showinfo("Success", "Registered for Event Successfully!")
                event_id_ent.delete(0, tk.END)
            else:
                messagebox.showerror("DB Connection", "Could not connect to Database.")

        tk.Button(card, text="Register Event", bg="#22C55E",activebackground="#16A34A", fg="white", font=("Arial", 10, "bold"), pady=10, command=confirm_registration).pack(fill="x")

    def registrations(self):
        self.clear_content()
        tk.Label(self.content, text="My Registrations", font=("Arial", 22, "bold"), bg="#121212", fg="#FFFFFF").pack(anchor="w", pady=(0,20))

        # Treeview Setup
        columns = ('Reg ID', 'Event Name', 'Event Date')
        self.tree = ttk.Treeview(self.content, columns=columns, show='headings', height=15)
        
        # Headings Setup
        for col in columns:
            self.tree.heading(col, text=col)

        # Width Setup
        self.tree.column("Reg ID", width=50, anchor='center')
        self.tree.column("Event Name", width=200, anchor='center')
        self.tree.column("Event Date", width=100, anchor='center')
        
        self.tree.pack(pady=10, fill='both', expand=True)

        # SQL Logic to fetch registrations
        try:
            query = """
            SELECT registrations.id, events.name, events.date 
            FROM registrations
            JOIN events ON registrations.event_id = events.id
            WHERE registrations.student_id = %s
            ORDER BY registrations.id DESC
            """
            self.cursor.execute(query, (self.user_id,))
            records = self.cursor.fetchall()

            for row in records:
                self.tree.insert('', tk.END, values=row)

        except Exception as e:
            messagebox.showerror("Database Error", f"Error fetching data: {e}")

    def show_all_events(self):
        self.clear_content()
        tk.Label(self.content, text="All Events", font=("Arial", 22, "bold"), bg="#121212", fg="#FFFFFF").pack(anchor="w", pady=(0,20))

        # Treeview Setup
        columns = ('ID', 'Title', 'Venue', 'Date', 'Description')
        self.tree = ttk.Treeview(self.content, columns=columns, show='headings', height=15)
        
        # Headings Setup
        for col in columns:
            self.tree.heading(col, text=col)

        # Width Setup
        self.tree.column("ID", width=50, anchor='center')
        self.tree.column("Title", width=150, anchor='center')
        self.tree.column("Venue", width=150, anchor='center')
        self.tree.column("Date", width=100, anchor='center')
        self.tree.column("Description", width=300, anchor='w')
        
        self.tree.pack(pady=10, fill='both', expand=True)

        # SQL Logic to fetch events
        try:
            self.cursor.execute("SELECT * FROM Events ORDER BY id DESC")
            records = self.cursor.fetchall()

            for row in records:
                self.tree.insert('', tk.END, values=row)

        except Exception as e:
            messagebox.showerror("Database Error", f"Error fetching data: {e}")

    def delete_registration(self):
        self.clear_content()
        tk.Label(self.content, text="Delete a Registration", font=("Arial", 32, "bold"),fg="#FFFFFF",bg="#121212").pack(anchor="w", pady=(10,25))

        card = tk.Frame(self.content, bg="#121212", padx=30, pady=30, relief="solid", bd=1)
        card.pack(fill="x")

        tk.Label(card, text="Registration ID to Delete:", fg="#FFFFFF", bg="#121212", padx=5).pack(anchor="w")
        event_id_ent = tk.Entry(card, font=("Arial", 26))
        event_id_ent.pack(fill="x", pady=(5, 15))


        def confirm_delete():
            conn = get_db_connection()
            if conn:
                cursor = conn.cursor(buffered =True)
                cursor.execute("DELETE FROM Registrations WHERE id = %s", (event_id_ent.get()))
                conn.commit()
                conn.close()
                messagebox.showinfo("Success", "Registration Deleted Successfully!")
                event_id_ent.delete(0, tk.END)
            else:
                messagebox.showerror("DB Connection", "Could not connect to Database.")

        tk.Button(card, text="Delete Registration", bg="#EF4444", fg="white", font=("Arial", 10, "bold"), pady=10, command=confirm_delete,cursor="hand2").pack(fill="x")

    def load_events(self):
        conn = get_db_connection()
        if conn:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM Events")
            for row in cursor.fetchall():
                self.tree.insert('', 'end', values=row)
            conn.close()

    def clear_content(self):
        for widget in self.content.winfo_children(): widget.destroy()


if __name__ == "__main__":
    root = tk.Tk()
    app = LoginPage(root)
    root.mainloop()