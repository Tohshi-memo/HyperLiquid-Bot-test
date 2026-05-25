# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-25T06:37:18.628017+00:00`
- Price records: `672`
- Market context records: `1818`
- Flow alert records: `7130`
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

- `market_context_high->crypto_alt_4h` score `6.9875` n `185` status `ready` deltaP `22.7794` edge `0.5449` maxDD `-5.1574`
- `market_context_high->metal_24h` score `6.8656` n `178` status `ready` deltaP `27.5905` edge `0.6308` maxDD `-12.7414`
- `news_risk_high->commodity_4h` score `6.5665` n `30` status `ready` deltaP `29.563` edge `0.4156` maxDD `-3.5713`
- `market_context_high->crypto_major_4h` score `6.5474` n `185` status `ready` deltaP `26.6883` edge `0.4923` maxDD `-4.9684`
- `market_context_high->unknown_4h` score `4.7177` n `185` status `ready` deltaP `17.5404` edge `0.4786` maxDD `-9.8581`
- `market_context_high->index_24h` score `3.643` n `178` status `ready` deltaP `17.8683` edge `0.3073` maxDD `-4.1604`
- `news_risk_high->commodity_1h` score `3.3117` n `30` status `ready` deltaP `25.1697` edge `0.1399` maxDD `-1.2043`
- `market_context_high->equity_4h` score `3.001` n `185` status `ready` deltaP `15.9196` edge `0.2534` maxDD `-5.0894`
- `market_context_high->equity_24h` score `2.6701` n `178` status `ready` deltaP `17.798` edge `0.5937` maxDD `-33.1875`
- `market_context_high->unknown_24h` score `2.4677` n `178` status `ready` deltaP `13.6919` edge `0.6464` maxDD `-35.8966`
- `news_risk_high->fx_4h` score `0.9058` n `30` status `ready` deltaP `21.6362` edge `-0.0009` maxDD `-0.1774`
- `market_context_high->index_4h` score `0.8369` n `185` status `ready` deltaP `11.7057` edge `0.1006` maxDD `-3.7119`
- `market_context_high->crypto_major_1h` score `0.4254` n `192` status `ready` deltaP `6.0099` edge `0.094` maxDD `-3.2225`
- `market_context_high->crypto_alt_1h` score `0.3603` n `192` status `ready` deltaP `6.5245` edge `0.0979` maxDD `-4.9097`
- `news_risk_high->unknown_4h` score `0.3382` n `30` status `ready` deltaP `9.5223` edge `0.0522` maxDD `-2.7857`
- `market_context_high->equity_1h` score `-0.148` n `192` status `ready` deltaP `3.9671` edge `0.0406` maxDD `-2.6836`
- `market_context_high->crypto_major_24h` score `-0.2388` n `178` status `ready` deltaP `17.8176` edge `0.7199` maxDD `-62.3533`
- `market_context_high->fx_24h` score `-0.2772` n `178` status `ready` deltaP `10.7405` edge `0.0102` maxDD `-1.3925`
- `market_context_high->index_1h` score `-0.3978` n `192` status `ready` deltaP `0.0406` edge `0.0119` maxDD `-1.7205`
- `news_risk_high->unknown_1h` score `-0.4169` n `30` status `ready` deltaP `16.8563` edge `-0.1186` maxDD `-2.1115`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
