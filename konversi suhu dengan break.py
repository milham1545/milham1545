while True:
    print('===============================================')
    print('Pilihlah suhu yang ingin anda hitung!\n[1.] Celcius\n[2.] Reamur\n[3.] Fahrenheit\n[4.] Kelvin\n[0.] Quit')
    print('===============================================')
    suhu = int(input('Masukkan pilihan anda: '))

    if suhu == 1:
        print('===============================================')
        c = int(input('Masukkan suhunya: '))
        r = c / 5 * 4
        f = c / 5 * 9 + 32
        k = c + 273
        print('===============================================')
        print("Hasil Reamurnya adalah: ", r)
        print('Hasil Fahrenheitnya adalah: ', f)
        print('Hasil Kelvinnya adalah: ', k)
        print('===============================================')
    
    elif suhu == 2:
        print('===============================================')
        r = int(input('Masukkan suhunya: '))
        c = r / 4 * 5
        f = (r / 4 * 9) + 32
        k = r / 4 * 5 + 273
        print('===============================================')
        print('Hasil Celciusnya adalah: ', c)
        print('Hasil Fahrenheitnya adalah: ', f)
        print('Hasil Kelvinnya adalah: ', k)
        print('===============================================')

    elif suhu == 3:
        print('===============================================')
        f = int(input('Masukkan suhunya: '))
        c = (f - 32) / 9 * 5
        r = (f - 32) / 9 * 4
        k = (f - 32) / 9 * 5 + 273
        print('===============================================')
        print('Hasil Celciusnya adalah: ', c)
        print('Hasil Reamurnya adalah: ', r)
        print('Hasil Kelvinnya adalah: ', k)
        print('===============================================')

    elif suhu == 4:
        print('===============================================')
        k = int(input('Masukkan suhunya: '))
        c = k - 273
        r = (k - 273) / 5 * 4
        f = (k - 273) / 5 * 9 + 32
        print('===============================================')
        print('Hasil Celciusnya adalah: ', c)
        print('Hasil Reamurnya adalah: ', r)
        print('Hasil Fahrenheitnya adalah: ', f)
        print('===============================================')

    elif suhu == 0:
        print('===============================================')
        print('Terima kasih telah menggunakan program ini.')
        print('===============================================')
        break

    else:
        print('===============================================')
        print('PILIHLAH opsi yang ada!!!')
        print('===============================================')