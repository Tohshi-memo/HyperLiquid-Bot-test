# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-01T15:07:33.120201+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `72`

- Symbol pattern count: `6876`

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

- `market_context_high->unknown_1h` score `333.7454` n `50` status `ready` deltaP `7.8802` edge `27.7645` maxDD `-0.0598`
- `market_context_high->unknown_4h` score `283.42` n `50` status `ready` deltaP `6.8598` edge `23.5726` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `19.4718` n `114` status `ready` deltaP `33.315` edge `1.4215` maxDD `-1.0093`
- `market_context_high->crypto_major_24h` score `9.7709` n `50` status `ready` deltaP `31.4792` edge `0.746` maxDD `-9.3299`
- `market_context_high->crypto_major_4h` score `7.3456` n `50` status `ready` deltaP `19.6768` edge `0.5513` maxDD `-3.294`
- `market_context_high->crypto_alt_4h` score `5.0488` n `50` status `ready` deltaP `16.4939` edge `0.4401` maxDD `-7.6792`
- `news_risk_high->crypto_major_24h` score `4.905` n `114` status `ready` deltaP `21.409` edge `0.5814` maxDD `-15.8971`
- `market_context_high->crypto_alt_24h` score `4.2432` n `50` status `ready` deltaP `9.0694` edge `0.4641` maxDD `-11.6768`
- `market_context_high->equity_24h` score `3.91` n `50` status `ready` deltaP `18.5208` edge `0.564` maxDD `-11.8957`
- `news_risk_high->equity_4h` score `3.4809` n `127` status `ready` deltaP `26.9361` edge `0.1801` maxDD `-2.9013`
- `news_risk_high->equity_24h` score `3.1955` n `114` status `ready` deltaP `22.4506` edge `0.4949` maxDD `-9.4579`
- `market_context_high->fx_4h` score `3.1092` n `50` status `ready` deltaP `35.128` edge `0.0384` maxDD `-0.0791`
- `market_context_high->crypto_major_1h` score `3.0419` n `50` status `ready` deltaP `14.8982` edge `0.1992` maxDD `-2.2692`
- `market_context_high->crypto_alt_1h` score `2.9698` n `50` status `ready` deltaP `13.7545` edge `0.2221` maxDD `-3.6387`
- `news_risk_high->index_24h` score `2.4754` n `114` status `ready` deltaP `24.1046` edge `0.0934` maxDD `-0.4916`
- `news_risk_high->metal_24h` score `2.2914` n `114` status `ready` deltaP `26.8457` edge `0.2422` maxDD `-2.192`
- `market_context_high->fx_1h` score `1.537` n `50` status `ready` deltaP `21.3892` edge `0.0119` maxDD `-0.113`
- `news_risk_high->equity_1h` score `0.828` n `127` status `ready` deltaP `8.2736` edge `0.0675` maxDD `-0.9592`
- `market_context_high->index_24h` score `0.7867` n `50` status `ready` deltaP `13.4028` edge `0.0686` maxDD `-1.2338`
- `market_context_high->fx_24h` score `0.5375` n `50` status `ready` deltaP `14.4306` edge `0.0745` maxDD `-1.8102`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
