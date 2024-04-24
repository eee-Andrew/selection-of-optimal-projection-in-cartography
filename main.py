import tkinter as tk
import math

def calculate():
    try:
        a = float(entry1.get())
        phi_degrees = int(entry2.get())
        # Convert degrees to radians
        phi_radians = math.radians(phi_degrees)
        # Calculate sin^2(phi)
        sin2_phi = math.sin(phi_radians)**2
        lamda = float(entry3.get())
        phi_b = float(entry4.get())
        phi_b_radians = math.radians(phi_b)

        # Calculate N
        N = a / (1 - 0.006694380 * sin2_phi)**(1/2)
        # Calculate r
        r = a * (1 - 0.006694380) / ((1 - 0.006694380 * sin2_phi)**3)**(1/2)
        # Calculate Rg
        Rg = (r * N)**(1/2)
        # Calculate x_orth_mek
        x_orth_mek = Rg * lamda
        # Calculate y_orth_mek
        y_orth_mek = Rg * math.log(math.tan(math.radians(math.pi)/4 + math.radians(phi_degrees)/2))
        # Additional calculations for m_m_orth_mek and M_orth_mek
        m_m_orth_mek = 1 / math.cos(math.radians(phi_degrees))
        cos2_phi = math.cos(phi_radians)**2
        M_orth_mek = 1 / cos2_phi
        # Calculate ρ της συμμορφης κωνικης
        # Calculate r'       
        r_prime = Rg * math.tan(phi_radians) * ((1 / math.tan(phi_radians / 2))**math.cos(phi_radians)) * ((math.tan(math.radians((90 - phi_degrees) / 2)))**math.cos(phi_radians))
        
        # Calculate r' zero
        r_prime_zero = Rg * math.tan(phi_radians) * ((1 / math.tan(phi_radians / 2))**math.cos(phi_radians)) * ((math.tan(math.radians(( phi_degrees) / 2)))**math.cos(phi_radians))

        # Calculate theta
        theta = lamda * math.sin(math.radians(phi_degrees))

        # Calculate x for Σύμ. Κων
        x_sum_kwn = r_prime * math.sin(math.radians(phi_degrees))
        # Calculate y for Σύμ. Κων
        y_sum_kwn = r_prime_zero - r_prime * math.cos(math.radians(phi_degrees))
        # Calculate m_m for Σύμ. Κων
        m_m_sum_kwn = r_prime * math.sin(math.radians(phi_degrees)) / (Rg * math.cos(math.radians(phi_degrees)))
        # Calculate M for Σύμ. Κων
        M_sum_kwn = m_m_sum_kwn ** 2

        #Eγκάρσια Μερκατορική
        # Calculate u for egkarsia merk
        cot_phi = 1 / math.tan(math.radians(phi_degrees))
        u_erg_mer = math.atan(1 / (cot_phi * math.cos(math.radians(lamda))))
        # Calculate V for egkarsia merk
        v_erg_mer = math.asin(math.cos(math.radians(phi_degrees)) * math.sin(math.radians(lamda)))
        # Calculate X for egkarsia merk
        x_erg_mer = Rg *math.log(math.tan((v_erg_mer/2)+math.radians(math.pi)/4))
        # Calculate Y for egkarsia merk
        y_erg_mer =  Rg * u_erg_mer
        # Calculate Y for egkarsia merk
        m_m_erg_mer= 1/math.cos(v_erg_mer)
        # Calculate Y for egkarsia mer
        M_erg_mer = m_m_erg_mer**2


        #1 ερωτημα συμορφη προβολη βορά , να υπολογίσεις x,y για Φβ που θα δίνει ο χρήστης "phi_b_radians"
        # το φβ είναι ίσο με Χο  και το Χ=90-Φβ
        r_prime_i = Rg * math.tan(phi_b_radians) * ((1 / math.tan(phi_b_radians / 2))**math.cos(phi_b_radians)) * ((math.tan(math.radians((90 - phi_b) / 2)))**math.cos(phi_b_radians))
        r_prime_i_zero = Rg * math.tan(phi_radians) * ((1 / math.tan(phi_b_radians / 2))**math.cos(phi_b_radians)) * ((math.tan(math.radians((90 - phi_degrees) / 2)))**math.cos(phi_b_radians))
        # Calculate x for Σύμ. Κων i
        x_sum_kwn_i = r_prime_i * math.sin(math.radians(phi_degrees))
        # Calculate y for Σύμ. κωνικησ i
        y_sum_kwn_i = r_prime_i_zero - r_prime_i * math.cos(math.radians(phi_degrees))
        # Calculate m_m for Σύμ. Κων i 
        m_m_sum_kwn_i = r_prime_i * math.sin(math.radians(phi_degrees)) / (Rg * math.cos(math.radians(phi_b)))
        # Calculate M for Σύμ. Κων i
        M_sum_kwn_i = m_m_sum_kwn_i ** 2


        #2 ερωτημα ορθή προβολη βορά 
        y_orth_mek_i = Rg * math.log(math.tan(math.radians(math.pi)/4 + math.radians(phi_b)/2))
        m_m_orth_mek_i = 1 / math.cos(math.radians(phi_b))
        cos2_phi_b_i = math.cos(phi_b_radians)**2
        M_orth_mek_i = 1 / cos2_phi_b_i

        #3 ερωτημα εγκαρσια μερκατορικη βοράk
        cot_phi_b = 1 / math.tan(math.radians(phi_b))
        u_erg_mer_i = math.atan(1 / (cot_phi_b * math.cos(math.radians(lamda))))
        # Calculate V for egkarsia merk i
        v_erg_mer_i = math.asin(math.cos(math.radians(phi_b)) * math.sin(math.radians(lamda)))
        # Calculate X for egkarsia merk i
        x_erg_mer_i = Rg *math.log(math.tan((v_erg_mer_i/2)+math.radians(math.pi)/4))
        # Calculate Y for egkarsia merk i
        y_erg_mer_i =  Rg * u_erg_mer_i
        # Calculate Y for egkarsia merk i
        m_m_erg_mer_i= 1/math.cos(v_erg_mer_i)
        # Calculate Y for egkarsia mer i
        M_erg_mer_i = m_m_erg_mer_i**2

       # Display results in the corresponding text boxes
        result_N.config(state=tk.NORMAL)
        result_r.config(state=tk.NORMAL)
        result_Rg.config(state=tk.NORMAL)
        result_x_orth_mek.config(state=tk.NORMAL)
        result_y_orth_mek.config(state=tk.NORMAL)
        result_m_m_orth_mek.config(state=tk.NORMAL)
        result_M_orth_mek.config(state=tk.NORMAL)
        result_r_prime.config(state=tk.NORMAL)
        result_r_prime_zero.config(state=tk.NORMAL)
        result_theta.config(state=tk.NORMAL)
        result_x_sum_kwn.config(state=tk.NORMAL)
        result_y_sum_kwn.config(state=tk.NORMAL)
        result_m_m_sum_kwn.config(state=tk.NORMAL)
        result_M_sum_kwn.config(state=tk.NORMAL)
        result_u_erg_mer.config(state=tk.NORMAL)
        result_v_erg_mer.config(state=tk.NORMAL)
        result_x_erg_mer.config(state=tk.NORMAL)
        result_y_erg_mer.config(state=tk.NORMAL)
        result_m_m_erg_mer.config(state=tk.NORMAL)
        result_M_erg_mer.config(state=tk.NORMAL)
        result_r_prime_i.config(state=tk.NORMAL)
        result_r_prime_i_zero.config(state=tk.NORMAL)
        result_x_sum_kwn_i.config(state=tk.NORMAL)
        result_y_sum_kwn_i.config(state=tk.NORMAL)
        result_m_m_sum_kwn_i.config(state=tk.NORMAL)
        result_M_sum_kwn_i.config(state=tk.NORMAL)
        result_u_erg_mer_i.config(state=tk.NORMAL)
        result_v_erg_mer_i.config(state=tk.NORMAL)
        result_x_erg_mer_i.config(state=tk.NORMAL)
        result_y_erg_mer_i.config(state=tk.NORMAL)
        result_m_m_erg_mer_i.config(state=tk.NORMAL)
        result_M_erg_mer_i.config(state=tk.NORMAL)

        result_N.delete(1.0, tk.END)
        result_r.delete(1.0, tk.END)
        result_Rg.delete(1.0, tk.END)
        result_x_orth_mek.delete(1.0, tk.END)
        result_y_orth_mek.delete(1.0, tk.END)
        result_m_m_orth_mek.delete(1.0, tk.END)
        result_M_orth_mek.delete(1.0, tk.END)
        result_r_prime.delete(1.0, tk.END)
        result_r_prime_zero.delete(1.0, tk.END)
        result_theta.delete(1.0, tk.END)
        result_x_sum_kwn.delete(1.0, tk.END)
        result_y_sum_kwn.delete(1.0, tk.END)
        result_m_m_sum_kwn.delete(1.0, tk.END)
        result_M_sum_kwn.delete(1.0, tk.END)
        result_u_erg_mer.delete(1.0, tk.END)
        result_v_erg_mer.delete(1.0, tk.END)
        result_x_erg_mer.delete(1.0, tk.END)
        result_y_erg_mer.delete(1.0, tk.END)
        result_m_m_erg_mer.delete(1.0, tk.END)
        result_M_erg_mer.delete(1.0, tk.END)
        result_r_prime_i.delete(1.0, tk.END)
        result_r_prime_i_zero.delete(1.0, tk.END)
        result_x_sum_kwn_i.delete(1.0, tk.END)
        result_y_sum_kwn_i.delete(1.0, tk.END)
        result_m_m_sum_kwn_i.delete(1.0, tk.END)
        result_M_sum_kwn_i.delete(1.0, tk.END)
        result_u_erg_mer_i.delete(1.0, tk.END)
        result_v_erg_mer_i.delete(1.0, tk.END)
        result_x_erg_mer_i.delete(1.0, tk.END)
        result_y_erg_mer_i.delete(1.0, tk.END)
        result_m_m_erg_mer_i.delete(1.0, tk.END)
        result_M_erg_mer_i.delete(1.0, tk.END)

        result_N.insert(tk.END, N)
        result_r.insert(tk.END, r)
        result_Rg.insert(tk.END, Rg)
        result_x_orth_mek.insert(tk.END, x_orth_mek)
        result_y_orth_mek.insert(tk.END, y_orth_mek)
        result_m_m_orth_mek.insert(tk.END, m_m_orth_mek)
        result_M_orth_mek.insert(tk.END, M_orth_mek)
        result_r_prime.insert(tk.END, r_prime)
        result_r_prime_zero.insert(tk.END, r_prime_zero)
        result_theta.insert(tk.END, theta)
        result_x_sum_kwn.insert(tk.END, x_sum_kwn)
        result_y_sum_kwn.insert(tk.END, y_sum_kwn)
        result_m_m_sum_kwn.insert(tk.END, m_m_sum_kwn)
        result_M_sum_kwn.insert(tk.END, M_sum_kwn)
        result_u_erg_mer.insert(tk.END, u_erg_mer)
        result_v_erg_mer.insert(tk.END, v_erg_mer)
        result_x_erg_mer.insert(tk.END, x_erg_mer)
        result_y_erg_mer.insert(tk.END, y_erg_mer)
        result_m_m_erg_mer.insert(tk.END, m_m_erg_mer)
        result_M_erg_mer.insert(tk.END, M_erg_mer)
        result_r_prime_i.insert(tk.END, r_prime_i)
        result_r_prime_i_zero.insert(tk.END, r_prime_i_zero)
        result_x_sum_kwn_i.insert(tk.END, x_sum_kwn_i)
        result_y_sum_kwn_i.insert(tk.END, y_sum_kwn_i)
        result_m_m_sum_kwn_i.insert(tk.END, m_m_sum_kwn_i)
        result_M_sum_kwn_i.insert(tk.END, M_sum_kwn_i)
        result_u_erg_mer_i.insert(tk.END, u_erg_mer_i)
        result_v_erg_mer_i.insert(tk.END, v_erg_mer_i)
        result_x_erg_mer_i.insert(tk.END, x_erg_mer_i)
        result_y_erg_mer_i.insert(tk.END, y_erg_mer_i)
        result_m_m_erg_mer_i.insert(tk.END, m_m_erg_mer_i)
        result_M_erg_mer_i.insert(tk.END, M_erg_mer_i)

        result_N.config(state=tk.DISABLED)
        result_r.config(state=tk.DISABLED)
        result_Rg.config(state=tk.DISABLED)
        result_x_orth_mek.config(state=tk.DISABLED)
        result_y_orth_mek.config(state=tk.DISABLED)
        result_m_m_orth_mek.config(state=tk.DISABLED)
        result_M_orth_mek.config(state=tk.DISABLED)
        result_r_prime.config(state=tk.DISABLED)
        result_r_prime_zero.config(state=tk.DISABLED)
        result_theta.config(state=tk.DISABLED)
        result_x_sum_kwn.config(state=tk.DISABLED)
        result_y_sum_kwn.config(state=tk.DISABLED)
        result_m_m_sum_kwn.config(state=tk.DISABLED)
        result_M_sum_kwn.config(state=tk.DISABLED)
        result_u_erg_mer.config(state=tk.DISABLED)
        result_v_erg_mer.config(state=tk.DISABLED)
        result_x_erg_mer.config(state=tk.DISABLED)
        result_y_erg_mer.config(state=tk.DISABLED)
        result_m_m_erg_mer.config(state=tk.DISABLED)
        result_M_erg_mer.config(state=tk.DISABLED)
        result_r_prime_i.config(state=tk.DISABLED)
        result_r_prime_i_zero.config(state=tk.DISABLED)
        result_x_sum_kwn_i.config(state=tk.DISABLED)
        result_y_sum_kwn_i.config(state=tk.DISABLED)
        result_m_m_sum_kwn_i.config(state=tk.DISABLED)
        result_M_sum_kwn_i.config(state=tk.DISABLED)
        result_u_erg_mer_i.config(state=tk.DISABLED)
        result_v_erg_mer_i.config(state=tk.DISABLED)
        result_x_erg_mer_i.config(state=tk.DISABLED)
        result_y_erg_mer_i.config(state=tk.DISABLED)
        result_m_m_erg_mer_i.config(state=tk.DISABLED)
        result_M_erg_mer_i.config(state=tk.DISABLED)

    except ValueError:
    # Error handling
    # Update the entry fields to indicate the error
        entry1.delete(0, tk.END)
        entry1.insert(0, "Invalid input!")
        entry2.delete(0, tk.END)
        entry2.insert(0, "Invalid input!")
        entry3.delete(0, tk.END)
        entry3.insert(0, "Invalid input!")
        entry4.delete(0, tk.END)
        entry4.insert(0, "Invalid input!")
