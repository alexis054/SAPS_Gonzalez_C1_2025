# -*- coding: utf-8 -*-
"""
Created on Sun Jun 22 14:40:52 2025

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


#%%

filename1 = 'pleth_72lpm_1000hz.txt'  # nombre dearchivo
filename2 = 'pleth_90lpm_1000hz.txt'  # nombre dearchivo
filename3 = 'pleth_120lpm_1000hz.txt'  # nombre dearchivo

senial1 = np.loadtxt(filename1) # la amplitud de la señal se encuentra en mV
senial2 = np.loadtxt(filename2)
senial3 = np.loadtxt(filename3)

           
fs = 1000  # frecuencia de muestreo 1000Hz

#una vez cargadas estas seniales se va a proceder a graficarlas para chequear su morfologia 


# tiempo de muestreo 
ts = 1 / fs       


# número de muestras en el archivo de audio                 
N1 = len(senial1)
N2 = len(senial2)
N3 = len(senial3)       
             

# vector de tiempo  
t1 = np.linspace(0, N1 * ts, N1)
t2 = np.linspace(0, N2 * ts, N2)
t3 = np.linspace(0, N3 * ts, N3)
 

seniales=[senial1,senial2,senial3] 
tiempos=[t1,t2,t3]

fig, axs = plt.subplots(3, 1, figsize=(18, 12), sharex=True)

for i in range(3):
    axs[i].plot(tiempos[i], seniales[i])
    axs[i].set_title(f'Señal {i+1}')
    axs[i].set_ylabel('Magnitud [V]')
    axs[i].grid(True)

axs[-1].set_xlabel('Tiempo [s]')
plt.tight_layout()
plt.show()

 #una vez verficiadas que estan cargadas adecuadamentes se procede con el disenio del filtro antialias

#%% 
 
"""
 Determinar la función de transferencia H(s) de un filtro que cumpla con la función de
 antialiasing y tenga respuesta máximamente plana en la banda de paso. Para ello cuenta con
 una serie de registros de la señal de PPG realizados a lo largo de una sesión de ejercicio
(pleth_72lpm_1000hz.txt, pleth_90lpm_1000hz.txt, pleth_120lpm_1000hz.txt), adquiridos a
 una frecuencia de muestreo mayor (1kHz).
