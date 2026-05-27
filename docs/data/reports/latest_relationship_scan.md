# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-27T14:07:27.733983+00:00`
- Price records: `672`
- Market context records: `2046`
- Flow alert records: `7784`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9105`

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

- `market_context_high->crypto_major_4h` score `9.112` n `205` status `ready` deltaP `32.0298` edge `0.5988` maxDD `-1.9063`
- `market_context_high->crypto_alt_4h` score `8.4495` n `205` status `ready` deltaP `24.5534` edge `0.6549` maxDD `-5.1574`
- `market_context_high->unknown_4h` score `6.2219` n `205` status `ready` deltaP `19.7709` edge `0.4616` maxDD `-2.6599`
- `market_context_high->equity_4h` score `3.0214` n `205` status `ready` deltaP `17.4498` edge `0.2449` maxDD `-5.0894`
- `market_context_high->unknown_24h` score `2.6331` n `205` status `ready` deltaP `17.5146` edge `0.6347` maxDD `-35.8966`
- `market_context_high->crypto_major_1h` score `1.6651` n `205` status `ready` deltaP `13.0765` edge `0.1502` maxDD `-3.2225`
- `market_context_high->index_4h` score `1.5716` n `205` status `ready` deltaP `13.5792` edge `0.1088` maxDD `-1.8022`
- `market_context_high->crypto_alt_1h` score `1.3097` n `205` status `ready` deltaP `10.2322` edge `0.1523` maxDD `-4.9097`
- `market_context_high->equity_24h` score `0.7927` n `205` status `ready` deltaP `17.0098` edge `0.4425` maxDD `-33.1875`
- `market_context_high->index_24h` score `0.6745` n `205` status `ready` deltaP `5.5118` edge `0.1423` maxDD `-4.1604`
- `market_context_high->equity_1h` score `0.3147` n `205` status `ready` deltaP `7.5092` edge `0.055` maxDD `-2.6402`
- `market_context_high->unknown_1h` score `0.1537` n `205` status `ready` deltaP `4.345` edge `0.0558` maxDD `-3.0902`
- `market_context_high->index_1h` score `-0.1803` n `205` status `ready` deltaP `3.4519` edge `0.021` maxDD `-1.3898`
- `market_context_high->fx_24h` score `-0.5083` n `205` status `ready` deltaP `11.1224` edge `0.0228` maxDD `-2.811`
- `market_context_high->metal_1h` score `-0.728` n `205` status `ready` deltaP `4.7064` edge `0.0267` maxDD `-5.166`
- `market_context_high->fx_1h` score `-0.7871` n `205` status `ready` deltaP `-0.5433` edge `0.0008` maxDD `-0.3548`
- `market_context_high->metal_4h` score `-0.9105` n `205` status `ready` deltaP `9.9289` edge `0.1202` maxDD `-11.9812`
- `market_context_high->crypto_major_24h` score `-1.2847` n `205` status `ready` deltaP `17.2234` edge `0.6367` maxDD `-62.3533`
- `market_context_high->fx_4h` score `-1.4185` n `205` status `ready` deltaP `-4.4355` edge `-0.0005` maxDD `-1.0513`
- `market_context_high->commodity_1h` score `-1.8971` n `205` status `ready` deltaP `2.1564` edge `-0.0018` maxDD `-15.7972`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
