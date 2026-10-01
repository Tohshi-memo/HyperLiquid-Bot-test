# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-01T15:37:31.747399+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `72`

- Symbol pattern count: `6786`

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

- `market_context_high->unknown_1h` score `333.9182` n `50` status `ready` deltaP `7.8802` edge `27.7789` maxDD `-0.0598`
- `market_context_high->unknown_4h` score `283.7068` n `50` status `ready` deltaP `6.8598` edge `23.5965` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `19.6591` n `113` status `ready` deltaP `33.6468` edge `1.4349` maxDD `-1.0093`
- `market_context_high->crypto_major_24h` score `9.8303` n `50` status `ready` deltaP `31.6528` edge `0.7498` maxDD `-9.3299`
- `market_context_high->crypto_major_4h` score `7.4168` n `50` status `ready` deltaP `19.9817` edge `0.5552` maxDD `-3.294`
- `market_context_high->crypto_alt_4h` score `5.1356` n `50` status `ready` deltaP `16.7988` edge `0.4453` maxDD `-7.6792`
- `news_risk_high->crypto_major_24h` score `4.9338` n `113` status `ready` deltaP `21.3342` edge `0.5843` maxDD `-15.8971`
- `market_context_high->crypto_alt_24h` score `4.4054` n `50` status `ready` deltaP `9.4167` edge `0.4753` maxDD `-11.6768`
- `market_context_high->equity_24h` score `3.9553` n `50` status `ready` deltaP `18.8681` edge `0.5675` maxDD `-11.8957`
- `news_risk_high->equity_4h` score `3.4875` n `126` status `ready` deltaP `27.0785` edge `0.1797` maxDD `-2.9013`
- `news_risk_high->equity_24h` score `3.1843` n `113` status `ready` deltaP `22.5495` edge `0.4928` maxDD `-9.4579`
- `market_context_high->fx_4h` score `3.114` n `50` status `ready` deltaP `35.128` edge `0.0388` maxDD `-0.0791`
- `market_context_high->crypto_major_1h` score `3.0911` n `50` status `ready` deltaP `15.0479` edge `0.2023` maxDD `-2.2692`
- `market_context_high->crypto_alt_1h` score `3.0213` n `50` status `ready` deltaP `13.9042` edge `0.2254` maxDD `-3.6387`
- `news_risk_high->index_24h` score `2.4919` n `113` status `ready` deltaP `24.281` edge `0.0936` maxDD `-0.4916`
- `news_risk_high->metal_24h` score `2.2882` n `113` status `ready` deltaP `26.8437` edge `0.2418` maxDD `-2.192`
- `market_context_high->fx_1h` score `1.5382` n `50` status `ready` deltaP `21.3892` edge `0.012` maxDD `-0.113`
- `market_context_high->index_24h` score `0.8157` n `50` status `ready` deltaP `13.75` edge `0.07` maxDD `-1.2338`
- `news_risk_high->equity_1h` score `0.7675` n `126` status `ready` deltaP `8.1171` edge `0.0635` maxDD `-0.9592`
- `market_context_high->fx_24h` score `0.5336` n `50` status `ready` deltaP `14.4306` edge `0.074` maxDD `-1.8102`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
