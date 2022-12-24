# STMCTF QUESTION

## Information
### Challenge name: 

`my dark history`

### Challenge:

`ulg_file`

### Difficulty:
- [ ] Easy
- [x] Normal
- [ ] Hard

### Categories:
 - `Misc`

### Challenge message:
```
TR:
Otonom uçuşlarda pixhawk uçuş kontrolcüsü kullanılır ise uçuş verileri, PX4 otopilotuna
özel bir format olan "ulog" formatında, .ulg uzantılı bir dosyaya kaydedilir. Ulog formatı
bozulur ise .ulg destekli herhangi bir parser, log dosyasını okuyamaz. Bu soruda da log
dosyası manipüle edilmiş olup (log verinde oynama yoktur, sadece formatı bozacak değişiklikler yapılmıştır),
yarışmacıların dosyayı düzelttikten sonra gizli mesajı bulmaları mümkündür.

Yarışmacıların, eğer bilmiyorlar ise, verilen dosyanın içeriğine bakarak bunun bir log
dosyası olduğunu anladıktan sonra hangi formatta yazıldığını bulmaları gerekir. Ulog fortmatında
yazıldığını anladıktan sonra neyin yanlış olduğunu tespit edip düzeltmeleri beklenir.

PX4 açık kaynatır. Ulog formatı resmi sitesinden incelenebilir.


EN:
If the pixhawk flight controller is used in autonomous flights, the flight data is saved
in a .ulg file with a format called "ulog" which is special to the PX4 autopilot.
If it gets corrupted, any parser with .ulg support cannot read the log file. Also in this
question, the file was manipulated (There is no change in the log data, only changes that will break the format),
and the contestants can finde the secret message after correcting the file.

If the contestants do not know that the given file is a log file, they need to understand
this is a log file (with a few google search they can find out). Once they understand that
it is a log file, they need to find out in what format it was written. After they understand
what it is ulog format, they are expected to identify what is wrong and correct it.

The PX4 is open-source. Ulog format can be viewed on the official site.
```

### Challenge files:
question.ulg -> link_here
solution.ulg -> link_here

### Author
`Koray ÇELİK`
`Ali Ahmet Taşkesen`

### Hint-1: 
`flight`

### Hint-2: 
`history`

### Flag:
`STMCTF{MANDALİNA}`

---

## Deployment

	# docker build -t gitrepo:v1.0 .
	# docker run -dit --name myrepo -v $PWD/repos:/var/www/git -p 35006:80 gitrepo:v1.0

---

## Solution:

*Change the first four characters of the "question.ulg" from "KAli" to "ULog" using a hex editor (Suggested: https://hexed.it).*
*Open the "question.ulg" with any flight review parser that supports .ulg files (Suggested: https://review.px4.io).*
*Check the pattern made by the UAV from above.*
*The pattern is the flag.*
*The flag -> https://ibb.co/8r4DS9z*
