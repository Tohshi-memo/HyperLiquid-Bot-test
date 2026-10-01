# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-01T17:22:30.639222+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `72`

- Symbol pattern count: `6812`

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

- `market_context_high->unknown_1h` score `334.889` n `50` status `ready` deltaP `7.8802` edge `27.8598` maxDD `-0.0598`
- `market_context_high->unknown_4h` score `284.6344` n `50` status `ready` deltaP `6.8598` edge `23.6738` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `20.2686` n `111` status `ready` deltaP `34.8301` edge `1.4778` maxDD `-1.0093`
- `market_context_high->crypto_major_24h` score `10.128` n `50` status `ready` deltaP `32.8681` edge `0.7665` maxDD `-9.3299`
- `market_context_high->crypto_major_4h` score `7.4938` n `50` status `ready` deltaP `20.1341` edge `0.5606` maxDD `-3.294`
- `market_context_high->crypto_alt_4h` score `5.221` n `50` status `ready` deltaP `16.9512` edge `0.4514` maxDD `-7.6792`
- `news_risk_high->crypto_major_24h` score `5.1258` n `111` status `ready` deltaP `22.0393` edge `0.5956` maxDD `-15.8971`
- `market_context_high->crypto_alt_24h` score `4.9814` n `50` status `ready` deltaP `10.6319` edge `0.5152` maxDD `-11.6768`
- `market_context_high->equity_24h` score `3.9975` n `50` status `ready` deltaP `19.2153` edge `0.5706` maxDD `-11.8957`
- `news_risk_high->equity_4h` score `3.3939` n `124` status `ready` deltaP `26.8982` edge `0.1731` maxDD `-2.9013`
- `market_context_high->fx_4h` score `3.1576` n `50` status `ready` deltaP `35.4329` edge `0.0404` maxDD `-0.0791`
- `news_risk_high->equity_24h` score `3.1033` n `111` status `ready` deltaP `22.3865` edge `0.4835` maxDD `-9.4579`
- `market_context_high->crypto_major_1h` score `3.0515` n `50` status `ready` deltaP `14.7485` edge `0.201` maxDD `-2.2692`
- `market_context_high->crypto_alt_1h` score `2.9554` n `50` status `ready` deltaP `13.6048` edge `0.2219` maxDD `-3.6387`
- `news_risk_high->index_24h` score `2.5472` n `111` status `ready` deltaP `24.9719` edge `0.0936` maxDD `-0.4916`
- `news_risk_high->metal_24h` score `2.3027` n `111` status `ready` deltaP `27.1678` edge `0.2415` maxDD `-2.192`
- `market_context_high->fx_1h` score `1.5777` n `50` status `ready` deltaP `21.8383` edge `0.0123` maxDD `-0.113`
- `market_context_high->index_24h` score `0.8941` n `50` status `ready` deltaP `14.7917` edge `0.0731` maxDD `-1.2338`
- `market_context_high->fx_24h` score `0.5203` n `50` status `ready` deltaP `14.4306` edge `0.0723` maxDD `-1.8102`
- `news_risk_high->equity_1h` score `0.4858` n `124` status `ready` deltaP `7.0408` edge `0.0472` maxDD `-0.9592`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
