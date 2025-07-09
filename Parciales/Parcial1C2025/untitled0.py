# -*- coding: utf-8 -*-
"""
Created on Wed Jun 18 16:59:50 2025

@author: alkas
"""

import numpy as np
import matplotlib.pyplot as plt
from funciones_fft import fft_mag
from import_ltspice import import_AC_LTSpice
from import_analogfilterwizard import import_AnalogFilterWizard
from scipy.io import wavfile 
from scipy import signal
import filter_parameters
import sympy as sy
from matplotlib import patches

archivo_audio1 = 'Seniales/tos1.wav' 
archivo_audio2 = 'Seniales/tos2.wav' 
archivo_audio3 = 'Seniales/tos3.wav' 
archivo_audio4 = 'Seniales/tos4.wav' 

fs, data1 = wavfile.read(archivo_audio1)   # frecuencia de muestreo y datos de la señal    
fs, data2 = wavfile.read(archivo_audio2)
fs, data3 = wavfile.read(archivo_audio3)
fs, data4 = wavfile.read(archivo_audio4)

# Definición de parámetro temporales 

# tiempo de muestreo 
ts = 1 / fs       


# número de muestras en el archivo de audio                 
N1 = len(data1)
N2 = len(data2)
N3 = len(data3)
N4 = len(data4)        
             

# vector de tiempo  
t1 = np.linspace(0, N1 * ts, N1)
t2 = np.linspace(0, N2 * ts, N2)
t3 = np.linspace(0, N3 * ts, N3)
t4 = np.linspace(0, N4 * ts, N4)
    

#se escala la señal a voltios (considerando un CAD de 16bits y Vref 3.3V)
senial1 = data1 * 3.3 / (2 ** 16 - 1)    
senial2 = data2 * 3.3 / (2 ** 16 - 1)
senial3 = data3 * 3.3 / (2 ** 16 - 1)
senial4 = data4 * 3.3 / (2 ** 16 - 1)  

seniales=[senial1,senial2,senial3,senial4] 
tiempos=[t1,t2,t3,t4]

fig, axs = plt.subplots(4, 1, figsize=(18, 12), sharex=True)

for i in range(4):
    axs[i].plot(tiempos[i], seniales[i])
    axs[i].set_title(f'Señal {i+1}')
    axs[i].set_ylabel('Magnitud [V]')
    axs[i].grid(True)

axs[-1].set_xlabel('Tiempo [s]')
plt.tight_layout()
plt.show()

"""
Determinar los requisitos de diseño de un filtro antialiasing adecuado para la 
aplicación, teniendo en cuenta que la adquisición de datos se realizará a 8 kHz con 
16 bits de resolución (Vref: 3,3 V). El filtro debe poseer una respuesta máximamente 
plana en la banda de paso. 
"""

#Una vez que ovserve que las señales estan cargadas adecuadamente y que tienen una morfologia que me esperaria
#para poder avanzar con el diseño del filtro antialias debo realizar un analisis frecuencial de estas

#paso mis seniales del dominio temporal al frecuencial con una fft

f1,h1=fft_mag(seniales[0], fs)
f2,h2=fft_mag(seniales[1], fs)
f3,h3=fft_mag(seniales[2], fs)
f4,h4=fft_mag(seniales[3], fs)
    
f=[f1,f2,f3,f4]
h=[h1,h2,h3,h4]

#grafico la fft 

fig2, axs2 = plt.subplots(4, 1, figsize=(18, 12), sharex=True)
for i in range(4):
    axs2[i].plot(f[i], h[i])
    axs2[i].set_title(f'FFT {i+1}')
    axs2[i].set_ylabel('Magnitud [V]')
    axs2[i].grid(True)

axs2[-1].set_xlabel('Frecuencia[Hz]')
plt.tight_layout()
plt.show()

#busco ahora los maximos de amplitud en frecuencia de mis seniales

# Se propone una nueva frecuencia de muestreo para el sistema
FS2 = 8000                                  # Nueva frecuencia de muestreo:8000Hz

f_nyquist1 = f[0][np.where(f[0]>=(FS2/2))][0]          # Valor más cercano a FS2/2
f_nyquist2 = f[1][np.where(f[1]>=(FS2/2))][1]          # Valor más cercano a FS2/2
f_nyquist3 = f[2][np.where(f[2]>=(FS2/2))][2]          # Valor más cercano a FS2/2
f_nyquist4 = f[3][np.where(f[3]>=(FS2/2))][3]          # Valor más cercano a FS2/2

# Para determinar los requerimientos del antialiasing, primero analizamos el 
# contenido espectral de las señales por encima de FS2/2 en dos puntos (peores casos):
    
