# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-05T15:37:37.751918+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11668`

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

- `market_context_high->unknown_24h` score `13.4303` n `90` status `ready` deltaP `7.0486` edge `1.0765` maxDD `-0.0103`
- `market_context_high->unknown_4h` score `4.5411` n `98` status `ready` deltaP `1.3751` edge `0.4688` maxDD `-3.6303`
- `market_context_high->commodity_4h` score `1.5157` n `98` status `ready` deltaP `16.0559` edge `0.1039` maxDD `-2.7703`
- `market_context_high->fx_24h` score `1.0209` n `90` status `ready` deltaP `25.7639` edge `0.0797` maxDD `-4.3126`
- `market_context_high->metal_24h` score `0.925` n `90` status `ready` deltaP `2.0139` edge `0.222` maxDD `-2.6802`
- `market_context_high->commodity_1h` score `0.409` n `100` status `ready` deltaP `7.3473` edge `0.0267` maxDD `-1.3282`
- `market_context_high->fx_1h` score `-0.0` n `100` status `ready` deltaP `5.7545` edge `-0.0034` maxDD `-0.7973`
- `market_context_high->fx_4h` score `-0.0648` n `98` status `ready` deltaP `10.649` edge `0.0067` maxDD `-1.8797`
- `market_context_high->metal_1h` score `-0.5406` n `100` status `ready` deltaP `-1.8383` edge `-0.0076` maxDD `-1.6224`
- `market_context_high->index_1h` score `-0.6733` n `100` status `ready` deltaP `-1.982` edge `-0.0197` maxDD `-1.6054`
- `market_context_high->metal_4h` score `-0.8631` n `98` status `ready` deltaP `1.7266` edge `0.0013` maxDD `-3.211`
- `market_context_high->crypto_alt_24h` score `-1.4078` n `90` status `ready` deltaP `0.9027` edge `-0.0422` maxDD `-4.5445`
- `market_context_high->crypto_alt_1h` score `-1.5342` n `100` status `ready` deltaP `-4.8443` edge `-0.0245` maxDD `-3.0178`
- `market_context_high->crypto_alt_4h` score `-1.6754` n `98` status `ready` deltaP `-1.8759` edge `-0.0633` maxDD `-5.7857`
- `market_context_high->equity_1h` score `-1.8` n `100` status `ready` deltaP `2.521` edge `-0.094` maxDD `-10.619`
- `market_context_high->index_4h` score `-1.9977` n `98` status `ready` deltaP `-10.9756` edge `-0.0575` maxDD `-4.7021`
- `market_context_high->index_24h` score `-2.5717` n `90` status `ready` deltaP `-11.5973` edge `-0.0329` maxDD `-7.8922`
- `market_context_high->unknown_1h` score `-3.0915` n `100` status `ready` deltaP `5.6048` edge `-0.2503` maxDD `-1.2421`
- `market_context_high->crypto_major_1h` score `-3.5967` n `100` status `ready` deltaP `-12.8982` edge `-0.0764` maxDD `-7.6533`
- `market_context_high->commodity_24h` score `-6.0413` n `90` status `ready` deltaP `10.8334` edge `-0.0253` maxDD `-51.0493`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
