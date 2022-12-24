# STMCTF QUESTION

## Information
### Challenge name: 

`image only`

### Challenge:

`images`

### Difficulty:
- [ ] Easy
- [ ] Normal
- [x] Hard

### Categories:
 - `Misc`

### Challenge message:
```
TR:
Bu soruda yarışmacılara puzzle haline getirilmiş bir fotoğraf verilir ve gizli mesajı bulması
beklenir. İki aşamalıdır. İlk aşamada bulmaca çözülmeli, ikinci aşamada fotoğraftaki gizli
mesaj bulunmalı. Görüntü işleme kazanımları ve hexadecimal işlemler gerektirir.

Zaten zor olan bu soruyu daha da zor yapmak için 4 farklı fotoğraftan uygun olanı seçmeyi
size bırakıyorum.

Seviye 1 | puzzeled_out_85_256  -> 256 parça, yüzde 85 opaklık
Seviye 2 | puzzeled_out_85_1024 -> 1024 parça, yüzde 85 opaklık
Seviye 3 | puzzeled_out_90_256  -> 256 parça, yüzde 90 opaklık
Seviye 4 | puzzeled_out_90_1024 -> 1024 parça, yüzde 90 opaklık

Parça sayısının çok olması geçilmesi gereken ilk aşamayı zorlaştırır.
Opaklığın çok olması ikinci aşamayı zorlaştırır.

İlk aşamayı geçmek için internetten hazır bir algoritma direk alıp kullanmaya karşı bir takım önlemler
alınmıştır. Hazır olarak alınan algoritma ile biraz uğraşmak gerekir.

EN:
In this question, the contestants are given a picture that has been turned into a puzzle and are
expected to find the secret message. It is two-stage. In the first stage, the puzzle should be solved,
in the second stage, the hidden message in the photo should be found. Requires image processing gains
and hexadecimal operations.

In order to make this already difficult question even more difficult, I leave it to you to choose the
appropriate one from 4 different photos.

Level 1 | puzzeled_out_85_256 -> 256 parts, 85 percent opacity
Level 2 | puzzeled_out_85_1024 -> 1024 parts, 85 percent opacity
Level 3 | puzzeled_out_90_256 -> 256 parts, 90 percent opacity
Level 4 | puzzeled_out_90_1024 -> 1024 parts, 90 percent opacity

The large number of pieces makes the first stage difficult to pass.
Too much opacity makes the second stage difficult.

In order to pass the first stage, some precautions have been taken against using a ready-made algorithm directly
from the internet. It is necessary to deal with the ready-made algorithm a little.
```

### Author
`Koray ÇELİK`

### Hint-1: 
`mask`

### Hint-2: 
`under`

### Flag:
`STMCTF{DÜNYA MAVİDİR, TIPKI PORTAKALLAR GİBİ}`

---

## Deployment

	# docker build -t gitrepo:v1.0 .
	# docker run -dit --name myrepo -v $PWD/repos:/var/www/git -p 35006:80 gitrepo:v1.0

---

## Solution:

*Firstly, the puzzle must be solved. There are two ways for it. First one is cutting all the pieces and put them together
by a human hands and intelligence. Other way is using and algorithm(suggested -> https://github.com/kryC1/Jigsaw-puzzle-solver).
The appropriate approach is comparing pieces by their edges in HSV channels. After solving the puzzle we shoulde have something
like this https://ibb.co/fSG9dSX hence the first stage is solved. Now we need to find the message. The message is hidden under
the ...8888888.... characters but it cannot be detected by human eyes. So, we need to apply appropriate masks to find it. The
suggested method is using a slider that we can apply every color range(HSV filter slider can be found in this dir.).
After using masks on solved puzzle we can see something like this https://ibb.co/QMc3JL2. Here some of the text we saw is
actually dummy data. Only the one in the up center is meaning something.
The message is "6962622E636F2F5A54665A584E4E" but it is hexadecimal characters. They translates into a link "https://ibb.co/ZTfZXNN"
wich is the flag*
