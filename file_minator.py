import csv


def csv_loader(file_name):
    with open(file_name, "r") as rfile:
        reader = list(csv.reader(rfile))
        return reader


def csv_saver(file_name, updated):
    with open(file_name, "a") as afile:
        writer = csv.writer(afile)
        writer.writerow(updated)


def csv_remover(file_name, id_to_delete):
    with open(file_name, "r") as rfile:
        reader = list(csv.reader(rfile))
    with open(file_name, "w") as wfile:
        writer = csv.writer(wfile)
        for line in reader:
            if id_to_delete not in line:
                writer.writerow(line)


def loader(file_name):
    with open(file_name, "r") as rfile:
        lines = rfile.readlines()
    table = [element.replace("\n", "").split(";") for element in lines]
    return table


def saver(file_name, story_elements):
    with open(file_name, "a") as afile:
        afile.write("\n")
        for items in story_elements:
            afile.write(items+';')


def remover(file_name, id_to_delete):
    with open(file_name, "r") as rfile:
        lines = rfile.readlines()
    return lines
    with open(file_name, "w") as wfile:
        for line in lines:
            if id_to_delete not in line:
                wfile.write(line)


if __name__ == '__main__':
    print(csv_remover("stories.csv", "test 03"))
