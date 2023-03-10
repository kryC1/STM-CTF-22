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
Size verile question.ulg dosyasından yola çıkarak gizli mesajı(flag) bulunuz.

EN:
Find the hidden message, the flag, using the given file question.ulg
```

### Challenge files:
question.ulg -> [click to download](https://drive.google.com/file/d/1RYcOY2ynTJRR6gmmj0-4avWZo8vwtC_L/view?usp=share_link)<br />
solution.ulg -> [click to download](https://drive.google.com/file/d/1x1K1wl_tORFDShsiC_1XFE9Inisni9Ab/view?usp=share_link)

### Authors
[Koray ÇELİK](https://github.com/kryC1)<br />
[Ali Ahmet Taşkesen](https://github.com/aliahmetggg)

### Hint-1: 
`flight`

### Hint-2: 
`history`
---

## Solution:
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

*Change the first four characters of the "question.ulg" from "KAli" to "ULog" using a hex editor (Suggested: https://hexed.it).*
*Open the "question.ulg" with any flight review parser that supports .ulg files (Suggested: https://review.px4.io).*
*Check the pattern made by the UAV from above.*
*The pattern is the flag.*
*The flag -> https://ibb.co/8r4DS9z*


### Flag:
`STMCTF{MANDALİNA}`
