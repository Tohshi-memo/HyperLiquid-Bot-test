# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-03T22:07:32.452763+00:00`
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

- `market_context_high->unknown_1h` score `381.1015` n `50` status `ready` deltaP `12.8204` edge `31.6779` maxDD `-0.0597`
- `market_context_high->unknown_4h` score `321.5792` n `50` status `ready` deltaP `12.8049` edge `26.7129` maxDD `0.0`
- `market_context_high->crypto_alt_24h` score `13.5684` n `50` status `ready` deltaP `29.286` edge `1.1058` maxDD `-11.6271`
- `market_context_high->crypto_major_24h` score `11.4923` n `50` status `ready` deltaP `37.1127` edge `0.8519` maxDD `-9.3299`
- `news_risk_high->equity_24h` score `10.7356` n `62` status `ready` deltaP `29.9575` edge `0.7434` maxDD `-2.8784`
- `news_risk_high->crypto_major_4h` score `10.4497` n `68` status `ready` deltaP `38.0291` edge `0.6376` maxDD `-0.6258`
- `news_risk_high->crypto_alt_4h` score `7.3474` n `68` status `ready` deltaP `26.3092` edge `0.5713` maxDD `-6.4195`
- `market_context_high->crypto_major_4h` score `7.0498` n `50` status `ready` deltaP `16.3232` edge `0.549` maxDD `-3.294`
- `market_context_high->crypto_alt_4h` score `5.6308` n `50` status `ready` deltaP `15.4268` edge `0.4953` maxDD `-7.6465`
- `news_risk_high->index_24h` score `4.5806` n `62` status `ready` deltaP `33.4629` edge `0.1745` maxDD `-0.2696`
- `news_risk_high->equity_4h` score `3.8303` n `68` status `ready` deltaP `26.9637` edge `0.2007` maxDD `-2.9013`
- `market_context_high->crypto_alt_1h` score `3.0756` n `50` status `ready` deltaP `13.3054` edge `0.2339` maxDD `-3.6376`
- `market_context_high->fx_4h` score `3.048` n `50` status `ready` deltaP `34.2134` edge `0.0394` maxDD `-0.0791`
- `news_risk_high->index_4h` score `2.9595` n `68` status `ready` deltaP `32.3888` edge `0.0569` maxDD `-0.4296`
- `news_risk_high->crypto_major_1h` score `2.9043` n `68` status `ready` deltaP `13.0592` edge `0.1905` maxDD `-1.5096`
- `market_context_high->crypto_major_1h` score `2.8395` n `50` status `ready` deltaP `12.3533` edge `0.1993` maxDD `-2.2692`
- `news_risk_high->metal_4h` score `2.4124` n `68` status `ready` deltaP `20.5972` edge `0.1053` maxDD `-0.993`
- `news_risk_high->index_1h` score `1.9599` n `68` status `ready` deltaP `24.1987` edge `0.017` maxDD `-0.1997`
- `market_context_high->equity_24h` score `1.5503` n `50` status `ready` deltaP `9.2478` edge `0.3233` maxDD `-11.8957`
- `market_context_high->fx_1h` score `1.5454` n `50` status `ready` deltaP `21.5389` edge `0.0116` maxDD `-0.113`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
