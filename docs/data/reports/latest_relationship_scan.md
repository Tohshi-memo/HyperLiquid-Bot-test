# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-27T11:07:24.517050+00:00`
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

- `news_risk_high->unknown_24h` score `51.0641` n `50` status `ready` deltaP `11.5717` edge `4.1782` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `18.3468` n `50` status `ready` deltaP `37.6235` edge `1.3222` maxDD `-2.8629`
- `news_risk_high->unknown_4h` score `12.64` n `50` status `ready` deltaP `26.4695` edge `0.8868` maxDD `-0.1279`
- `news_risk_high->equity_24h` score `4.7605` n `50` status `ready` deltaP `25.6235` edge `0.3187` maxDD `-4.7584`
- `news_risk_high->fx_4h` score `4.0612` n `50` status `ready` deltaP `47.3354` edge `0.0319` maxDD `-0.0559`
- `news_risk_high->metal_24h` score `4.0296` n `50` status `ready` deltaP `43.2504` edge `0.0517` maxDD `-0.0053`
- `market_context_high->unknown_4h` score `3.6586` n `128` status `ready` deltaP `24.657` edge `0.1812` maxDD `-0.5894`
- `news_risk_high->unknown_1h` score `2.9023` n `50` status `ready` deltaP `16.5269` edge `0.1673` maxDD `-0.8495`
- `news_risk_high->index_24h` score `2.7452` n `50` status `ready` deltaP `30.487` edge `0.0406` maxDD `-0.2064`
- `market_context_high->unknown_24h` score `1.7762` n `127` status `ready` deltaP `5.2725` edge `0.1861` maxDD `-3.1917`
- `news_risk_high->fx_1h` score `1.5456` n `50` status `ready` deltaP `20.6527` edge `0.0081` maxDD `-0.0257`
- `market_context_high->unknown_1h` score `1.3421` n `137` status `ready` deltaP `11.7094` edge `0.0788` maxDD `-1.6015`
- `news_risk_high->equity_1h` score `1.2014` n `50` status `ready` deltaP `16.8144` edge `0.0159` maxDD `-0.2301`
- `news_risk_high->equity_4h` score `0.6655` n `50` status `ready` deltaP `17.9207` edge `0.0123` maxDD `-2.105`
- `news_risk_high->commodity_1h` score `0.5837` n `50` status `ready` deltaP `15.3473` edge `0.0038` maxDD `-0.5024`
- `news_risk_high->index_1h` score `0.1592` n `50` status `ready` deltaP `7.9581` edge `0.0013` maxDD `-0.0486`
- `news_risk_high->metal_1h` score `0.1131` n `50` status `ready` deltaP `5.7006` edge `-0.0009` maxDD `-0.1413`
- `news_risk_high->index_4h` score `-0.1403` n `50` status `ready` deltaP `4.4939` edge `-0.002` maxDD `-0.1719`
- `news_risk_high->metal_4h` score `-0.2106` n `50` status `ready` deltaP `6.5488` edge `-0.0081` maxDD `-0.249`
- `market_context_high->fx_1h` score `-0.517` n `137` status `ready` deltaP `1.2074` edge `-0.0011` maxDD `-0.8587`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
