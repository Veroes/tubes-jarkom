# Tugas Besar Jarkom

## Cara Penggunaan project webserver ini 

### Setup Web Server

1. gunakan command 'Git clone https://github.com/Veroes/tubes-jarkom.git' (pastikan Git sudah terininstall di komputer anda)

2. Buka directory tersebut dan jalankan webserver.py

3. Jalankan lewat cmd dan ketik py ./webserver.py

4. Web Server akan menyala dan siap menerima request dari client browser

### Client-side

1. buka browser dan masukkan localhost:8001/<file>(ekstensi .html)

2. Jika file valid [dalam kasus ini index.html], maka webserver mengirim HTTP Header Status 200 dan file index.html

3. Jika file tidak ada di directornya maka webserver akan mengrim HTTP Header Status 404 dan file nonexist.html
