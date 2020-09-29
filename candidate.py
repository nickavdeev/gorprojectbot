from constituency import Constituency
import constants


class Candidate:
    def __init__(self, name):
        self.name = name

    @staticmethod
    def get_my_candidate(address=None, location=None):
        """Получение кандидата по округу"""
        if address is not None:
            address = Constituency.get_coordinates(address)
            point = (float(address[0]), float(address[1]))
        else:
            point = location

        constituency_number = 0
        for i in range(len(constituencies.keys())):
            if Constituency.is_constituency(point, list(constituencies.values())[i].boundaries):
                constituency_number = list(constituencies.values())[i].number
                break

        if constituency_number == 9:
            return f'\u270A\U0001F3FB *Дом входит в {constituency_number}-й избирательный округ Екатеринбурга!*'
            # f'Приглашаем на довыборы в Городскую думу Екатеринбурга 22-го ноября. ' \
            # f'Ваш кандидат: {constituencies.get(constituency_number).candidate.name}.'
        return '\U0001F614 В этом году по этому адресу не проходят выборы.'


constituencies = {
    3: Constituency(3, Candidate('Владислав Постников'), constants.constituency_3),
    9: Constituency(9, Candidate('Константин Плашиннов'), constants.constituency_9)
}