"""

#para esto entonces primero debo realizar un analisis espectral de mi senial para ver que requerimientos va a necesitar el filtro 
f1,h1=fft_mag(seniales[0], fs)
f2,h2=fft_mag(seniales[1], fs)
f3,h3=fft_mag(seniales[2], fs)

f=[f1,f2,f3]
h=[h1,h2,h3]

#grafico la fft 

fig2, axs2 = plt.subplots(3, 1, figsize=(18, 12), sharex=True)
for i in range(3):
    axs2[i].plot(f[i], h[i])
    axs2[i].set_title(f'FFT {i+1}')
    axs2[i].set_ylabel('Magnitud [V]')
    axs2[i].grid(True)

axs2[-1].set_xlabel('Frecuencia[Hz]')
plt.tight_layout()
plt.show()


#busco ahora los maximos de amplitud en frecuencia de mis seniales

# Se propone una nueva frecuencia de muestreo para el sistema
FS2 = 15                                 # Nueva frecuencia de muestreo:15Hz
f_nyquist=FS2/2

# Encontrar el índice donde la diferencia con fs2 sea mínima
idx_nyquist1 = np.argmin(np.abs(f[0] - f_nyquist))
idx_nyquist2 = np.argmin(np.abs(f[1] - f_nyquist))
idx_nyquist3 = np.argmin(np.abs(f[2] - f_nyquist))

# Obtener el valor más cercano a FS2/2
f_nyquist1 = f[0][idx_nyquist1]
f_nyquist2 = f[1][idx_nyquist2]
f_nyquist3 = f[2][idx_nyquist3]

# Donde se encuentre el máximo a partir de FS2/2
h_max1 = np.max( h[0] [np.where(f[0] >= f_nyquist1) ] )
h_max2 = np.max( h[1] [np.where(f[1] >= f_nyquist2) ] )
h_max3 = np.max( h[2] [np.where(f[2] >= f_nyquist3) ] )


f_max1 = f[0][ np.argmax(h[0][np.where(f[0] >=  f_nyquist1)])] + f_nyquist1
f_max2 = f[1][ np.argmax(h[1][np.where(f[1] >=  f_nyquist2)])] + f_nyquist2
f_max3 = f[2][ np.argmax(h[2][np.where(f[2] >=  f_nyquist3)])] + f_nyquist3


# Exactamente en FS2/2
h1_fs_2 = np.max( h[0] [np.where(f[0] ==f_nyquist1) ] )
h2_fs_2 = np.max( h[1] [np.where(f[1] ==f_nyquist2) ] )
h3_fs_2 = np.max( h[2][np.where(f[2] ==f_nyquist3) ] )

f1_fs_2 = f[0][ np.argmax( h[0][ np.where(f[0] == f_nyquist1) ] ) ] + f_nyquist1
f2_fs_2 = f[1][ np.argmax( h[1][ np.where(f[1] == f_nyquist2) ] ) ] + f_nyquist2
f3_fs_2 = f[2][ np.argmax( h[2][ np.where(f[2] == f_nyquist3) ] ) ] + f_nyquist3

h_max=[h_max1,h_max2,h_max3]
f_max=[f_max1,f_max2,f_max3]

h_fs_2=[h1_fs_2,h2_fs_2,h3_fs_2]
f_fs_2=[f1_fs_2,f2_fs_2,f3_fs_2]

fig3, axs3 = plt.subplots(3, 1, figsize=(18, 12), sharex=True)
for i in range(3):
    
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

#como criterio tomo en cuenta el peor caso, en mi analisis puedo ver que la senial 2 tiene mas interferencia en
# la frecuencia de nyquist, con una amplitud de 2.86mv, y como el resto tiene el ruido maximo en 50 hz y tiene 
#la misma amplitud de interferencia, tomo mi senial 2 como mi peor caso asi que con esto procedo a calcular
#que atenuacion debe cumplir mi filtro antialias



# Determinar requerimienos del filtro antialiasing

# Parámetros ADC:
V_REF = 3300        # Tensión de referencia en mV
N_BITS = 14       # Resolución en bits

RES = V_REF/(2**N_BITS - 1)     # Resolución en mV

# Atenuaciones necesarias 
at_max = 20*np.log10(h_max[1]/RES) 
at_fs2_2 = 20*np.log10(h_fs_2[1]/RES)

print("Banda de paso hasta 1200Hz")   # Banda de paso determinada en guía 1
print(f"Atenuación mayor a {at_max:.2f}dB en {f_max[1]}Hz")
print(f"Atenuación mayor a {at_fs2_2:.2f}dB en {f_fs_2[1]}Hz")
print("\r")
    
#entonces con este criterio, la atenuacion en 50hz debe ser de 39.7 db y en 7.516hz de 23.07db, se procede entonces a diseniar el 
#filtro en el wizard, con el requisito adicional de que debe ser completamente plano en la banda de paso por lo que voy a hacer un butterworth
#teniendo en cuenta que posteriormente se me pide una banda de paso hasta 2.3hz, supongo que las frecuencias de interes de mi senial van hasta ahi

#%%
"""
Calcular los componentes (con valores comerciales) del circuito activo necesario para la
 implementación del filtro antialiasing, utilizando celdas de múltiple realimentación. Simular
 la respuesta en frecuencia en LTSpice y comparar con la original
""" 
# importo el filtro diseñado

f, mag = import_AnalogFilterWizard('C:/Repositorio/SAPS_Gonzalez_C1_2025/Parciales/Parcial_03-06-24/design/Data Files/Magnitude(dB).csv')


#Importar resultados de simulación en LTSpice
f_sim, mag_sim, _ = import_AC_LTSpice('ACAnalysis.txt')

# Análisis de la atenuación del filtro simulado en las frecuencias de interés
F_AT1 = FS2/2
F_AT2 = f_max[1]
# se calcula la atenuación en el punto mas cercano a la frecuencia de interés
at1 = mag_sim[np.argmin(np.abs(f_sim-F_AT1))] 
print("La atenuación del filtro simulado en {}Hz es de {:.2f}dB".format(F_AT1, at1))
at2 = mag_sim[np.argmin(np.abs(f_sim-F_AT2))] 
print("La atenuación del filtro simulado en {}Hz es de {:.2f}dB".format(F_AT2, at2))
print("\r")

# Comparación de las respuestas en frecuencia del filtro diseñado y el simulado 

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

#vemos que el filtro cumple correctamente con los requerimientos

#%%

"""
Utilizando pyFDA, diseñar un filtro digital que permita separar las componentes relacionadas
 a la FC de las relacionadas a la FR. El mismo de tener las siguientes características:
 ○ Tipo:IIR
 ○ Bandadepaso: 1.5Hza2.3Hz
 ○ Atenuaciónenla banda de paso: menor a 0.5 dB
 ○ Atenuaciónpara las componentes relacionadas a la FR: mayor a 30 dB
 
"""

#implementado en fda

#%%

"""
Utilizando pyFDA, diseñar un filtro digital que permita separar las componentes relacionadas
 a la FR de las relacionadas a la FC. El mismo de tener las siguientes características:
 ○ Tipo:FIR
 ○ Bandadepaso: 0.05Hza0.55Hz
 ○ Atenuaciónenla banda de paso: menor a 1 dB
 ○ Atenuaciónpara las componentes relacionadas a la FC: mayor a 30 dB
