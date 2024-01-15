# portfolio_601.py

"""
[601] 이터레이션 사용(220817)
220924 설명 보완

"""


class Portfolio:

    def __init__(self, holdings):
        self._holdings = holdings  # 프라이빗 어트리뷰트로 변경

    def __iter__(self):
        return self._holdings.__iter__()

    def __len__(self):
        return len(self._holdings)

    def __getitem__(self, index):
        return self._holdings[index]

    def __contains__(self, name):
        return any([s.name == name for s in self._holdings])

    @property
    def total_cost(self):
        """
        보유주식들의 매수금액 합계
        :return:
        """
        return sum(s.shares * s.price for s in self._holdings)

    def tabulate_shares(self):
        """
        주식 증감을 계산한다
        :return: 총주식 수량
        """
        from collections import Counter
        total_shares = Counter()
        for s in self._holdings:
            total_shares[s.name] += s.shares
        return total_shares
