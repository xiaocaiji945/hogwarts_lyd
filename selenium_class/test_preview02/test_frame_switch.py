from selenium_class.test_preview02.driver_import import DrIm

'''
打开包含frame的web页面 https://www.runoob.com/try/try.php?filename=jqueryui-api-droppable
打印"请拖拽我"元素的文本
打印"点击运行"元素的文本
'''


class TestFrame(DrIm):
    def test_frame01(self, open_url):
        self.driver.get('https://www.runoob.com/try/try.php?filename=jqueryui-api-droppable')

        self.driver.switch_to_frame('iframeResult')
        text01_input = self.driver.find_element_by_id('draggable')
        text02_input = self.driver.find_element_by_id('droppable')
        text01 = text01_input.text
        text02 = text02_input.text
        print(f'\n第一个文案是： {text01}')
        print(f'第二个文案是： {text02}')

        # self.driver.switch_to.parent_frame()
        self.driver.switch_to.default_content()
        text03_in = self.driver.find_element_by_id('submitBTN')
        text03 = text03_in.text
        print(f'第三个文案是： {text03}')
