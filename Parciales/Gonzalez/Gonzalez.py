# -*- coding: utf-8 -*-
"""
Created on Mon Jun  9 09:17:44 2025

@author: alkas
"""

from scipy.io import wavfile
import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import find_peaks
from funciones_fft import fft_mag
from import_analogfilterwizard import import_AnalogFilterWizard
from import_ltspice import import_AC_LTSpice
import filter_parameters
import sympy as sy
from time import time
from scipy import signal

#cargo los archivos

tos1 = 'tos1.wav'
tos2= 'tos2.wav'
tos3='tos3.wav'
tos4='tos4.wav'

fs1, tos1 = wavfile.read(tos1)   # frecuencia de muestreo y datos de la señal   
fs2, tos2 = wavfile.read(tos2)   #la fs es 48khz
fs3, tos3 = wavfile.read(tos3)
fs4, tos4 = wavfile.read(tos4)

# Definición de parámetro temporales
ts = 1 / fs1                     		# tiempo de muestreo


N1 = len(tos1)                   		# número de muestras en el archivo de audio
N2 = len(tos2)
N3 = len(tos3)
N4 = len(tos4)

t1 = np.linspace(0, N1 * ts, N1)   	# vector de tiempo
t2 = np.linspace(0, N2 * ts, N2)
t3 = np.linspace(0, N3 * ts, N3)
t4 = np.linspace(0, N4 * ts, N4)
 
tos1_signal = tos1 * 3.3 / (2 ** 16 - 1)       #se escala la señal a voltios (considerando un CAD de 16bits y Vref 3.3V)
tos2_signal = tos2* 3.3 / (2 ** 16 - 1) 
tos3_signal = tos3 * 3.3 / (2 ** 16 - 1) 
tos4_signal = tos4 * 3.3 / (2 ** 16 - 1) 
"""
#verifico que esten bien cargadas ploteando
plt.figure(figsize=(14, 6))
plt.plot(t1, tos1_signal)
plt.xlabel('tiempo[s]')
plt.ylabel('Volts[V]')
plt.title('senial tos 1')
plt.grid(True)
plt.show()

plt.figure(figsize=(14, 6))
plt.plot(t2, tos2_signal)
plt.xlabel('tiempo[s]')
plt.ylabel('Volts[V]')
plt.title('senial tos 2')
plt.grid(True)
plt.show()

plt.figure(figsize=(14, 6))
plt.plot(t3,tos3_signal)
plt.xlabel('tiempo[s]')
plt.ylabel('Volts[V]')
plt.title('senial tos 3')
plt.grid(True)
plt.show()

plt.figure(figsize=(14, 6))
plt.plot(t4, tos4_signal)
plt.xlabel('tiempo[s]')
plt.ylabel('Volts[V]')
plt.title('senial tos 4')
plt.grid(True)
plt.show()
"""

#parecen estar cargadas correctamente por lo que continuo con el filtro antialias
"""

Determinar los requisitos de diseño de un filtro antialiasing adecuado para 
la aplicación, teniendo en cuenta que la adquisición de datos se realizará a 
8 kHz con 16 bits de resolución (Vref: 3,3 V). El filtro debe poseer una respuesta 
máximamente plana en la banda de paso

"""

#para determinar los requisitos de disenio del filtro antialias, es necesario realizar un analisis frecuencial
#y ver en que frecuencias mayores a fm/2 me generan aliasing, esto seria que la amplitud del modulo en las frecuencias 
#mayores a fm/2 no deben superar la resolucion de mi adc, y si lo hace tengo que ver cuanto tengo que atenuar para que no o haga

#calculo la fft
f1, fft_tos1 = fft_mag(tos1, fs1)
f2, fft_tos2 = fft_mag(tos2, fs2)
f3, fft_tos3 = fft_mag(tos3, fs3)
f4, fft_tos4 = fft_mag(tos4, fs4)

#nuevamente grafico para verificar visualmente que las transformadas son correctas

plt.figure(figsize=(14, 6))
plt.plot(f1, fft_tos1)
plt.xlabel('Frecuencia [Hz]')
plt.ylabel('Magnitud')
plt.title('FFT de la tos1')
plt.grid(True)
plt.show()

