# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-22T04:22:14.328984+00:00`
- Price records: `672`
- Market context records: `1492`
- Flow alert records: `6205`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8810`

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

- `market_context_high->metal_24h` score `11.9982` n `172` status `ready` deltaP `19.2749` edge `0.9964` maxDD `-6.3373`
- `market_context_high->crypto_alt_24h` score `11.6976` n `172` status `ready` deltaP `28.985` edge `0.9832` maxDD `-15.1306`
- `market_context_high->crypto_major_24h` score `10.6268` n `172` status `ready` deltaP `27.3538` edge `0.8164` maxDD `-8.0553`
- `market_context_high->index_24h` score `3.9434` n `172` status `ready` deltaP `20.3327` edge `0.3017` maxDD `-5.3574`
- `market_context_high->equity_24h` score `3.4377` n `172` status `ready` deltaP `13.6144` edge `0.4284` maxDD `-14.2815`
- `market_context_high->equity_4h` score `1.3752` n `202` status `ready` deltaP `7.3337` edge `0.1487` maxDD `-3.6396`
- `market_context_high->fx_24h` score `0.8737` n `172` status `ready` deltaP `18.6167` edge `0.0536` maxDD `-1.3925`
- `market_context_high->crypto_alt_4h` score `-0.065` n `202` status `ready` deltaP `11.0012` edge `0.2532` maxDD `-19.5565`
- `market_context_high->equity_1h` score `-0.0819` n `202` status `ready` deltaP `2.2188` edge `0.0384` maxDD `-2.8014`
- `market_context_high->index_1h` score `-0.2093` n `202` status `ready` deltaP `2.6798` edge `0.0112` maxDD `-1.7205`
- `market_context_high->crypto_alt_1h` score `-0.5077` n `202` status `ready` deltaP `1.5533` edge `0.0497` maxDD `-4.1892`
- `market_context_high->fx_1h` score `-0.5311` n `202` status `ready` deltaP `-0.2653` edge `-0.0031` maxDD `-0.3914`
- `market_context_high->crypto_major_4h` score `-0.6278` n `202` status `ready` deltaP `6.8507` edge `0.1729` maxDD `-13.3376`
- `market_context_high->metal_1h` score `-0.7427` n `202` status `ready` deltaP `5.8591` edge `-0.0007` maxDD `-6.3532`
- `market_context_high->index_4h` score `-0.8529` n `202` status `ready` deltaP `-1.3463` edge `0.0468` maxDD `-3.7119`
- `market_context_high->fx_4h` score `-0.979` n `202` status `ready` deltaP `-3.5438` edge `-0.009` maxDD `-1.4313`
- `market_context_high->commodity_1h` score `-1.1152` n `202` status `ready` deltaP `-0.2994` edge `0.0012` maxDD `-4.7041`
- `market_context_high->metal_4h` score `-1.3259` n `202` status `ready` deltaP `10.7387` edge `0.0871` maxDD `-12.5349`
- `market_context_high->crypto_major_1h` score `-1.5569` n `202` status `ready` deltaP `-1.1635` edge `0.0137` maxDD `-6.1883`
- `market_context_high->commodity_4h` score `-4.2694` n `202` status `ready` deltaP `-13.7451` edge `-0.0841` maxDD `-17.3969`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
