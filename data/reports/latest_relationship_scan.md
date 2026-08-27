# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-27T10:52:21.907547+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `14748`

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

- `news_risk_high->unknown_24h` score `51.0209` n `50` status `ready` deltaP `11.5717` edge `4.1746` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `18.2232` n `50` status `ready` deltaP `37.6235` edge `1.3119` maxDD `-2.8629`
- `news_risk_high->unknown_4h` score `12.6388` n `50` status `ready` deltaP `26.4695` edge `0.8867` maxDD `-0.1279`
- `news_risk_high->equity_24h` score `4.7893` n `50` status `ready` deltaP `25.6235` edge `0.3211` maxDD `-4.7584`
- `news_risk_high->fx_4h` score `4.0612` n `50` status `ready` deltaP `47.3354` edge `0.0319` maxDD `-0.0559`
- `news_risk_high->metal_24h` score `3.9918` n `50` status `ready` deltaP `43.0777` edge `0.0497` maxDD `-0.0053`
- `market_context_high->unknown_4h` score `3.6226` n `129` status `ready` deltaP `24.7176` edge `0.1778` maxDD `-0.5894`
- `news_risk_high->unknown_1h` score `2.9023` n `50` status `ready` deltaP `16.5269` edge `0.1673` maxDD `-0.8495`
- `news_risk_high->index_24h` score `2.7662` n `50` status `ready` deltaP `30.6598` edge `0.0412` maxDD `-0.2064`
- `market_context_high->unknown_24h` score `1.7622` n `128` status `ready` deltaP `5.3217` edge `0.1846` maxDD `-3.1917`
- `news_risk_high->fx_1h` score `1.5336` n `50` status `ready` deltaP `20.503` edge `0.0081` maxDD `-0.0257`
- `market_context_high->unknown_1h` score `1.3409` n `137` status `ready` deltaP `11.7094` edge `0.0787` maxDD `-1.6015`
- `news_risk_high->equity_1h` score `1.2086` n `50` status `ready` deltaP `16.8144` edge `0.0165` maxDD `-0.2301`
- `news_risk_high->equity_4h` score `0.7041` n `50` status `ready` deltaP `18.0732` edge `0.0145` maxDD `-2.105`
- `news_risk_high->commodity_1h` score `0.5752` n `50` status `ready` deltaP `15.1976` edge `0.0037` maxDD `-0.5024`
- `news_risk_high->index_1h` score `0.1678` n `50` status `ready` deltaP `8.1078` edge `0.0014` maxDD `-0.0486`
- `news_risk_high->metal_1h` score `0.1139` n `50` status `ready` deltaP `5.7006` edge `-0.0008` maxDD `-0.1413`
- `news_risk_high->index_4h` score `-0.1257` n `50` status `ready` deltaP `4.6463` edge `-0.0018` maxDD `-0.1719`
- `news_risk_high->metal_4h` score `-0.2252` n `50` status `ready` deltaP `6.3963` edge `-0.0083` maxDD `-0.249`
- `market_context_high->fx_1h` score `-0.4861` n `137` status `ready` deltaP `1.7877` edge `-0.001` maxDD `-0.8587`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