plt.figure(figsize=(14, 6))
plt.plot(f2, fft_tos2)
plt.xlabel('Frecuencia [Hz]')
plt.ylabel('Magnitud')
plt.title('FFT de la tos2')
plt.grid(True)
plt.show()

plt.figure(figsize=(14, 6))
plt.plot(f3, fft_tos3)
plt.xlabel('Frecuencia [Hz]')
plt.ylabel('Magnitud')
plt.title('FFT de la tos3')
plt.grid(True)
plt.show()

plt.figure(figsize=(14, 6))
plt.plot(f4, fft_tos4)
plt.xlabel('Frecuencia [Hz]')
plt.ylabel('Magnitud')
plt.title('FFT de la tos4')
plt.grid(True)
plt.show()


#ahora calculo mis requerimientos para mi filtro antialias

f_resample=8000 #se va a remuestrear a 8khz
f_nyquist=f_resample/2

V_REF = 3.3
N_BITS = 16

RES = V_REF / (2**N_BITS - 1)  # resolución en V

#una vez que yo se cuales son los valores de frecuencia a los que voy a remuestrear la senial, debo analizar el contenido espectral de mi senial
#siendo de interes los valores por encima de fs/2 que me van a generar aliasing , tengo dos puntos de interes, en fm/2 (atenuacion con la que tengo 
#que ingresar a esta zona) y en la max amp despues de fm/2
# atenuacion maxima que tiene que tener el filtro 


mask1 = f1 >= f_nyquist
mask2 = f2 >= f_nyquist
mask3 = f3 >= f_nyquist
mask4 = f4 >= f_nyquist

fft_cut1 = fft_tos1[mask1]
fft_cut2 = fft_tos2[mask2]
fft_cut3 = fft_tos3[mask3]
fft_cut4 = fft_tos4[mask4]

f_cut1 = f1[mask1]
f_cut2 = f2[mask2]
f_cut3 = f3[mask3]
f_cut4 = f4[mask4]

# Encontrar picos prominentes
peaks1, props1 = find_peaks(fft_cut1, height=2   , prominence=0.5, distance=10)
peaks2, props2 = find_peaks(fft_cut2, height= 2   , prominence=0.5, distance=10)
peaks3, props3 = find_peaks(fft_cut3, height= 2   , prominence=0.5, distance=10)
peaks4, props4 = find_peaks(fft_cut4, height=2   , prominence=0.5, distance=10)

f_peaks1 = f_cut1[peaks1]
f_peaks2 = f_cut2[peaks2]
f_peaks3 = f_cut3[peaks3]
f_peaks4 = f_cut4[peaks4]

h_peaks1 = fft_cut1[peaks1]
h_peaks2 = fft_cut2[peaks2]
h_peaks3 = fft_cut3[peaks3]
h_peaks4 = fft_cut4[peaks4]

# Mostrar los más importantes
sorted_indices1 = np.argsort(h_peaks1)[::-1]  # ordenar de mayor a menor amplitud
sorted_indices2 = np.argsort(h_peaks2)[::-1]  # ordenar de mayor a menor amplitud
sorted_indices3 = np.argsort(h_peaks3)[::-1]  # ordenar de mayor a menor amplitud
sorted_indices4 = np.argsort(h_peaks4)[::-1]  # ordenar de mayor a menor amplitud

top_n = 10  # número máximo de picos relevantes a mostrar
f_top1 = f_peaks1[sorted_indices1[:top_n]]
f_top2 = f_peaks2[sorted_indices2[:top_n]]
f_top3 = f_peaks3[sorted_indices3[:top_n]]
f_top4 = f_peaks4[sorted_indices4[:top_n]]

h_top1 = h_peaks1[sorted_indices1[:top_n]]
h_top2 = h_peaks2[sorted_indices2[:top_n]]
h_top3 = h_peaks3[sorted_indices3[:top_n]]
h_top4 = h_peaks4[sorted_indices4[:top_n]]


# --- Valor en fs/2
idx_nyq1 = np.argmin(np.abs(f1 - f_nyquist))  # índice de la frecuencia más cercana a fs/2
f1_fs2 = f1[idx_nyq1]
h1_fs2 = fft_tos1[idx_nyq1]