pass

# Create the main window
root = tk.Tk()
root.title("Math Calculations")

# Create entry boxes for input
label1 = tk.Label(root, text="Μεταβλητή Α :")
label1.grid(row=0, column=0)
entry1 = tk.Entry(root)
entry1.grid(row=0, column=1)

label2 = tk.Label(root, text="Γωνία Φο :")
label2.grid(row=1, column=0)
entry2 = tk.Entry(root)
entry2.grid(row=1, column=1)

label3 = tk.Label(root, text="Λ :")
label3.grid(row=2, column=0)
entry3 = tk.Entry(root)
entry3.grid(row=2, column=1)

label4 = tk.Label(root, text="Φ(i) :")
label4.grid(row=3, column=0)
entry4 = tk.Entry(root)
entry4.grid(row=3, column=1)

# Create text boxes for displaying results
N_label = tk.Label(root, text="N :")
N_label.grid(row=4, column=0)
result_N = tk.Text(root, height=1, width=28, state=tk.DISABLED)
result_N.grid(row=4, column=1)

r_label = tk.Label(root, text="ρ :")
r_label.grid(row=5, column=0)
result_r = tk.Text(root, height=1, width=28, state=tk.DISABLED)
result_r.grid(row=5, column=1)

Rg_label = tk.Label(root, text="Rg :")
Rg_label.grid(row=6, column=0)
result_Rg = tk.Text(root, height=1, width=28, state=tk.DISABLED)
result_Rg.grid(row=6, column=1)

