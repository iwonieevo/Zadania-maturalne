# https://arkusze.pl/maturalne/informatyka-2022-czerwiec-matura-rozszerzona-2.pdf

kluby = open("kluby.txt", "r").readlines()[1:]  # Id_klubu;Nazwa;Miasto
mecze = open("mecze.txt", "r").readlines()[1:]  # Id_meczu;Data;Id_klubu;Sety_wygrane;Sety_przegrane;Id_sedziego
sedziowie = open("sedziowie.txt", "r").readlines()[1:]  # Id_sedziego;Imie;Nazwisko
odpowiedz = open("wyniki6.txt", "w")

for i in range(len(kluby)):
    kluby[i] = kluby[i].split(";")

for i in range(len(mecze)):
    mecze[i] = mecze[i].split(";")

for i in range(len(sedziowie)):
    sedziowie[i] = sedziowie[i].split(";")
    # NOTE: formatowanie danych do wygodnej postaci listy list
licznik_tie_breakow = 0
miasta = {}
sedziowie_dict = {}
_sedziowie = []  # sedziowie prowadzacy minimum 1 mecz w tym okresie w tych miastach
szukani_sedziowie = []  # odpowiedz do podpunktu 4
zestawienie_klubow = {}
for mecz in mecze:
    if int(mecz[3]) + int(mecz[4]) == 5:
        licznik_tie_breakow += 1
    id_klubu = int(mecz[2])
    miasto = None
    for klub in kluby:
        if int(klub[0]) == id_klubu:
            miasto = klub[2].replace("\n", "").replace(" ", "")
            break
    if miasta.keys().__contains__(miasto):
        miasta[miasto] += 1
    else:
        miasta[miasto] = 1
    id_sedziego = mecz[5].replace("\n", "")

    if sedziowie_dict.__contains__(id_sedziego):
        sedziowie_dict[id_sedziego] += 1
    else:
        sedziowie_dict[id_sedziego] = 1
    data = mecz[1].split("-")
    if data[0] == '2019' and (
            (data[1] == '10' and int(data[2]) >= 15) or (data[1] == '11') or (data[1] == '12' and int(data[2]) <= 15)):
        if (miasto == 'Licowo' or miasto == 'Szymbark') and not _sedziowie.__contains__(int(mecz[5])):
            _sedziowie.append(int(mecz[5]))
        if not szukani_sedziowie.__contains__(int(mecz[5])):
            szukani_sedziowie.append(int(mecz[5]))
    if zestawienie_klubow.__contains__(str(id_klubu)):
        zestawienie_klubow[str(id_klubu)][0] += 1
    else:
        zestawienie_klubow[str(id_klubu)] = [1, 0]
    wygrana = False
    if int(mecz[3]) > int(mecz[4]):
        wygrana = True
    if wygrana:
        zestawienie_klubow[str(id_klubu)][1] += 1

odpowiedz.write("6.1\n{}\n".format(licznik_tie_breakow))

odpowiedz.write("\n6.2\n")
zestawienie_miast = list(reversed(sorted(miasta.items(), key=lambda it: it[1])))
for item in zestawienie_miast:
    odpowiedz.write("{}:{}\n".format(item[0], item[1]))

odpowiedz.write("\n6.3\n")
average = 0
for v in sedziowie_dict.values():
    average += v
average /= len(sedziowie_dict)
for item in sedziowie_dict.items():
    id_sedziego = int(item[0])
    imie_nazwisko = None
    for sedzia in sedziowie:
        if int(sedzia[0]) == id_sedziego:
            imie_nazwisko = "{} {}".format(sedzia[1], sedzia[2].replace("\n", ""))
            break
    if item[1] > average:
        odpowiedz.write("{}:{}\n".format(imie_nazwisko, item[1]))

odpowiedz.write("\n6.4\n")
for s in _sedziowie:
    szukani_sedziowie.remove(s)

for s in szukani_sedziowie:
    imie_nazwisko = None
    for sedzia in sedziowie:
        if int(sedzia[0]) == s:
            imie_nazwisko = "{} {}".format(sedzia[1], sedzia[2].replace("\n", ""))
            break
    odpowiedz.write("{}\n".format(imie_nazwisko))

odpowiedz.write("\n6.5\n")
for item in zestawienie_klubow.items():
    if item[1][1] >= item[1][0]/2:
        nazwa = None
        miasto = None
        for klub in kluby:
            if klub[0] == item[0]:
                nazwa = klub[1]
                miasto = klub[2].replace("\n", "")
                break
        odpowiedz.write("Nazwa klubu: {}\nMiasto: {}\nWygrane mecze: {}\nPrzegrane mecze: {}\n\n".format(nazwa, miasto, item[1][1], item[1][0] - item[1][1]))
