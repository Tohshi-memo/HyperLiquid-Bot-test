# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-21T07:07:15.300381+00:00`
- Price records: `672`
- Market context records: `1400`
- Flow alert records: `5944`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8784`

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

- `market_context_high->crypto_major_24h` score `12.5846` n `156` status `ready` deltaP `27.751` edge `0.9769` maxDD `-8.0553`
- `market_context_high->crypto_alt_24h` score `11.4673` n `156` status `ready` deltaP `28.8061` edge `0.9652` maxDD `-15.1306`
- `market_context_high->metal_24h` score `11.2966` n `156` status `ready` deltaP `11.2046` edge `1.0334` maxDD `-6.3373`
- `market_context_high->index_24h` score `3.8826` n `156` status `ready` deltaP `19.4978` edge `0.3022` maxDD `-5.3574`
- `market_context_high->equity_24h` score `2.243` n `156` status `ready` deltaP `12.6603` edge `0.3352` maxDD `-14.2815`
- `market_context_high->equity_4h` score `1.3066` n `195` status `ready` deltaP `7.6469` edge `0.1409` maxDD `-3.6396`
- `market_context_high->fx_24h` score `0.0518` n `156` status `ready` deltaP `9.7088` edge `0.0445` maxDD `-1.3925`
- `market_context_high->index_1h` score `-0.0121` n `204` status `ready` deltaP `4.6496` edge `0.0145` maxDD `-1.7205`
- `market_context_high->equity_1h` score `-0.0703` n `204` status `ready` deltaP `3.0439` edge `0.0297` maxDD `-2.8014`
- `market_context_high->fx_1h` score `-0.2621` n `204` status `ready` deltaP `3.9773` edge `-0.0018` maxDD `-0.3914`
- `market_context_high->index_4h` score `-0.594` n `195` status `ready` deltaP `0.4948` edge `0.0561` maxDD `-3.7119`
- `market_context_high->metal_1h` score `-0.6741` n `204` status `ready` deltaP `5.2307` edge `-0.0038` maxDD `-5.0663`
- `market_context_high->crypto_alt_1h` score `-0.7681` n `204` status `ready` deltaP `0.2613` edge `0.0213` maxDD `-3.6309`
- `market_context_high->commodity_1h` score `-0.8992` n `204` status `ready` deltaP `-1.6878` edge `-0.0022` maxDD `-2.252`
- `market_context_high->crypto_major_4h` score `-1.485` n `195` status `ready` deltaP `4.595` edge `0.1165` maxDD `-13.3376`
- `market_context_high->crypto_major_1h` score `-1.4909` n `204` status `ready` deltaP `-1.6731` edge `-0.0024` maxDD `-6.1883`
- `market_context_high->fx_4h` score `-1.4978` n `195` status `ready` deltaP `-2.8893` edge `-0.0085` maxDD `-1.4313`
- `market_context_high->crypto_alt_4h` score `-1.5694` n `195` status `ready` deltaP `6.1758` edge `0.16` maxDD `-19.5565`
- `market_context_high->metal_4h` score `-1.6634` n `195` status `ready` deltaP `6.5767` edge `0.014` maxDD `-9.3833`
- `market_context_high->commodity_4h` score `-4.1785` n `195` status `ready` deltaP `-11.1367` edge `-0.0193` maxDD `-8.04`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