# Donde se encuentre el máximo a partir de FS2/2
h_max1 = np.max( h[0] [np.where(f[0] >= f_nyquist1) ] )
h_max2 = np.max( h[1] [np.where(f[1] >= f_nyquist2) ] )
h_max3 = np.max( h[2] [np.where(f[2] >= f_nyquist3) ] )
h_max4 = np.max( h[3] [np.where(f[3] >= f_nyquist3) ] )

f_max1 = f[0][ np.argmax(h[0][np.where(f[0] >=  f_nyquist1)])] + f_nyquist1
f_max2 = f[1][ np.argmax(h[1][np.where(f[1] >=  f_nyquist2)])] + f_nyquist2
f_max3 = f[2][ np.argmax(h[2][np.where(f[2] >=  f_nyquist3)])] + f_nyquist3
f_max4 = f[3][ np.argmax(h[3][np.where(f[3] >=  f_nyquist4)])] + f_nyquist4

# Exactamente en FS2/2
h1_fs_2 = np.max( h[0] [np.where(f[0] ==f_nyquist1) ] )
h2_fs_2 = np.max( h[1] [np.where(f[1] ==f_nyquist2) ] )
h3_fs_2 = np.max( h[2][np.where(f[2] ==f_nyquist3) ] )
h4_fs_2 = np.max( h[3] [np.where(f[3] ==f_nyquist4) ] )

f1_fs_2 = f[0][ np.argmax( h[0][ np.where(f[0] == f_nyquist1) ] ) ] + f_nyquist1
f2_fs_2 = f[1][ np.argmax( h[1][ np.where(f[1] == f_nyquist2) ] ) ] + f_nyquist2
f3_fs_2 = f[2][ np.argmax( h[2][ np.where(f[2] == f_nyquist3) ] ) ] + f_nyquist3
f4_fs_2 = f[3][ np.argmax( h[3][ np.where(f[3] == f_nyquist4) ] ) ] + f_nyquist4

h_max=[h_max1,h_max2,h_max3,h_max4]
f_max=[f_max1,f_max2,f_max3,f_max4]

h_fs_2=[h1_fs_2,h2_fs_2,h3_fs_2,h4_fs_2]
f_fs_2=[f1_fs_2,f2_fs_2,f3_fs_2,f4_fs_2]

fig3, axs3 = plt.subplots(4, 1, figsize=(18, 12), sharex=True)
for i in range(4):
    
    print(f"Interferencia de {h_max[i]:.7f}V en {f_max[i]}Hz para la señal {i+1}")
    print(f"Interferencia de {h_fs_2[i]:.7f}V en {f_fs_2[i]}Hz para la señal {i+1}")
    print("\r")

    axs3[i].plot(f[i], h[i])
    axs3[i].set_title(f'FFT {i+1}')
    axs3[i].set_ylabel('Magnitud [V]')
    axs3[i].grid(True)
    axs3[i].axvline(x=FS2/2, color="black", linestyle="--")
    axs3[i].plot(f_max[i], h_max[i], marker='X', markersize=12, label='Amplitud en fs/2')
    axs3[i].plot(f_fs_2[i], h_fs_2[i], marker='X', markersize=12, label='Máximo a partir de fs/2')
    axs3[i].legend(loc='upper right');

axs2[-1].set_xlabel('Frecuencia[Hz]')
plt.tight_layout()
plt.show

#como criterio entonces se va a tomar el peor caso de las peores señales, en el caso del punto de fs/2 vemos que la señal que mas atenacion necesita es
#la señal 2, y para el otro punto hay algo que tambien tenemos que tener en cuenta eque es la cercania a la frecuencia de nyquist, no solo el valor de 
#amplitud, entonces vemos que por amplia diferencia tambien la señal 2 posee el mayor modulo de frecuencia con un valor de 0.0009171 en 5201hz
#por lo que tomaremos como criterio unicamente estos 2 valores y diseñaremos nuestro filtro en base a eso
 

#%% Determinar requerimienos del filtro antialiasing

# Parámetros ADC:
V_REF = 3.3        # Tensión de referencia en mV
N_BITS = 16        # Resolución en bits

RES = V_REF/(2**N_BITS - 1)     # Resolución en mV

# Atenuaciones necesarias 
at_max = 20*np.log10(h_max[1]/RES) 
at_fs2_2 = 20*np.log10(h_fs_2[1]/RES)

print("Banda de paso hasta 1200Hz")   # Banda de paso determinada en guía 1
print(f"Atenuación mayor a {at_max:.2f}dB en {f_max[1]}Hz")
print(f"Atenuación mayor a {at_fs2_2:.2f}dB en {f_fs_2[1]}Hz")
print("\r")
    
