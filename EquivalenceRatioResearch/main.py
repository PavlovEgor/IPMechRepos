import os
import shutil
from InitionCondition.MakeConcentration import make_concentration_CH4_H2_air, make_concentration_CH4_air
import subprocess


def name(prefix, phi, xi=False):
    if xi:
        return prefix + 'Phi=' + str(round(phi, 2)) + 'Xi=' + str(round(xi, 2))
    else:
        return prefix + 'Phi=' + str(round(phi, 2))


def copy_and_rename_folder(source_folder, destination_folder):
    # Проверяем, существует ли исходная папка
    if not os.path.exists(source_folder):
        print(f"Исходная папка {source_folder} не существует.")
        return

    # Копируем папку
    try:
        shutil.copytree(source_folder, destination_folder)
    except Exception as e:
        print(f"Ошибка при копировании папки: {e}")

def create_new_calculation(path, path_of_template, prefix, phi, xi=False):
    if xi:
        cur_path = path + '/' + name(prefix, phi, xi)
        species, Y = make_concentration_CH4_H2_air(phi=phi, xi=xi)
    else:
        cur_path = path + '/' + name(prefix, phi)
        species, Y = make_concentration_CH4_air(phi=phi, xi=xi)


    copy_and_rename_folder(path_of_template, cur_path)



    with open(cur_path + '/system/setFieldsDict', 'r') as file:
        lines = file.readlines()
        new_lines = lines
        # for line in lines:
        #     print(line)

        for i, line in enumerate(lines):
            if line == 'defaultFieldValues\n':
                for j in range(len(species)):
                    new_lines[i+3+j] = f'    volScalarFieldValue {species[j]}  {Y[j]}  \n'
                break

    with open(cur_path + '/system/setFieldsDict', 'w') as file:
        file.writelines(new_lines)

    return cur_path


def run_shell_command(command):
    """
    Выполняет команду shell и возвращает её вывод.

    :param command: Команда shell для выполнения.
    :return: Вывод команды.
    """
    try:
        # Выполняем команду shell
        result = subprocess.run(command, shell=True, check=True, text=True, capture_output=True)
        # Возвращаем стандартный вывод команды
        return result.stdout
    except subprocess.CalledProcessError as e:
        # Если команда завершилась с ошибкой, возвращаем сообщение об ошибке
        return f"Ошибка при выполнении команды: {e.stderr}"



path = '/home/tgd323/OpenFOAM/tgd323-v2406/run/6Step/1D/reactingCTDyMFoamCantera/EquivalenceRatioSearchXi=0.3'
path_of_template = path + '/ClTemplate'
prefix = 'Cl'

# Phi = [0.85, 0.9, 0.95, 1.0, 1.05, 1.1, 1.15, 1.2]
# Phi = [0.85, 0.95, 1.05, 1.15]
xi = 0.3
Phi = [0.8]

for phi in Phi:

    cur_path = create_new_calculation(path, path_of_template, prefix, phi, xi=xi)
    run_shell_command(cur_path + '/Allrun')

