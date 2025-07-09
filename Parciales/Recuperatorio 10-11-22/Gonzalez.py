# -*- coding: utf-8 -*-
"""
Created on Fri May 30 17:45:27 2025

Se desea implementar un sistema de filtrado que permita remover de una señal de ECG
artefactos producto del movimiento del paciente. La señal cuenta además con algunas
interferencias productos de armónicos superiores de la señal de línea (50Hz)

@author: alkas
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import find_peaks
from funciones_fft import fft_mag
from import_analogfilterwizard import import_AnalogFilterWizard
from import_ltspice import import_AC_LTSpice
import filter_parameters
import sympy as sy
from time import time

"""
1. Proponga la función de transferencia analógica de un filtro pasa-banda con los
siguientes requerimientos:
● Atenuación menor a 0.1dB en la banda de paso (0.67 Hz a 40 Hz).
● Atenuación de al menos 30dB para frecuencias menores a 0.2 Hz, para
remover los artefactos de movimiento.
● Se desea utilizar la sección pasabajos del filtro pasa-banda como filtro anti
-alias. La señal será adquirida a una frecuencia de 300Hz con un CAD de 16
bits y Vref=5V.
● Cuenta con la señal ecg 860Hz.txt (muestreada a 860Hz) para analizar el
espectro y obtener los requisitos.

