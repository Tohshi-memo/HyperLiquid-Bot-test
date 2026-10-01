# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-01T16:22:30.563580+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `72`

- Symbol pattern count: `6796`

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

- `market_context_high->unknown_1h` score `334.301` n `50` status `ready` deltaP `7.8802` edge `27.8108` maxDD `-0.0598`
- `market_context_high->unknown_4h` score `284.2468` n `50` status `ready` deltaP `6.8598` edge `23.6415` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `19.9311` n `111` status `ready` deltaP `34.1357` edge `1.4543` maxDD `-1.0093`
- `market_context_high->crypto_major_24h` score `9.9548` n `50` status `ready` deltaP `32.1736` edge `0.7567` maxDD `-9.3299`
- `market_context_high->crypto_major_4h` score `7.5012` n `50` status `ready` deltaP `20.2866` edge `0.5602` maxDD `-3.294`
- `market_context_high->crypto_alt_4h` score `5.2236` n `50` status `ready` deltaP `17.1037` edge `0.4506` maxDD `-7.6792`
- `news_risk_high->crypto_major_24h` score `4.9526` n `111` status `ready` deltaP `21.3448` edge `0.5858` maxDD `-15.8971`
- `market_context_high->crypto_alt_24h` score `4.6439` n `50` status `ready` deltaP `9.9375` edge `0.4917` maxDD `-11.6768`
- `market_context_high->equity_24h` score `4.0136` n `50` status `ready` deltaP `19.3889` edge `0.5715` maxDD `-11.8957`
- `news_risk_high->equity_4h` score `3.4205` n `124` status `ready` deltaP `27.0506` edge `0.1743` maxDD `-2.9013`
- `market_context_high->fx_4h` score `3.1224` n `50` status `ready` deltaP `35.128` edge `0.0395` maxDD `-0.0791`
- `news_risk_high->equity_24h` score `3.1193` n `111` status `ready` deltaP `22.5601` edge `0.4844` maxDD `-9.4579`
- `market_context_high->crypto_major_1h` score `3.1043` n `50` status `ready` deltaP `15.0479` edge `0.2034` maxDD `-2.2692`
- `market_context_high->crypto_alt_1h` score `3.0153` n `50` status `ready` deltaP `13.9042` edge `0.2249` maxDD `-3.6387`
- `news_risk_high->index_24h` score `2.4911` n `111` status `ready` deltaP `24.451` edge `0.0924` maxDD `-0.4916`
- `news_risk_high->metal_24h` score `2.2639` n `111` status `ready` deltaP `26.647` edge `0.24` maxDD `-2.192`
- `market_context_high->fx_1h` score `1.5394` n `50` status `ready` deltaP `21.3892` edge `0.0121` maxDD `-0.113`
- `market_context_high->index_24h` score `0.8576` n `50` status `ready` deltaP `14.2708` edge `0.0719` maxDD `-1.2338`
- `news_risk_high->equity_1h` score `0.5817` n `124` status `ready` deltaP `7.6396` edge `0.0512` maxDD `-0.9592`
- `market_context_high->fx_24h` score `0.5266` n `50` status `ready` deltaP `14.4306` edge `0.0731` maxDD `-1.8102`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
