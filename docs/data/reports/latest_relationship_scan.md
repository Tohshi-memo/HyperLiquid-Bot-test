# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-21T17:07:16.649932+00:00`
- Price records: `672`
- Market context records: `1442`
- Flow alert records: `6066`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8798`

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

- `market_context_high->crypto_alt_24h` score `12.5117` n `154` status `ready` deltaP `28.7811` edge `1.0524` maxDD `-15.1306`
- `market_context_high->metal_24h` score `12.19` n `154` status `ready` deltaP `13.8979` edge `1.0899` maxDD `-6.3373`
- `market_context_high->crypto_major_24h` score `11.6204` n `154` status `ready` deltaP `27.3539` edge `0.8992` maxDD `-8.0553`
- `market_context_high->index_24h` score `4.2189` n `154` status `ready` deltaP `19.3813` edge `0.331` maxDD `-5.3574`
- `market_context_high->equity_24h` score `3.6783` n `154` status `ready` deltaP `12.5271` edge `0.4557` maxDD `-14.2815`
- `market_context_high->equity_4h` score `1.3042` n `215` status `ready` deltaP `6.8215` edge `0.1462` maxDD `-3.6396`
- `market_context_high->fx_24h` score `0.2092` n `154` status `ready` deltaP `10.4009` edge `0.053` maxDD `-1.3925`
- `market_context_high->index_1h` score `-0.132` n `225` status `ready` deltaP `3.6614` edge `0.0111` maxDD `-1.7205`
- `market_context_high->equity_1h` score `-0.1414` n `225` status `ready` deltaP `2.1503` edge `0.0339` maxDD `-2.8014`
- `market_context_high->index_4h` score `-0.662` n `215` status `ready` deltaP `0.0794` edge `0.0532` maxDD `-3.7119`
- `market_context_high->crypto_alt_1h` score `-0.7137` n `225` status `ready` deltaP `1.364` edge `0.0338` maxDD `-4.1892`
- `market_context_high->commodity_1h` score `-0.7159` n `225` status `ready` deltaP `-0.821` edge `0.0073` maxDD `-2.252`
- `market_context_high->fx_1h` score `-0.7357` n `225` status `ready` deltaP `0.648` edge `-0.0024` maxDD `-0.3914`
- `market_context_high->crypto_alt_4h` score `-0.8822` n `215` status `ready` deltaP `9.6363` edge `0.1942` maxDD `-19.5565`
- `market_context_high->fx_4h` score `-1.0787` n `215` status `ready` deltaP `-4.7001` edge `-0.0099` maxDD `-1.4313`
- `market_context_high->metal_1h` score `-1.1938` n `225` status `ready` deltaP `4.9195` edge `0.0013` maxDD `-6.3532`
- `market_context_high->crypto_major_4h` score `-1.2292` n `215` status `ready` deltaP `5.1375` edge `0.1342` maxDD `-13.3376`
- `market_context_high->crypto_major_1h` score `-1.7153` n `225` status `ready` deltaP `-1.2981` edge `0.0014` maxDD `-6.1883`
- `market_context_high->metal_4h` score `-2.3598` n `215` status `ready` deltaP `6.4549` edge `0.0295` maxDD `-12.5349`
- `market_context_high->commodity_4h` score `-4.1746` n `215` status `ready` deltaP `-10.4729` edge `-0.0234` maxDD `-8.04`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
