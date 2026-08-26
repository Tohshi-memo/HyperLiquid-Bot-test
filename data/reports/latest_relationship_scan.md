# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-26T09:52:28.229629+00:00`
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

- `news_risk_high->unknown_24h` score `45.6774` n `52` status `ready` deltaP `11.6319` edge `3.7289` maxDD `0.0`
- `news_risk_high->unknown_4h` score `11.7802` n `53` status `ready` deltaP `22.9981` edge `0.8383` maxDD `-0.1281`
- `news_risk_high->crypto_alt_24h` score `9.0749` n `52` status `ready` deltaP `31.2366` edge `0.5705` maxDD `-1.4667`
- `news_risk_high->equity_24h` score `7.0386` n `52` status `ready` deltaP `29.5406` edge `0.4827` maxDD `-4.7801`
- `news_risk_high->index_24h` score `4.1129` n `52` status `ready` deltaP `40.8788` edge `0.0854` maxDD `-0.2147`
- `news_risk_high->fx_4h` score `2.7695` n `53` status `ready` deltaP `33.4388` edge `0.0213` maxDD `-0.0746`
- `news_risk_high->unknown_1h` score `2.7291` n `53` status `ready` deltaP `15.2638` edge `0.1612` maxDD `-0.8426`
- `market_context_high->unknown_4h` score `2.4133` n `136` status `ready` deltaP `21.3056` edge `0.0999` maxDD `-0.5994`
- `news_risk_high->equity_4h` score `1.8455` n `53` status `ready` deltaP `20.3463` edge `0.0952` maxDD `-2.164`
- `news_risk_high->metal_24h` score `1.6299` n `52` status `ready` deltaP `29.1533` edge `-0.0543` maxDD `-0.0053`
- `news_risk_high->fx_1h` score `1.065` n `53` status `ready` deltaP `15.0209` edge `0.0056` maxDD `-0.0257`
- `market_context_high->unknown_1h` score `1.0475` n `136` status `ready` deltaP `11.3376` edge `0.0566` maxDD `-1.5916`
- `news_risk_high->commodity_1h` score `0.5158` n `53` status `ready` deltaP `11.575` edge `-0.0029` maxDD `-0.5024`
- `news_risk_high->equity_1h` score `0.4263` n `53` status `ready` deltaP `12.7754` edge `0.0059` maxDD `-0.9128`
- `news_risk_high->index_4h` score `0.1449` n `53` status `ready` deltaP `6.6613` edge `0.0074` maxDD `-0.1788`
- `news_risk_high->index_1h` score `-0.0807` n `53` status `ready` deltaP `3.7002` edge `0.0003` maxDD `-0.1583`
- `news_risk_high->metal_1h` score `-0.4199` n `53` status `ready` deltaP `-0.1638` edge `-0.0113` maxDD `-0.1413`
- `market_context_high->fx_1h` score `-0.4466` n `136` status `ready` deltaP `2.5625` edge `-0.0011` maxDD `-0.8587`
- `news_risk_high->metal_4h` score `-0.496` n `53` status `ready` deltaP `4.6623` edge `-0.0193` maxDD `-0.249`
- `news_risk_high->commodity_4h` score `-0.9724` n `53` status `ready` deltaP `-1.0585` edge `0.0057` maxDD `-1.1986`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
