# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-11T01:37:30.608168+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11744`

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

- `market_context_high->unknown_24h` score `4.8097` n `145` status `ready` deltaP `-14.5772` edge `0.7434` maxDD `-9.6329`
- `market_context_high->fx_24h` score `1.1085` n `145` status `ready` deltaP `20.4064` edge `0.0371` maxDD `-1.4613`
- `market_context_high->commodity_4h` score `0.9569` n `168` status `ready` deltaP `12.4201` edge `0.0684` maxDD `-2.7169`
- `market_context_high->commodity_1h` score `0.6789` n `180` status `ready` deltaP `9.3114` edge `0.0288` maxDD `-0.7439`
- `market_context_high->fx_4h` score `-0.0937` n `168` status `ready` deltaP `6.25` edge `0.0063` maxDD `-0.4647`
- `market_context_high->fx_1h` score `-0.1442` n `180` status `ready` deltaP `4.1218` edge `-0.0008` maxDD `-0.613`
- `market_context_high->metal_1h` score `-1.2924` n `180` status `ready` deltaP `-5.2195` edge `-0.0093` maxDD `-2.0884`
- `market_context_high->index_1h` score `-1.3326` n `180` status `ready` deltaP `-7.0758` edge `-0.0051` maxDD `-1.0359`
- `market_context_high->equity_1h` score `-1.4559` n `180` status `ready` deltaP `-6.0545` edge `-0.0186` maxDD `-6.8818`
- `market_context_high->metal_24h` score `-1.6122` n `145` status `ready` deltaP `2.5482` edge `-0.0189` maxDD `-2.9283`
- `market_context_high->index_4h` score `-1.9758` n `168` status `ready` deltaP `-8.1446` edge `-0.0199` maxDD `-1.5693`
- `market_context_high->index_24h` score `-2.0094` n `145` status `ready` deltaP `-8.5914` edge `0.0092` maxDD `-6.7627`
- `market_context_high->crypto_alt_1h` score `-2.6859` n `180` status `ready` deltaP `-9.5143` edge `-0.0418` maxDD `-6.4874`
- `market_context_high->commodity_24h` score `-3.1695` n `145` status `ready` deltaP `6.2272` edge `0.0483` maxDD `-29.36`
- `market_context_high->metal_4h` score `-3.2802` n `168` status `ready` deltaP `-8.5439` edge `-0.04` maxDD `-6.1111`
- `market_context_high->crypto_major_1h` score `-3.8228` n `180` status `ready` deltaP `-10.642` edge `-0.0572` maxDD `-11.9002`
- `market_context_high->equity_4h` score `-4.6121` n `168` status `ready` deltaP `-17.6829` edge `-0.1625` maxDD `-15.8728`
- `market_context_high->crypto_major_24h` score `-6.1595` n `145` status `ready` deltaP `-11.1767` edge `-0.1744` maxDD `-31.5949`
- `market_context_high->crypto_alt_4h` score `-7.0345` n `168` status `ready` deltaP `-14.4454` edge `-0.1551` maxDD `-20.1177`
- `market_context_high->equity_24h` score `-8.5712` n `145` status `ready` deltaP `-8.436` edge `-0.2346` maxDD `-50.643`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
