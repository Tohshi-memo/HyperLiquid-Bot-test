# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-21T09:22:21.226012+00:00`
- Price records: `672`
- Market context records: `1410`
- Flow alert records: `5971`
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

- `market_context_high->crypto_major_24h` score `11.9796` n `156` status `ready` deltaP `27.4038` edge `0.9288` maxDD `-8.0553`
- `market_context_high->crypto_alt_24h` score `11.4937` n `156` status `ready` deltaP `28.8061` edge `0.9674` maxDD `-15.1306`
- `market_context_high->metal_24h` score `11.1606` n `156` status `ready` deltaP `10.5101` edge `1.0267` maxDD `-6.3373`
- `market_context_high->index_24h` score `3.7854` n `156` status `ready` deltaP `19.4978` edge `0.2941` maxDD `-5.3574`
- `market_context_high->equity_24h` score `2.2838` n `156` status `ready` deltaP `12.6603` edge `0.3386` maxDD `-14.2815`
- `market_context_high->equity_4h` score `0.8261` n `204` status `ready` deltaP `5.0753` edge `0.118` maxDD `-3.6396`
- `market_context_high->fx_24h` score `0.0674` n `156` status `ready` deltaP `9.7088` edge `0.0458` maxDD `-1.3925`
- `market_context_high->index_1h` score `-0.1236` n `204` status `ready` deltaP `3.9011` edge `0.0102` maxDD `-1.7205`
- `market_context_high->equity_1h` score `-0.2154` n `204` status `ready` deltaP `2.2954` edge `0.0226` maxDD `-2.8014`
- `market_context_high->fx_1h` score `-0.2477` n `204` status `ready` deltaP `4.127` edge `-0.0016` maxDD `-0.3914`
- `market_context_high->crypto_alt_1h` score `-0.731` n `204` status `ready` deltaP `0.411` edge `0.0234` maxDD `-3.6309`
- `market_context_high->commodity_1h` score `-0.7409` n `204` status `ready` deltaP `-0.9393` edge `0.006` maxDD `-2.252`
- `market_context_high->metal_1h` score `-0.7731` n `204` status `ready` deltaP `4.3325` edge `-0.0105` maxDD `-5.0663`
- `market_context_high->index_4h` score `-0.9043` n `204` status `ready` deltaP `-1.6141` edge `0.0443` maxDD `-3.7119`
- `market_context_high->crypto_major_4h` score `-1.4576` n `204` status `ready` deltaP `5.0125` edge `0.116` maxDD `-13.3376`
- `market_context_high->crypto_alt_4h` score `-1.5244` n `204` status `ready` deltaP `6.4084` edge `0.1622` maxDD `-19.5565`
- `market_context_high->crypto_major_1h` score `-1.5688` n `204` status `ready` deltaP `-2.1222` edge `-0.0059` maxDD `-6.1883`
- `market_context_high->fx_4h` score `-1.5984` n `204` status `ready` deltaP `-3.9963` edge `-0.0095` maxDD `-1.4313`
- `market_context_high->commodity_4h` score `-2.5952` n `204` status `ready` deltaP `-10.0879` edge `-0.0108` maxDD `-8.04`
- `market_context_high->metal_4h` score `-2.8339` n `204` status `ready` deltaP `4.358` edge `-0.0054` maxDD `-11.7852`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
