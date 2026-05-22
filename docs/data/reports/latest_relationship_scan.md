# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-22T04:37:14.928797+00:00`
- Price records: `672`
- Market context records: `1493`
- Flow alert records: `6208`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8811`

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

- `market_context_high->metal_24h` score `12.1276` n `172` status `ready` deltaP `19.6827` edge `1.0003` maxDD `-6.3373`
- `market_context_high->crypto_alt_24h` score `11.6328` n `172` status `ready` deltaP `28.985` edge `0.9778` maxDD `-15.1306`
- `market_context_high->crypto_major_24h` score `10.5536` n `172` status `ready` deltaP `27.3538` edge `0.8103` maxDD `-8.0553`
- `market_context_high->index_24h` score `3.929` n `172` status `ready` deltaP `20.3327` edge `0.3005` maxDD `-5.3574`
- `market_context_high->equity_24h` score `3.3765` n `172` status `ready` deltaP `13.6144` edge `0.4233` maxDD `-14.2815`
- `market_context_high->equity_4h` score `1.3509` n `201` status `ready` deltaP `7.2254` edge `0.1474` maxDD `-3.6396`
- `market_context_high->fx_24h` score `0.9123` n `172` status `ready` deltaP `19.0245` edge `0.0541` maxDD `-1.3925`
- `market_context_high->equity_1h` score `-0.1063` n `201` status `ready` deltaP `2.0488` edge `0.0375` maxDD `-2.8014`
- `market_context_high->crypto_alt_4h` score `-0.1252` n `201` status `ready` deltaP `10.8338` edge `0.2493` maxDD `-19.5565`
- `market_context_high->index_1h` score `-0.1957` n `201` status `ready` deltaP `2.8503` edge `0.0112` maxDD `-1.7205`
- `market_context_high->crypto_alt_1h` score `-0.4892` n `201` status `ready` deltaP `1.6795` edge `0.0504` maxDD `-4.1892`
- `market_context_high->fx_1h` score `-0.5255` n `201` status `ready` deltaP `-0.1564` edge `-0.0031` maxDD `-0.3914`
- `market_context_high->crypto_major_4h` score `-0.637` n `201` status `ready` deltaP `6.661` edge `0.1734` maxDD `-13.3376`
- `market_context_high->metal_1h` score `-0.7554` n `201` status `ready` deltaP `5.6596` edge `-0.001` maxDD `-6.3532`
- `market_context_high->index_4h` score `-0.8759` n `201` status `ready` deltaP `-1.5137` edge `0.046` maxDD `-3.7119`
- `market_context_high->fx_4h` score `-0.9742` n `201` status `ready` deltaP `-3.45` edge `-0.009` maxDD `-1.4313`
- `market_context_high->commodity_1h` score `-1.0905` n `201` status `ready` deltaP `-0.0506` edge `0.0016` maxDD `-4.7041`
- `market_context_high->metal_4h` score `-1.2705` n `201` status `ready` deltaP `11.0416` edge `0.0897` maxDD `-12.5349`
- `market_context_high->crypto_major_1h` score `-1.5314` n `201` status `ready` deltaP `-1.0546` edge `0.0151` maxDD `-6.1883`
- `market_context_high->commodity_4h` score `-4.2919` n `201` status `ready` deltaP `-13.9228` edge `-0.0858` maxDD `-17.3969`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