x_orth_mek_label = tk.Label(root, text="Ορθή Mεκατορική X :")
x_orth_mek_label.grid(row=7, column=0)
result_x_orth_mek = tk.Text(root, height=1, width=28, state=tk.DISABLED)
result_x_orth_mek.grid(row=7, column=1)

y_orth_mek_label = tk.Label(root, text="Ορθή Mεκατορική Y :")
y_orth_mek_label.grid(row=8, column=0)
result_y_orth_mek = tk.Text(root, height=1, width=28, state=tk.DISABLED)
result_y_orth_mek.grid(row=8, column=1)

m_m_orth_mek_label = tk.Label(root, text="Ορθή Mεκατορική m_m :")
m_m_orth_mek_label.grid(row=9, column=0)
result_m_m_orth_mek = tk.Text(root, height=1, width=28, state=tk.DISABLED)
result_m_m_orth_mek.grid(row=9, column=1)

M_orth_mek_label = tk.Label(root, text="Ορθή Mεκατορική M :")
M_orth_mek_label.grid(row=10, column=0)
result_M_orth_mek = tk.Text(root, height=1, width=28, state=tk.DISABLED)
result_M_orth_mek.grid(row=10, column=1)

# Additional text box for displaying result r'
r_prime_label = tk.Label(root, text="Σύμμορφη Κωνική ρ :")
r_prime_label.grid(row=11, column=0)
result_r_prime = tk.Text(root, height=1, width=28, state=tk.DISABLED)
result_r_prime.grid(row=11, column=1)

