# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-21T17:37:17.760632+00:00`
- Price records: `672`
- Market context records: `1445`
- Flow alert records: `6072`
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

- `market_context_high->crypto_alt_24h` score `12.6411` n `155` status `ready` deltaP `28.7937` edge `1.0631` maxDD `-15.1306`
- `market_context_high->metal_24h` score `12.1116` n `155` status `ready` deltaP `14.0278` edge `1.0825` maxDD `-6.3373`
- `market_context_high->crypto_major_24h` score `11.6776` n `155` status `ready` deltaP `27.379` edge `0.9038` maxDD `-8.0553`
- `market_context_high->index_24h` score `4.2524` n `155` status `ready` deltaP `19.4399` edge `0.3334` maxDD `-5.3574`
- `market_context_high->equity_24h` score `3.7989` n `155` status `ready` deltaP `12.5941` edge `0.4653` maxDD `-14.2815`
- `market_context_high->equity_4h` score `1.3865` n `217` status `ready` deltaP `7.0101` edge `0.1518` maxDD `-3.6396`
- `market_context_high->fx_24h` score `0.2324` n `155` status `ready` deltaP `10.7504` edge `0.0526` maxDD `-1.3925`
- `market_context_high->index_1h` score `-0.1739` n `225` status `ready` deltaP `3.362` edge `0.0096` maxDD `-1.7205`
- `market_context_high->equity_1h` score `-0.2013` n `225` status `ready` deltaP `1.8509` edge `0.0309` maxDD `-2.8014`
- `market_context_high->index_4h` score `-0.6087` n `217` status `ready` deltaP `0.3709` edge `0.0557` maxDD `-3.7119`
- `market_context_high->commodity_1h` score `-0.6535` n `225` status `ready` deltaP `-0.5216` edge `0.0105` maxDD `-2.252`
- `market_context_high->fx_1h` score `-0.7105` n `225` status `ready` deltaP `0.9474` edge `-0.0023` maxDD `-0.3914`
- `market_context_high->crypto_alt_4h` score `-0.7524` n `217` status `ready` deltaP `9.9535` edge `0.2029` maxDD `-19.5565`
- `market_context_high->crypto_alt_1h` score `-0.7868` n `225` status `ready` deltaP `1.0646` edge `0.0297` maxDD `-4.1892`
- `market_context_high->fx_4h` score `-1.0853` n `217` status `ready` deltaP `-4.8282` edge `-0.0099` maxDD `-1.4313`
- `market_context_high->crypto_major_4h` score `-1.1586` n `217` status `ready` deltaP `5.3452` edge `0.1387` maxDD `-13.3376`
- `market_context_high->metal_1h` score `-1.243` n `225` status `ready` deltaP `4.6201` edge `-0.0008` maxDD `-6.3532`
- `market_context_high->crypto_major_1h` score `-1.7788` n `225` status `ready` deltaP `-1.5975` edge `-0.0019` maxDD `-6.1883`
- `market_context_high->metal_4h` score `-2.2074` n `217` status `ready` deltaP `6.845` edge `0.0396` maxDD `-12.5349`
- `market_context_high->commodity_4h` score `-2.8165` n `217` status `ready` deltaP `-10.833` edge `-0.0342` maxDD `-8.04`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
