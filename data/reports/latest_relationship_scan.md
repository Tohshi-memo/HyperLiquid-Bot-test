# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-28T02:22:24.641715+00:00`
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

- `news_risk_high->unknown_24h` score `52.5378` n `50` status `ready` deltaP `11.6319` edge `4.3006` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `25.3338` n `50` status `ready` deltaP `37.8403` edge `1.903` maxDD `-2.8629`
- `news_risk_high->unknown_4h` score `12.704` n `50` status `ready` deltaP `24.9451` edge `0.9023` maxDD `-0.1279`
- `news_risk_high->metal_24h` score `5.1521` n `50` status `ready` deltaP `47.3056` edge `0.1182` maxDD `-0.0053`
- `news_risk_high->equity_24h` score `5.0537` n `50` status `ready` deltaP `27.9236` edge `0.3278` maxDD `-4.7584`
- `news_risk_high->fx_4h` score `3.7715` n `50` status `ready` deltaP `44.1341` edge `0.0291` maxDD `-0.0559`
- `market_context_high->unknown_24h` score `3.1134` n `128` status `ready` deltaP `5.3819` edge `0.2968` maxDD `-3.1917`
- `news_risk_high->unknown_1h` score `2.9144` n `50` status `ready` deltaP `15.9281` edge `0.1723` maxDD `-0.8495`
- `news_risk_high->index_24h` score `2.8493` n `50` status `ready` deltaP `31.9236` edge `0.0397` maxDD `-0.2064`
- `market_context_high->unknown_4h` score `2.261` n `148` status `ready` deltaP `18.1073` edge `0.1084` maxDD `-0.5894`
- `news_risk_high->fx_1h` score `1.5264` n `50` status `ready` deltaP `20.503` edge `0.0075` maxDD `-0.0257`
- `news_risk_high->equity_1h` score `1.3284` n `50` status `ready` deltaP `18.012` edge `0.0185` maxDD `-0.2301`
- `news_risk_high->equity_4h` score `1.26` n `50` status `ready` deltaP `21.122` edge `0.0405` maxDD `-2.105`
- `market_context_high->unknown_1h` score `0.791` n `148` status `ready` deltaP `8.2254` edge `0.0561` maxDD `-1.6015`
- `news_risk_high->commodity_1h` score `0.5697` n `50` status `ready` deltaP `15.1976` edge `0.003` maxDD `-0.5024`
- `news_risk_high->index_1h` score `0.1553` n `50` status `ready` deltaP `7.9581` edge `0.0008` maxDD `-0.0486`
- `news_risk_high->metal_1h` score `0.149` n `50` status `ready` deltaP `6.1497` edge `0.0007` maxDD `-0.1413`
- `news_risk_high->metal_4h` score `0.1413` n `50` status `ready` deltaP `9.5976` edge `0.0009` maxDD `-0.249`
- `news_risk_high->index_4h` score `-0.0699` n `50` status `ready` deltaP `5.1037` edge `-0.0002` maxDD `-0.1719`
- `market_context_high->metal_24h` score `-0.2363` n `128` status `ready` deltaP `11.8056` edge `0.0659` maxDD `-3.8102`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
