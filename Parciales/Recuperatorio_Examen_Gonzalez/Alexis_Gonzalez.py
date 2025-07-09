# -*- coding: utf-8 -*-
"""
Created on Mon Jun 23 01:38:41 2025

@author: alexis gonzalez
"""


import numpy as np
import matplotlib.pyplot as plt
from funciones_fft import fft_mag
from import_ltspice import import_AC_LTSpice
from import_analogfilterwizard import import_AnalogFilterWizard
from scipy import signal
import filter_parameters
import sympy as sy
import pandas as pd
    
#primro cargo los archivos 
   
archivo_caida1 = 'caida1_500Hz.csv'  # Cambiar por el archivo deseado
df = pd.read_csv(archivo_caida1)

t_caida1 = df['timestamp'].values

senial1 = df['Ax'].values #La señal está en G y la relación a Voltios es 1 a 1. 
senial2 = df['Ay'].values
senial3 = df['Az'].values   #aca yo le asigno senial 1 al eje x, senial 2 al eje y y senial 3 al eje z

           
fs = 500  # frecuencia de muestreo 500Hz

#una vez cargadas estas seniales se va a proceder a graficarlas para chequear su morfologia 


# tiempo de muestreo 
ts = 1 / fs       


# número de muestras en el archivo de audio                 
N1 = len(senial1)
N2 = len(senial2)
N3 = len(senial3)       
             

# vectores de tiempo  
t1 = np.linspace(0, N1 * ts, N1)
t2 = np.linspace(0, N2 * ts, N2)
t3 = np.linspace(0, N3 * ts, N3)
 

seniales=[senial1,senial2,senial3] 
tiempos=[t1,t2,t3]

#se grafican las seniales

fig, axs = plt.subplots(3, 1, figsize=(18, 12), sharex=True)

for i in range(3):
    axs[i].plot(tiempos[i], seniales[i])
    axs[i].set_title(f'Señal {i+1}')
    axs[i].set_ylabel('Magnitud [V]')
    axs[i].grid(True)

axs[-1].set_xlabel('Tiempo [s]')
plt.tight_layout()
plt.show()


#%% 
"""
Diseñe un filtro pasa-bajos utilizando la herramienta Analog Filter Wizard. 
El mismo debe responder a una aproximación de Chebyshev con 0.1dB de ripple.
 El fin de la banda de ripple debe coincidir con la frecuencia máxima de interés de la señal.
 Además, son necesarios 60dB de atenuación en 200Hz. Para la implementación utilice, 
 resistencias del 10% de precisión y capacitores del 20%
"""
#del enunciado se que mi ancho de banda de interes esta entre 1-11hz, entonces si este filtro chebyshev
#posteriormente se utilizara como filtro antialias, la banda de rechazo se debe ubicar despues de 22hz, con un
#factor de seguridad puedo definir donde tengo mi banda de rechazo, utilizo un factor de seguridad de 3 
#para no exigir un filtro antialias con muchos componentes, no elijo uno de orden superior porque con 33hz
#ya queda un cheby de orden 3 que es adecuado, si elijiese un factor de seguridad mayor estaria exigiendo al 
#conversor adc. En cuanto a la atenuacion de 60 db el filtro cumple con esto.
#El filtro se implemento en analog filter wizard, se selecciono la opcion de valores comerciales E6 y
#se aproximo los valores de resistencias y capacitores a los valores de la tabla proporcionados por la catedra, no hizo
#falta cambiar estos valores en el ltspice 

#%%

"""
En base al filtro pasa-bajos diseñado en el punto anterior, y analizando las señales provistas, 
proponga una nueva frecuencia de muestreo entre 50 y 200 Hz de tal manera que el filtro pueda ser usado como 
filtro anti-alias. Considere que se digitalizará con un CAD de 16 bits y Vref de 3.3V.
"""
#aca vi que me pide que la frecuencia de muestreo tiene que ir entre 50 y 200hz entonces el analisis anterior 
#es incorrecto ya que se va a tener que elegir un factor de seguridad mayor 

#para ver si mi filtro cumple como filtro antialias primero
#tengo que realizar primero un analisis frecuencial de la señal y 
#ver si el filtro atenua correctamente
#las frecuencias que me van a generar aliasing

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

AB=11  #ancho de banda de interes de la señal
k=10    # factor de seguridad lo voy variando hasta que mi filtro cumpla, cumple con 10
FS2 = AB*k  # Nueva frecuencia de muestreo:110hz

f_nyquist=FS2/2 #frecuencia de nyquist de mi sistema

# Encuentro el índice donde la diferencia con fs2 sea mínima
idx_nyquist1 = np.argmin(np.abs(f[0] - f_nyquist))
idx_nyquist2 = np.argmin(np.abs(f[1] - f_nyquist))
idx_nyquist3 = np.argmin(np.abs(f[2] - f_nyquist))

