# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-01T19:37:27.607109+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `72`

- Symbol pattern count: `6822`

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

- `market_context_high->unknown_1h` score `340.409` n `50` status `ready` deltaP `8.479` edge `28.3158` maxDD `-0.0598`
- `market_context_high->unknown_4h` score `285.8788` n `50` status `ready` deltaP `6.8598` edge `23.7775` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `20.3446` n `104` status `ready` deltaP `35.7505` edge `1.478` maxDD `-1.0093`
- `market_context_high->crypto_major_24h` score `10.2247` n `50` status `ready` deltaP `33.0417` edge `0.7734` maxDD `-9.3299`
- `market_context_high->crypto_major_4h` score `7.3223` n `50` status `ready` deltaP `19.2195` edge `0.5524` maxDD `-3.294`
- `market_context_high->crypto_alt_24h` score `5.48` n `50` status `ready` deltaP `11.6736` edge `0.5498` maxDD `-11.6768`
- `market_context_high->crypto_alt_4h` score `5.0944` n `50` status `ready` deltaP `16.4939` edge `0.4439` maxDD `-7.6792`
- `news_risk_high->crypto_major_24h` score `4.862` n `104` status `ready` deltaP `20.2725` edge `0.5854` maxDD `-15.8971`
- `market_context_high->equity_24h` score `3.8949` n `50` status `ready` deltaP `19.0417` edge `0.5586` maxDD `-11.8957`
- `news_risk_high->equity_4h` score `3.3526` n `117` status `ready` deltaP `27.598` edge `0.165` maxDD `-2.9013`
- `market_context_high->fx_4h` score `3.1684` n `50` status `ready` deltaP `35.4329` edge `0.0413` maxDD `-0.0791`
- `market_context_high->crypto_major_1h` score `3.0371` n `50` status `ready` deltaP `14.5988` edge `0.2008` maxDD `-2.2692`
- `market_context_high->crypto_alt_1h` score `2.9566` n `50` status `ready` deltaP `13.6048` edge `0.222` maxDD `-3.6387`
- `news_risk_high->equity_24h` score `2.9006` n `104` status `ready` deltaP `21.234` edge `0.4652` maxDD `-9.4579`
- `news_risk_high->index_24h` score `2.3541` n `104` status `ready` deltaP `23.6379` edge `0.0864` maxDD `-0.4916`
- `news_risk_high->metal_24h` score `2.1846` n `104` status `ready` deltaP `25.4808` edge `0.2376` maxDD `-2.192`
- `market_context_high->fx_1h` score `1.5526` n `50` status `ready` deltaP `21.5389` edge `0.0122` maxDD `-0.113`
- `market_context_high->index_24h` score `0.905` n `50` status `ready` deltaP `14.7917` edge `0.0745` maxDD `-1.2338`
- `news_risk_high->equity_1h` score `0.5414` n `117` status `ready` deltaP `7.796` edge `0.0468` maxDD `-0.9592`
- `market_context_high->fx_24h` score `0.5016` n `50` status `ready` deltaP `14.4306` edge `0.0699` maxDD `-1.8102`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