# Additional text box for displaying result r' zero
r_prime_zero_label = tk.Label(root, text="Σύμμορφη Κωνική ρ (zero) :")
r_prime_zero_label.grid(row=12, column=0)
result_r_prime_zero = tk.Text(root, height=1, width=28, state=tk.DISABLED)
result_r_prime_zero.grid(row=12, column=1)

# Additional text box for displaying result theta
theta_label = tk.Label(root, text="Σύμμορφη Κωνική θ :")
theta_label.grid(row=13, column=0)
result_theta = tk.Text(root, height=1, width=28, state=tk.DISABLED)
result_theta.grid(row=13, column=1)

# Additional text box for displaying result x_sum_kwn
x_sum_kwn_label = tk.Label(root, text="Σύμμορφη Κωνική x :")
x_sum_kwn_label.grid(row=14, column=0)
result_x_sum_kwn = tk.Text(root, height=1, width=28, state=tk.DISABLED)
result_x_sum_kwn.grid(row=14, column=1)

# Additional text box for displaying result y_sum_kwn
y_sum_kwn_label = tk.Label(root, text="Σύμμορφη Κωνική y :")
y_sum_kwn_label.grid(row=15, column=0)
result_y_sum_kwn = tk.Text(root, height=1, width=28, state=tk.DISABLED)
result_y_sum_kwn.grid(row=15, column=1)

