# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-29T17:37:30.887114+00:00`
- Price records: `672`
- Market context records: `5166`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `5650`

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

- `market_context_high->unknown_24h` score `29.2989` n `65` status `ready` deltaP `33.0823` edge `2.24` maxDD `-0.8515`
- `market_context_high->unknown_4h` score `5.86` n `141` status `ready` deltaP `20.0474` edge `0.4569` maxDD `-5.5109`
- `market_context_high->crypto_alt_24h` score `4.7817` n `65` status `ready` deltaP `20.016` edge `0.8183` maxDD `-23.4292`
- `market_context_high->crypto_major_24h` score `4.7044` n `65` status `ready` deltaP `18.1784` edge `0.8481` maxDD `-22.6266`
- `market_context_high->crypto_alt_4h` score `4.6749` n `141` status `ready` deltaP `14.8039` edge `0.4508` maxDD `-9.46`
- `market_context_high->crypto_major_4h` score `3.9783` n `141` status `ready` deltaP `13.6904` edge `0.4695` maxDD `-14.0065`
- `market_context_high->unknown_1h` score `3.7821` n `149` status `ready` deltaP `9.7989` edge `0.314` maxDD `-2.7986`
- `market_context_high->commodity_24h` score `0.9331` n `65` status `ready` deltaP `18.3333` edge `0.1417` maxDD `-6.2099`
- `market_context_high->crypto_major_1h` score `0.8008` n `149` status `ready` deltaP `8.0376` edge `0.1377` maxDD `-6.9639`
- `market_context_high->crypto_alt_1h` score `0.7614` n `149` status `ready` deltaP `5.2656` edge `0.1245` maxDD `-5.0257`
- `market_context_high->equity_4h` score `0.6227` n `141` status `ready` deltaP `8.4079` edge `0.1597` maxDD `-7.4425`
- `market_context_high->metal_24h` score `0.508` n `65` status `ready` deltaP `-0.2297` edge `0.2226` maxDD `-6.8086`
- `market_context_high->equity_1h` score `0.3043` n `149` status `ready` deltaP `7.7231` edge `0.0704` maxDD `-5.0555`
- `market_context_high->index_1h` score `-0.0489` n `149` status `ready` deltaP `4.8889` edge `0.0137` maxDD `-1.0296`
- `market_context_high->metal_1h` score `-0.0944` n `149` status `ready` deltaP `4.8266` edge `0.0149` maxDD `-2.0682`
- `market_context_high->fx_1h` score `-0.1952` n `149` status `ready` deltaP `2.9428` edge `0.0006` maxDD `-0.6194`
- `market_context_high->index_4h` score `-0.4026` n `141` status `ready` deltaP `4.6229` edge `0.0293` maxDD `-2.9391`
- `market_context_high->fx_4h` score `-0.4626` n `141` status `ready` deltaP `5.4586` edge `0.0077` maxDD `-1.6047`
- `market_context_high->fx_24h` score `-0.4684` n `65` status `ready` deltaP `6.4797` edge `0.0073` maxDD `-0.8294`
- `market_context_high->commodity_1h` score `-0.5527` n `149` status `ready` deltaP `1.3061` edge `0.0013` maxDD `-2.4692`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
