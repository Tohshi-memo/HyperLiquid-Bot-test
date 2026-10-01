# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-01T07:37:32.731553+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `72`

- Symbol pattern count: `6722`

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

- `market_context_high->unknown_1h` score `324.7971` n `50` status `ready` deltaP `7.2814` edge `27.0228` maxDD `-0.0598`
- `market_context_high->unknown_4h` score `281.134` n `50` status `ready` deltaP `6.8598` edge `23.3821` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `19.4011` n `124` status `ready` deltaP `29.1163` edge `1.4436` maxDD `-1.0093`
- `market_context_high->crypto_major_24h` score `8.8861` n `39` status `ready` deltaP `29.7944` edge `0.6835` maxDD `-9.3299`
- `market_context_high->crypto_major_4h` score `6.4921` n `50` status `ready` deltaP `17.5427` edge `0.4944` maxDD `-3.294`
- `news_risk_high->equity_24h` score `5.7149` n `124` status `ready` deltaP `22.8046` edge `0.5591` maxDD `-9.4579`
- `market_context_high->crypto_alt_24h` score `4.4357` n `39` status `ready` deltaP `12.7805` edge `0.4554` maxDD `-11.6768`
- `news_risk_high->equity_4h` score `4.2051` n `124` status `ready` deltaP `28.2308` edge `0.2111` maxDD `-1.2436`
- `news_risk_high->crypto_major_24h` score `4.0986` n `124` status `ready` deltaP `21.9366` edge `0.6946` maxDD `-15.8971`
- `market_context_high->crypto_alt_4h` score `3.3582` n `50` status `ready` deltaP `12.8354` edge `0.3236` maxDD `-7.6792`
- `market_context_high->crypto_major_1h` score `2.9711` n `50` status `ready` deltaP `14.8982` edge `0.1933` maxDD `-2.2692`
- `market_context_high->fx_4h` score `2.9338` n `50` status `ready` deltaP `33.1463` edge `0.037` maxDD `-0.0791`
- `news_risk_high->crypto_alt_4h` score `2.8873` n `124` status `ready` deltaP `12.1902` edge `0.36` maxDD `-10.7193`
- `market_context_high->equity_24h` score `2.729` n `39` status `ready` deltaP `10.1496` edge `0.4684` maxDD `-11.8957`
- `market_context_high->crypto_alt_1h` score `2.6195` n `50` status `ready` deltaP `12.5569` edge `0.2009` maxDD `-3.6387`
- `news_risk_high->index_24h` score `2.5567` n `124` status `ready` deltaP `24.4456` edge `0.0979` maxDD `-0.4916`
- `news_risk_high->metal_24h` score `2.1704` n `124` status `ready` deltaP `25.6889` edge `0.2344` maxDD `-2.192`
- `market_context_high->fx_1h` score `1.4292` n `50` status `ready` deltaP `20.1916` edge `0.0109` maxDD `-0.113`
- `news_risk_high->equity_1h` score `0.8333` n `124` status `ready` deltaP `8.0549` edge `0.0694` maxDD `-0.9592`
- `news_risk_high->crypto_alt_1h` score `0.5769` n `124` status `ready` deltaP `7.0408` edge `0.0922` maxDD `-4.2849`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