# Obtengo el valor más cercano a FS2/2
f_nyquist1 = f[0][idx_nyquist1]
f_nyquist2 = f[1][idx_nyquist2]
f_nyquist3 = f[2][idx_nyquist3]

# Interferencia donde se encuentre el máximo a partir de FS2/2
h_max1 = np.max( h[0] [np.where(f[0] >= f_nyquist1) ] )
h_max2 = np.max( h[1] [np.where(f[1] >= f_nyquist2) ] )
h_max3 = np.max( h[2] [np.where(f[2] >= f_nyquist3) ] )

#frecuencia de ese maximo
f_max1 = f[0][ np.argmax(h[0][np.where(f[0] >=  f_nyquist1)])] + f_nyquist1
f_max2 = f[1][ np.argmax(h[1][np.where(f[1] >=  f_nyquist2)])] + f_nyquist2
f_max3 = f[2][ np.argmax(h[2][np.where(f[2] >=  f_nyquist3)])] + f_nyquist3


# Interferencia exactamente en FS2/2
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

#grafico la fft con los maximos marcados, verifico graficamente si las interferencias son correctas 
fig3, axs3 = plt.subplots(3, 1, figsize=(18, 12), sharex=True)
for i in range(3):
    
    print(f"Interferencia de {h_max[i]:.2f}V en {f_max[i]}Hz para la señal {i+1}")
    print(f"Interferencia de {h_fs_2[i]:.2f}V en {f_fs_2[i]}Hz para la señal {i+1}")
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


# Parámetros ADC:
V_REF = 3.3       # Tensión de referencia en V
N_BITS = 16      # Resolución en bits

RES = V_REF/(2**N_BITS - 1)  # Resolución en V

# Atenuaciones necesarias aca elijo el peor caso osea la señal que mas interferencia tiene

#la señal 2 es la que mas interferencia tiene despues de la frecuencia de muestreo
#la señal 3 es la que mas interferencia tiene en la frecuencia de muestreo

at_max = 20*np.log10(h_max[1]/RES) 
at_fs2_2 = 20*np.log10(h_fs_2[2]/RES)

print("Banda de paso hasta 11Hz")   
print(f"Atenuación mayor a {at_max:.2f}dB en {f_max[1]}Hz")
print(f"Atenuación mayor a {at_fs2_2:.2f}dB en {f_fs_2[1]}Hz")
print("\r")
    
#entonces con este criterio, la atenuacion en 50hz debe ser de 62.67 db y en 11hz de 16.5db
#ahora verifico que el filtro cumpla con mis requisitos

ruta_diseniado='C:/Repositorio/SAPS_Gonzalez_C1_2025/Parciales/Recuperatorio_Examen_Gonzalez/files/Data Files/Magnitude(dB).csv'
f, mag = import_AnalogFilterWizard(ruta_diseniado)


#Importar resultados de simulación en LTSpice
ruta_LTspice='ACAnalysis.txt'
f_sim, mag_sim, _ = import_AC_LTSpice(ruta_LTspice)

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

ax3.set_title('Filtro antialias', fontsize=18)
ax3.set_xlabel('Frecuencia [Hz]', fontsize=15)
ax3.set_ylabel('|H(jw)|² [dB]', fontsize=15)
ax3.set_xscale('log')
ax3.grid(True, which="both")
ax3.plot(f[1],  mag[1], label='Diseñado')
ax3.plot(f_sim,  mag_sim, label='Simulado')
ax3.plot(f_fs_2[1], -at_fs2_2, marker='X', markersize=12, label='Requisito en fs/2')
ax3.plot(f_max[1], -at_max, marker='X', markersize=12, label='Requisito en máximo a partir de fs/2')
ax3.legend(loc="lower left", fontsize=15)

#vemos que ahora si el filtro antialias cumple pero queda el ruido de 50 hz que va a necesitar ser filtrado
# con un filtro digital

#%%

"""
Utilizando la herramienta pyFDA diseñe un filtro de tipo IIR que permita rescatar el
 rango de frecuencias de interés y tenga una atenuación de 60 dB para frecuencias de 50Hz. 
 Pruebe el filtro diseñado sobre la señal de prueba (remuestreado previamente a la frecuencia elegida).
 Grafique la señal y su espectro antes y después del filtrado (no es necesario hacerlo en todos los canales, 
  con uno basta).

""" 
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


senial1 = signal.resample(seniales[0], N2_resample)
senial2 = signal.resample(seniales[1], N2_resample)
senial3 = signal.resample(seniales[2], N2_resample)

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
senial_iir1 = signal.lfilter(Num_iir, Den_iir, senial1)
senial_iir2 = signal.lfilter(Num_iir, Den_iir, senial2)
senial_iir3 = signal.lfilter(Num_iir, Den_iir, senial3)

fig5,ax3=plt.subplots(2,1, figsize=(12,10))

