# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-21T04:37:16.713471+00:00`
- Price records: `672`
- Market context records: `1389`
- Flow alert records: `5913`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8804`

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

- `market_context_high->crypto_major_24h` score `13.329` n `157` status `ready` deltaP `28.7011` edge `1.0326` maxDD `-8.0553`
- `market_context_high->crypto_alt_24h` score `11.7479` n `157` status `ready` deltaP `28.8184` edge `0.9885` maxDD `-15.1306`
- `market_context_high->metal_24h` score `11.5314` n `157` status `ready` deltaP `12.4303` edge `1.0448` maxDD `-6.3373`
- `market_context_high->index_24h` score `4.2097` n `157` status `ready` deltaP `20.0759` edge `0.3256` maxDD `-5.3574`
- `market_context_high->equity_24h` score `2.6439` n `157` status `ready` deltaP `13.2464` edge `0.3647` maxDD `-14.2815`
- `market_context_high->equity_4h` score `1.6334` n `186` status `ready` deltaP `8.4612` edge `0.1627` maxDD `-3.6396`
- `market_context_high->fx_24h` score `0.0379` n `157` status `ready` deltaP `9.8803` edge `0.0422` maxDD `-1.3925`
- `market_context_high->index_1h` score `0.0355` n `198` status `ready` deltaP `4.9901` edge `0.0162` maxDD `-1.7205`
- `market_context_high->equity_1h` score `-0.0331` n `198` status `ready` deltaP `3.3433` edge `0.0308` maxDD `-2.8014`
- `market_context_high->metal_4h` score `-0.3187` n `186` status `ready` deltaP `9.3807` edge `0.054` maxDD `-6.4478`
- `market_context_high->fx_1h` score `-0.3215` n `198` status `ready` deltaP `3.3101` edge `-0.0023` maxDD `-0.3914`
- `market_context_high->index_4h` score `-0.4682` n `186` status `ready` deltaP `0.8376` edge `0.0643` maxDD `-3.7119`
- `market_context_high->crypto_alt_1h` score `-0.4743` n `198` status `ready` deltaP `2.0747` edge `0.0337` maxDD `-3.6309`
- `market_context_high->metal_1h` score `-0.5545` n `198` status `ready` deltaP `5.3484` edge `0.0011` maxDD `-4.2945`
- `market_context_high->commodity_1h` score `-0.8816` n `198` status `ready` deltaP `-1.497` edge `-0.002` maxDD `-2.252`
- `market_context_high->crypto_alt_4h` score `-1.1633` n `186` status `ready` deltaP `8.2826` edge `0.1798` maxDD `-19.5565`
- `market_context_high->crypto_major_1h` score `-1.2285` n `198` status `ready` deltaP `-0.2631` edge `0.0059` maxDD `-6.1883`
- `market_context_high->crypto_major_4h` score `-1.2286` n `186` status `ready` deltaP `4.9354` edge `0.1356` maxDD `-13.3376`
- `market_context_high->fx_4h` score `-1.7124` n `186` status `ready` deltaP `-5.2714` edge `-0.0105` maxDD `-1.4313`
- `market_context_high->commodity_4h` score `-4.5947` n `186` status `ready` deltaP `-13.3687` edge `-0.0391` maxDD `-8.04`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
