import json


class doJson:
    @staticmethod
    def Ljson(data):
        return json.loads(data, ensure_ascii=False, indent=4)

if __name__ == '__main__':
    pass