# Additional text box for displaying result m_m_sum_kwn
m_m_sum_kwn_label = tk.Label(root, text="Σύμμορφη Κωνική m_m :")
m_m_sum_kwn_label.grid(row=16, column=0)
result_m_m_sum_kwn = tk.Text(root, height=1, width=28, state=tk.DISABLED)
result_m_m_sum_kwn.grid(row=16, column=1)

# Additional text box for displaying result M_sum_kwn
M_sum_kwn_label = tk.Label(root, text="Σύμμορφη Κωνική M :")
M_sum_kwn_label.grid(row=17, column=0)
result_M_sum_kwn = tk.Text(root, height=1, width=28, state=tk.DISABLED)
result_M_sum_kwn.grid(row=17, column=1)

# Additional text box for displaying result M_sum_kwn
M_sum_kwn_label = tk.Label(root, text="Eγκάρσια Μερκατορική u :")
M_sum_kwn_label.grid(row=18, column=0)
result_u_erg_mer = tk.Text(root, height=1, width=28, state=tk.DISABLED)
result_u_erg_mer.grid(row=18, column=1)

# Additional text box for displaying result M_sum_kwn
M_sum_kwn_label = tk.Label(root, text="Eγκάρσια Μερκατορική v :")
M_sum_kwn_label.grid(row=19, column=0)
result_v_erg_mer = tk.Text(root, height=1, width=28, state=tk.DISABLED)
result_v_erg_mer.grid(row=19, column=1)

# Additional text box for displaying result M_sum_kwn
M_sum_kwn_label = tk.Label(root, text="Eγκάρσια Μερκατορική x :")
M_sum_kwn_label.grid(row=20, column=0)
result_x_erg_mer = tk.Text(root, height=1, width=28, state=tk.DISABLED)
result_x_erg_mer.grid(row=20, column=1)

# Additional text box for displaying result M_sum_kwn
M_sum_kwn_label = tk.Label(root, text="Eγκάρσια Μερκατορική y :")
M_sum_kwn_label.grid(row=21, column=0)
result_y_erg_mer = tk.Text(root, height=1, width=28, state=tk.DISABLED)
result_y_erg_mer.grid(row=21, column=1)

# Additional text box for displaying result M_sum_kwn
M_sum_kwn_label = tk.Label(root, text="Eγκάρσια Μερκατορική m_m :")
M_sum_kwn_label.grid(row=22, column=0)
result_m_m_erg_mer = tk.Text(root, height=1, width=28, state=tk.DISABLED)
result_m_m_erg_mer.grid(row=22, column=1)

# Additional text box for displaying result M_sum_kwn
M_sum_kwn_label = tk.Label(root, text="Eγκάρσια Μερκατορική M :")
M_sum_kwn_label.grid(row=23, column=0)
result_M_erg_mer = tk.Text(root, height=1, width=28, state=tk.DISABLED)
result_M_erg_mer.grid(row=23, column=1)


