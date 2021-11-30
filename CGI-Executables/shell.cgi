#!/bin/bash

echo "Content-type: text/html;charset=utf-8"
echo ""
echo "<html><title>Shell CGI Script</title><body>"
username=`who`
echo "<h3>Hello, CGI form Shell Script</h3>"
echo "<p>$username</p>"
echo "<p>on `/bin/hostname`</p>"
echo "<br>"
echo "以下是環境變量："
echo "<pre>"
echo "服務器" SERVER_SOFTWARE = $SERVER_SOFTWARE
echo "服務器主機名" SERVER_NAME = $SERVER_NAME
echo "CGI版本" GATEWAY_INTERFACE = $GATEWAY_INTERFACE
echo "通信使用的協議" SERVER_PROTOCOL = $SERVER_PROTOCOL
echo "服務器的端口號" SERVER_PORT = $SERVER_PORT
echo "HTTP 請求方法" REQUEST_METHOD = $REQUEST_METHOD
echo "HTTP定義的瀏覽器能夠接受的數據類型" HTTP_ACCEPT = $HTTP_ACCEPT 
echo "當前運行的腳本" SCRIPT_NAME = $SCRIPT_NAME
echo "url 的 QUERY_STRING" QUERY_STRING = $QUERY_STRING
echo "客戶端的ip" REMOTE_ADDR = $REMOTE_ADDR
echo "</pre>"
echo "<br>"
echo "以下是伺服器狀態："
echo '<pre>'
df -Hl | {
  read keys;
  keys="${keys%% on}";
  while read ${keys//%}; do
    echo "`basename "$Mounted"` - $Used/$Size ($Capacity)";
  done
}
echo '<pre>'
echo "</body></html>"