"""

filename='ecg_860Hz.txt'
signal=np.loadtxt(filename)

N=len(signal)
fs=860
T=N/fs
ts=1/fs
t=np.linspace(0, N*ts,N)

f_resample=300

# FFT
f, fft_signal = fft_mag(signal, fs)

plt.figure(figsize=(14, 6))
plt.plot(f, fft_signal)
plt.xlabel('Frecuencia [Hz]')
plt.ylabel('Magnitud')
plt.title('FFT de la señal ECG')
plt.grid(True)
plt.show()

# Frecuencia máxima para banda de paso
fb = 40
f_nyquist=150
# --------------------------------------
# 🔍 Búsqueda de picos después de 40 Hz
# --------------------------------------
# Parámetros del ADC
V_REF = 5
N_BITS = 16
RES = V_REF / (2**N_BITS - 1)  # resolución en V
mask = f >= f_nyquist
fft_cut = fft_signal[mask]
f_cut = f[mask]

# Encontrar picos prominentes
peaks, props = find_peaks(fft_cut, height= 0.5   , prominence=0.0002, distance=10)
f_peaks = f_cut[peaks]
h_peaks = fft_cut[peaks]

# Mostrar los más importantes
sorted_indices = np.argsort(h_peaks)[::-1]  # ordenar de mayor a menor amplitud
top_n = 10  # número máximo de picos relevantes a mostrar
f_top = f_peaks[sorted_indices[:top_n]]
h_top = h_peaks[sorted_indices[:top_n]]

# --------------------------------------
# 🧮 Cálculo de atenuaciones necesarias
# --------------------------------------



print("Banda de paso hasta 40 Hz")
print("\nPicos relevantes fuera de banda:")
for i in range(len(f_top)):
    at = 20 * np.log10(h_top[i] / RES)
    print(f"→ Interferencia de {h_top[i]*1000:.2f} mV en {f_top[i]:.2f} Hz: se necesita atenuación ≥ {at:.2f} dB")


# --- Valor en fs/2
idx_nyq = np.argmin(np.abs(f - f_nyquist))  # índice de la frecuencia más cercana a fs/2
f_fs2 = f[idx_nyq]
h_fs2 = fft_signal[idx_nyq]

# --------------------------------------
# 📈 Visualización
# --------------------------------------

# --- Imprimir resultados
print("Banda de paso hasta 40 Hz\n")
print("Picos relevantes fuera de banda:")
for i in range(len(f_top)):
    at = 20 * np.log10(h_top[i] / RES)
    print(f"→ Interferencia de {h_top[i]*1000:.2f} mV en {f_top[i]:.2f} Hz: se necesita atenuación ≥ {at:.2f} dB")

# --- Valor en fs/2
at_fs2 = 20 * np.log10(h_fs2 / RES)
print(f"\nValor en Nyquist (fs/2 = {f_fs2:.2f} Hz): {h_fs2*1000:.2f} mV → atenuación necesaria ≥ {at_fs2:.2f} dB")

# --- Gráfico
plt.figure(figsize=(18, 10))
plt.plot(f, fft_signal, color='green', label='Magnitud FFT')
plt.axvline(x=f_nyquist, color="black", linestyle="--", label='f_nyquist = 150 Hz')
plt.axvline(x=f_fs2, color="gray", linestyle="--", label=f'fs/2 = {f_fs2:.2f} Hz')
plt.plot(f_top, h_top, 'rx', markersize=10, label='Picos detectados')
plt.plot(f_fs2, h_fs2, 'rx', markersize=10, label='Valor en fs/2')
plt.title("Espectro de la señal ECG + interferencias detectadas")
plt.xlabel("Frecuencia [Hz]")
plt.ylabel("Magnitud")
plt.grid(True)
plt.legend()
plt.show()

#ahora que se que los valores de atenuacion de mi filtro deben de ser 34.44 db en 300hz, 30.99 db en 200 hz  y en nyquist como el valor es menor 
#a 1 me da una atenuacion que en realidad es una ganancia entonces pierde sentido porque ya es menor que el valor de resolucion del adc.
#la consulta aca es, me interesa a mi hacer un filtro analogico un poco mejor para evitar filros de alto orden digital? o este filtro analogico 
#lo hago un pasabajo que atenue hasta 150 hz y despues hago otro filtro que filtre bien en 40?

f, mag = import_AnalogFilterWizard('Files/Data Files/Magnitude(dB).csv')

f_sim, mag_sim, _ = import_AC_LTSpice('Files/ACAnalysis.txt')

# --- Gráfico comparativo de la respuesta del filtro y las atenuaciones necesarias ---
fig3, ax3 = plt.subplots(1, 1, figsize=(14, 8))

ax3.set_title('Comparación del filtro con los requisitos de atenuación', fontsize=18)
ax3.set_xlabel('Frecuencia [Hz]', fontsize=15)
ax3.set_ylabel('Magnitud [dB]', fontsize=15)
ax3.set_xscale('log')
ax3.grid(True, which="both")

# Curvas del filtro
ax3.plot(f, mag, label='Filtro diseñado', linewidth=2)
ax3.plot(f_sim, mag_sim, label='Filtro simulado', linestyle='--', linewidth=2)

# Requisitos de atenuación marcados en los picos detectados
for i in range(len(f_top)):
    at_req = 20 * np.log10(h_top[i] / RES)
    ax3.plot(f_top[i], -at_req, 'rx', markersize=10)
    ax3.annotate(f"{at_req:.1f} dB", (f_top[i], -at_req), textcoords="offset points", xytext=(0, 10), ha='center', fontsize=10, color='red')

# Valor en Nyquist
ax3.plot(f_fs2, -at_fs2, 'ko', label='Atenuación requerida en fs/2')
ax3.annotate(f"{at_fs2:.1f} dB", (f_fs2, -at_fs2), textcoords="offset points", xytext=(0, 10), ha='center', fontsize=10)

# Leyenda
ax3.legend(loc="lower left", fontsize=12)

#este grafico tendria un poco mas de sentido si no fuese una situacion ficticia en la que tengo todos los valores de resistencia y comerciales
#disponibles, ademas despues se podria comparar con la atenuacion en un filtro real, midiendolo con un osiloscopio y viendo como atenua
#levantando una curva y compararla con los filtros diseniados simulados e implementados

#ahora lo que quiero hacer es un filtro digital pasabanda para terminar con pb 0.65 a 40hz con -0.1db y frecuencias menores a 0.2 con 30db atenuacion


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

#%% Análisis de los Filtros 

# Se calcula la respuesta en frecuencia de los filtros
f_iir, h_iir = signal.freqz(Num_iir, Den_iir, worN=f, fs=f_resample)

# Se grafican las respuestas de los filtros
ax2[0].plot(f_fir, abs(h_fir), label='Filtro FIR', color='orange')
ax2[0].legend(loc="upper right", fontsize=15)
ax2[1].plot(f_iir, abs(h_iir), label='Filtro IIR', color='green')
ax2[1].legend(loc="upper right", fontsize=15)

# Se evalúa la atenuación en las frecuncias de interés 
_, h1_fir = signal.freqz(Num_fir, Den_fir, worN=[0.01, 20], fs=FS_resample)
_, h1_iir = signal.freqz(Num_iir, Den_iir, worN=[0.01, 20], fs=FS_resample)

print("La atenuación del filtro FIR en 0.01Hz es de {:.2f}dB".format(20*np.log10(abs(h1_fir[0]))))
print("La atenuación del filtro FIR en 20Hz es de {:.2f}dB".format(20*np.log10(abs(h1_fir[1]))))
print("La atenuación del filtro IIR en 0.01Hz es de {:.2f}dB".format(20*np.log10(abs(h1_iir[0]))))
print("La atenuación del filtro IIR en 20Hz es de {:.2f}dB".format(20*np.log10(abs(h1_iir[1]))))
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

print("El algoritmo de filtrado FIR toma {:.3f}s".format(t_end_fir - t_start_fir))
print("El algoritmo de filtrado IIR toma {:.3f}s".format(t_end_iir - t_start_iir))


process_code.iir_sos_header('cheby6.h', signal.tf2sos(Num_iir, Den_iir))






