# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-28T01:22:19.389670+00:00`
- Price records: `672`
- Market context records: `2095`
- Flow alert records: `7924`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9146`

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

- `market_context_high->crypto_alt_4h` score `10.576` n `186` status `ready` deltaP `30.8697` edge `0.79` maxDD `-5.1574`
- `market_context_high->crypto_major_4h` score `10.4512` n `186` status `ready` deltaP `37.0246` edge `0.6771` maxDD `-1.9063`
- `market_context_high->unknown_4h` score `6.4746` n `186` status `ready` deltaP `23.9051` edge `0.4551` maxDD `-2.6599`
- `market_context_high->equity_4h` score `4.1278` n `186` status `ready` deltaP `22.2053` edge `0.3054` maxDD `-5.0894`
- `market_context_high->unknown_24h` score `3.492` n `185` status `ready` deltaP `22.3866` edge `0.6738` maxDD `-35.8966`
- `market_context_high->index_4h` score `2.5219` n `186` status `ready` deltaP `18.6025` edge `0.1545` maxDD `-1.8022`
- `market_context_high->crypto_major_1h` score `2.3007` n `186` status `ready` deltaP `16.2514` edge `0.182` maxDD `-3.2225`
- `market_context_high->index_24h` score `2.1438` n `185` status `ready` deltaP `11.2934` edge `0.2262` maxDD `-4.1604`
- `market_context_high->crypto_alt_1h` score `2.0773` n `186` status `ready` deltaP `13.4071` edge `0.1951` maxDD `-4.9097`
- `market_context_high->equity_24h` score `1.7351` n `185` status `ready` deltaP `22.4306` edge `0.4849` maxDD `-33.1875`
- `market_context_high->equity_1h` score `0.8318` n `186` status `ready` deltaP `10.8831` edge `0.0756` maxDD `-2.6402`
- `market_context_high->unknown_1h` score `0.6852` n `186` status `ready` deltaP `6.0846` edge `0.0885` maxDD `-3.0902`
- `market_context_high->index_1h` score `0.1559` n `186` status `ready` deltaP `6.1394` edge `0.0311` maxDD `-1.3898`
- `market_context_high->crypto_major_24h` score `0.0934` n `185` status `ready` deltaP `21.1147` edge `0.7256` maxDD `-62.3533`
- `market_context_high->fx_24h` score `-0.1172` n `185` status `ready` deltaP `14.8854` edge `0.0303` maxDD `-2.811`
- `market_context_high->metal_4h` score `-0.1786` n `186` status `ready` deltaP `13.0229` edge `0.1528` maxDD `-11.3602`
- `market_context_high->metal_1h` score `-0.2528` n `186` status `ready` deltaP `6.751` edge `0.036` maxDD `-5.166`
- `market_context_high->fx_1h` score `-0.8191` n `186` status `ready` deltaP `-1.0479` edge `0.0015` maxDD `-0.3548`
- `market_context_high->metal_24h` score `-1.22` n `185` status `ready` deltaP `10.6275` edge `0.2176` maxDD `-23.2095`
- `market_context_high->fx_4h` score `-1.4573` n `186` status `ready` deltaP `-4.9502` edge `-0.0003` maxDD `-1.0513`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
