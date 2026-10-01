# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-01T11:22:29.073338+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `72`

- Symbol pattern count: `7046`

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

- `market_context_high->unknown_1h` score `324.5043` n `50` status `ready` deltaP `7.4311` edge `26.9974` maxDD `-0.0598`
- `market_context_high->unknown_4h` score `281.0068` n `50` status `ready` deltaP `6.8598` edge `23.3715` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `20.0036` n `121` status `ready` deltaP `30.8124` edge `1.4825` maxDD `-1.0093`
- `market_context_high->crypto_major_24h` score `8.7321` n `50` status `ready` deltaP `30.0903` edge `0.6687` maxDD `-9.3299`
- `market_context_high->crypto_major_4h` score `6.9175` n `50` status `ready` deltaP `18.9146` edge `0.5207` maxDD `-3.294`
- `news_risk_high->equity_24h` score `5.6848` n `121` status `ready` deltaP `22.3384` edge `0.5597` maxDD `-9.4579`
- `news_risk_high->equity_4h` score `4.5137` n `122` status `ready` deltaP `29.6432` edge `0.2274` maxDD `-1.2436`
- `market_context_high->crypto_alt_4h` score `4.1017` n `50` status `ready` deltaP `14.3598` edge `0.3754` maxDD `-7.6792`
- `news_risk_high->crypto_major_24h` score `3.9664` n `121` status `ready` deltaP `21.644` edge `0.6796` maxDD `-15.8971`
- `market_context_high->equity_24h` score `3.5521` n `50` status `ready` deltaP `16.7847` edge `0.5297` maxDD `-11.8957`
- `market_context_high->fx_4h` score `2.9594` n `50` status `ready` deltaP `33.4512` edge `0.0371` maxDD `-0.0791`
- `news_risk_high->crypto_alt_4h` score `2.9287` n `122` status `ready` deltaP `12.3926` edge `0.3621` maxDD `-10.7193`
- `market_context_high->crypto_major_1h` score `2.8571` n `50` status `ready` deltaP `14.4491` edge `0.1868` maxDD `-2.2692`
- `market_context_high->crypto_alt_1h` score `2.6027` n `50` status `ready` deltaP `12.5569` edge `0.1995` maxDD `-3.6387`
- `news_risk_high->index_24h` score `2.5565` n `121` status `ready` deltaP `24.3529` edge `0.0985` maxDD `-0.4916`
- `news_risk_high->metal_24h` score `2.2979` n `121` status `ready` deltaP `27.046` edge `0.2417` maxDD `-2.192`
- `market_context_high->crypto_alt_24h` score `2.2973` n `50` status `ready` deltaP `6.4653` edge `0.3193` maxDD `-11.6768`
- `market_context_high->fx_1h` score `1.4448` n `50` status `ready` deltaP `20.3413` edge `0.0112` maxDD `-0.113`
- `news_risk_high->equity_1h` score `0.8124` n `134` status `ready` deltaP `7.8984` edge `0.0687` maxDD `-0.9592`
- `market_context_high->index_24h` score `0.6995` n `50` status `ready` deltaP `12.5347` edge `0.0632` maxDD `-1.2338`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
