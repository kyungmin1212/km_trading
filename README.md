# km_trading
- tradingview의 webhook 기능을 이용한 자동매매 프로젝트

---

# 사용법
- 가상환경 세팅

- pip install -r requirements.txt

- .env 파일을 생성하고 다음 내용 작성
    - BINANCE_KEY
    - BINANCE_SECRET
    - DISCORD_WEBHOOK_URL

- 포트포워딩을 통해 반드시 80번 포트에서 내가 지정한 포트인 8000번 포트를 열어주어야함.

- 서버 실행
    ```
    python main.py
    ```

- tradingview pinescirpt 예시코드
    - 정확한 자동매매를 위해서는 start_time의 시작시간을 반드시 현재 시간보다 늦게 세팅해두어야함.
    ```
    //@version=5
    //@strategy_alert_message {{strategy.order.alert_message}}

    alert_message() =>
        json =  '{'
                + str.format(
                ' 
                        "exchange" : "{0}",
                        "ticker" : "{1}",
                        "side" : "{2}",
                        "amount" : "{3}"
                    ', syminfo.prefix, syminfo.ticker, "{{strategy.order.action}}", "{{strategy.order.contracts}}")
                +'}'

        json

    strategy("내 전략", overlay=true,initial_capital = 100,  default_qty_type = strategy.percent_of_equity, default_qty_value= 10)

    start_time = input.time(timestamp("2023-03-24T00:00:00+09:00"),title = "자동매매 시작")
    end_time = input.time(timestamp("2099-01-01T00:00:00+09:00"),title = "자동매매 종료")

    if (time>=start_time) and (time<=end_time)
        strategy.entry("롱", strategy.long, alert_message = alert_message())
    ```

- alert 만들기
    - 설정 -> 조건 -> '내 전략'
    - 알림 -> 웹훅 URL 체크 ->  http:// 내 ip/order

---

# Pine Scripts 정리

- https://kyungmin961212.notion.site/Pine-Script-f8ebe8f5cda245c29bfb6c3b6c6d3c33

---

# 버전 정보
## v1.0 (2022-03-24)
- 초기 버전 출시
- 바이낸스에서 시장가 거래 지원 (One-way Mode만 지원)
