# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-03T21:52:29.158479+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `4252`

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

- `market_context_high->unknown_1h` score `381.0379` n `50` status `ready` deltaP `12.6707` edge `31.6736` maxDD `-0.0597`
- `market_context_high->unknown_4h` score `321.5624` n `50` status `ready` deltaP `12.8049` edge `26.7115` maxDD `0.0`
- `market_context_high->crypto_alt_24h` score `13.5948` n `50` status `ready` deltaP `29.286` edge `1.108` maxDD `-11.6271`
- `market_context_high->crypto_major_24h` score `11.5115` n `50` status `ready` deltaP `37.1127` edge `0.8535` maxDD `-9.3299`
- `news_risk_high->equity_24h` score `10.732` n `62` status `ready` deltaP `29.9575` edge `0.7431` maxDD `-2.8784`
- `news_risk_high->crypto_major_4h` score `10.4279` n `68` status `ready` deltaP `37.8766` edge `0.6368` maxDD `-0.6258`
- `news_risk_high->crypto_alt_4h` score `7.3414` n `68` status `ready` deltaP `26.3092` edge `0.5708` maxDD `-6.4195`
- `market_context_high->crypto_major_4h` score `7.028` n `50` status `ready` deltaP `16.1707` edge `0.5482` maxDD `-3.294`
- `market_context_high->crypto_alt_4h` score `5.6248` n `50` status `ready` deltaP `15.4268` edge `0.4948` maxDD `-7.6465`
- `news_risk_high->index_24h` score `4.5818` n `62` status `ready` deltaP `33.4629` edge `0.1746` maxDD `-0.2696`
- `news_risk_high->equity_4h` score `3.8303` n `68` status `ready` deltaP `26.9637` edge `0.2007` maxDD `-2.9013`
- `market_context_high->crypto_alt_1h` score `3.072` n `50` status `ready` deltaP `13.3054` edge `0.2336` maxDD `-3.6376`
- `market_context_high->fx_4h` score `3.0602` n `50` status `ready` deltaP `34.3659` edge `0.0394` maxDD `-0.0791`
- `news_risk_high->index_4h` score `2.9595` n `68` status `ready` deltaP `32.3888` edge `0.0569` maxDD `-0.4296`
- `news_risk_high->crypto_major_1h` score `2.9043` n `68` status `ready` deltaP `13.0592` edge `0.1905` maxDD `-1.5096`
- `market_context_high->crypto_major_1h` score `2.8395` n `50` status `ready` deltaP `12.3533` edge `0.1993` maxDD `-2.2692`
- `news_risk_high->metal_4h` score `2.4124` n `68` status `ready` deltaP `20.5972` edge `0.1053` maxDD `-0.993`
- `news_risk_high->index_1h` score `1.9599` n `68` status `ready` deltaP `24.1987` edge `0.017` maxDD `-0.1997`
- `market_context_high->fx_1h` score `1.5573` n `50` status `ready` deltaP `21.6886` edge `0.0116` maxDD `-0.113`
- `market_context_high->equity_24h` score `1.548` n `50` status `ready` deltaP `9.2478` edge `0.323` maxDD `-11.8957`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