"""


#implementado en fda

#%%
"""
Probar el funcionamiento de ambos filtros utilizando las señales de prueba muestreadas a 15
 Hz (pleth_72lpm_15hz.txt, pleth_90lpm_15hz.txt, pleth_120lpm_15hz.txt). Graficar las
 señales antes y después de ser filtradas.
"""

"""
#calculo los tiempos de duracion de cada una de las señales, no duran lo mismo
T1=ts*N1
T2=ts*N2
T3=ts*N3


#calculo el numero de muestras del remuestreo          
N1_resample = int(T1*FS2)
N2_resample = int(T2*FS2)
N3_resample = int(T3*FS2)


#se crea un vector de tiempos resampleado
t1_resampled = np.linspace(0, N1_resample / FS2, N1_resample)
t2_resampled = np.linspace(0, N2_resample / FS2, N2_resample)
t3_resampled = np.linspace(0, N3_resample / FS2, N3_resample)


senial = signal.resample(seniales[1], N2_resample)

esto esta comentado porque lo necesito hacer en caso de no tener la senial resampleada pero viendo la consigna me di cuenta que si la tengo
"""

senial=np.loadtxt('pleth_90lpm_15hz.txt')

N2_resample = len(senial)
fs_resample=15
ts_resample=1/fs_resample
t2_resampled = np.linspace(0, N2_resample * ts_resample, N2_resample)
# Se cargan los archivo generado mediante pyFDA

filtro_iir = np.load('Cheby.npz', allow_pickle=True) 

# Se muestran parámetros de diseño

print("Filtro IIR:")
filter_parameters.filter_parameters('Cheby.npz')
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



# Se calcula la respuesta en frecuencia de los filtros
f_iir, h_iir = signal.freqz(Num_iir, Den_iir, worN=f, fs=FS2)


# Se aplica el filtrado sobre la señal
senial_iir = signal.lfilter(Num_iir, Den_iir, senial)

fig5,ax3=plt.subplots(2,1, figsize=(12,10))

# Se grafican las señales filtradas

ax3[0].plot(t2_resampled, senial, label='Señal con ruido')
ax3[0].set_title('senial con ruido')
ax3[0].set_ylabel('Magnitud [mV]')
ax3[0].grid(True)
ax3[0].legend(loc='upper right');

ax3[1].plot(t2_resampled, senial_iir, label='Señal Filtrada (IIR)', color='purple')
ax3[1].legend(loc="upper right", fontsize=15)
ax3[1].set_ylabel('Magnitud [mV]')
ax3[1].grid(True)

# Se calculan y grafican sus espectros (normalizados)
f1_iir, senial_iir_fft_mod = fft_mag(senial_iir, FS2)
f2, senial_fft_mod = fft_mag(seniales[1], FS2)
senial_filtrada=senial_iir_fft_mod/np.max(senial_fft_mod)
fig6,ax6=plt.subplots(1,1, figsize=(12,10))
ax6.plot(f1_iir, senial_filtrada , 
            label='Senial Filtrada IIR', color='purple')
ax6.legend(loc="upper right", fontsize=15)
plt.show()


#%%pruebo el fir

# Se cargan los archivo generado mediante pyFDA
filtro_fir = np.load('FIR2.npz', allow_pickle=True)

# Se muestran parámetros de diseño
print("Filtro FIR:")
filter_parameters.filter_parameters('FIR2.npz')
print("\r\n")

# Se extraen los coeficientes de numerador y denominador
Num_fir, Den_fir = filtro_fir['ba']     

# Análisis de los Filtros 

# Filtrado de la Señal 
ceros_agregar =  filtro_fir['N']//2
senial_fir=senial
senial_fir=np.pad(senial,(0,ceros_agregar),mode='constant')

# Se aplica el filtrado sobre la señal
senial_fir = signal.lfilter(Num_fir, Den_fir, senial_fir)
senial_fir=senial_fir[ceros_agregar:]

# Se grafican las señales filtradas
fig32, ax32 = plt.subplots(1, 1, figsize=(12, 10))
ax32.plot(t2_resampled, senial_fir, label='Señal Filtrada (FIR)', color='green')
ax32.legend(loc="upper right", fontsize=15)


# Se calculan y grafican sus espectros (normalizadoss)
fig9, ax9 = plt.subplots(1, 1, figsize=(12, 10))

f1_fir, senial_fir_fft_mod = fft_mag(senial_fir, FS2)
ax9.plot(f1_fir, senial_fir_fft_mod/np.max(senial_fft_mod), 
            label='Senial Filtrada FIR', color='red')
ax9.legend(loc="upper right", fontsize=15)

