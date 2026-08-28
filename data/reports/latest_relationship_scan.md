# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-28T04:07:25.089487+00:00`
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

- `news_risk_high->unknown_24h` score `52.6662` n `50` status `ready` deltaP `11.6319` edge `4.3113` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `26.7606` n `50` status `ready` deltaP `37.8403` edge `2.0219` maxDD `-2.8629`
- `news_risk_high->unknown_4h` score `12.642` n `50` status `ready` deltaP `24.3354` edge `0.9012` maxDD `-0.1279`
- `news_risk_high->metal_24h` score `5.3033` n `50` status `ready` deltaP `48.5208` edge `0.1227` maxDD `-0.0053`
- `news_risk_high->equity_24h` score `5.1767` n `50` status `ready` deltaP `28.9653` edge `0.3311` maxDD `-4.7584`
- `news_risk_high->fx_4h` score `3.8689` n `50` status `ready` deltaP `45.2012` edge `0.0301` maxDD `-0.0559`
- `market_context_high->unknown_24h` score `3.2418` n `128` status `ready` deltaP `5.3819` edge `0.3075` maxDD `-3.1917`
- `news_risk_high->unknown_1h` score `2.9792` n `50` status `ready` deltaP `16.0778` edge `0.1767` maxDD `-0.8495`
- `news_risk_high->index_24h` score `2.7763` n `50` status `ready` deltaP `31.0556` edge `0.0394` maxDD `-0.2064`
- `market_context_high->unknown_4h` score `2.199` n `148` status `ready` deltaP `17.4976` edge `0.1073` maxDD `-0.5894`
- `news_risk_high->fx_1h` score `1.5767` n `50` status `ready` deltaP `21.1018` edge `0.0077` maxDD `-0.0257`
- `news_risk_high->equity_1h` score `1.344` n `50` status `ready` deltaP `18.1617` edge `0.0188` maxDD `-0.2301`
- `news_risk_high->equity_4h` score `1.2368` n `50` status `ready` deltaP `20.8171` edge `0.0406` maxDD `-2.105`
- `market_context_high->unknown_1h` score `0.8558` n `148` status `ready` deltaP `8.3751` edge `0.0605` maxDD `-1.6015`
- `news_risk_high->commodity_1h` score `0.5331` n `50` status `ready` deltaP `14.5988` edge `0.0023` maxDD `-0.5024`
- `news_risk_high->metal_4h` score `0.2554` n `50` status `ready` deltaP `10.6646` edge `0.0033` maxDD `-0.249`
- `news_risk_high->index_1h` score `0.1639` n `50` status `ready` deltaP `8.1078` edge `0.0009` maxDD `-0.0486`
- `news_risk_high->metal_1h` score `0.1575` n `50` status `ready` deltaP `6.2994` edge `0.0008` maxDD `-0.1413`
- `news_risk_high->index_4h` score `-0.0747` n `50` status `ready` deltaP `5.1037` edge `-0.0006` maxDD `-0.1719`
- `market_context_high->metal_24h` score `-0.0851` n `128` status `ready` deltaP `13.0208` edge `0.0704` maxDD `-3.8102`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