#entonces con este criterio, la atenuacion en 5201hz debe ser de 25.21 db y en 4000hz de 11.74db, se procede entonces a diseniar el 
#filtro en el wizard, con el requisito adicional de que debe ser completamente plano en la banda de paso por lo que voy a hacer un butterworth

"""
En base a los requerimientos anteriores, diseñe el filtro antialiasing utilizando la 
herramienta Analog Filter Wizard. Para la implementación utilice una configuración 
de Múltiples Realimentaciones, resistencias del 10% de precisión y capacitores del 
20% (ver tabla)
"""
#implementado en el wizard

#%% importo el filtro diseñado

f, mag = import_AnalogFilterWizard('C:/Repositorio/SAPS_Gonzalez_C1_2025/Parciales/Parcial1C2025/design_Files/Data Files/Magnitude(dB).csv')


#%% Importar resultados de simulación en LTSpice
f_sim, mag_sim, _ = import_AC_LTSpice('C:/Repositorio/SAPS_Gonzalez_C1_2025/Parciales/Parcial1C2025/design_Files/SPICE Files/LTspice/ACAnalysis.txt')

# Análisis de la atenuación del filtro simulado en las frecuencias de interés
F_AT1 = FS2/2
F_AT2 = f_max[1]
# se calcula la atenuación en el punto mas cercano a la frecuencia de interés
at1 = mag_sim[np.argmin(np.abs(f_sim-F_AT1))] 
print("La atenuación del filtro simulado en {}Hz es de {:.2f}dB".format(F_AT1, at1))
at2 = mag_sim[np.argmin(np.abs(f_sim-F_AT2))] 
print("La atenuación del filtro simulado en {}Hz es de {:.2f}dB".format(F_AT2, at2))
print("\r")

#%% Comparación de las respuestas en frecuencia del filtro diseñado y el simulado 

# Se crea una gráfica para comparar los filtros 
fig4, ax3 = plt.subplots(1, 1, figsize=(12, 10))

ax3.set_title('Filtro orden 4', fontsize=18)
ax3.set_xlabel('Frecuencia [Hz]', fontsize=15)
ax3.set_ylabel('|H(jw)|² [dB]', fontsize=15)
ax3.set_xscale('log')
ax3.grid(True, which="both")
ax3.plot(f[1],  mag[1], label='Diseñado')
ax3.plot(f_sim,  mag_sim, label='Simulado')
ax3.plot(f_fs_2[1], -at_fs2_2, marker='X', markersize=12, label='Requisito en fs/2')
ax3.plot(f_max[1], -at_max, marker='X', markersize=12, label='Requisito en máximo a partir de fs/2')
ax3.legend(loc="lower left", fontsize=15)

#vemos que el filtro diseñado cumple con los 2 requisitos que se le plantearon
#%% Filtrado Digital
"""
Utilizando la herramienta pyFDA diseñe un filtro de tipo IIR de orden 8 que permita 
rescatar el rango de frecuencias de interés. Pruebe el filtro diseñado sobre una de 
las señales de prueba (remuestreado previamente a 8 kHz). Grafique la señal y su 
espectro antes y después del filtrado
"""
#se implementa el filtro en pyfda

#para probarlo debo primero remuestrear la señal, para esto primero debo saber cuantas muestras debo tener 

#calculo los tiempos de duracion de cada una de las señales, no duran lo mismo
T1=ts*N1
T2=ts*N2
T3=ts*N3
T4=ts*N4

#calculo el numero de muestras del remuestreo          
N1_resample = int(T1*FS2)
N2_resample = int(T2*FS2)
N3_resample = int(T3*FS2)
N4_resample = int(T4*FS2)

#se crea un vector de tiempos resampleado
t1_resampled = np.linspace(0, N1_resample / FS2, N1_resample)
t2_resampled = np.linspace(0, N2_resample / FS2, N2_resample)
t3_resampled = np.linspace(0, N3_resample / FS2, N3_resample)
t4_resampled = np.linspace(0, N4_resample / FS2, N4_resample)

senial = signal.resample(seniales[1], N2_resample)


# Se cargan los archivo generado mediante pyFDA

filtro_iir = np.load('filtro_iir.npz', allow_pickle=True) 

# Se muestran parámetros de diseño

print("Filtro IIR:")
filter_parameters.filter_parameters('filtro_iir.npz')
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
f_iir, h_iir = signal.freqz(Num_iir, Den_iir, worN=f, fs=FS2)

# Se grafican las respuestas de los filtros
fig5, ax5 = plt.subplots(1, 1, figsize=(12, 10))

ax5.plot(f_iir, abs(h_iir), label='Filtro IIR', color='green')
ax5.legend(loc="upper right", fontsize=15)
ax5.set_xlim(0,4000)
ax5.grid(True, which="both")
# Se evalúa la atenuación en las frecuncias de interés 

