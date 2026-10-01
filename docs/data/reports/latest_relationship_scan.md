# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-01T15:52:37.343141+00:00`
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

- `market_context_high->unknown_1h` score `334.019` n `50` status `ready` deltaP `7.8802` edge `27.7873` maxDD `-0.0598`
- `market_context_high->unknown_4h` score `283.828` n `50` status `ready` deltaP `6.8598` edge `23.6066` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `19.7978` n `112` status `ready` deltaP `33.8046` edge `1.4454` maxDD `-1.0093`
- `market_context_high->crypto_major_24h` score `9.861` n `50` status `ready` deltaP `31.8264` edge `0.7512` maxDD `-9.3299`
- `market_context_high->crypto_major_4h` score `7.453` n `50` status `ready` deltaP `20.1341` edge `0.5572` maxDD `-3.294`
- `market_context_high->crypto_alt_4h` score `5.1754` n `50` status `ready` deltaP `16.9512` edge `0.4476` maxDD `-7.6792`
- `news_risk_high->crypto_major_24h` score `4.967` n `112` status `ready` deltaP `21.255` edge `0.5876` maxDD `-15.8971`
- `market_context_high->crypto_alt_24h` score `4.4709` n `50` status `ready` deltaP `9.5903` edge `0.4796` maxDD `-11.6768`
- `market_context_high->equity_24h` score `3.9729` n `50` status `ready` deltaP `19.0417` edge `0.5686` maxDD `-11.8957`
- `news_risk_high->equity_4h` score `3.4565` n `125` status `ready` deltaP `27.0659` edge `0.1772` maxDD `-2.9013`
- `news_risk_high->equity_24h` score `3.1731` n `112` status `ready` deltaP `22.4703` edge `0.4919` maxDD `-9.4579`
- `market_context_high->fx_4h` score `3.1176` n `50` status `ready` deltaP `35.128` edge `0.0391` maxDD `-0.0791`
- `market_context_high->crypto_major_1h` score `3.0947` n `50` status `ready` deltaP `15.0479` edge `0.2026` maxDD `-2.2692`
- `market_context_high->crypto_alt_1h` score `3.0177` n `50` status `ready` deltaP `13.9042` edge `0.2251` maxDD `-3.6387`
- `news_risk_high->index_24h` score `2.4907` n `112` status `ready` deltaP `24.2807` edge `0.0935` maxDD `-0.4916`
- `news_risk_high->metal_24h` score `2.2772` n `112` status `ready` deltaP `26.6617` edge `0.2416` maxDD `-2.192`
- `market_context_high->fx_1h` score `1.5394` n `50` status `ready` deltaP `21.3892` edge `0.0121` maxDD `-0.113`
- `market_context_high->index_24h` score `0.8294` n `50` status `ready` deltaP `13.9236` edge `0.0706` maxDD `-1.2338`
- `news_risk_high->equity_1h` score `0.7006` n `125` status `ready` deltaP `7.9557` edge `0.059` maxDD `-0.9592`
- `market_context_high->fx_24h` score `0.5313` n `50` status `ready` deltaP `14.4306` edge `0.0737` maxDD `-1.8102`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
