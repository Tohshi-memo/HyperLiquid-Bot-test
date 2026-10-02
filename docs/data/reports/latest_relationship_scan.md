# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-02T23:52:27.575874+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `4818`

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

- `market_context_high->unknown_1h` score `364.0762` n `50` status `ready` deltaP `10.5749` edge `30.2741` maxDD `-0.0597`
- `market_context_high->unknown_4h` score `291.7971` n `50` status `ready` deltaP `10.5183` edge `24.2463` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `16.3888` n `70` status `ready` deltaP `39.2113` edge `1.1313` maxDD `-1.1582`
- `market_context_high->crypto_alt_24h` score `10.6975` n `50` status `ready` deltaP `20.3542` edge `0.9261` maxDD `-11.6271`
- `news_risk_high->equity_24h` score `9.293` n `70` status `ready` deltaP `33.7351` edge `0.598` maxDD `-2.8784`
- `market_context_high->crypto_major_24h` score `9.033` n `50` status `ready` deltaP `31.8264` edge `0.6822` maxDD `-9.3299`
- `market_context_high->crypto_major_4h` score `7.7853` n `50` status `ready` deltaP `19.0671` edge `0.592` maxDD `-3.294`
- `news_risk_high->crypto_alt_4h` score `6.9648` n `110` status `ready` deltaP `27.2561` edge `0.5331` maxDD `-6.4195`
- `market_context_high->crypto_alt_4h` score `6.2427` n `50` status `ready` deltaP `17.2561` edge `0.5341` maxDD `-7.6465`
- `market_context_high->crypto_alt_1h` score `3.2997` n `50` status `ready` deltaP `15.1018` edge `0.2406` maxDD `-3.6376`
- `market_context_high->crypto_major_1h` score `3.0421` n `50` status `ready` deltaP `13.7006` edge `0.2072` maxDD `-2.2692`
- `news_risk_high->equity_4h` score `2.9595` n `110` status `ready` deltaP `24.9584` edge `0.1415` maxDD `-2.9013`
- `news_risk_high->crypto_major_24h` score `2.9007` n `70` status `ready` deltaP `8.3978` edge `0.5445` maxDD `-10.9549`
- `market_context_high->fx_4h` score `2.8031` n `50` status `ready` deltaP `31.3171` edge `0.0383` maxDD `-0.0791`
- `news_risk_high->crypto_major_4h` score `2.5096` n `110` status `ready` deltaP `19.2489` edge `0.3707` maxDD `-8.183`
- `market_context_high->fx_1h` score `1.4591` n `50` status `ready` deltaP `20.491` edge `0.0114` maxDD `-0.113`
- `news_risk_high->metal_24h` score `1.4269` n `70` status `ready` deltaP `14.6528` edge `0.2112` maxDD `-2.0759`
- `market_context_high->equity_24h` score `1.2959` n `50` status `ready` deltaP `6.0208` edge `0.3122` maxDD `-11.8957`
- `news_risk_high->index_24h` score `1.2825` n `70` status `ready` deltaP `16.7262` edge `0.0404` maxDD `-0.2696`
- `news_risk_high->crypto_alt_1h` score `1.2248` n `110` status `ready` deltaP `5.4654` edge `0.1217` maxDD `-2.4854`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