idx_nyq2 = np.argmin(np.abs(f2 - f_nyquist))  # índice de la frecuencia más cercana a fs/2
f2_fs2 = f2[idx_nyq2]
h2_fs2 = fft_tos2[idx_nyq2]

idx_nyq3 = np.argmin(np.abs(f3 - f_nyquist))  # índice de la frecuencia más cercana a fs/2
f3_fs2 = f3[idx_nyq3]
h3_fs2 = fft_tos3[idx_nyq3]

idx_nyq4 = np.argmin(np.abs(f4 - f_nyquist))  # índice de la frecuencia más cercana a fs/2
f4_fs2 = f4[idx_nyq4]
h4_fs2 = fft_tos4[idx_nyq4]



print("Banda de paso hasta 4000 Hz\n")
print("Picos relevantes fuera de banda:")
for i in range(len(f_top1)):
    at1 = 20 * np.log10(h_top1[i] / RES)
    at2 = 20 * np.log10(h_top2[i] / RES)
    at3 = 20 * np.log10(h_top3[i] / RES)
    at4 = 20 * np.log10(h_top4[i] / RES)
    
    print(f"→ EN TOS 1 Interferencia de {h_top1[i]*1000:.2f} mV en {f_top1[i]:.2f} Hz: se necesita atenuación ≥ {at1:.2f} dB")
    print(f"→ EN TOS 2 Interferencia de {h_top2[i]*1000:.2f} mV en {f_top2[i]:.2f} Hz: se necesita atenuación ≥ {at2:.2f} dB")
    print(f"→ EN TOS 3 Interferencia de {h_top3[i]*1000:.2f} mV en {f_top3[i]:.2f} Hz: se necesita atenuación ≥ {at3:.2f} dB")
    print(f"→ EN TOS 4 Interferencia de {h_top4[i]*1000:.2f} mV en {f_top4[i]:.2f} Hz: se necesita atenuación ≥ {at4:.2f} dB")

# --- Atenuacion en fs/2
at1_fs2 = 20 * np.log10(h1_fs2 / RES)
at2_fs2 = 20 * np.log10(h2_fs2 / RES)
at3_fs2 = 20 * np.log10(h3_fs2 / RES)
at4_fs2 = 20 * np.log10(h4_fs2 / RES)

print(f"\nValor en Nyquist  para la tos 1(fs/2 = {f1_fs2:.2f} Hz): {h1_fs2*1000:.2f} mV → atenuación necesaria ≥ {at1_fs2:.2f} dB")
print(f"\nValor en Nyquist  para la tos 2(fs/2 = {f2_fs2:.2f} Hz): {h2_fs2*1000:.2f} mV → atenuación necesaria ≥ {at2_fs2:.2f} dB")
print(f"\nValor en Nyquist  para la tos 3(fs/2 = {f3_fs2:.2f} Hz): {h3_fs2*1000:.2f} mV → atenuación necesaria ≥ {at3_fs2:.2f} dB")
print(f"\nValor en Nyquist  para la tos 4(fs/2 = {f4_fs2:.2f} Hz): {h4_fs2*1000:.2f} mV → atenuación necesaria ≥ {at4_fs2:.2f} dB")

# --- Gráfico
plt.figure(figsize=(18, 10))
plt.plot(f1, fft_tos1, color='green', label='Magnitud FFT')
plt.axvline(x=f_nyquist, color="black", linestyle="--", label='f_nyquist = 4000 Hz')
plt.axvline(x=f1_fs2, color="gray", linestyle="--", label=f'fs/2 = {f1_fs2:.2f} Hz')
plt.plot(f_top1, h_top1, 'rx', markersize=10, label='Picos detectados')
plt.plot(f1_fs2, h1_fs2, 'rx', markersize=10, label='Valor en fs/2')
plt.title("Espectro de la señal tos1 + interferencias detectadas")
plt.xlabel("Frecuencia [Hz]")
plt.ylabel("Magnitud")
plt.grid(True)
plt.legend()
plt.show()