# Additional labels for displaying results of Σύμμορφη Κωνική projection
x_sum_kwn_i_label = tk.Label(root, text="Σύμμορφη Κωνική X (i) :")
x_sum_kwn_i_label.grid(row=26, column=0)
result_x_sum_kwn_i = tk.Text(root, height=1, width=28, state=tk.DISABLED)
result_x_sum_kwn_i.grid(row=26, column=1)

y_sum_kwn_i_label = tk.Label(root, text="Σύμμορφη Κωνική Y (i) :")
y_sum_kwn_i_label.grid(row=27, column=0)
result_y_sum_kwn_i = tk.Text(root, height=1, width=28, state=tk.DISABLED)
result_y_sum_kwn_i.grid(row=27, column=1)

m_m_sum_kwn_i_label = tk.Label(root, text="Σύμμορφη Κωνική m_m (i) :")
m_m_sum_kwn_i_label.grid(row=28, column=0)
result_m_m_sum_kwn_i = tk.Text(root, height=1, width=28, state=tk.DISABLED)
result_m_m_sum_kwn_i.grid(row=28, column=1)

M_sum_kwn_i_label = tk.Label(root, text="Σύμμορφη Κωνική M (i) :")
M_sum_kwn_i_label.grid(row=29, column=0)
result_M_sum_kwn_i = tk.Text(root, height=1, width=28, state=tk.DISABLED)
result_M_sum_kwn_i.grid(row=29, column=1)

# Additional labels for displaying the value of "r_prime_i" and "r_prime_i_zero"
r_prime_i_label = tk.Label(root, text="Σύμμορφη Κωνική ρ (i):")
r_prime_i_label.grid(row=24, column=0)
result_r_prime_i = tk.Text(root, height=1, width=28, state=tk.DISABLED)
result_r_prime_i.grid(row=24, column=1)

r_prime_i_zero_label = tk.Label(root, text="Σύμμορφη Κωνική ρ (zero)(i):")
r_prime_i_zero_label.grid(row=25, column=0)
result_r_prime_i_zero = tk.Text(root, height=1, width=28, state=tk.DISABLED)
result_r_prime_i_zero.grid(row=25, column=1)

u_erg_mer_i_label = tk.Label(root, text="Eγκάρσια Μερκατορική u (i):")
u_erg_mer_i_label.grid(row=30, column=0)
result_u_erg_mer_i = tk.Text(root, height=1, width=28, state=tk.DISABLED)
result_u_erg_mer_i.grid(row=30, column=1)

v_erg_mer_i_label = tk.Label(root, text="Eγκάρσια Μερκατορική v (i):")
v_erg_mer_i_label.grid(row=31, column=0)
result_v_erg_mer_i = tk.Text(root, height=1, width=28, state=tk.DISABLED)
result_v_erg_mer_i.grid(row=31, column=1)

x_erg_mer_i_label = tk.Label(root, text="Eγκάρσια Μερκατορική x (i):")
x_erg_mer_i_label.grid(row=32, column=0)
result_x_erg_mer_i = tk.Text(root, height=1, width=28, state=tk.DISABLED)
result_x_erg_mer_i.grid(row=32, column=1)

y_erg_mer_i_label = tk.Label(root, text="Eγκάρσια Μερκατορική y (i):")
y_erg_mer_i_label.grid(row=33, column=0)
result_y_erg_mer_i = tk.Text(root, height=1, width=28, state=tk.DISABLED)
result_y_erg_mer_i.grid(row=33, column=1)

m_m_erg_mer_i_label = tk.Label(root, text="Eγκάρσια Μερκατορική m_m (i):")
m_m_erg_mer_i_label.grid(row=34, column=0)
result_m_m_erg_mer_i = tk.Text(root, height=1, width=28, state=tk.DISABLED)
result_m_m_erg_mer_i.grid(row=34, column=1)

M_erg_mer_i_label = tk.Label(root, text="Eγκάρσια Μερκατορική M (i):")
M_erg_mer_i_label.grid(row=35, column=0)
result_M_erg_mer_i = tk.Text(root, height=1, width=28, state=tk.DISABLED)
result_M_erg_mer_i.grid(row=35, column=1)

# Create a button to perform calculations
calculate_button = tk.Button(root, text="Calculate", command=calculate)
calculate_button.grid(row=36, columnspan=2)

# Run the Tkinter event loop
root.mainloop()
