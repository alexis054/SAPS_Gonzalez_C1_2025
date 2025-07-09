
#%% Item 1: Determinar la función de transferencia H(s) de un filtro que cumpla con la función de 
# antialiasing y tenga respuesta máximamente plana en la banda de paso. Para ello cuenta con un registro 
# de la señal de presión en el manguito (nibp_1000hz.txt), adquiridos a una frecuencia de muestreo mayor 
# (1kHz), y cuya magnitud está expresada en mV. 

# importo las bibliotecas necesarias
import numpy as np
import matplotlib.pyplot as plt
from funciones_fft import fft_mag
from import_analogfilterwizard import import_AnalogFilterWizard
from import_ltspice import import_AC_LTSpice
fs=1000
filename='nibp_1000hz.txt'
signal= np.loadtxt(filename, dtype=float, delimiter=',')
N=len(signal)
T=N/fs
ts=1/fs

t = np.linspace(0, N * ts, N)   # vector de tiempos

fig2, ax2 = plt.subplots(1, 1, figsize=(18, 12))
#calculo la fft    

 # Cálculo y graficación de la FFT
 
f,fft_signal=fft_mag(signal,fs)
 # Como la transformada de fourier genera un espectro simetrico, se considera solamente la mitad y graficamos
 #desde 0 hasta nyquist, tambien como consideramos la mitad para mantener la relacion de parseval debemos multiplicar
 #por 2  la amplitud de la FFT, tambien debo dividir por N para normalizar la senial
     
plt.plot(f, fft_signal)
plt.xlabel('Frecuencia [Hz]')
plt.title('Magnitud')
plt.show()

#como la fft me muestra que el ancho de banda de interes en mi senial es hasta 8hz, voy a tener que remuestrar la senial. idealmente por teorema
#muestreo al doble de mi ab esto quiere decir que como minimo necesitaria muestrear a 16 hz, pero como los filtros no son ideales, con la finalidad 
#brindar un margen para poder tener un menor orden de filtro (ya que si muestreo a 16 hz voy a necesitar un filtro de orden infinito porque todo lo que este sobre ese valor me va a generar aliasing)
#voy a remuestrear mi senial por un valor mayor a Ab*2, como estamos trabajando con una esp-edu esta placa me permite muestrear a afrecuencias mucho mas altas, me puedo permitir un n=10.65
#esto en realidad lo hago asi porque en el parcial se me da ya la resampleada a 85 hz dios sabra por que motivo pero si no estoy loco veo hasta 8 hz yo en frecuencia

Ab=8 #rango de frecuencias en hz de interes en mi senial
n=10.625  #factor por el cual multiplico mi Ab para cumplir con nyquist y reducir el orden de mi filtro
f_resample=Ab*n #propongo una nueva frecuencia de muestreo 

#una vez que yo se cuales son los valores de frecuencia a los que voy a remuestrear la senial, debo analizar el contenido espectral de mi senial
#siendo de interes los valores por encima de fs/2 que me van a generar aliasing , tengo dos puntos de interes, en fm/2 (atenuacion con la que tengo que ingresar a esta zona) y en la max amp despues de fm/2
# atenuacion maxima que tiene que tener el filtro 

fs2_2=f_resample/2 #fm sobre 2

# Donde se encuentre el máximo a partir de FS2/2
h_max = np.max( fft_signal [np.where(f >= fs2_2) ] ) 
f_max = f[ np.argmax(fft_signal[np.where(f >= fs2_2)])] + fs2_2 # frec asociada a esa ampliud 
# Exactamente en FS2/2
h_fs_2 = np.max( fft_signal [np.where(f == fs2_2) ] )
f_fs_2 = f[ np.argmax( fft_signal[ np.where(f == fs2_2) ] ) ] + fs2_2

print(f"Interferencia de {h_max:.2f}mV en {f_max}Hz")
print(f"Interferencia de {h_fs_2:.2f}mV en {f_fs_2}Hz")
print("\r")

ax2.axvline(x=f_resample/2, color="black", linestyle="--")
ax2.plot(f_max, h_max, marker='X', markersize=12, label='Amplitud en fs/2')
ax2.plot(f_fs_2, h_fs_2, marker='X', markersize=12, label='Máximo a partir de fs/2')
ax2.legend(loc='upper right');


#tengo una duda aca y es que en el plot, ni bien paso fs/2 tengo un pico importante en frecuencia, esto no me estaria indicando que quiza la atenuacion
#en fs2 no sea suficiente?, es la mejor forma? no deberia de calcular la atenuacion para puntos mas cercanos a fs2?


# Determinar requerimienos del filtro antialiasing

# Parámetros ADC:
V_REF = 5000       # Tensión de referencia en mV
N_BITS = 16         # Resolución en bits

RES = V_REF/(2**N_BITS - 1)     # Resolución en mV

# Atenuaciones necesarias 
at_max = 20*np.log10(h_max/RES) 
at_fs2_2 = 20*np.log10(h_fs_2/RES) #es importante interpretar lo que esta pasando aca, el valor es casi 0v, incluso en  el calculo en mv, el script e lo trunca a 0 mv porque es
                                 #0.002mv la amplitud en ese punto, por eso da un valor tan alto, ya es menor que la resolucion del adc entonces el calculo no tiene sentido por eso es negativo

#esto quiere decir que no tengo que tener un filtro antialias? no, siempre se necesita uno y si tengo mas ruido en 50hz?

