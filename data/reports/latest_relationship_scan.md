# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-24T14:22:31.010392+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `10084`

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

- `market_context_high->unknown_1h` score `88.8487` n `47` status `ready` deltaP `10.116` edge `7.3437` maxDD `-0.2334`
- `market_context_high->crypto_major_24h` score `42.4208` n `47` status `ready` deltaP `29.9017` edge `3.375` maxDD `-2.4756`
- `market_context_high->crypto_alt_24h` score `28.402` n `47` status `ready` deltaP `24.782` edge `2.2396` maxDD `-2.7051`
- `market_context_high->equity_24h` score `23.9493` n `47` status `ready` deltaP `27.4712` edge `1.8482` maxDD `-2.1786`
- `market_context_high->index_24h` score `7.8293` n `47` status `ready` deltaP `34.9364` edge `0.4325` maxDD `-0.3705`
- `news_risk_high->crypto_alt_24h` score `6.9759` n `99` status `ready` deltaP `0.6471` edge `1.2783` maxDD `-49.7699`
- `news_risk_high->crypto_major_24h` score `6.3423` n `99` status `ready` deltaP `2.9514` edge `1.6977` maxDD `-63.6743`
- `market_context_high->metal_24h` score `3.5315` n `47` status `ready` deltaP `30.5445` edge `0.1145` maxDD `-0.2401`
- `market_context_high->index_4h` score `3.07` n `47` status `ready` deltaP `34.941` edge `0.0383` maxDD `-0.2323`
- `news_risk_high->crypto_alt_1h` score `2.9194` n `120` status `ready` deltaP `13.518` edge `0.2022` maxDD `-1.5895`
- `market_context_high->equity_4h` score `2.6491` n `47` status `ready` deltaP `17.7542` edge `0.1442` maxDD `-1.3444`
- `news_risk_high->crypto_major_1h` score `2.3662` n `120` status `ready` deltaP `15.7635` edge `0.1356` maxDD `-1.8141`
- `news_risk_high->fx_4h` score `1.8463` n `110` status `ready` deltaP `26.408` edge `0.0414` maxDD `-0.421`
- `news_risk_high->fx_24h` score `1.297` n `99` status `ready` deltaP `30.2399` edge `0.1278` maxDD `-1.7159`
- `news_risk_high->commodity_24h` score `1.1398` n `99` status `ready` deltaP `16.5562` edge `0.1025` maxDD `-2.431`
- `news_risk_high->metal_24h` score `1.1392` n `99` status `ready` deltaP `24.7633` edge `0.1258` maxDD `-7.2536`
- `market_context_high->index_1h` score `0.9643` n `47` status `ready` deltaP `14.6101` edge `0.0108` maxDD `-0.2275`
- `market_context_high->equity_1h` score `0.8983` n `47` status `ready` deltaP `10.8676` edge `0.0427` maxDD `-1.5564`
- `news_risk_high->crypto_major_4h` score `0.5095` n `110` status `ready` deltaP `13.1069` edge `0.1911` maxDD `-13.719`
- `news_risk_high->metal_1h` score `0.477` n `120` status `ready` deltaP `15.2595` edge `0.0171` maxDD `-0.6142`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
