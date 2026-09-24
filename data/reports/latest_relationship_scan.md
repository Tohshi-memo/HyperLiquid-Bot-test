# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-24T20:07:32.700618+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9717`

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

- `market_context_high->unknown_1h` score `83.7691` n `47` status `ready` deltaP `10.116` edge `6.9204` maxDD `-0.2334`
- `market_context_high->crypto_major_24h` score `45.0497` n `47` status `ready` deltaP `30.4226` edge `3.5906` maxDD `-2.4756`
- `market_context_high->crypto_alt_24h` score `29.9776` n `47` status `ready` deltaP `24.782` edge `2.3709` maxDD `-2.7051`
- `market_context_high->equity_24h` score `24.9305` n `47` status `ready` deltaP `31.2906` edge `1.9045` maxDD `-2.1786`
- `news_risk_high->unknown_1h` score `14.0286` n `111` status `ready` deltaP `-4.5476` edge `1.2238` maxDD `-0.9543`
- `market_context_high->index_24h` score `7.8509` n `47` status `ready` deltaP `34.9364` edge `0.4343` maxDD `-0.3705`
- `market_context_high->metal_24h` score `3.9869` n `47` status `ready` deltaP `34.0167` edge `0.1293` maxDD `-0.2401`
- `news_risk_high->crypto_alt_1h` score `3.5576` n `111` status `ready` deltaP `17.4449` edge `0.2292` maxDD `-1.5895`
- `market_context_high->index_4h` score `2.9145` n `47` status `ready` deltaP `33.4166` edge `0.0355` maxDD `-0.2323`
- `news_risk_high->crypto_major_1h` score `2.7534` n `111` status `ready` deltaP `17.8886` edge `0.1537` maxDD `-1.8141`
- `news_risk_high->crypto_major_4h` score `2.5469` n `106` status `ready` deltaP `16.4692` edge `0.3156` maxDD `-13.719`
- `news_risk_high->crypto_alt_4h` score `2.5465` n `106` status `ready` deltaP `8.8558` edge `0.3983` maxDD `-15.9436`
- `market_context_high->equity_4h` score `2.3697` n `47` status `ready` deltaP `16.992` edge `0.126` maxDD `-1.3444`
- `news_risk_high->commodity_24h` score `2.1198` n `82` status `ready` deltaP `22.3407` edge `0.0917` maxDD `-1.7857`
- `news_risk_high->crypto_major_24h` score `1.922` n `82` status `ready` deltaP `-3.4383` edge `1.1736` maxDD `-63.6743`
- `news_risk_high->metal_1h` score `1.6641` n `111` status `ready` deltaP `21.0134` edge `0.0271` maxDD `-0.6142`
- `news_risk_high->fx_4h` score `1.6446` n `106` status `ready` deltaP `23.8121` edge `0.0419` maxDD `-0.421`
- `market_context_high->index_1h` score `0.9858` n `47` status `ready` deltaP `14.9095` edge `0.0106` maxDD `-0.2275`
- `market_context_high->equity_1h` score `0.9378` n `47` status `ready` deltaP `11.6161` edge `0.041` maxDD `-1.5564`
- `news_risk_high->metal_24h` score `0.81` n `82` status `ready` deltaP `22.9632` edge `0.0956` maxDD `-7.2536`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
