# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-21T14:52:18.305641+00:00`
- Price records: `672`
- Market context records: `1432`
- Flow alert records: `6038`
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

- `market_context_high->crypto_alt_24h` score `12.0485` n `154` status `ready` deltaP `28.7811` edge `1.0138` maxDD `-15.1306`
- `market_context_high->metal_24h` score `11.9399` n `154` status `ready` deltaP `12.8562` edge `1.076` maxDD `-6.3373`
- `market_context_high->crypto_major_24h` score `11.702` n `154` status `ready` deltaP `27.3539` edge `0.906` maxDD `-8.0553`
- `market_context_high->index_24h` score `3.9681` n `154` status `ready` deltaP `19.3813` edge `0.3101` maxDD `-5.3574`
- `market_context_high->equity_24h` score `3.1095` n `154` status `ready` deltaP `12.5271` edge `0.4083` maxDD `-14.2815`
- `market_context_high->equity_4h` score `1.0299` n `206` status `ready` deltaP `5.9274` edge `0.1293` maxDD `-3.6396`
- `market_context_high->fx_24h` score `0.1248` n `154` status `ready` deltaP `9.7065` edge `0.0506` maxDD `-1.3925`
- `market_context_high->index_1h` score `-0.2003` n `218` status `ready` deltaP `3.0023` edge `0.0098` maxDD `-1.7205`
- `market_context_high->equity_1h` score `-0.3143` n `218` status `ready` deltaP `1.8334` edge `0.0216` maxDD `-2.8014`
- `market_context_high->index_4h` score `-0.654` n `206` status `ready` deltaP `0.0296` edge `0.0542` maxDD `-3.7119`
- `market_context_high->fx_1h` score `-0.6794` n `218` status `ready` deltaP `0.8158` edge `-0.003` maxDD `-0.3914`
- `market_context_high->commodity_1h` score `-0.694` n `218` status `ready` deltaP `-0.7581` edge `0.0087` maxDD `-2.252`
- `market_context_high->crypto_alt_1h` score `-0.7881` n `218` status `ready` deltaP `1.1537` edge `0.029` maxDD `-4.1892`
- `market_context_high->metal_1h` score `-0.9218` n `218` status `ready` deltaP `3.9156` edge `-0.0107` maxDD `-6.3532`
- `market_context_high->crypto_alt_4h` score `-1.1619` n `206` status `ready` deltaP `8.285` edge `0.1799` maxDD `-19.5565`
- `market_context_high->crypto_major_4h` score `-1.3592` n `206` status `ready` deltaP `4.8026` edge `0.1256` maxDD `-13.3376`
- `market_context_high->fx_4h` score `-1.5979` n `206` status `ready` deltaP `-4.0197` edge `-0.0093` maxDD `-1.4313`
- `market_context_high->crypto_major_1h` score `-1.737` n `218` status `ready` deltaP `-1.2992` edge `-0.0004` maxDD `-6.1883`
- `market_context_high->metal_4h` score `-1.7898` n `206` status `ready` deltaP `4.9387` edge `0.0068` maxDD `-12.5349`
- `market_context_high->commodity_4h` score `-4.1305` n `206` status `ready` deltaP `-10.431` edge `-0.02` maxDD `-8.04`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
