# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-28T02:52:24.716045+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11831`

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

- `news_risk_high->unknown_24h` score `52.5762` n `50` status `ready` deltaP `11.6319` edge `4.3038` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `25.6806` n `50` status `ready` deltaP `37.8403` edge `1.9319` maxDD `-2.8629`
- `news_risk_high->unknown_4h` score `12.7064` n `50` status `ready` deltaP `24.9451` edge `0.9025` maxDD `-0.1279`
- `news_risk_high->metal_24h` score `5.1978` n `50` status `ready` deltaP `47.6528` edge `0.1197` maxDD `-0.0053`
- `news_risk_high->equity_24h` score `5.0796` n `50` status `ready` deltaP `28.0972` edge `0.3288` maxDD `-4.7584`
- `news_risk_high->fx_4h` score `3.7983` n `50` status `ready` deltaP `44.439` edge `0.0293` maxDD `-0.0559`
- `market_context_high->unknown_24h` score `3.1518` n `128` status `ready` deltaP `5.3819` edge `0.3` maxDD `-3.1917`
- `news_risk_high->unknown_1h` score `2.9072` n `50` status `ready` deltaP `15.7784` edge `0.1727` maxDD `-0.8495`
- `news_risk_high->index_24h` score `2.8493` n `50` status `ready` deltaP `31.9236` edge `0.0397` maxDD `-0.2064`
- `market_context_high->unknown_4h` score `2.2634` n `148` status `ready` deltaP `18.1073` edge `0.1086` maxDD `-0.5894`
- `news_risk_high->fx_1h` score `1.5264` n `50` status `ready` deltaP `20.503` edge `0.0075` maxDD `-0.0257`
- `news_risk_high->equity_1h` score `1.3512` n `50` status `ready` deltaP `18.1617` edge `0.0194` maxDD `-0.2301`
- `news_risk_high->equity_4h` score `1.26` n `50` status `ready` deltaP `21.122` edge `0.0405` maxDD `-2.105`
- `market_context_high->unknown_1h` score `0.7838` n `148` status `ready` deltaP `8.0757` edge `0.0565` maxDD `-1.6015`
- `news_risk_high->commodity_1h` score `0.5518` n `50` status `ready` deltaP `14.8982` edge `0.0027` maxDD `-0.5024`
- `news_risk_high->metal_4h` score `0.1752` n `50` status `ready` deltaP `9.9024` edge `0.0017` maxDD `-0.249`
- `news_risk_high->index_1h` score `0.1561` n `50` status `ready` deltaP `7.9581` edge `0.0009` maxDD `-0.0486`
- `news_risk_high->metal_1h` score `0.1513` n `50` status `ready` deltaP `6.1497` edge `0.001` maxDD `-0.1413`
- `news_risk_high->index_4h` score `-0.0711` n `50` status `ready` deltaP `5.1037` edge `-0.0003` maxDD `-0.1719`
- `market_context_high->metal_24h` score `-0.1905` n `128` status `ready` deltaP `12.1528` edge `0.0674` maxDD `-3.8102`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
