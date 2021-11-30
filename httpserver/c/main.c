#include "httpd.h"

int main(int c, char** v)
{
    serve_forever("3000");
    return 0;
}

void route()
{
    ROUTE_START()

    ROUTE_GET("/")
    {
        printf("HTTP/1.1 200 OK\r\n\r\n");
        printf("request headers:\r\n\r\n");

        header_t *h = request_headers();

        while (h->name) {
            printf("%s: %s\n", h->name, h->value);
            h++;
        }
    }

    ROUTE_GET("/john")
    {
        printf("HTTP/1.1 200 OK\r\n\r\n");
        printf("<!DOCTYPE html> <html lang='zh-TW'> <head> <meta charset='UTF-8'> <meta name='viewport' content='width=device-width, initial-scale=1.0'> <meta http-equiv='X-UA-Compatible' content='ie=edge'> <title>this is c http server</title> <style> body{ background: cornflowerblue; color: #0b52b8; font-size: 5em; height: 100vh; display: flex; align-content: center; justify-content: center; } div{ height: 200px; cursor: pointer; } #j:hover{ color: red; } </style> </head> <body> <div id='j'>Hello! John</div> </body> </html>");
    }

    ROUTE_GET("/books")
    {
        printf("HTTP/1.1 200 OK\r\n");
        printf("Access-Control-Allow-Origin: *\r\n");
        printf("Content-Type: application/json; charset=utf-8\r\n");
        printf("\r\n");
        printf("[{\"title\":\"xxxx\"},{\"title\":\"yyyyy\"}]");
    }

    ROUTE_POST("/books")
    {
        printf("HTTP/1.1 200 OK\r\n");
        printf("Access-Control-Allow-Origin: *\r\n");
        printf("Content-Type: text/html; charset=utf-8\r\n");
        printf("\r\n");
        printf("{\"respond\":\"ok\"}");
    }

    ROUTE_POST("/")
    {
        printf("HTTP/1.1 200 OK\r\n");
        printf("Access-Control-Allow-Origin: *\r\n");
        printf("Content-Type: text/html; charset=utf-8\r\n");
        printf("\r\n");
        printf("{\"哈哈哈\":\"POST\"}");
    }

    ROUTE("HIT","/")
    {
        printf("HTTP/1.1 200 OK\r\n\r\n");
        printf("Are yor HIT me?");
    }
 
    ROUTE_FUCK("/you")
    {
        printf("HTTP/9.9 404 Shit\r\n\r\n");
        printf("Access-Control-Allow-Origin: *\r\n");
        printf("Content-Type: text/html; charset=utf-8\r\n");
        printf("FUCK YOU TOO.");
    }


  
    ROUTE_END()
}