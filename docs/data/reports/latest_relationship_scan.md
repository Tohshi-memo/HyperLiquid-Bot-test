# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-21T13:52:22.601367+00:00`
- Price records: `672`
- Market context records: `1428`
- Flow alert records: `6027`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8785`

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

- `market_context_high->crypto_alt_24h` score `11.8265` n `154` status `ready` deltaP `28.7811` edge `0.9953` maxDD `-15.1306`
- `market_context_high->metal_24h` score `11.7758` n `154` status `ready` deltaP `12.3354` edge `1.0658` maxDD `-6.3373`
- `market_context_high->crypto_major_24h` score `11.7236` n `154` status `ready` deltaP `27.3539` edge `0.9078` maxDD `-8.0553`
- `market_context_high->index_24h` score `3.8625` n `154` status `ready` deltaP `19.3813` edge `0.3013` maxDD `-5.3574`
- `market_context_high->equity_24h` score `2.8287` n `154` status `ready` deltaP `12.5271` edge `0.3849` maxDD `-14.2815`
- `market_context_high->equity_4h` score `1.0354` n `202` status `ready` deltaP `5.847` edge `0.1303` maxDD `-3.6396`
- `market_context_high->fx_24h` score `0.0803` n `154` status `ready` deltaP `9.3592` edge `0.0492` maxDD `-1.3925`
- `market_context_high->index_1h` score `-0.2047` n `214` status `ready` deltaP `2.9773` edge `0.0096` maxDD `-1.7205`
- `market_context_high->equity_1h` score `-0.3045` n `214` status `ready` deltaP `2.1517` edge `0.0203` maxDD `-2.8014`
- `market_context_high->fx_1h` score `-0.4705` n `214` status `ready` deltaP `1.4928` edge `-0.0026` maxDD `-0.3914`
- `market_context_high->index_4h` score `-0.6042` n `202` status `ready` deltaP `0.4422` edge `0.0556` maxDD `-3.7119`
- `market_context_high->commodity_1h` score `-0.6177` n `214` status `ready` deltaP `-0.4491` edge `0.013` maxDD `-2.252`
- `market_context_high->crypto_alt_1h` score `-0.8007` n `214` status `ready` deltaP `1.2662` edge `0.0272` maxDD `-4.1892`
- `market_context_high->metal_1h` score `-0.9512` n `214` status `ready` deltaP `3.7705` edge `-0.0135` maxDD `-6.3532`
- `market_context_high->crypto_alt_4h` score `-1.0906` n `202` status `ready` deltaP `8.4113` edge `0.185` maxDD `-19.5565`
- `market_context_high->crypto_major_4h` score `-1.2686` n `202` status `ready` deltaP `5.29` edge `0.1299` maxDD `-13.3376`
- `market_context_high->fx_4h` score `-1.5654` n `202` status `ready` deltaP `-3.6585` edge `-0.009` maxDD `-1.4313`
- `market_context_high->crypto_major_1h` score `-1.8153` n `214` status `ready` deltaP `-1.7236` edge `-0.0041` maxDD `-6.1883`
- `market_context_high->metal_4h` score `-2.6843` n `202` status `ready` deltaP `4.7588` edge `0.0044` maxDD `-11.7852`
- `market_context_high->commodity_4h` score `-2.7292` n `202` status `ready` deltaP `-10.6994` edge `-0.0239` maxDD `-8.04`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