print("Banda de paso hasta 8Hz")   # Banda de paso determinada en guía 1
print(f"Atenuación mayor a {at_max:.2f}dB en {f_max}Hz")
print(f"Atenuación mayor a {at_fs2_2:.2f}dB en {f_fs_2}Hz")
print("\r")

 #at necesaria a 50hz 14 db, en 42.5 lo dejo en 1db




#%% Item 2: Calcular los componentes (con valores comerciales) del circuito activo necesario para la 
# implementación del filtro antialiasing, utilizando celdas de Sallen-Key. Simular la respuesta en 
# frecuencia en LTSpice y comparar con la original.


#ahora paso a la pagina del wizzard, cargo mi banda de paso, como quiero que la banda de paso sea lo mas plana posible en lugar de ponerle -3db le pongo -0.5, si le pusiese
# menos el orden subiria mucho y tampoco quiero tener un filtro con muchas etapas.Siempre lo mantengo como un butter ya que el cheby me generaria
# un ripple que no cumpliria con mis requerimientos 

#una vez que tengo el filtro pasabajos, ahora me descargo los archivos del wizzard y con la biblioteca LTspice importo estos archivos y los cargo 

f, mag = import_AnalogFilterWizard('Design Files/Data Files/Magnitude(dB).csv')

#ahora importo del LTSPICE para ver como se comportaria mi filtro real con los valores de resistencias que tengo(como es un caso ficticio supongo que me va a dar exactamente igual)
#%% Importar resultados de simulación en LTSpice
f_sim, mag_sim, _ = import_AC_LTSpice('FiltroManguito.csv')

# Análisis de la atenuación del filtro simulado en las frecuencias de interés
F_AT1 = f_resample/2
F_AT2 = f_max
# se calcula la atenuación en el punto mas cercano a la frecuencia de interés
at1 = mag_sim[np.argmin(np.abs(f_sim-F_AT1))] 
print("La atenuación del filtro simulado en {}Hz es de {:.2f}dB".format(F_AT1, at1))
at2 = mag_sim[np.argmin(np.abs(f_sim-F_AT2))] 
print("La atenuación del filtro simulado en {}Hz es de {:.2f}dB".format(F_AT2, at2))
print("\r")

#en 42.5 Hz La atenuacion es de 20.19 mientras que la necesitaba era de 1 lo que supera ampliamente mis requerimientos
#en 50 Hz la atenuacion es de 22.96 cuando la que necesitaba era de 14.04 por lo que mi filtro satisface ampliamente los requerimientos 

# Se crea una gráfica para comparar los filtros 
fig3, ax3 = plt.subplots(1, 1, figsize=(12, 10))

ax3.set_title('Filtro orden 1', fontsize=18)
ax3.set_xlabel('Frecuencia [Hz]', fontsize=15)
ax3.set_ylabel('|H(jw)|² [dB]', fontsize=15)
ax3.set_xscale('log')
ax3.grid(True, which="both")
ax3.plot(f,  mag, label='Diseñado')
ax3.plot(f_sim,  mag_sim, label='Simulado')
ax3.plot(f_max, -at_max, marker='X', markersize=12, label='Requisito en máximo a partir de fs/2')
ax3.legend(loc="lower left", fontsize=15)
#este grafico tendria un poco mas de sentido si no fuese una situacion ficticia en la que tengo todos los valores de resistencia y comerciales
#disponibles, ademas despues se podria comparar con la atenuacion en un filtro real, midiendolo con un osiloscopio y viendo como atenua
#levantando una curva y compararla con los filtros diseniados simulados e implementados



#%% Item 3: Utilizando pyFDA, diseñar un filtro digital que permita separar las componentes relacionadas
#  a los pulsos oscilométricos. El mismo debe tener las siguientes características:
# - Tipo: IIR
# - Atenuación en la banda de paso: no mayor a 0.5 dB
# - Atenuación para las componentes relacionadas a la presión en el manguito: mayor a 60 dB

#IMPLEMENTADO EN pyFDA

#%% Item 4: Utilizando pyFDA, diseñar un filtro digital que permita separar las componentes relacionadas 
# al nivel de presión de inflado en el manguito, atenuando los pulsos oscilométricos. El mismo de tener 
# las siguientes características:
# - Tipo: FIR 
# - Atenuación en la banda de paso: menor a 1 dB 
# - Atenuación en la frecuencia fundamental relacionada los pulsos oscilométricos: mayor a 30 dB

# Se diseño un pasabajos, que dejara pasar todo por debajo de 0.5 Hz ya que por debajo de este valor de frecuencia
# se halla la señal de presion del manguito

#no entiendo, como que por debajo de 0.5 hz estan las seniales del manguito
#%% Item 5: Probar el funcionamiento de ambos filtros digitales utilizando la señal de prueba muestreada 
# a 85 Hz (nibp_85hz.txt), también expresada en mV. Graficar las señales y sus espectros antes y después 
# de ser filtradas.

#primero cargo los datos de mi senial remuestreada
resample_filename='nibp_85hz.txt'
signal_resample=np.loadtxt(resample_filename,  dtype=float, delimiter=',')

N_resample=len(signal_resample)
t_resample = np.linspace(0, N_resample / f_resample, N_resample)





#%% Item 6: Calcular analíticamente la Presión Arterial Media (MAP) en mmHg y la Frecuencia Cardíaca en
# LPM (latidos por minuto). La primera se puede estimar a partir del valor de presión en el manguito en
# el momento en que la señal de pulsos oscilométricos alcanza su máximo (ver fig. 1). La segunda, a partir
# de determinar el valor en frecuencia donde se encuentra el máximo en el espectro de la señal de pulsos 
# oscilométricos.