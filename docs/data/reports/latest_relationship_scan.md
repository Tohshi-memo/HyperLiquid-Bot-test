# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-22T06:18:15.341735+00:00`
- Price records: `672`
- Market context records: `1500`
- Flow alert records: `6229`
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

- `market_context_high->metal_24h` score `13.1195` n `168` status `ready` deltaP `22.371` edge `1.0442` maxDD `-6.3373`
- `market_context_high->crypto_alt_24h` score `11.1927` n `168` status `ready` deltaP `28.9435` edge `0.9414` maxDD `-15.1306`
- `market_context_high->crypto_major_24h` score `10.3011` n `168` status `ready` deltaP `27.2569` edge `0.7899` maxDD `-8.0553`
- `market_context_high->index_24h` score `3.8199` n `168` status `ready` deltaP `20.1389` edge `0.2927` maxDD `-5.3574`
- `market_context_high->equity_24h` score `2.9304` n `168` status `ready` deltaP `13.3929` edge `0.3876` maxDD `-14.2815`
- `market_context_high->equity_4h` score `1.1305` n `194` status `ready` deltaP `6.4355` edge `0.1343` maxDD `-3.6396`
- `market_context_high->fx_24h` score `0.9942` n `168` status `ready` deltaP `19.494` edge `0.0578` maxDD `-1.3925`
- `market_context_high->index_1h` score `-0.2219` n `194` status `ready` deltaP `2.9725` edge `0.0082` maxDD `-1.7205`
- `market_context_high->equity_1h` score `-0.2702` n `194` status `ready` deltaP `1.1096` edge `0.0301` maxDD `-2.8014`
- `market_context_high->fx_1h` score `-0.539` n `194` status `ready` deltaP `-0.4167` edge `-0.0031` maxDD `-0.3914`
- `market_context_high->crypto_alt_1h` score `-0.5994` n `194` status `ready` deltaP `1.4121` edge `0.043` maxDD `-4.1892`
- `market_context_high->crypto_alt_4h` score `-0.7172` n `194` status `ready` deltaP `9.6131` edge `0.2081` maxDD `-19.5565`
- `market_context_high->metal_1h` score `-0.7249` n `194` status `ready` deltaP `5.7519` edge `0.0023` maxDD `-6.3532`
- `market_context_high->crypto_major_4h` score `-0.9283` n `194` status `ready` deltaP `5.5837` edge `0.1563` maxDD `-13.3376`
- `market_context_high->fx_4h` score `-0.9772` n `194` status `ready` deltaP `-3.4479` edge `-0.0094` maxDD `-1.4313`
- `market_context_high->crypto_major_1h` score `-1.0221` n `194` status `ready` deltaP `-1.1482` edge `0.0123` maxDD `-6.1883`
- `market_context_high->index_4h` score `-1.0851` n `194` status `ready` deltaP `-2.7344` edge `0.0367` maxDD `-3.7119`
- `market_context_high->metal_4h` score `-1.1471` n `194` status `ready` deltaP `11.6089` edge `0.0962` maxDD `-12.5349`
- `market_context_high->commodity_1h` score `-1.2768` n `194` status `ready` deltaP `-1.3303` edge `-0.0054` maxDD `-4.7041`
- `market_context_high->commodity_4h` score `-4.4045` n `194` status `ready` deltaP `-14.9924` edge `-0.0931` maxDD `-17.3969`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
