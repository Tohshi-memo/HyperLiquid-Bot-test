# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-01T20:22:30.005444+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `72`

- Symbol pattern count: `6818`

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

- `market_context_high->unknown_1h` score `337.7521` n `50` status `ready` deltaP `8.479` edge `28.0944` maxDD `-0.0598`
- `market_context_high->unknown_4h` score `286.3312` n `50` status `ready` deltaP `6.8598` edge `23.8152` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `20.312` n `101` status `ready` deltaP `35.867` edge `1.4745` maxDD `-1.0093`
- `market_context_high->crypto_major_24h` score `10.2367` n `50` status `ready` deltaP `33.0417` edge `0.7744` maxDD `-9.3299`
- `market_context_high->crypto_major_4h` score `7.2583` n `50` status `ready` deltaP `18.9146` edge `0.5491` maxDD `-3.294`
- `market_context_high->crypto_alt_24h` score `5.6067` n `50` status `ready` deltaP `11.8472` edge `0.5592` maxDD `-11.6768`
- `market_context_high->crypto_alt_4h` score `5.0474` n `50` status `ready` deltaP `16.3415` edge `0.441` maxDD `-7.6792`
- `news_risk_high->crypto_major_24h` score `4.7193` n `101` status `ready` deltaP `19.3585` edge `0.5796` maxDD `-15.8971`
- `market_context_high->equity_24h` score `3.8567` n `50` status `ready` deltaP `19.0417` edge `0.5537` maxDD `-11.8957`
- `news_risk_high->equity_4h` score `3.3368` n `114` status `ready` deltaP `27.8055` edge `0.1623` maxDD `-2.9013`
- `market_context_high->fx_4h` score `3.144` n `50` status `ready` deltaP `35.128` edge `0.0413` maxDD `-0.0791`
- `market_context_high->crypto_major_1h` score `3.0143` n `50` status `ready` deltaP `14.4491` edge `0.1999` maxDD `-2.2692`
- `market_context_high->crypto_alt_1h` score `2.929` n `50` status `ready` deltaP `13.4551` edge `0.2207` maxDD `-3.6387`
- `news_risk_high->equity_24h` score `2.8038` n `101` status `ready` deltaP `20.3486` edge `0.4587` maxDD `-9.4579`
- `news_risk_high->index_24h` score `2.2474` n `101` status `ready` deltaP `23.0095` edge `0.0817` maxDD `-0.4916`
- `news_risk_high->metal_24h` score `2.1104` n `101` status `ready` deltaP `24.3691` edge `0.2355` maxDD `-2.192`
- `market_context_high->fx_1h` score `1.5154` n `50` status `ready` deltaP `21.0898` edge `0.0121` maxDD `-0.113`
- `market_context_high->index_24h` score `0.9058` n `50` status `ready` deltaP `14.7917` edge `0.0746` maxDD `-1.2338`
- `news_risk_high->commodity_24h` score `0.8769` n `101` status `ready` deltaP `19.8226` edge `0.0991` maxDD `-7.3206`
- `news_risk_high->equity_1h` score `0.5342` n `114` status `ready` deltaP `7.661` edge `0.0471` maxDD `-0.9592`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
