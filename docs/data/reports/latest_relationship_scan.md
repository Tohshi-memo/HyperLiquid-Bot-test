# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-03T08:22:26.554843+00:00`
- Price records: `672`
- Market context records: `2746`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9237`

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

- `market_context_high->unknown_24h` score `7.5155` n `116` status `ready` deltaP `15.3317` edge `0.5569` maxDD `-1.6255`
- `market_context_high->crypto_alt_24h` score `6.0555` n `116` status `ready` deltaP `13.4399` edge `1.0361` maxDD `-19.9486`
- `market_context_high->unknown_4h` score `0.9967` n `143` status `ready` deltaP `6.5539` edge `0.1447` maxDD `-3.7602`
- `market_context_high->index_4h` score `0.1484` n `143` status `ready` deltaP `10.8563` edge `0.0308` maxDD `-2.3986`
- `market_context_high->unknown_1h` score `-0.0992` n `143` status `ready` deltaP `3.4976` edge `0.0415` maxDD `-3.1801`
- `market_context_high->index_1h` score `-0.1643` n `143` status `ready` deltaP `3.0506` edge `0.008` maxDD `-1.2855`
- `market_context_high->fx_1h` score `-0.5219` n `143` status `ready` deltaP `-0.3475` edge `0.0032` maxDD `-0.2164`
- `market_context_high->crypto_alt_1h` score `-0.629` n `143` status `ready` deltaP `5.9954` edge `0.0554` maxDD `-10.747`
- `market_context_high->commodity_1h` score `-0.6776` n `143` status `ready` deltaP `-0.5464` edge `-0.0079` maxDD `-4.3601`
- `market_context_high->metal_1h` score `-0.7255` n `143` status `ready` deltaP `-0.8009` edge `-0.0031` maxDD `-3.0996`
- `market_context_high->crypto_major_1h` score `-0.9534` n `143` status `ready` deltaP `3.6473` edge `0.0404` maxDD `-9.622`
- `market_context_high->crypto_alt_4h` score `-0.9546` n `143` status `ready` deltaP `15.7535` edge `0.2495` maxDD `-28.7261`
- `market_context_high->fx_4h` score `-1.1601` n `143` status `ready` deltaP `-3.9453` edge `0.0075` maxDD `-0.5631`
- `market_context_high->fx_24h` score `-1.2402` n `116` status `ready` deltaP `0.006` edge `-0.0162` maxDD `-0.6418`
- `market_context_high->equity_1h` score `-1.2627` n `143` status `ready` deltaP `-4.6846` edge `0.0093` maxDD `-2.6634`
- `market_context_high->commodity_24h` score `-1.3334` n `116` status `ready` deltaP `4.2504` edge `0.1101` maxDD `-12.4171`
- `market_context_high->commodity_4h` score `-1.6069` n `143` status `ready` deltaP `-0.3155` edge `-0.0119` maxDD `-10.0279`
- `market_context_high->crypto_major_24h` score `-1.9413` n `116` status `ready` deltaP `4.1487` edge `0.7162` maxDD `-61.4192`
- `market_context_high->equity_4h` score `-2.0171` n `143` status `ready` deltaP `-1.2493` edge `-0.0218` maxDD `-5.7037`
- `market_context_high->metal_4h` score `-2.3784` n `143` status `ready` deltaP `-2.1864` edge `-0.0353` maxDD `-11.4038`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