# Se grafican las señales filtradas
#aca ploteo solo la senial 2 porque es la que mas ruido tiene en 50 hz

ax3[0].plot(t2_resampled, senial2, label='Señal con ruido')
ax3[0].set_title('senial con ruido')
ax3[0].set_ylabel('Magnitud [mV]')
ax3[0].grid(True)
ax3[0].legend(loc='upper right');

ax3[1].plot(t2_resampled, senial_iir2, label='Señal Filtrada (IIR)', color='purple')
ax3[1].legend(loc="upper right", fontsize=15)
ax3[1].set_ylabel('Magnitud [mV]')
ax3[1].grid(True)

# Se calculan y grafican sus espectros (normalizados)
f1_iir, senial_iir_fft_mod = fft_mag(senial_iir2, FS2)
f2, senial_fft_mod = fft_mag(seniales[1], FS2)
senial_filtrada=senial_iir_fft_mod/np.max(senial_fft_mod)
fig6,ax6=plt.subplots(1,1, figsize=(12,10))
ax6.plot(f1_iir, senial_filtrada , 
            label=' Espectro Senial Filtrada IIR', color='purple')
ax6.legend(loc="upper right", fontsize=15)
ax6.set_xlabel('Frecuencia [Hz]', fontsize=15)
ax6.set_ylabel('|H(jw)|² [dB]', fontsize=15)
ax6.legend(loc="upper right", fontsize=15)
ax6.grid(True)
plt.show()

#todavia siguen pasando componentes de altas frecuencias, se deberia de implementar un filtro de mayor orden para eliminarlas

#%%

"""
Para poder detectar el evento de caída, es necesario primero calcular la envolvente de 
la magnitud de la aceleración. Para esto se debe primero calcular la magnitud de la señal 
(np.sqrt(x**2+y**2+z**2)), luego rectificar la señal (np.abs()) y finalmente aplicarle un 
filtro pasabajos, que en este caso debe tener frecuencia de corte en 1 Hz y atenuar al menos 60 dB a 
las componentes a partir de 5 Hz. Diseñe un filtro FIR en pyFDA que cumpla con estos requisitos, y 
realice el cálculo de la envolvente de la señal filtrada en el punto 3. Grafique la envolvente.

"""

magnitud=(np.sqrt(senial_iir1**2+senial_iir2**2+senial_iir3**2))
rectificada=np.abs(magnitud)


filtro_fir = np.load('FIR.npz', allow_pickle=True)

# Se muestran parámetros de diseño
print("Filtro FIR:")
filter_parameters.filter_parameters('FIR.npz')
print("\r\n")

# Se extraen los coeficientes de numerador y denominador
Num_fir, Den_fir = filtro_fir['ba']     

# Análisis de los Filtros 

# Filtrado de la Señal 
ceros_agregar =  filtro_fir['N']//2
senial_fir=rectificada
senial_fir=np.pad(senial_fir,(0,ceros_agregar),mode='constant')

# Se aplica el filtrado sobre la señal
senial_fir = signal.lfilter(Num_fir, Den_fir, senial_fir)
senial_fir=senial_fir[ceros_agregar:]



# Se grafican las señales filtradas
fig32, ax32 = plt.subplots(1, 1, figsize=(12, 10))
ax32.plot(t2_resampled, rectificada, label='Señal Filtrada (FIR)', color='green')
ax32.set_xlabel('Tiempo[s]', fontsize=15)
ax32.set_ylabel('Voltios[V]', fontsize=15)
ax32.legend(loc="upper right", fontsize=15)
ax32.legend(loc="upper right", fontsize=15)
ax32.grid(True)


# Se calculan y grafican sus espectros (normalizadoss)
fig9, ax9 = plt.subplots(1, 1, figsize=(12, 10))

f1_fir, senial_fir_fft_mod = fft_mag(senial_fir, FS2)
ax9.plot(f1_fir, senial_fir_fft_mod/np.max(senial_fft_mod), 
            label='Espectro Senial Filtrada FIR', color='red')
ax9.set_xlabel('Frecuencia [Hz]', fontsize=15)
ax9.set_ylabel('|H(jw)|² [dB]', fontsize=15)
ax9.legend(loc="upper right", fontsize=15)
ax9.set_xscale('log')
ax9.grid(True)

#%%

"""
Localice el evento utilizando el máximo de la envolvente para ello.
 ¿Cómo afectará la localización del máximo el haber utilizado un filtro FIR para la obtención de la envolvente?

"""

#graficamente podemos ver que el maximo lo encontramos en 4.2s, el haber usado un filtro fir nos puede generar
#un retardo temporal lo que puede desplazar este maximo hacia la derecha en el eje del tiempo
 
t_max = t2_resampled[ np.argmax(rectificada)]
print("El pico maximo de la envolvente esta ubicado en {:.2f} s".format(t_max))
