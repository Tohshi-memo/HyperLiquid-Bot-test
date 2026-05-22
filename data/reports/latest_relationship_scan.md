# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-22T06:07:15.737586+00:00`
- Price records: `672`
- Market context records: `1499`
- Flow alert records: `6227`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8791`

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

- `market_context_high->metal_24h` score `12.9862` n `169` status `ready` deltaP `21.9952` edge `1.0356` maxDD `-6.3373`
- `market_context_high->crypto_alt_24h` score `11.2247` n `169` status `ready` deltaP `28.9541` edge `0.944` maxDD `-15.1306`
- `market_context_high->crypto_major_24h` score `10.273` n `169` status `ready` deltaP `27.2816` edge `0.7874` maxDD `-8.0553`
- `market_context_high->index_24h` score `3.8322` n `169` status `ready` deltaP `20.1882` edge `0.2934` maxDD `-5.3574`
- `market_context_high->equity_24h` score `2.9745` n `169` status `ready` deltaP `13.4492` edge `0.3909` maxDD `-14.2815`
- `market_context_high->equity_4h` score `1.1506` n `195` status `ready` deltaP `6.5518` edge `0.1352` maxDD `-3.6396`
- `market_context_high->fx_24h` score `0.9941` n `169` status `ready` deltaP `19.5821` edge `0.0572` maxDD `-1.3925`
- `market_context_high->index_1h` score `-0.2533` n `195` status `ready` deltaP `2.6394` edge `0.0078` maxDD `-1.7205`
- `market_context_high->equity_1h` score `-0.2724` n `195` status `ready` deltaP `1.1423` edge `0.0297` maxDD `-2.8014`
- `market_context_high->fx_1h` score `-0.5452` n `195` status `ready` deltaP `-0.5366` edge `-0.0031` maxDD `-0.3914`
- `market_context_high->crypto_alt_1h` score `-0.6352` n `195` status `ready` deltaP `1.1293` edge `0.0419` maxDD `-4.1892`
- `market_context_high->crypto_alt_4h` score `-0.6417` n `195` status `ready` deltaP `9.7928` edge `0.2132` maxDD `-19.5565`
- `market_context_high->metal_1h` score `-0.7525` n `195` status `ready` deltaP `5.4453` edge `0.0008` maxDD `-6.3532`
- `market_context_high->crypto_major_4h` score `-0.8967` n `195` status `ready` deltaP `5.6348` edge `0.1586` maxDD `-13.3376`
- `market_context_high->fx_4h` score `-0.9819` n `195` status `ready` deltaP `-3.5546` edge `-0.0093` maxDD `-1.4313`
- `market_context_high->crypto_major_1h` score `-1.0499` n `195` status `ready` deltaP `-1.4125` edge `0.0105` maxDD `-6.1883`
- `market_context_high->index_4h` score `-1.0552` n `195` status `ready` deltaP `-2.5547` edge `0.038` maxDD `-3.7119`
- `market_context_high->metal_4h` score `-1.1293` n `195` status `ready` deltaP `11.8019` edge `0.0964` maxDD `-12.5349`
- `market_context_high->commodity_1h` score `-1.2439` n `195` status `ready` deltaP `-1.0686` edge `-0.0044` maxDD `-4.7041`
- `market_context_high->commodity_4h` score `-4.4059` n `195` status `ready` deltaP `-15.0039` edge `-0.0932` maxDD `-17.3969`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
