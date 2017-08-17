中央研究院資訊科學研究所

.. _hf243d2d3c27707d29a394ca2f4750:

\ |IMG1|\ 健康雲巨量資訊技術平台
********************************


.. toctree:: 
    :maxdepth: 2
    :hidden:

    Accounts
    blocks
    datasets
    doquery
    shortcuts
    Workspace
    autotests

.. _h478615d56794d73701b57135e2d52:

平台簡介s
=========

\ |IMG2|\ 

本平台協助使用者產生資料庫查詢，使用者可以利用本平台提供的Google Blockly方塊，設定過濾查詢條件，並查詢資料庫內的紀錄。

.. _hd7b751276e3b5a272340277219674:

在這網路發達的現代，
********************

在這網路發達的現代，只要將自己作品上傳到社交平台，遠至地球另一邊都能看到，所以我們心中想做的事情，比

.. code:: 

    import sys,os
    #sys.path.insert(0,os.path.abspath(os.path.join(os.path.dirname(__file__),'.')))
    #sys.path.insert(0,os.path.abspath(os.path.join(os.path.dirname(__file__),'..')))
    from daemon_addons.services import GenericService
    from types import ListType,TupleType
    from collections import deque
    class SimpleQueue(GenericService):
        name = 'SimpleQueue'
        def __init__(self,context):
            super(SimpleQueue,self).__init__(context)
            self.items = deque()
            print 'create a new simple queue',self
    
        def push(self,newitems):
            if type(newitems) in (ListType,TupleType):
                self.items.extend(newitems)
            else:
                self.items.append(newitems)
    
        def pull(self,max_size=1):
            if len(self.items) == 0: return []
            results = []
            for i in range(0,max_size):
                try:
                    results.append(self.items.popleft())
                except IndexError:
                    break
            return results
        def dump(self,formatter=None):
            if len(self.items) == 0:
    


.. code-block:: python
    :linenos:

    import sys,os
    #sys.path.insert(0,os.path.abspath(os.path.join(os.path.dirname(__file__),'.')))
    #sys.path.insert(0,os.path.abspath(os.path.join(os.path.dirname(__file__),'..')))
    from daemon_addons.services import GenericService
    from types import ListType,TupleType
    from collections import deque
    class SimpleQueue(GenericService):
        name = 'SimpleQueue'
        def __init__(self,context):
            super(SimpleQueue,self).__init__(context)
            self.items = deque()
            print 'create a new simple queue',self
    
        def push(self,newitems):
            if type(newitems) in (ListType,TupleType):
                self.items.extend(newitems)
            else:
                self.items.append(newitems)
    
        def pull(self,max_size=1):
            if len(self.items) == 0: return []
            results = []
            for i in range(0,max_size):
                try:
                    results.append(self.items.popleft())
                except IndexError:
                    break
            return results
        def dump(self,formatter=None):
            if len(self.items) == 0:
    

上一代人容易實踐。來自香港的周兆豐（周生）從事設計行業十多年，興趣是拍照，兩年前曾在灣仔富德樓舉行以「手」為主題的攝影展，最近在自己《臉書》眾籌推出奇怪攝影相集《旅行》。香港《蘋果日報》報導，約十年前，周生每天都會隨身攜帶相機，造就「每日一拍」，後來買了一台相機，一直沿用至今。他說：「上班下班、沒事做才會拍照。」所以大部份照片都在乘搭地鐵上班時拍攝。十年時間，他存下海量照片，自覺有部份較為特別，所以萌起以眾籌方式推出攝影集的念頭，希望整理一下照片和令拍攝方向更清晰。

\ |IMG3|\ 


+----------------------------------+-----------------------------------+----------------------------------+
|用至今。他說：「上班下班、沒事做才|b用至今。他說：「上班下班、沒事做才|                                  |
+----------------------------------+-----------------------------------+----------------------------------+
|                                  |                                   |用至今。他說：「上班下班、沒事做才|
+----------------------------------+-----------------------------------+----------------------------------+
|                                  |用至今。他說：「上班下班、沒事做才 |                                  |
+----------------------------------+-----------------------------------+----------------------------------+


..  Attention:: 

    用至今。他說：「上班下班、沒事做才


.. bottom of content

.. |IMG1| image:: static/index_1.png
   :height: 82 px
   :width: 82 px

.. |IMG2| image:: static/index_2.png
   :height: 202 px
   :width: 601 px

.. |IMG3| image:: static/index_3.png
   :height: 412 px
   :width: 601 px
