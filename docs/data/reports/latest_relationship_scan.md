# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-21T17:52:17.221507+00:00`
- Price records: `672`
- Market context records: `1446`
- Flow alert records: `6075`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8808`

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

- `market_context_high->crypto_alt_24h` score `12.7405` n `156` status `ready` deltaP `28.8061` edge `1.0713` maxDD `-15.1306`
- `market_context_high->metal_24h` score `12.0523` n `156` status `ready` deltaP `14.156` edge `1.0767` maxDD `-6.3373`
- `market_context_high->crypto_major_24h` score `11.7492` n `156` status `ready` deltaP `27.4038` edge `0.9096` maxDD `-8.0553`
- `market_context_high->index_24h` score `4.2834` n `156` status `ready` deltaP `19.4978` edge `0.3356` maxDD `-5.3574`
- `market_context_high->equity_24h` score `3.9014` n `156` status `ready` deltaP `12.6603` edge `0.4734` maxDD `-14.2815`
- `market_context_high->equity_4h` score `1.4287` n `218` status `ready` deltaP `7.1031` edge `0.1547` maxDD `-3.6396`
- `market_context_high->fx_24h` score `0.2391` n `156` status `ready` deltaP `10.9241` edge `0.052` maxDD `-1.3925`
- `market_context_high->index_1h` score `-0.1507` n `226` status `ready` deltaP `3.3676` edge `0.0115` maxDD `-1.7205`
- `market_context_high->equity_1h` score `-0.1678` n `226` status `ready` deltaP `1.8507` edge `0.0337` maxDD `-2.8014`
- `market_context_high->fx_1h` score `-0.4509` n `226` status `ready` deltaP `1.1579` edge `-0.0023` maxDD `-0.3914`
- `market_context_high->index_4h` score `-0.584` n `218` status `ready` deltaP `0.5146` edge `0.0568` maxDD `-3.7119`
- `market_context_high->crypto_alt_4h` score `-0.6751` n `218` status `ready` deltaP `10.1099` edge `0.2083` maxDD `-19.5565`
- `market_context_high->crypto_alt_1h` score `-0.7147` n `226` status `ready` deltaP `1.2612` edge `0.0344` maxDD `-4.1892`
- `market_context_high->commodity_1h` score `-0.8554` n `226` status `ready` deltaP `-0.7419` edge `0.0057` maxDD `-3.0961`
- `market_context_high->fx_4h` score `-1.071` n `218` status `ready` deltaP `-4.583` edge `-0.0097` maxDD `-1.4313`
- `market_context_high->crypto_major_4h` score `-1.1242` n `218` status `ready` deltaP `5.3703` edge `0.1414` maxDD `-13.3376`
- `market_context_high->metal_1h` score `-1.2105` n `226` status `ready` deltaP `4.6513` edge `0.0017` maxDD `-6.3532`
- `market_context_high->crypto_major_1h` score `-1.7332` n `226` status `ready` deltaP `-1.5367` edge `0.0015` maxDD `-6.1883`
- `market_context_high->metal_4h` score `-2.138` n `218` status `ready` deltaP `7.0374` edge `0.0441` maxDD `-12.5349`
- `market_context_high->commodity_4h` score `-2.8663` n `218` status `ready` deltaP `-11.0106` edge `-0.0394` maxDD `-8.04`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
