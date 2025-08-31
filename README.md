# pccsearch  
Buscador de precios de PCComponentes en python.
 
   
Para evitar conflictos, primero crea un entorno virtual:  

    python -m venv venv
Despues instala los requerimientos:  

    ./venv/bin/pip install -r requirements.txt  


Y ya puedes usar la aplicación para buscar precios de artículos. Puedes excluir términos con "-palabra":

    ❯ ./venv/bin/python pccsearch.py "caja hyte h70 blanco -y60 -y40"  
    Nombre;Precio  
    Caja HYTE Y70 Touch Infinite Negro/Blanco Display IPS 14.9” EATX Vidrio Templado;466,36€  
    Hyte Y70 Caja Atx Vidrio Templado Blanco;273,10€  
    Hyte Revolt 3 SFF USB 3.2 Blanco;110,11€  
    Hyte Y70 Cristal Templado USB 3.2 Blanco Reacondicionado;238,99€  
    Hyte Y70 Cristal Templado USB 3.2 Blanco/Negro;209,90€  
    Kimex Caja Blanca para Tablet iPad Pro 12.9" Generación 3;41,66€  
    Elite Screens Rollo Pantallas de Proyección 150" Formato 16:9;343,85€  
    Elite Screens Rollo Pantalla de Proyección 71" Formato 1:1;102,35€  
    Elite Screens Rollo Pantalla de Proyección 100" Formato 16:9;171,35€  
    Elite Screens Rollo Pantallas de Proyección 120" Formato 16:9;270,25€  
    Lian-Li UNI FAN TL Ventilador Suplementario 140mm Blanco;38,41€  
    EKWB AIO Nucleus CR240 Lux D-RGB Kit de Refrigeración Líquida Blanco;159,81€  
    Apple Watch SE GPS +Cellular 44mm Caja Aluminio Blanco Estrella con Correa Loop Deportiva Verde Lago;315,99€  
    Lian Li Lancool 206 Caja Atx Blanca Vidrio Templado;91,46€  
    Apple Watch SE GPS 44mm Caja Aluminio Blanco Estrella con Correa Deportiva Blanco Estrella M/L;267,99€  
    Apple Watch SE GPS 44mm Caja Aluminio Blanco Estrella con Correa Deportiva Blanco Estrella M/L Reacondicionado;203,67€  
    Phanteks NV9 Premium LED Kit 3x Módulos D-ARGB para Caja NV9 Blanca;79,71€  
    Phanteks NV5 Premium LED Kit 3x Módulos D-ARGB para Caja NV5 Blanca;59,90€  
    Tiza blanca Caja 100 unidades Arcilla escolar y oficina alta calidad;3,99€  
    Caja PC XPG Valor Air Plus Blanco Midi Tower ATX/SPCC 3x120mm Frontal 1x120mm Trasero Ventana Lateral;74,95€  
    Apple Watch SE GPS 40mm Caja de Aluminio Blanco Estrella con Correa Deportiva Blanco Estrella S/M;238,99€  
    Apple Watch SE GPS 40mm Caja de Aluminio Blanco Estrella con Correa Deportiva Blanco Estrella S/M Reacondicionado;218,22€  
    Apple Watch SE GPS 40mm Caja de Aluminio Blanco Estrella con Correa Deportiva Blanco Estrella M/L;238,99€  
    Apple Watch SE GPS 44mm Caja de Aluminio Blanco Estrella con Correa Loop Deportiva Verde Lago;267,99€  
    Caja DeepCool CH260 Blanca Micro ATX ABS/SPCC/Vidrio Templado USB-C;71,24€  
    Mars Gaming MS-OM Altavoces Gaming RGB 20W Bluetooth 5.3 Caja Control Volumen Blanco;17,89€  
    Apple Watch SE GPS 40mm Caja de Aluminio Blanco Estrella con Correa Loop Deportiva Verde Lago;238,99€  
    Bluelounge CableBox Mini Caja Recogecables Ignífuga Blanca;26,95€  
    Bluelounge CableBox Caja Recogecables Ignífuga Blanca;69,75€  
    Mars Gaming MS-PRO Altavoces RGB Flow con Caja de Control 10W Blanco;6,32€  
    Caja PC Aerocool P500C Blanca ARGB Vidrio Templado ATX/Micro-ATX/Mini-ITX 4 Ventiladores;92,11€  
    Caja PC DeepCool CH510 Blanco Mini-ATX Display LED USB Tipo C ABS/SPCC;82,70€  
    Caja Thermaltake Midi Tower Blanca SPCC RGB Vidrio Templado ATX/EATX USB-C;127,19€  
    Caja Jonsbo D41 MESH Blanco ATX MicroATX Mini-ITX Acero Ventilación Gaming;64,90€  
    Caja PC GIGABYTE C301GW Blanco Midi Tower Vidrio Templado RGB USB-C Gaming;94,41€  
    Torre Fractal Design Torrent Blanco Acero Vidrio Templado ATX EATX Iluminación RGB;213,76€  
    Raspberry Carcasa Blanca/Roja para Raspberry Pi 4;7,17€  
    Caja PC GIGABYTE C102 Glass Blanco Ventana Lateral Midi Tower Mini-ATX Vidrio Templado;60,01€  
    Caja PC Gigabyte C500 Panoramic Stealth Blanco ATX Vidrio Templado Gaming;95,94€  
    In Win 101C Cristal Templado USB 3.1 Blanca;95,19€  


O puedes buscar el precio de un artículo en concreto si le pasas la url y te devuelve directamente el precio:

    ❯ ./venv/bin/python pccsearch.py "https://www.pccomponentes.com/torre-pc-hyte-y70-caja-atx-vidrio-templado-blanco"  
    273,10€
