# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-28T07:22:36.442620+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `72`

- Symbol pattern count: `7886`

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

- `news_risk_high->unknown_24h` score `669.516` n `139` status `ready` deltaP `1.2153` edge `55.7849` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `4.0214` n `139` status `ready` deltaP `17.3099` edge `0.6149` maxDD `-29.2814`
- `news_risk_high->index_24h` score `2.0833` n `139` status `ready` deltaP `21.845` edge `0.0975` maxDD `-2.2287`
- `news_risk_high->equity_24h` score `1.449` n `139` status `ready` deltaP `16.2132` edge `0.2683` maxDD `-11.1179`
- `news_risk_high->crypto_major_24h` score `1.3451` n `139` status `ready` deltaP `12.741` edge `0.4706` maxDD `-26.1424`
- `news_risk_high->metal_24h` score `1.149` n `139` status `ready` deltaP `20.3013` edge `0.1459` maxDD `-6.8392`
- `news_risk_high->equity_4h` score `1.1447` n `139` status `ready` deltaP `20.3139` edge `0.1209` maxDD `-9.2079`
- `news_risk_high->crypto_alt_1h` score `0.3485` n `139` status `ready` deltaP `5.82` edge `0.0813` maxDD `-4.2849`
- `news_risk_high->index_1h` score `0.176` n `139` status `ready` deltaP `5.6079` edge `0.0063` maxDD `-0.3214`
- `news_risk_high->equity_1h` score `0.1484` n `139` status `ready` deltaP `5.1588` edge `0.0441` maxDD `-1.957`
- `news_risk_high->crypto_alt_4h` score `0.0` n `139` status `ready` deltaP `5.7543` edge `0.2276` maxDD `-15.9436`
- `news_risk_high->metal_1h` score `-0.5807` n `139` status `ready` deltaP `0.8917` edge `0.0086` maxDD `-0.7016`
- `news_risk_high->index_4h` score `-0.6616` n `139` status `ready` deltaP `2.0848` edge `0.0163` maxDD `-1.493`
- `news_risk_high->crypto_major_1h` score `-0.8615` n `139` status `ready` deltaP `-1.4992` edge `0.0278` maxDD `-7.2607`
- `news_risk_high->fx_1h` score `-1.1586` n `139` status `ready` deltaP `-8.6687` edge `-0.0027` maxDD `-1.0436`
- `news_risk_high->fx_4h` score `-1.2539` n `139` status `ready` deltaP `9.5247` edge `-0.0029` maxDD `-3.0414`
- `news_risk_high->metal_4h` score `-1.6409` n `139` status `ready` deltaP `-11.9001` edge `0.0184` maxDD `-3.6214`
- `news_risk_high->commodity_1h` score `-1.9625` n `139` status `ready` deltaP `-10.8183` edge `-0.012` maxDD `-3.3986`
- `news_risk_high->crypto_major_4h` score `-2.5154` n `139` status `ready` deltaP `-8.4445` edge `0.0053` maxDD `-13.719`
- `news_risk_high->commodity_4h` score `-3.6684` n `139` status `ready` deltaP `-9.9502` edge `0.0025` maxDD `-8.6825`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
