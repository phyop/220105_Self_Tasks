
#######################################
"""
《在 Mac 雙擊執行Shell Script》
https://notes.wadeism.net/mac/2588/

macOS 的 bash 一樣是認 xxx.sh 的副檔名，
不過要在 macOS 的桌面環境中用滑鼠執行，必須將副檔名從 .sh 改為 .command。

將 shell script 的副檔名改成 .command 就可以用滑鼠雙擊執行，
但執行完後 terminal 的視窗並不會自動關閉，這時必須到
「終端機」→「偏好設定」，在描述檔設定中的 「Shell」 頁籤裡，
找到「當 shell 結束時」的選項，可以設定 shell script 執行完後的動作，
在這裡改成「Shell 完全結束時才關閉視窗」，這樣跑完 script 就不用手動關閉 terminal 視窗了。


"""
#######################################