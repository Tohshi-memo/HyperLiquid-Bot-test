# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-21T14:22:25.831783+00:00`
- Price records: `672`
- Market context records: `1430`
- Flow alert records: `6032`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8796`

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

- `market_context_high->crypto_alt_24h` score `11.9285` n `154` status `ready` deltaP `28.7811` edge `1.0038` maxDD `-15.1306`
- `market_context_high->metal_24h` score `11.8437` n `154` status `ready` deltaP `12.509` edge `1.0703` maxDD `-6.3373`
- `market_context_high->crypto_major_24h` score `11.72` n `154` status `ready` deltaP `27.3539` edge `0.9075` maxDD `-8.0553`
- `market_context_high->index_24h` score `3.9081` n `154` status `ready` deltaP `19.3813` edge `0.3051` maxDD `-5.3574`
- `market_context_high->equity_24h` score `2.9631` n `154` status `ready` deltaP `12.5271` edge `0.3961` maxDD `-14.2815`
- `market_context_high->equity_4h` score `0.9963` n `204` status `ready` deltaP `5.718` edge `0.1279` maxDD `-3.6396`
- `market_context_high->fx_24h` score `0.1026` n `154` status `ready` deltaP `9.5329` edge `0.0499` maxDD `-1.3925`
- `market_context_high->index_1h` score `-0.1942` n `216` status `ready` deltaP `2.9885` edge `0.0104` maxDD `-1.7205`
- `market_context_high->equity_1h` score `-0.2918` n `216` status `ready` deltaP `2.1457` edge `0.0214` maxDD `-2.8014`
- `market_context_high->fx_1h` score `-0.6139` n `216` status `ready` deltaP `0.9952` edge `-0.0029` maxDD `-0.3914`
- `market_context_high->index_4h` score `-0.6514` n `204` status `ready` deltaP `0.0627` edge `0.0542` maxDD `-3.7119`
- `market_context_high->commodity_1h` score `-0.6716` n `216` status `ready` deltaP `-0.7624` edge `0.0106` maxDD `-2.252`
- `market_context_high->crypto_alt_1h` score `-0.8251` n `216` status `ready` deltaP `1.0507` edge `0.0266` maxDD `-4.1892`
- `market_context_high->metal_1h` score `-0.9435` n `216` status `ready` deltaP `3.8423` edge `-0.013` maxDD `-6.3532`
- `market_context_high->crypto_alt_4h` score `-1.2009` n `204` status `ready` deltaP `7.9328` edge `0.179` maxDD `-19.5565`
- `market_context_high->crypto_major_4h` score `-1.3872` n `204` status `ready` deltaP `4.7076` edge `0.1239` maxDD `-13.3376`
- `market_context_high->fx_4h` score `-1.5826` n `204` status `ready` deltaP `-3.8439` edge `-0.0092` maxDD `-1.4313`
- `market_context_high->crypto_major_1h` score `-1.8203` n `216` status `ready` deltaP `-1.7409` edge `-0.0044` maxDD `-6.1883`
- `market_context_high->commodity_4h` score `-2.6696` n `204` status `ready` deltaP `-10.3927` edge `-0.0183` maxDD `-8.04`
- `market_context_high->metal_4h` score `-2.8286` n `204` status `ready` deltaP `4.5104` edge `0.0034` maxDD `-12.5349`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