plt.figure(figsize=(18, 10))
plt.plot(f2, fft_tos2, color='red', label='Magnitud FFT')
plt.axvline(x=f_nyquist, color="black", linestyle="--", label='f_nyquist = 4000 Hz')
plt.axvline(x=f2_fs2, color="gray", linestyle="--", label=f'fs/2 = {f2_fs2:.2f} Hz')
plt.plot(f_top2, h_top2, 'rx', markersize=10, label='Picos detectados')
plt.plot(f2_fs2, h2_fs2, 'rx', markersize=10, label='Valor en fs/2')
plt.title("Espectro de la señal tos 2 + interferencias detectadas")
plt.xlabel("Frecuencia [Hz]")
plt.ylabel("Magnitud")
plt.grid(True)
plt.legend()
plt.show()

plt.figure(figsize=(18, 10))
plt.plot(f3, fft_tos3, color='black', label='Magnitud FFT')
plt.axvline(x=f_nyquist, color="black", linestyle="--", label='f_nyquist = 4000 Hz')
plt.axvline(x=f3_fs2, color="gray", linestyle="--", label=f'fs/2 = {f3_fs2:.2f} Hz')
plt.plot(f_top3, h_top3, 'rx', markersize=10, label='Picos detectados')
plt.plot(f3_fs2, h3_fs2, 'rx', markersize=10, label='Valor en fs/2')
plt.title("Espectro de la señal de la tos 3 + interferencias detectadas")
plt.xlabel("Frecuencia [Hz]")
plt.ylabel("Magnitud")
plt.grid(True)
plt.legend()
plt.show()

plt.figure(figsize=(18, 10))
plt.plot(f4, fft_tos4, color='Violet', label='Magnitud FFT')
plt.axvline(x=f_nyquist, color="black", linestyle="--", label='f_nyquist = 4000 Hz')
plt.axvline(x=f4_fs2, color="gray", linestyle="--", label=f'fs/2 = {f4_fs2:.2f} Hz')
plt.plot(f_top4, h_top4, 'rx', markersize=10, label='Picos detectados')
plt.plot(f4_fs2, h4_fs2, 'rx', markersize=10, label='Valor en fs/2')
plt.title("Espectro de la señal de la tos 4 + interferencias detectadas")
plt.xlabel("Frecuencia [Hz]")
plt.ylabel("Magnitud")
plt.grid(True)
plt.legend()
plt.show()

#de esto puedo ver que mi peor caso es la senial 2 de la voz por lo que voy a hacer un filtro antialias que 
#cubra estos requerimientos  fs2_2=100.35 db de atenuacion y evaluo, porque en tos3 tengo picos mucho menores que en
#tos2 pero mas cerca de mi fs/2 asi que procedo a ver si mi filtro cumple con los requerimientos de atenuacion en
#tos3 f=4066 at=98.14 db  y en tos 2 en 5201hz una at de 111.17 dB como tengo 100.35 db como requisito de 
#atenuacion en mi fs/2 entonces se que el de tos 3 lo voy a cumplir por lo que procedo a realizar el filtro

"""
En base a los requerimientos anteriores, diseñe el filtro antialiasing utilizando la herramienta Analog Filter Wizard.
Para la implementación utilice una configuración de Múltiples Realimentaciones, resistencias del 10% de precisión y 
capacitores del 20% (ver tabla).

"""
 
#con los requisitos planteados para tos 2 como mi bp esta entre 500hz y 1200hz, entonces puedo plantear un sobremuestreo
#ademas como se me pide una bp maximamente plana me esta pidiendo que sea un butterworth
#como la consigna me pide que use resistencias del 10% y capacitores del 20% planteo esto como un requerimiento tambien
#como tengo que tener un filtro butter con la respuesta lo mas plana posible por lo que intente mantener esto pero si quiero
#no implementar un chebyshev voy a necesitar aumentar mucho el orden y el wizard no me deja aumentarlo sobre n=10 entonces
#algo de ruido voy a tener que dejar pasar, se consigue en el peor de los casos con los peores componentes cerca 
#de 90 db en 4khz

#se implemento en wizzard



"""
Utilizando la herramienta pyFDA diseñe un filtro de tipo IIR de orden 8 que permita rescatar
 el rango de frecuencias de interés. Pruebe el filtro diseñado sobre una de las señales de prueba 
 (remuestreado previamente a 8 kHz). Grafique la señal y su espectro antes y después del filtrado.
 
"""

filtro_iir = np.load('IIR.npz', allow_pickle=True) 
print("\r\n")
print("Filtro IIR:")
filter_parameters.filter_parameters('IIR.npz')
print("\r\n")


