# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-03T19:22:29.987826+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `4238`

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

- `market_context_high->unknown_1h` score `371.8148` n `50` status `ready` deltaP `11.9222` edge `30.91` maxDD `-0.0597`
- `market_context_high->unknown_4h` score `312.159` n `50` status `ready` deltaP `12.6524` edge `25.9289` maxDD `0.0`
- `market_context_high->crypto_alt_24h` score `13.9596` n `50` status `ready` deltaP `29.286` edge `1.1384` maxDD `-11.6271`
- `market_context_high->crypto_major_24h` score `11.6819` n `50` status `ready` deltaP `37.1127` edge `0.8677` maxDD `-9.3299`
- `news_risk_high->equity_24h` score `10.6816` n `62` status `ready` deltaP `29.9575` edge `0.7389` maxDD `-2.8784`
- `news_risk_high->crypto_major_4h` score `10.3625` n `68` status `ready` deltaP `37.4193` edge `0.6344` maxDD `-0.6258`
- `news_risk_high->crypto_alt_4h` score `7.3814` n `68` status `ready` deltaP `26.6141` edge `0.5721` maxDD `-6.4195`
- `market_context_high->crypto_major_4h` score `6.9626` n `50` status `ready` deltaP `15.7134` edge `0.5458` maxDD `-3.294`
- `market_context_high->crypto_alt_4h` score `5.6648` n `50` status `ready` deltaP `15.7317` edge `0.4961` maxDD `-7.6465`
- `news_risk_high->index_24h` score `4.5794` n `62` status `ready` deltaP `33.4629` edge `0.1744` maxDD `-0.2696`
- `news_risk_high->equity_4h` score `3.8303` n `68` status `ready` deltaP `26.9637` edge `0.2007` maxDD `-2.9013`
- `market_context_high->crypto_alt_1h` score `3.1403` n `50` status `ready` deltaP `13.6048` edge `0.2373` maxDD `-3.6376`
- `market_context_high->fx_4h` score `3.1114` n `50` status `ready` deltaP `34.9756` edge `0.0396` maxDD `-0.0791`
- `news_risk_high->index_4h` score `2.9984` n `68` status `ready` deltaP `32.8461` edge `0.0571` maxDD `-0.4296`
- `news_risk_high->crypto_major_1h` score `2.8803` n `68` status `ready` deltaP `12.9095` edge `0.1895` maxDD `-1.5096`
- `market_context_high->crypto_major_1h` score `2.8155` n `50` status `ready` deltaP `12.2036` edge `0.1983` maxDD `-2.2692`
- `news_risk_high->metal_4h` score `2.4002` n `68` status `ready` deltaP `20.4448` edge `0.1053` maxDD `-0.993`
- `news_risk_high->index_1h` score `1.9839` n `68` status `ready` deltaP `24.4981` edge `0.017` maxDD `-0.1997`
- `market_context_high->fx_1h` score `1.6436` n `50` status `ready` deltaP `22.7365` edge `0.0118` maxDD `-0.113`
- `market_context_high->equity_24h` score `1.5152` n `50` status `ready` deltaP `9.2478` edge `0.3188` maxDD `-11.8957`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