_, h1_iir = signal.freqz(Num_iir, Den_iir, worN=[200, 2000], fs=FS2)


print("La atenuación del filtro IIR en 400Hz es de {:.2f}dB".format(20*np.log10(abs(h1_iir[0]))))
print("La atenuación del filtro IIR en 1300Hz es de {:.2f}dB".format(20*np.log10(abs(h1_iir[1]))))
print("\r\n")

# Se extraen polos y ceros de los filtros
  
zeros_iir, polos_iir, k_iir =   filtro_iir['zpk']

# Se grafican las distribuciones de ceros y polos
fig3, ax3 = plt.subplots(1, 1, figsize=(12, 10))
fig3.suptitle("Distribución de Ceros y Polos en el plano Z", fontsize=18)


ax3.set_title('Filto IIR', fontsize=15)
ax3.add_patch(patches.Circle((0,0), radius=1, fill=False, alpha=0.1))
ax3.plot(polos_iir.real, polos_iir.imag, 'x', label='Polos', color='red',
            markersize=10, alpha=0.5)
ax3.plot(zeros_iir.real, zeros_iir.imag, 'o', label='Ceros', color='none',
            markersize=10, alpha=0.5, markeredgecolor='blue')
lim = 1.2 * np.max([np.max(abs(polos_iir)), np.max(abs(zeros_iir))])
ax3.set_xlim(-lim, lim)
ax3.set_ylim(-lim, lim)
ax3.set_ylabel('Imag(z)', fontsize=15)
ax3.set_xlabel('Real(z)', fontsize=15)
ax3.grid()
ax3.legend(loc="upper right", fontsize=12)

#%% Filtrado de la Señal 

# Se aplica el filtrado sobre la señal
senial_iir = signal.lfilter(Num_iir, Den_iir, senial)

# Se grafican las señales filtradas
fig5,ax1=plt.subplots(1,1, figsize=(12,10))
ax1.plot(t2, seniales[1], label='Señal con ruido',color='red')
ax1.plot(t2_resampled, senial, label='Señal con ruido')
ax1.plot(t2_resampled, senial_iir, label='Señal Filtrada (IIR)', color='purple')
ax1.legend(loc="upper right", fontsize=15)

# Se calculan y grafican sus espectros (normalizados)
f1_iir, senial_iir_fft_mod = fft_mag(senial_iir, FS2)
f2, senial_fft_mod = fft_mag(seniales[2], FS2)
senial_filtrada=senial_iir_fft_mod/np.max(senial_fft_mod)
fig6,ax6=plt.subplots(1,1, figsize=(12,10))
ax6.plot(f1_iir, senial_filtrada , 
            label='Senial Filtrada IIR', color='purple')
ax6.legend(loc="upper right", fontsize=15)
plt.show()


#%% envolvente

# Se cargan los archivo generado mediante pyFDA
filtro_fir = np.load('FIR.npz', allow_pickle=True)

# Se muestran parámetros de diseño
print("Filtro FIR:")
filter_parameters.filter_parameters('FIR.npz')
print("\r\n")

# Se extraen los coeficientes de numerador y denominador
Num_fir, Den_fir = filtro_fir['ba']     


#%% Análisis de los Filtros 

# Se calcula la respuesta en frecuencia de los filtros
f_fir, h_fir = signal.freqz(Num_fir, Den_fir, worN=f[1], fs=FS2)

# Se grafican las respuestas de los filtros
fig8, ax8 = plt.subplots(1, 1, figsize=(12, 10))
ax8.plot(f_fir, abs(h_fir), label='Filtro FIR', color='orange')
ax8.legend(loc="upper right", fontsize=15)

#%% Filtrado de la Señal 
ceros_agregar =  filtro_fir['N']//2
senial_iir=np.abs(senial_iir)
senial=np.pad(senial_iir,(0,ceros_agregar),mode='constant')
# Se aplica el filtrado sobre la señal
senial_fir = signal.lfilter(Num_fir, Den_fir, senial)
senial_fir=senial_fir[ceros_agregar:]

# Se grafican las señales filtradas
fig1, ax1 = plt.subplots(1, 1, figsize=(12, 10))
ax1.plot(t2_resampled, senial_fir, label='Señal Filtrada (FIR)', color='red')
ax1.legend(loc="upper right", fontsize=15)


# Se calculan y grafican sus espectros (normalizados)
fig9, ax9 = plt.subplots(1, 1, figsize=(12, 10))

f1_fir, senial_fir_fft_mod = fft_mag(senial_fir, FS2)
ax9.plot(f1_fir, senial_fir_fft_mod/np.max(senial_fft_mod), 
            label='Senial Filtrada FIR', color='red')
ax9.legend(loc="upper right", fontsize=15)