# Se extraen los coeficientes de numerador y denominador

Num_iir, Den_iir = filtro_iir['ba'] 

# Se expresan las funciones de transferencias (H(z))
z = sy.Symbol('z') # Se crea una variable simbólica z
Hz = sy.Symbol('H(z)')


Numz_iir = 0
Denz_iir = 0
for i in range(len(Num_iir)): # Se arma el polinomio del numerador
    Numz_iir += Num_iir[i] * np.power(z, -i)
for i in range(len(Den_iir)): # Se arma el polinomio del denominador
    Denz_iir += Den_iir[i] * np.power(z, -i)
print("La función de transferencia del Filtro IIR es:")
print(sy.pretty(sy.Eq(Hz, Numz_iir.evalf(3) / Denz_iir.evalf(3)))) 
print("\r\n")

#%% Análisis de los Filtros               de aca para abajo no anda nada



T=N2*ts
N_resample= int(4000*T)
tos2= signal.resample(tos2[0:N2], N_resample)

# Se calcula la respuesta en frecuencia de los filtros
f_iir, h_iir = signal.freqz(Num_iir, Den_iir, worN=f2, fs=f_resample)

# Se grafican las respuestas de los filtros
fig2, ax2 = plt.subplots(2, 1, figsize=(15, 15), sharex=True)
ax2[1].plot(f_iir, abs(h_iir), label='Filtro IIR', color='green')
ax2[1].legend(loc="upper right", fontsize=15)

# Se evalúa la atenuación en las frecuncias de interés 

print("La atenuación del filtro IIR en 0.01Hz es de {:.2f}dB".format(20*np.log10(abs(h_iir[0]))))
print("La atenuación del filtro IIR en 20Hz es de {:.2f}dB".format(20*np.log10(abs(h_iir[1]))))
print("\r\n")

# Se extraen polos y ceros de los filtros  
zeros_iir, polos_iir, k_iir =   filtro_iir['zpk']

# Se grafican las distribuciones de ceros y polos
fig3, ax3 = plt.subplots(1, 2, figsize=(15, 7))
fig3.suptitle("Distribución de Ceros y Polos en el plano Z", fontsize=18)


ax3[1].set_title('Filto IIR', fontsize=15)
ax3[1].add_patch(patches.Circle((0,0), radius=1, fill=False, alpha=0.1))
ax3[1].plot(polos_iir.real, polos_iir.imag, 'x', label='Polos', color='red',
            markersize=10, alpha=0.5)
ax3[1].plot(zeros_iir.real, zeros_iir.imag, 'o', label='Ceros', color='none',
            markersize=10, alpha=0.5, markeredgecolor='blue')
lim = 1.2 * np.max([np.max(abs(polos_iir)), np.max(abs(zeros_iir))])
ax3[1].set_xlim(-lim, lim)
ax3[1].set_ylim(-lim, lim)
ax3[1].set_ylabel('Imag(z)', fontsize=15)
ax3[1].set_xlabel('Real(z)', fontsize=15)
ax3[1].grid()
ax3[1].legend(loc="upper right", fontsize=12)

#%% Filtrado de la Señal 

# Se aplica el filtrado sobre la señal
senial_iir = signal.lfilter(Num_iir, Den_iir, senial)

    
# Se grafican las señales filtradas

ax1[0].plot(t_resampled, senial_iir, label='Señal Filtrada (IIR)', color='purple')

# Se calculan y grafican sus espectros (normalizados)

f1_iir, senial_iir_fft_mod = funciones_fft.fft_mag(senial_iir, FS_resample)

ax2[0].plot(f1_iir, senial_iir_fft_mod/np.max(senial_fft_mod), 
            label='Senial Filtrada IIR', color='purple')

plt.show()

#%% Evaluar Performance del Filtro 

# Se aplica el filtrado sobre la señal 500 veces y se mide el tiempo requerido
# por el algoritmo

t_start_iir = time()
for i in range(500):
    senial_iir = signal.lfilter(Num_iir, Den_iir, senial)
t_end_iir = time()

print("El algoritmo de filtrado IIR toma {:.3f}s".format(t_end_iir - t_start_iir))











        











