from src.base.Bbox import Bbox


class BoxFactory:

    @staticmethod
    def RapperswilBhf():
        return Bbox("47.224729942195445", "8.814670787352005", "47.226369315435", "8.818962321775663")

    @staticmethod
    def ZurichBellvue():
        return Bbox(47.366177501999516,8.54279671719532, 47.36781249586627, 8.547088251618977)