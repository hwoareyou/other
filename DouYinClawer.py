import os

import time
from com.dtmilano.android.viewclient import ViewClient


def search_douyin_for_recommend_user(douyin_id):
    """采集指定抖音账号的关注推荐数据
    """
    print(u'准备采集"{}"对应的关注推荐数据'.format(douyin_id))
    # 连设备
    serialno = None
    if serialno:
        os.system('adb connect {}'.format(serialno or ''))
        time.sleep(3)

    device, serialno = ViewClient.connectToDeviceOrExit(serialno=serialno)
    vc = ViewClient(device, serialno, autodump=False)

    # 强制关闭抖音
    print(u'强制关闭抖音.')
    device.shell('am force-stop com.ss.android.ugc.aweme')
    time.sleep(2)

    # 启动抖音
    print(u'启动抖音.')
    device.shell('am start -n com.ss.android.ugc.aweme/.main.MainActivity')
    time.sleep(5)
    # 暂停视频播放
    print(u'点击屏幕，暂停视频播放.')
    device.touch(514, 1048)

    # 点击搜索按钮
    vc.dump()
    search_btn = vc.findViewById('com.ss.android.ugc.aweme:id/amj')
    if search_btn:
        print(u'点击搜索按钮，跳转到搜索页面.')
        search_btn.touch()

        vc.dump()
        # 点击搜索输入框
        search_input = vc.findViewById('com.ss.android.ugc.aweme:id/ad_')
        if search_input:
            print(u'点击搜索框，准备输入关键词.')
            search_input.touch()

            # 输入抖音ID
            print(u'输入搜索关键词: {}.'.format(douyin_id))
            device.type(douyin_id.encode('UTF-8'))

            # 点击搜索按钮
            search_btn = vc.findViewById('com.ss.android.ugc.aweme:id/cp8')
            if search_btn:
                print(u'提交搜索.')
                search_btn.touch()
                time.sleep(2)
                vc.dump()

                ## 切换到用户
                # user_tab = vc.findViewWithText(u'用户')
                # user_tab.touch()

                # 找到匹配的
                matches = []

                def find_matches(view):
                    if view.getClass() == 'android.widget.TextView':
                        text = view.getText()
                        if douyin_id.lower() in text.lower():
                            # 找到匹配的了
                            print(u'找到匹配的: {}'.format(text))
                            matches.append(view)
                        else:
                            # print text
                            pass

                vc.traverse(transform=lambda view: find_matches(view))
                if matches:
                    # 有没有已关注按钮
                    btn = vc.findViewWithText(u'已关注')
                    if btn:
                        # 先取消关注
                        print(u'之前关注过，先取消关注.')
                        btn.touch()
                        time.sleep(1)
                    user_matched = matches[0]
                    print(u'点击进入个人主页.')
                    user_matched.touch()
                    time.sleep(1)

                    # 点关注
                    vc.dump()
                    follow_btn = vc.findViewById('com.ss.android.ugc.aweme:id/aei')
                    if follow_btn:
                        # 点击关注
                        print(u'点击关注')
                        follow_btn.touch()
                        time.sleep(1)
                        # 点击查看更多
                        vc.dump()
                        viewmore_btn = vc.findViewById('com.ss.android.ugc.aweme:id/bqn')
                        if viewmore_btn:
                            # 点击查看更多
                            print(u'点击查看更多系统推荐')
                            viewmore_btn.touch()
                            time.sleep(1)
                            i = 0
                            while True:
                                # 上滑动
                                device.drag((345, 1762), (345, 550), duration=100)
                                print(u'上滑以加载更多')
                                i += 1
                                if i % 5 == 0:
                                    # 拖动10次判断一下是否还有更多
                                    vc.dump()
                                    if vc.findViewWithText(u'暂时没有更多了'):
                                        print(u'暂时没有更多了, "{}"的关注推荐数据采集完毕.'.format(douyin_id))
                                        # 采集成功了
                                        return True
                                    failed_tip = vc.findViewWithText(u'加载失败，点击重试')
                                    if failed_tip:
                                        print(u'加载失败,点击重试.')
                                        failed_tip.touch()
                        else:
                            # 没有找到查看更多按钮
                            print(u'没有找到查看更多按钮')
                    else:
                        # 没有找到加关注按钮
                        print(u'没有找到加关注按钮')
                else:
                    # 没有找到匹配的用户
                    print(u'没有找到匹配的用户')
            else:
                # 没有找到搜索提交按钮
                print(u'没有找到搜索提交按钮.')
        else:
            # 没有找到搜索输入框
            print(u'没有找到搜索输入框.')
    else:
        # 没有找到搜索按钮
        print(u'没有找到搜索按钮.')
