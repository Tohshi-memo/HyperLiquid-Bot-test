# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-25T06:22:15.861303+00:00`
- Price records: `672`
- Market context records: `1817`
- Flow alert records: `7127`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `4474`

## Conditions

- `news_risk_high`: News Risk is elevated.
- `macro_risk_high`: Macro Risk is elevated.
- `risk_on_high`: Risk-On score is elevated.
- `market_context_high`: Market Context is supportive.
- `polymarket_volume_spike`: Polymarket 24h volume z-score is elevated.
- `flow_alert_high`: Flow Alert score is elevated.
- `news_and_polymarket`: News Risk and Polymarket volume spike happen together.
- `risk_on_and_context`: Risk-On and Market Context are both supportive.
- `macro_and_flow`: Macro Risk and Flow Alert are elevated together.

## Top Patterns

- `market_context_high->crypto_alt_4h` score `6.9952` n `184` status `ready` deltaP `22.7996` edge `0.5454` maxDD `-5.1574`
- `market_context_high->metal_24h` score `6.8596` n `178` status `ready` deltaP `27.5905` edge `0.6303` maxDD `-12.7414`
- `market_context_high->crypto_major_4h` score `6.5679` n `184` status `ready` deltaP `26.7498` edge `0.4936` maxDD `-4.9684`
- `news_risk_high->commodity_4h` score `6.5641` n `30` status `ready` deltaP `29.563` edge `0.4154` maxDD `-3.5713`
- `market_context_high->unknown_4h` score `4.7187` n `184` status `ready` deltaP `17.5372` edge `0.4787` maxDD `-9.8581`
- `market_context_high->index_24h` score `3.6502` n `178` status `ready` deltaP `17.8683` edge `0.3079` maxDD `-4.1604`
- `news_risk_high->commodity_1h` score `3.3309` n `30` status `ready` deltaP `25.3194` edge `0.1405` maxDD `-1.2043`
- `market_context_high->equity_4h` score `2.9916` n `184` status `ready` deltaP `15.7874` edge `0.2535` maxDD `-5.0894`
- `market_context_high->equity_24h` score `2.7128` n `178` status `ready` deltaP `17.9716` edge `0.5961` maxDD `-33.1875`
- `market_context_high->unknown_24h` score `2.4382` n `178` status `ready` deltaP `13.5183` edge `0.6451` maxDD `-35.8966`
- `news_risk_high->fx_4h` score `0.9058` n `30` status `ready` deltaP `21.6362` edge `-0.0009` maxDD `-0.1774`
- `market_context_high->index_4h` score `0.8218` n `184` status `ready` deltaP `11.5324` edge `0.1005` maxDD `-3.7119`
- `market_context_high->crypto_major_1h` score `0.4398` n `192` status `ready` deltaP `6.1596` edge `0.0942` maxDD `-3.2225`
- `market_context_high->crypto_alt_1h` score `0.3771` n `192` status `ready` deltaP `6.6742` edge `0.0983` maxDD `-4.9097`
- `news_risk_high->unknown_4h` score `0.3649` n `30` status `ready` deltaP `9.6748` edge `0.0546` maxDD `-2.7857`
- `market_context_high->equity_1h` score `-0.1659` n `192` status `ready` deltaP `3.8174` edge `0.0401` maxDD `-2.6836`
- `market_context_high->crypto_major_24h` score `-0.2448` n `178` status `ready` deltaP `17.8176` edge `0.7194` maxDD `-62.3533`
- `market_context_high->fx_24h` score `-0.2971` n `178` status `ready` deltaP `10.5669` edge `0.0097` maxDD `-1.3925`
- `market_context_high->index_1h` score `-0.3986` n `192` status `ready` deltaP `0.0406` edge `0.0118` maxDD `-1.7205`
- `news_risk_high->unknown_1h` score `-0.4146` n `30` status `ready` deltaP `16.8563` edge `-0.1183` maxDD `-2.1115`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
