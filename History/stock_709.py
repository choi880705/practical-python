# stock_709.py

"""
405 : 클래스 적용(220811)
410 : 특수 메서드 적용(220816)
508 : 데코레이션(프로퍼티, setter) 적용(220817)
      [220831] 설명 보완
709 : 클로저 적용(220905)
"""


from typedproperty_709 import String, Integer, Float


class Stock:
    """
    name, shares, price로 구성된 보유주식의 인스턴스?
    """

    name = String('name')  # name을 str 타입으로 강제 변경
    shares = Integer('shares')  # shares를 int 타입으로 강제 변경
    price = Float('price')  # price를 float 타입으로 강제 변경

    def __init__(self, name, shares, price):
        """
        어트리뷰트 초기화
        :param name: 종목이름
        :param shares: 수량
        :param price: 매입가격
        """
        self.name = name
        self.shares = shares
        self.price = price

    def __repr__(self):
        """
        보기 편하게 만든다
        :return:
        """
        return f'Stock({self.name}, {self.shares}, {self.price})'

    @property
    def cost(self):
        """
        수량 * 가격을 매입금액으로 리턴
        :return: 매입금액
        """
        return self.shares * self.price

    def sell(self, sell_shares):
        """
        매도된 수량을 처리
        :param sell_shares:
        :return: 남은 수량
        """
        self.shares -= sell_shares


class MyStock(Stock):
    """
    Stock 클래스의 하위 클래스
    """

    # inti 재정의 - 새로운 어트리뷰트(factor)를 추가
    def __init__(self, name, shares, price, factor):
        """
        어트리뷰트 초기화
        :param name:
        :param shares:
        :param price:
        :param factor:
        """
        # 'super'와 '__init__'에 대한 호출을 확인
        super().__init__(name, shares, price)
        self.factor = factor

    # 새 메서드 추가
    def panic(self):
        """
        :param 없다. 인스턴스만 있으면 된다
        :return:
        """
        self.sell(self.shares)  # 보유 주식을 모두 판다

    # 메서드 재정의
    def cost(self):
        """
        :param 없다. 인스턴스만 있으면 된다
        :return: cost에 factor를 적용해서 리턴한다.
        """
        return self.factor * super().cost()
