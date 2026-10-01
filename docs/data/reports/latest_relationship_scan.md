# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-01T23:52:27.839258+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `72`

- Symbol pattern count: `6574`

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

- `market_context_high->unknown_1h` score `338.574` n `50` status `ready` deltaP `9.5269` edge `28.1559` maxDD `-0.0598`
- `market_context_high->unknown_4h` score `287.1355` n `50` status `ready` deltaP `8.0793` edge `23.8741` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `19.6778` n `87` status `ready` deltaP `37.2844` edge `1.4122` maxDD `-1.0093`
- `market_context_high->crypto_major_24h` score `10.7791` n `50` status `ready` deltaP `35.4722` edge `0.8034` maxDD `-9.3299`
- `market_context_high->crypto_major_4h` score `7.2873` n `50` status `ready` deltaP `19.0671` edge `0.5505` maxDD `-3.294`
- `market_context_high->crypto_alt_24h` score `6.5747` n `50` status `ready` deltaP `13.5833` edge `0.6283` maxDD `-11.6768`
- `market_context_high->crypto_alt_4h` score `5.0284` n `50` status `ready` deltaP `16.4939` edge `0.4384` maxDD `-7.6792`
- `news_risk_high->crypto_major_24h` score `3.7787` n `87` status `ready` deltaP `16.6906` edge `0.519` maxDD `-15.8971`
- `market_context_high->equity_24h` score `3.6867` n `50` status `ready` deltaP `19.0417` edge `0.5319` maxDD `-11.8957`
- `market_context_high->crypto_major_1h` score `3.0587` n `50` status `ready` deltaP `14.8982` edge `0.2006` maxDD `-2.2692`
- `market_context_high->crypto_alt_1h` score `3.0081` n `50` status `ready` deltaP `14.0539` edge `0.2233` maxDD `-3.6387`
- `market_context_high->fx_4h` score `2.9944` n `50` status `ready` deltaP `33.6037` edge `0.039` maxDD `-0.0791`
- `news_risk_high->equity_4h` score `2.9015` n `100` status `ready` deltaP `25.4085` edge `0.142` maxDD `-2.9013`
- `news_risk_high->equity_24h` score `2.299` n `87` status `ready` deltaP `15.4095` edge `0.4269` maxDD `-9.4579`
- `news_risk_high->crypto_alt_4h` score `2.0816` n `100` status `ready` deltaP `8.4939` edge `0.2512` maxDD `-6.4152`
- `news_risk_high->metal_24h` score `1.7202` n `87` status `ready` deltaP `18.9356` edge `0.2217` maxDD `-2.192`
- `news_risk_high->commodity_24h` score `1.7002` n `87` status `ready` deltaP `26.9516` edge `0.1507` maxDD `-3.9922`
- `news_risk_high->index_24h` score `1.6394` n `87` status `ready` deltaP `19.5043` edge `0.0544` maxDD `-0.4916`
- `market_context_high->fx_1h` score `1.5154` n `50` status `ready` deltaP `21.0898` edge `0.0121` maxDD `-0.113`
- `market_context_high->index_24h` score `0.9182` n `50` status `ready` deltaP `14.7917` edge `0.0762` maxDD `-1.2338`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
