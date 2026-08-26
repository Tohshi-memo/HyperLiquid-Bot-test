# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-26T10:01:57.554892+00:00`
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

- `news_risk_high->unknown_24h` score `45.7134` n `52` status `ready` deltaP `11.6319` edge `3.7319` maxDD `0.0`
- `news_risk_high->unknown_4h` score `11.8032` n `53` status `ready` deltaP `23.1506` edge `0.8392` maxDD `-0.1281`
- `news_risk_high->crypto_alt_24h` score `9.2916` n `52` status `ready` deltaP `31.4102` edge `0.5874` maxDD `-1.4667`
- `news_risk_high->equity_24h` score `7.053` n `52` status `ready` deltaP `29.5406` edge `0.4839` maxDD `-4.7801`
- `news_risk_high->index_24h` score `4.1304` n `52` status `ready` deltaP `41.0524` edge `0.0857` maxDD `-0.2147`
- `news_risk_high->fx_4h` score `2.7829` n `53` status `ready` deltaP `33.5913` edge `0.0214` maxDD `-0.0746`
- `news_risk_high->unknown_1h` score `2.7471` n `53` status `ready` deltaP `15.4135` edge `0.1617` maxDD `-0.8426`
- `market_context_high->unknown_4h` score `2.4363` n `136` status `ready` deltaP `21.4581` edge `0.1008` maxDD `-0.5994`
- `news_risk_high->equity_4h` score `1.8311` n `53` status `ready` deltaP `20.3463` edge `0.094` maxDD `-2.164`
- `news_risk_high->metal_24h` score `1.6467` n `52` status `ready` deltaP `29.1533` edge `-0.0529` maxDD `-0.0053`
- `market_context_high->unknown_1h` score `1.0654` n `136` status `ready` deltaP `11.4873` edge `0.0571` maxDD `-1.5916`
- `news_risk_high->fx_1h` score `1.053` n `53` status `ready` deltaP `14.8712` edge `0.0056` maxDD `-0.0257`
- `news_risk_high->commodity_1h` score `0.5146` n `53` status `ready` deltaP `11.575` edge `-0.003` maxDD `-0.5024`
- `news_risk_high->equity_1h` score `0.4302` n `53` status `ready` deltaP `12.7754` edge `0.0064` maxDD `-0.9128`
- `news_risk_high->index_4h` score `0.1571` n `53` status `ready` deltaP `6.8138` edge `0.0074` maxDD `-0.1788`
- `news_risk_high->index_1h` score `-0.0721` n `53` status `ready` deltaP `3.8499` edge `0.0004` maxDD `-0.1583`
- `news_risk_high->metal_1h` score `-0.4055` n `53` status `ready` deltaP `-0.0141` edge `-0.0111` maxDD `-0.1413`
- `market_context_high->fx_1h` score `-0.4543` n `136` status `ready` deltaP `2.4128` edge `-0.0011` maxDD `-0.8587`
- `news_risk_high->metal_4h` score `-0.4682` n `53` status `ready` deltaP `4.8147` edge `-0.018` maxDD `-0.249`
- `news_risk_high->commodity_4h` score `-0.963` n `53` status `ready` deltaP `-0.906` edge `0.0059` maxDD `-1.1986`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
