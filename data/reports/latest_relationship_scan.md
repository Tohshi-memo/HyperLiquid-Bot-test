# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-30T19:52:26.578647+00:00`
- Price records: `672`
- Market context records: `5280`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `80`

- Symbol pattern count: `9650`

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

- `market_context_high->unknown_24h` score `25.2091` n `153` status `ready` deltaP `28.2067` edge `1.9217` maxDD `-0.3859`
- `market_context_high->crypto_major_24h` score `7.508` n `153` status `ready` deltaP `25.7353` edge `0.8691` maxDD `-26.5332`
- `market_context_high->crypto_alt_4h` score `4.296` n `174` status `ready` deltaP `16.4073` edge `0.4127` maxDD `-9.46`
- `market_context_high->crypto_major_4h` score `3.9038` n `174` status `ready` deltaP `15.6102` edge `0.4505` maxDD `-14.0065`
- `market_context_high->equity_24h` score `3.7562` n `153` status `ready` deltaP `19.9653` edge `0.7428` maxDD `-40.0306`
- `market_context_high->equity_4h` score `0.9538` n `174` status `ready` deltaP `9.7719` edge `0.1782` maxDD `-7.4425`
- `market_context_high->unknown_4h` score `0.7109` n `174` status `ready` deltaP `14.3345` edge `0.0659` maxDD `-5.5109`
- `market_context_high->fx_24h` score `0.5697` n `153` status `ready` deltaP `13.3068` edge `0.0483` maxDD `-0.8294`
- `market_context_high->crypto_alt_1h` score `0.5434` n `181` status `ready` deltaP `5.3305` edge `0.1059` maxDD `-5.0257`
- `market_context_high->crypto_major_1h` score `0.3096` n `181` status `ready` deltaP `6.0219` edge `0.1102` maxDD `-6.9639`
- `market_context_high->index_24h` score `0.2311` n `153` status `ready` deltaP `20.8231` edge `0.0543` maxDD `-7.413`
- `market_context_high->equity_1h` score `0.0845` n `181` status `ready` deltaP `6.9847` edge `0.057` maxDD `-5.0555`
- `market_context_high->index_1h` score `0.0292` n `181` status `ready` deltaP `6.2254` edge `0.0113` maxDD `-1.0296`
- `market_context_high->index_4h` score `-0.2786` n `174` status `ready` deltaP `7.4134` edge `0.0266` maxDD `-2.9391`
- `market_context_high->metal_1h` score `-0.3216` n `181` status `ready` deltaP `3.1776` edge `0.0112` maxDD `-2.0682`
- `market_context_high->fx_1h` score `-0.3537` n `181` status `ready` deltaP `0.5401` edge `0.0` maxDD `-0.5823`
- `market_context_high->fx_4h` score `-0.7449` n `174` status `ready` deltaP `0.8585` edge `0.0017` maxDD `-1.567`
- `market_context_high->commodity_1h` score `-1.3747` n `181` status `ready` deltaP `-2.4862` edge `-0.0062` maxDD `-3.3428`
- `market_context_high->metal_4h` score `-1.6693` n `174` status `ready` deltaP `-3.0856` edge `0.0069` maxDD `-9.3609`
- `market_context_high->unknown_1h` score `-2.5377` n `181` status `ready` deltaP `6.3859` edge `-0.1899` maxDD `-2.7986`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
