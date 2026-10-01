# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-01T08:07:46.990092+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `72`

- Symbol pattern count: `6702`

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

- `market_context_high->unknown_1h` score `324.6351` n `50` status `ready` deltaP `7.2814` edge `27.0093` maxDD `-0.0598`
- `market_context_high->unknown_4h` score `281.0644` n `50` status `ready` deltaP `6.8598` edge `23.3763` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `19.4623` n `124` status `ready` deltaP `29.1163` edge `1.4487` maxDD `-1.0093`
- `market_context_high->crypto_major_24h` score `8.7994` n `41` status `ready` deltaP `30.4962` edge `0.6716` maxDD `-9.3299`
- `market_context_high->crypto_major_4h` score `6.4489` n `50` status `ready` deltaP `17.5427` edge `0.4908` maxDD `-3.294`
- `news_risk_high->equity_24h` score `5.7473` n `124` status `ready` deltaP `22.8046` edge `0.5618` maxDD `-9.4579`
- `news_risk_high->equity_4h` score `4.1907` n `124` status `ready` deltaP `28.2308` edge `0.2099` maxDD `-1.2436`
- `market_context_high->crypto_alt_24h` score `4.171` n `41` status `ready` deltaP `13.656` edge `0.4275` maxDD `-11.6768`
- `news_risk_high->crypto_major_24h` score `4.0787` n `124` status `ready` deltaP `21.7629` edge `0.6932` maxDD `-15.8971`
- `market_context_high->crypto_alt_4h` score `3.3282` n `50` status `ready` deltaP `12.8354` edge `0.3211` maxDD `-7.6792`
- `market_context_high->crypto_major_1h` score `2.9615` n `50` status `ready` deltaP `14.8982` edge `0.1925` maxDD `-2.2692`
- `market_context_high->fx_4h` score `2.9594` n `50` status `ready` deltaP `33.4512` edge `0.0371` maxDD `-0.0791`
- `market_context_high->equity_24h` score `2.8632` n `41` status `ready` deltaP `12.0257` edge `0.4731` maxDD `-11.8957`
- `news_risk_high->crypto_alt_4h` score `2.8573` n `124` status `ready` deltaP `12.1902` edge `0.3575` maxDD `-10.7193`
- `market_context_high->crypto_alt_1h` score `2.6135` n `50` status `ready` deltaP `12.5569` edge `0.2004` maxDD `-3.6387`
- `news_risk_high->index_24h` score `2.5615` n `124` status `ready` deltaP `24.4456` edge `0.0983` maxDD `-0.4916`
- `news_risk_high->metal_24h` score `2.1751` n `124` status `ready` deltaP `25.6889` edge `0.235` maxDD `-2.192`
- `market_context_high->fx_1h` score `1.4316` n `50` status `ready` deltaP `20.1916` edge `0.0111` maxDD `-0.113`
- `news_risk_high->equity_1h` score `0.8249` n `124` status `ready` deltaP `8.0549` edge `0.0687` maxDD `-0.9592`
- `news_risk_high->crypto_alt_1h` score `0.5709` n `124` status `ready` deltaP `7.0408` edge `0.0917` maxDD `-4.2849`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
