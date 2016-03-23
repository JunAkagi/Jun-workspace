'''
Created on 2016/03/16

@author: JUN_AKAGI
'''
"""
駒の表現
"""

Empty = 0   #駒なし
Black = 16  #数値一括変更用

"""
白の駒の識別子
"""
WPo = 1     #白のポーン
WRo = 2     #白のルーク
WKn = 3     #白のナイト
WBi = 4     #白のビショップ
WQu = 5     #白のクイーン
WKi = 6     #白のキング

"""
空き数値は変則（フェアリー）駒用
"""

WhiteUnits={
            WPo:"WhitePone",
            WRo:"WhiteRook",
            WKn:"WhiteKnight",
            WBi:"WhiteBishop",
            WQu:"WhiteQueen",
            WKi:"WhiteKing"
            }

"""
黒の駒の識別子
"""
BPo = WPo + Black       #黒のポーン
BRo = WRo + Black       #黒のルーク
BKn = WKn + Black       #黒のナイト
BBi = WBi + Black       #黒のビショップ
BQu = WQu + Black       #黒のクイーン
BKi = WKi + Black       #黒のキング

BlackUnits={
            BPo:"BlackPone",
            BRo:"BlackRook",
            BKn:"BlackKnight",
            BBi:"BlackBishop",
            BQu:"BlackQueen",
            BKi:"BlackKing"
            }

"""
盤面の状況
"""


"""
OnBoard={
         1:{1:Empty,2:Empty,3:Empty,4:Empty,5:Empty,6:Empty,7:Empty,8:Empty},
         2:{1:Empty,2:Empty,3:Empty,4:Empty,5:Empty,6:Empty,7:Empty,8:Empty},
         3:{1:Empty,2:Empty,3:Empty,4:Empty,5:Empty,6:Empty,7:Empty,8:Empty},
         4:{1:Empty,2:Empty,3:Empty,4:Empty,5:Empty,6:Empty,7:Empty,8:Empty},
         5:{1:Empty,2:Empty,3:Empty,4:Empty,5:Empty,6:Empty,7:Empty,8:Empty},
         6:{1:Empty,2:Empty,3:Empty,4:Empty,5:Empty,6:Empty,7:Empty,8:Empty},
         7:{1:Empty,2:Empty,3:Empty,4:Empty,5:Empty,6:Empty,7:Empty,8:Empty},
         8:{1:Empty,2:Empty,3:Empty,4:Empty,5:Empty,6:Empty,7:Empty,8:Empty},
         }
"""
HeightBorad={}

OutBoardUnits={}
