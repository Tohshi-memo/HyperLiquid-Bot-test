# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-18T03:22:27.546658+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11837`

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

- `market_context_high->crypto_major_24h` score `4.2629` n `73` status `ready` deltaP `14.4939` edge `0.3794` maxDD `-4.9964`
- `market_context_high->metal_24h` score `0.649` n `73` status `ready` deltaP `4.8384` edge `0.0776` maxDD `-1.1283`
- `market_context_high->commodity_24h` score `0.5975` n `73` status `ready` deltaP `12.6469` edge `0.1488` maxDD `-4.666`
- `market_context_high->commodity_4h` score `0.498` n `106` status `ready` deltaP `11.2546` edge `0.0515` maxDD `-2.4692`
- `market_context_high->unknown_1h` score `0.2235` n `106` status `ready` deltaP `7.5331` edge `-0.0057` maxDD `-0.7386`
- `market_context_high->index_1h` score `0.1064` n `106` status `ready` deltaP `7.8635` edge `0.0032` maxDD `-0.3584`
- `market_context_high->equity_1h` score `-0.0879` n `106` status `ready` deltaP `3.7171` edge `0.0242` maxDD `-1.8201`
- `market_context_high->fx_4h` score `-0.1393` n `106` status `ready` deltaP `5.5655` edge `0.002` maxDD `-0.3904`
- `market_context_high->metal_4h` score `-0.1481` n `106` status `ready` deltaP `7.8808` edge `-0.0009` maxDD `-2.3165`
- `market_context_high->crypto_major_4h` score `-0.2419` n `106` status `ready` deltaP `4.1648` edge `0.0563` maxDD `-4.2067`
- `market_context_high->index_24h` score `-0.3873` n `73` status `ready` deltaP `9.3184` edge `-0.0497` maxDD `-1.2427`
- `market_context_high->metal_1h` score `-0.5762` n `106` status `ready` deltaP `-0.644` edge `-0.0028` maxDD `-1.3425`
- `market_context_high->fx_1h` score `-0.6953` n `106` status `ready` deltaP `-3.3697` edge `0.0007` maxDD `-0.2273`
- `market_context_high->commodity_1h` score `-0.7333` n `106` status `ready` deltaP `-5.0164` edge `0.0007` maxDD `-1.5684`
- `market_context_high->index_4h` score `-0.8541` n `106` status `ready` deltaP `-5.715` edge `-0.0033` maxDD `-0.7818`
- `market_context_high->equity_24h` score `-0.9204` n `73` status `ready` deltaP `11.0017` edge `-0.0744` maxDD `-4.3846`
- `market_context_high->crypto_major_1h` score `-0.9433` n `106` status `ready` deltaP `-3.429` edge `-0.0025` maxDD `-3.6463`
- `market_context_high->unknown_24h` score `-1.0507` n `73` status `ready` deltaP `2.6186` edge `-0.0857` maxDD `-1.3173`
- `market_context_high->crypto_alt_1h` score `-1.2195` n `106` status `ready` deltaP `-2.5308` edge `0.0041` maxDD `-3.1082`
- `market_context_high->equity_4h` score `-1.6225` n `106` status `ready` deltaP `-8.4014` edge `-0.029` maxDD `-5.1734`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
