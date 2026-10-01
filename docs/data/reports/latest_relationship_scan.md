# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-01T07:07:28.007222+00:00`
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

- `market_context_high->unknown_1h` score `324.8019` n `50` status `ready` deltaP `7.2814` edge `27.0232` maxDD `-0.0598`
- `market_context_high->unknown_4h` score `281.1112` n `50` status `ready` deltaP `6.8598` edge `23.3802` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `19.3579` n `124` status `ready` deltaP `29.1163` edge `1.44` maxDD `-1.0093`
- `market_context_high->crypto_major_24h` score `8.8007` n `37` status `ready` deltaP `28.9978` edge `0.6817` maxDD `-9.3299`
- `market_context_high->crypto_major_4h` score `6.5583` n `50` status `ready` deltaP `17.6951` edge `0.4989` maxDD `-3.294`
- `news_risk_high->equity_24h` score `5.6897` n `124` status `ready` deltaP `22.8046` edge `0.557` maxDD `-9.4579`
- `market_context_high->crypto_alt_24h` score `4.4577` n `37` status `ready` deltaP `11.8103` edge `0.4637` maxDD `-11.6768`
- `news_risk_high->equity_4h` score `4.2401` n `124` status `ready` deltaP `28.3832` edge `0.213` maxDD `-1.2436`
- `news_risk_high->crypto_major_24h` score `4.1271` n `124` status `ready` deltaP `22.1102` edge `0.6971` maxDD `-15.8971`
- `market_context_high->crypto_alt_4h` score `3.4075` n `50` status `ready` deltaP `12.9878` edge `0.3267` maxDD `-7.6792`
- `market_context_high->crypto_major_1h` score `2.9651` n `50` status `ready` deltaP `14.8982` edge `0.1928` maxDD `-2.2692`
- `news_risk_high->crypto_alt_4h` score `2.9367` n `124` status `ready` deltaP `12.3426` edge `0.3631` maxDD `-10.7193`
- `market_context_high->fx_4h` score `2.9216` n `50` status `ready` deltaP `32.9939` edge `0.037` maxDD `-0.0791`
- `market_context_high->crypto_alt_1h` score `2.6087` n `50` status `ready` deltaP `12.5569` edge `0.2` maxDD `-3.6387`
- `news_risk_high->index_24h` score `2.5543` n `124` status `ready` deltaP `24.4456` edge `0.0977` maxDD `-0.4916`
- `market_context_high->equity_24h` score `2.5249` n `37` status `ready` deltaP `8.0706` edge `0.4561` maxDD `-11.8957`
- `news_risk_high->metal_24h` score `2.1665` n `124` status `ready` deltaP `25.6889` edge `0.2339` maxDD `-2.192`
- `market_context_high->fx_1h` score `1.4304` n `50` status `ready` deltaP `20.1916` edge `0.011` maxDD `-0.113`
- `news_risk_high->equity_1h` score `0.8333` n `124` status `ready` deltaP `8.0549` edge `0.0694` maxDD `-0.9592`
- `news_risk_high->crypto_alt_1h` score `0.5661` n `124` status `ready` deltaP `7.0408` edge `0.0913` maxDD `-4.2849`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
