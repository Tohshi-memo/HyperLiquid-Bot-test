# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-01T13:09:00.856991+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `72`

- Symbol pattern count: `7070`

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

- `market_context_high->unknown_1h` score `334.7919` n `50` status `ready` deltaP `7.7305` edge `27.8527` maxDD `-0.0598`
- `market_context_high->unknown_4h` score `281.086` n `50` status `ready` deltaP `6.8598` edge `23.3781` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `18.8747` n `115` status `ready` deltaP `31.9415` edge `1.3809` maxDD `-1.0093`
- `market_context_high->crypto_major_24h` score `9.3702` n `50` status `ready` deltaP `30.6111` edge `0.7184` maxDD `-9.3299`
- `market_context_high->crypto_major_4h` score `7.1325` n `50` status `ready` deltaP `19.0671` edge `0.5376` maxDD `-3.294`
- `market_context_high->crypto_alt_4h` score `4.6635` n `50` status `ready` deltaP `15.4268` edge `0.4151` maxDD `-7.6792`
- `news_risk_high->equity_4h` score `4.1331` n `123` status `ready` deltaP `29.1158` edge `0.1992` maxDD `-1.2436`
- `market_context_high->equity_24h` score `3.7352` n `50` status `ready` deltaP `17.3056` edge `0.5497` maxDD `-11.8957`
- `market_context_high->crypto_alt_24h` score `3.3881` n `50` status `ready` deltaP `7.6806` edge `0.4021` maxDD `-11.6768`
- `news_risk_high->equity_24h` score `3.1395` n `115` status `ready` deltaP `21.4795` edge `0.4942` maxDD `-9.4579`
- `news_risk_high->crypto_major_24h` score `3.084` n `115` status `ready` deltaP `20.785` edge `0.5722` maxDD `-15.8971`
- `market_context_high->fx_4h` score `3.013` n `50` status `ready` deltaP `34.061` edge `0.0375` maxDD `-0.0791`
- `market_context_high->crypto_major_1h` score `2.9603` n `50` status `ready` deltaP `14.7485` edge `0.1934` maxDD `-2.2692`
- `market_context_high->crypto_alt_1h` score `2.7527` n `50` status `ready` deltaP `12.8563` edge `0.21` maxDD `-3.6387`
- `news_risk_high->index_24h` score `2.3906` n `115` status `ready` deltaP `23.4043` edge `0.091` maxDD `-0.4916`
- `news_risk_high->metal_24h` score `2.2294` n `115` status `ready` deltaP `26.1474` edge `0.2389` maxDD `-2.192`
- `market_context_high->fx_1h` score `1.4567` n `50` status `ready` deltaP `20.491` edge `0.0112` maxDD `-0.113`
- `news_risk_high->equity_1h` score `0.8174` n `128` status `ready` deltaP `8.2757` edge `0.0666` maxDD `-0.9592`
- `news_risk_high->crypto_alt_4h` score `0.8024` n `123` status `ready` deltaP `8.0284` edge `0.214` maxDD `-10.7193`
- `market_context_high->index_24h` score `0.7135` n `50` status `ready` deltaP `12.5347` edge `0.065` maxDD `-1.2338`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
