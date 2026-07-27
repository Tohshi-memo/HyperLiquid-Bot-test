# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-27T04:37:30.725014+00:00`
- Price records: `672`
- Market context records: `8057`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11848`

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

- `market_context_high->equity_24h` score `20.1808` n `74` status `ready` deltaP `35.2897` edge `1.5375` maxDD `-4.9489`
- `market_context_high->equity_4h` score `8.5099` n `87` status `ready` deltaP `33.1826` edge `0.5359` maxDD `-2.5032`
- `market_context_high->metal_24h` score `8.3924` n `74` status `ready` deltaP `35.8752` edge `0.4602` maxDD `0.0`
- `market_context_high->commodity_24h` score `5.7395` n `74` status `ready` deltaP `37.0579` edge `0.3467` maxDD `-6.2367`
- `market_context_high->index_4h` score `3.3161` n `87` status `ready` deltaP `31.893` edge `0.0825` maxDD `-0.5022`
- `market_context_high->index_24h` score `2.5604` n `74` status `ready` deltaP `14.2934` edge `0.1851` maxDD `-1.3621`
- `market_context_high->equity_1h` score `2.5132` n `87` status `ready` deltaP `16.073` edge `0.1456` maxDD `-2.1322`
- `market_context_high->metal_4h` score `2.2974` n `87` status `ready` deltaP `21.1487` edge `0.1127` maxDD `-0.979`
- `market_context_high->fx_24h` score `1.3786` n `74` status `ready` deltaP `29.1302` edge `0.0529` maxDD `-0.6283`
- `market_context_high->index_1h` score `1.1494` n `87` status `ready` deltaP `15.1215` edge `0.0217` maxDD `-0.4716`
- `market_context_high->metal_1h` score `0.8638` n `87` status `ready` deltaP `11.9726` edge `0.03` maxDD `-0.6936`
- `market_context_high->crypto_major_1h` score `0.5867` n `87` status `ready` deltaP `9.6204` edge `0.0258` maxDD `-1.6171`
- `market_context_high->crypto_major_4h` score `0.3728` n `87` status `ready` deltaP `7.4958` edge `0.1529` maxDD `-6.7444`
- `market_context_high->crypto_alt_4h` score `0.2716` n `87` status `ready` deltaP `3.7427` edge `0.1094` maxDD `-3.9374`
- `market_context_high->fx_4h` score `0.0097` n `87` status `ready` deltaP `6.9649` edge `0.0051` maxDD `-0.3563`
- `market_context_high->crypto_alt_1h` score `-0.3359` n `87` status `ready` deltaP `-0.2753` edge `0.0171` maxDD `-1.4603`
- `market_context_high->commodity_1h` score `-0.3705` n `87` status `ready` deltaP `2.3281` edge `-0.0007` maxDD `-1.9855`
- `market_context_high->fx_1h` score `-0.4071` n `87` status `ready` deltaP `-2.4778` edge `0.0007` maxDD `-0.2428`
- `market_context_high->commodity_4h` score `-0.8242` n `87` status `ready` deltaP `5.8067` edge `0.0058` maxDD `-5.3478`
- `market_context_high->unknown_1h` score `-2.359` n `87` status `ready` deltaP `4.1193` edge `-0.1817` maxDD `-1.054`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
