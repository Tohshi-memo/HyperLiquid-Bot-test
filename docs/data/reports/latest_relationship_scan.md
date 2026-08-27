# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-27T11:52:32.525445+00:00`
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

- `news_risk_high->unknown_24h` score `51.1841` n `50` status `ready` deltaP `11.5717` edge `4.1882` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `18.7224` n `50` status `ready` deltaP `37.6235` edge `1.3535` maxDD `-2.8629`
- `news_risk_high->unknown_4h` score `12.6484` n `50` status `ready` deltaP `26.4695` edge `0.8875` maxDD `-0.1279`
- `news_risk_high->equity_24h` score `4.6897` n `50` status `ready` deltaP `25.6235` edge `0.3128` maxDD `-4.7584`
- `news_risk_high->metal_24h` score `4.1383` n `50` status `ready` deltaP `43.7686` edge `0.0573` maxDD `-0.0053`
- `news_risk_high->fx_4h` score `4.0612` n `50` status `ready` deltaP `47.3354` edge `0.0319` maxDD `-0.0559`
- `market_context_high->unknown_4h` score `3.5614` n `130` status `ready` deltaP `24.7772` edge `0.1723` maxDD `-0.5894`
- `news_risk_high->unknown_1h` score `2.9419` n `50` status `ready` deltaP `16.8263` edge `0.1686` maxDD `-0.8495`
- `news_risk_high->index_24h` score `2.7008` n `50` status `ready` deltaP `30.1416` edge `0.0392` maxDD `-0.2064`
- `market_context_high->unknown_24h` score `1.7598` n `128` status `ready` deltaP `5.3217` edge `0.1844` maxDD `-3.1917`
- `news_risk_high->fx_1h` score `1.5827` n `50` status `ready` deltaP `21.1018` edge `0.0082` maxDD `-0.0257`
- `market_context_high->unknown_1h` score `1.2175` n `140` status `ready` deltaP `11.112` edge `0.0724` maxDD `-1.6015`
- `news_risk_high->equity_1h` score `1.1714` n `50` status `ready` deltaP `16.8144` edge `0.0134` maxDD `-0.2301`
- `news_risk_high->commodity_1h` score `0.5938` n `50` status `ready` deltaP `15.497` edge `0.0041` maxDD `-0.5024`
- `news_risk_high->equity_4h` score `0.5749` n `50` status `ready` deltaP `17.4634` edge `0.0078` maxDD `-2.105`
- `news_risk_high->index_1h` score `0.1382` n `50` status `ready` deltaP `7.6587` edge `0.0006` maxDD `-0.0486`
- `news_risk_high->metal_1h` score `0.0804` n `50` status `ready` deltaP `5.2515` edge `-0.0021` maxDD `-0.1413`
- `news_risk_high->index_4h` score `-0.1829` n `50` status `ready` deltaP `4.0366` edge `-0.0025` maxDD `-0.1719`
- `news_risk_high->metal_4h` score `-0.1913` n `50` status `ready` deltaP `6.7012` edge `-0.0075` maxDD `-0.249`
- `market_context_high->fx_1h` score `-0.5546` n `140` status `ready` deltaP `0.5304` edge `-0.0014` maxDD `-0.8587`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
