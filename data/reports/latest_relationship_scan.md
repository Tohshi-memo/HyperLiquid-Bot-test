# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-09T03:37:36.772383+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `64`

- Symbol pattern count: `6599`

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

- `market_context_high->equity_24h` score `10.8783` n `32` status `ready` deltaP `17.8819` edge `1.0246` maxDD `-16.6495`
- `market_context_high->commodity_24h` score `2.8483` n `32` status `ready` deltaP `9.375` edge `0.2336` maxDD `-1.6995`
- `market_context_high->index_24h` score `1.5063` n `32` status `ready` deltaP `18.0556` edge `0.119` maxDD `-2.3671`
- `market_context_high->equity_1h` score `0.977` n `70` status `ready` deltaP `4.6535` edge `0.1701` maxDD `-5.5762`
- `market_context_high->metal_1h` score `0.8942` n `70` status `ready` deltaP `10.9795` edge `0.0341` maxDD `-0.6226`
- `market_context_high->fx_24h` score `0.6633` n `32` status `ready` deltaP `10.5903` edge `-0.0065` maxDD `-0.0397`
- `market_context_high->metal_4h` score `0.5848` n `58` status `ready` deltaP `9.0307` edge `0.0673` maxDD `-1.2025`
- `market_context_high->commodity_4h` score `0.3172` n `58` status `ready` deltaP `1.9712` edge `0.0605` maxDD `-1.1102`
- `market_context_high->commodity_1h` score `0.1389` n `70` status `ready` deltaP `7.3867` edge `0.0211` maxDD `-1.7019`
- `market_context_high->index_4h` score `0.0378` n `58` status `ready` deltaP `11.4592` edge `0.0213` maxDD `-2.4279`
- `market_context_high->index_1h` score `-0.1887` n `70` status `ready` deltaP `3.0753` edge `0.0221` maxDD `-0.6664`
- `market_context_high->crypto_alt_1h` score `-0.5316` n `70` status `ready` deltaP `11.1035` edge `0.0471` maxDD `-10.1421`
- `market_context_high->fx_1h` score `-0.8964` n `70` status `ready` deltaP `-10.7357` edge `-0.0039` maxDD `-0.4893`
- `market_context_high->fx_4h` score `-1.2658` n `58` status `ready` deltaP `-5.1357` edge `-0.0036` maxDD `-1.2893`
- `market_context_high->metal_24h` score `-1.509` n `32` status `ready` deltaP `1.0417` edge `-0.1451` maxDD `-1.4245`
- `market_context_high->crypto_major_1h` score `-1.8405` n `70` status `ready` deltaP `2.3139` edge `-0.0415` maxDD `-11.7911`
- `market_context_high->equity_4h` score `-3.886` n `58` status `ready` deltaP `6.802` edge `0.0088` maxDD `-24.9053`
- `market_context_high->crypto_major_24h` score `-4.6822` n `32` status `ready` deltaP `-4.8611` edge `0.0065` maxDD `-23.1423`
- `market_context_high->crypto_alt_4h` score `-7.404` n `58` status `ready` deltaP `5.6508` edge `-0.1878` maxDD `-30.6833`
- `market_context_high->crypto_alt_24h` score `-8.863` n `32` status `ready` deltaP `-18.75` edge `-0.1557` maxDD `-29.9639`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
