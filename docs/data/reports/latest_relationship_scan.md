# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-01T14:07:29.921441+00:00`
- Price records: `672`
- Market context records: `5359`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11494`

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

- `market_context_high->unknown_24h` score `12.5397` n `167` status `ready` deltaP `17.5098` edge `0.9414` maxDD `-0.3859`
- `market_context_high->crypto_major_24h` score `5.1551` n `167` status `ready` deltaP `21.9624` edge `0.7372` maxDD `-29.6555`
- `market_context_high->equity_24h` score `4.0347` n `167` status `ready` deltaP `16.9214` edge `0.7863` maxDD `-40.0306`
- `market_context_high->crypto_major_4h` score `2.3187` n `194` status `ready` deltaP `13.0312` edge `0.3356` maxDD `-14.0065`
- `market_context_high->crypto_alt_4h` score `1.932` n `194` status `ready` deltaP `9.5973` edge `0.2611` maxDD `-9.46`
- `market_context_high->equity_4h` score `1.5934` n `194` status `ready` deltaP `9.7875` edge `0.2314` maxDD `-7.4425`
- `market_context_high->index_24h` score `0.7179` n `167` status `ready` deltaP `23.1495` edge `0.1012` maxDD `-7.413`
- `market_context_high->fx_24h` score `0.1679` n `167` status `ready` deltaP `9.9343` edge `0.0373` maxDD `-0.8294`
- `market_context_high->equity_1h` score `0.0759` n `203` status `ready` deltaP `6.0375` edge `0.0626` maxDD `-5.0555`
- `market_context_high->crypto_major_1h` score `0.0341` n `203` status `ready` deltaP `4.2882` edge `0.0988` maxDD `-6.9639`
- `market_context_high->crypto_alt_1h` score `-0.01` n `203` status `ready` deltaP `1.893` edge `0.0827` maxDD `-5.0257`
- `market_context_high->index_1h` score `-0.1261` n `203` status `ready` deltaP `4.5544` edge `0.0095` maxDD `-1.0296`
- `market_context_high->index_4h` score `-0.4196` n `194` status `ready` deltaP `5.6119` edge `0.0247` maxDD `-2.9391`
- `market_context_high->fx_1h` score `-0.4733` n `203` status `ready` deltaP `-1.5501` edge `-0.0014` maxDD `-0.5823`
- `market_context_high->metal_1h` score `-0.6454` n `203` status `ready` deltaP `0.8451` edge `0.0081` maxDD `-2.0682`
- `market_context_high->fx_4h` score `-0.6668` n `194` status `ready` deltaP `2.1357` edge `0.0032` maxDD `-1.567`
- `market_context_high->unknown_4h` score `-1.2159` n `194` status `ready` deltaP `7.908` edge `-0.0358` maxDD `-6.126`
- `market_context_high->commodity_1h` score `-1.5404` n `203` status `ready` deltaP `-4.0567` edge `-0.008` maxDD `-3.4655`
- `market_context_high->metal_4h` score `-2.7796` n `194` status `ready` deltaP `-8.5963` edge `-0.0466` maxDD `-12.8631`
- `market_context_high->crypto_alt_24h` score `-3.7806` n `167` status `ready` deltaP `11.9137` edge `0.3056` maxDD `-54.2437`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
