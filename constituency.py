from yandex_geocoder import Client


class Constituency:
    """Избирательный округ"""

    def __init__(self, number, candidate, boundaries):
        self.number = number
        self.candidate = candidate
        self.boundaries = boundaries

    @staticmethod
    def is_constituency(point, polygon):
        """
        Попадает ли точка на карте в округ
        :param tuple point: точка на карте
        :param list(list) polygon: координаты границ округа
        :return bool: да / нет
        """
        size = len(polygon)

        result = False
        j = size - 1
        for i in range(size):
            if ((polygon[i][0] < point[0] <= polygon[j][0] or polygon[j][0] < point[0] <= polygon[i][0])
                    and (polygon[i][1] + (point[0] - polygon[i][0])
                         / (polygon[j][0] - polygon[i][0]) * (polygon[j][1] - polygon[i][1]) < point[1])):
                result = not result
            j = i

        return result

    @staticmethod
    def get_coordinates(address):
        """
        Определение координат по адресу
        :param str address: Адрес в произвольном формате
        :return tuple: широта и долгота
        """
        client = Client("f7d838a6-9c1c-4070-a337-88f69121df6c")
        coordinates = client.coordinates(f'Екатеринбург {address}')
        return coordinates
