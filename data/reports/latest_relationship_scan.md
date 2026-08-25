# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-25T11:52:29.003127+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `14760`

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

- `news_risk_high->unknown_24h` score `43.6079` n `51` status `ready` deltaP `2.0833` edge `3.6201` maxDD `0.0`
- `news_risk_high->unknown_4h` score `12.5074` n `52` status `ready` deltaP `23.8977` edge `0.888` maxDD `-0.0695`
- `news_risk_high->equity_24h` score `9.5485` n `51` status `ready` deltaP `35.5495` edge `0.6518` maxDD `-4.7801`
- `news_risk_high->index_24h` score `4.5396` n `51` status `ready` deltaP `44.6078` edge `0.0961` maxDD `-0.2147`
- `news_risk_high->unknown_1h` score `3.0638` n `53` status `ready` deltaP `16.0123` edge `0.1841` maxDD `-0.8426`
- `news_risk_high->fx_4h` score `3.0043` n `52` status `ready` deltaP `35.6239` edge `0.0263` maxDD `-0.0746`
- `news_risk_high->equity_4h` score `2.377` n `52` status `ready` deltaP `22.6548` edge `0.1241` maxDD `-2.164`
- `market_context_high->unknown_4h` score `2.0149` n `133` status `ready` deltaP `20.2251` edge `0.0739` maxDD `-0.5994`
- `news_risk_high->fx_1h` score `1.1273` n `53` status `ready` deltaP `15.6197` edge `0.0068` maxDD `-0.0257`
- `news_risk_high->equity_1h` score `0.6647` n `53` status `ready` deltaP `15.47` edge `0.0185` maxDD `-0.9128`
- `news_risk_high->index_4h` score `0.4414` n `52` status `ready` deltaP `9.7678` edge `0.0114` maxDD `-0.1788`
- `news_risk_high->commodity_1h` score `0.3217` n `53` status `ready` deltaP `9.7786` edge `-0.0071` maxDD `-0.5024`
- `market_context_high->unknown_1h` score `0.0462` n `133` status `ready` deltaP `11.5719` edge `-0.0284` maxDD `-1.5916`
- `news_risk_high->index_1h` score `-0.009` n `53` status `ready` deltaP `4.8978` edge `0.0015` maxDD `-0.1583`
- `news_risk_high->metal_4h` score `-0.2612` n `52` status `ready` deltaP `6.637` edge `-0.0129` maxDD `-0.249`
- `news_risk_high->metal_1h` score `-0.306` n `53` status `ready` deltaP `0.7344` edge `-0.0078` maxDD `-0.1413`
- `market_context_high->fx_1h` score `-0.4584` n `133` status `ready` deltaP `2.1994` edge `-0.0002` maxDD `-0.8587`
- `news_risk_high->metal_24h` score `-0.696` n `51` status `ready` deltaP `21.6503` edge `-0.1981` maxDD `-0.0053`
- `market_context_high->metal_4h` score `-0.7015` n `133` status `ready` deltaP `6.2466` edge `-0.0364` maxDD `-2.4293`
- `market_context_high->index_1h` score `-1.1568` n `133` status `ready` deltaP `-5.4725` edge `-0.0061` maxDD `-1.3054`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
