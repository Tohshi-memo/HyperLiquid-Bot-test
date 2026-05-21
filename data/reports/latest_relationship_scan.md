# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-21T04:40:39.518351+00:00`
- Price records: `672`
- Market context records: `1390`
- Flow alert records: `5914`
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
- `market_context_high->crypto_alt_24h` score `11.7455` n `157` status `ready` deltaP `28.8184` edge `0.9883` maxDD `-15.1306`
- `market_context_high->metal_24h` score `11.5302` n `157` status `ready` deltaP `12.4303` edge `1.0447` maxDD `-6.3373`
- `market_context_high->index_24h` score `4.2085` n `157` status `ready` deltaP `20.0759` edge `0.3255` maxDD `-5.3574`
- `market_context_high->equity_24h` score `2.6427` n `157` status `ready` deltaP `13.2464` edge `0.3646` maxDD `-14.2815`
- `market_context_high->equity_4h` score `1.6358` n `186` status `ready` deltaP `8.4612` edge `0.1629` maxDD `-3.6396`
- `market_context_high->fx_24h` score `0.0379` n `157` status `ready` deltaP `9.8803` edge `0.0422` maxDD `-1.3925`
- `market_context_high->index_1h` score `0.0367` n `198` status `ready` deltaP `4.9901` edge `0.0163` maxDD `-1.7205`
- `market_context_high->equity_1h` score `-0.0331` n `198` status `ready` deltaP `3.3433` edge `0.0308` maxDD `-2.8014`
- `market_context_high->metal_4h` score `-0.3175` n `186` status `ready` deltaP `9.3807` edge `0.0541` maxDD `-6.4478`
- `market_context_high->fx_1h` score `-0.3215` n `198` status `ready` deltaP `3.3101` edge `-0.0023` maxDD `-0.3914`
- `market_context_high->index_4h` score `-0.467` n `186` status `ready` deltaP `0.8376` edge `0.0644` maxDD `-3.7119`
- `market_context_high->crypto_alt_1h` score `-0.4707` n `198` status `ready` deltaP `2.0747` edge `0.034` maxDD `-3.6309`
- `market_context_high->metal_1h` score `-0.553` n `198` status `ready` deltaP `5.3484` edge `0.0013` maxDD `-4.2945`
- `market_context_high->commodity_1h` score `-0.9112` n `198` status `ready` deltaP `-1.8524` edge `-0.0021` maxDD `-2.252`
- `market_context_high->crypto_alt_4h` score `-1.1585` n `186` status `ready` deltaP `8.2826` edge `0.1802` maxDD `-19.5565`
- `market_context_high->crypto_major_1h` score `-1.2273` n `198` status `ready` deltaP `-0.2631` edge `0.006` maxDD `-6.1883`
- `market_context_high->crypto_major_4h` score `-1.2274` n `186` status `ready` deltaP `4.9354` edge `0.1357` maxDD `-13.3376`
- `market_context_high->fx_4h` score `-1.7124` n `186` status `ready` deltaP `-5.2714` edge `-0.0105` maxDD `-1.4313`
- `market_context_high->commodity_4h` score `-4.5971` n `186` status `ready` deltaP `-13.3687` edge `-0.0393` maxDD `-8.04`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
