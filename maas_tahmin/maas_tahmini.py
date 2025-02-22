import tkinter as tk
# from tkinter import messagebox
import pandas as pd
veriler = pd.read_csv("maaslar_yeni.csv")
print(veriler)

test_verisi = veriler.iloc[:,2:5].values
maas = veriler.iloc[:,-1:].values

##random forest modeli
from sklearn.ensemble import RandomForestRegressor
rf_reg = RandomForestRegressor(n_estimators = 10 , random_state=0)   ### n_estimators = karar ağacı sayısı
rf_reg.fit(test_verisi,maas)

##decision tree modeli
from sklearn.tree import DecisionTreeRegressor
tree_reg = DecisionTreeRegressor(random_state=0)
tree_reg .fit(test_verisi,maas)


##arayüz
arayüz = tk.Tk()
var = tk.StringVar()
var1 = tk.IntVar()
arayüz.title("Maaş Tahmin Arayüzü")
arayüz.geometry("500x500")

tk.Label(arayüz, text="Unvan Seviyesi:").pack()
unvan_entry = tk.Entry(arayüz)
unvan_entry.pack()

tk.Label(arayüz, text="Kıdem:").pack()
kidem_entry = tk.Entry(arayüz)
kidem_entry.pack()

tk.Label(arayüz, text="Puan:").pack()
puan_entry = tk.Entry(arayüz)
puan_entry.pack()

tk.Label(arayüz, text="Gerçek Maaş:").pack()
maas_entry = tk.Entry(arayüz)
maas_entry.pack()

label = tk.Label(textvariable=var).pack()
label2= tk.Label(textvariable=var1).pack()


    
    

def PREDICT_BUTTON():
    # try:
    unvanSeviyesi = int(unvan_entry.get())
    kidem = int(kidem_entry.get())
    puan = int(puan_entry.get())
    maas = float(maas_entry.get())
        
    maas_pre_rf = rf_reg.predict([[unvanSeviyesi, kidem, puan]])
    maas_pre_tree = tree_reg.predict([[unvanSeviyesi, kidem, puan]])
        
    Fınal_pre = (maas_pre_rf+maas_pre_tree)/2
    percentage = (abs(Fınal_pre-maas)/maas)*100
    print(f"maaş tahmini : {Fınal_pre[0]}")
    print(f"Hata yüzdesi : {percentage[0]}")
    var1.set(f"Hata yüzdesi : %{percentage[0]}")
    var.set( f"maaş tahmini : {Fınal_pre[0]}")
    
        # Yeni veriyi dosyaya ekle
    yeni_veri = pd.DataFrame([[unvanSeviyesi, kidem, puan, maas]], columns=['UnvanSeviyesi', 'Kidem', 'Puan', 'maas'])
    global veriler
    veriler = pd.concat([veriler, yeni_veri], ignore_index=True)
    veriler.to_csv("maaslar_yeni.csv", index=False)
        
    #     messagebox.showinfo("Bilgi", "Yeni veri başarıyla kaydedildi!")
    # except ValueError:
    #     messagebox.showerror("Hata", "Lütfen geçerli sayısal değerler girin!")
tk.Button(arayüz, text="tahmin",command=PREDICT_BUTTON).pack()
arayüz.mainloop()

# ##lineer regression modeli
# from sklearn.linear_model import LinearRegression
# lin_reg = LinearRegression()
# lin_reg.fit(test_verisi,maas)
# maas_pre_lin = lin_reg.predict([[unvanSeviyesi, kidem, puan]])
# print(f" lr Tahmini Maaş: {maas_pre_lin[0]}")

##polinomial regression model
# from sklearn.preprocessing import PolynomialFeatures
# poly_reg = PolynomialFeatures( degree = 2)

# veri_poly = poly_reg.fit_transform(test_verisi)
# lin_reg.fit(veri_poly,maas)

# plt.scatter(veriler.iloc[:,0:1],maas)
# plt.plot(veriler.iloc[:,0:1], lin_reg.predict(veri_poly) )
