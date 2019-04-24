def pedir_confi(promp, reintentos=4, recordatorio='intentar denuevo'):
    while True:
        ok = input(promp)
        if ok in ('s', 'S', 'si', 'Si', 'sI', 'SI'):
            return True
        if ok in ('n', 'no', 'No', 'NO'):
            return False
        reintentos = reintentos - 1
        if reintentos < 0:
            raise ValueError('Error, respuesta invalida')
        print(recordatorio)


pedir_confi('Sobreescribir archivo?', 2, 'vamos, solo si o no!')
