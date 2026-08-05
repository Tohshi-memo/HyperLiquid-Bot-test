# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-05T14:44:00.428501+00:00`
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

- `market_context_high->unknown_24h` score `13.7405` n `89` status `ready` deltaP `7.7306` edge `1.0978` maxDD `-0.0103`
- `market_context_high->unknown_4h` score `4.5665` n `98` status `ready` deltaP `1.5275` edge `0.4699` maxDD `-3.6303`
- `market_context_high->commodity_4h` score `1.4807` n `98` status `ready` deltaP `15.9034` edge `0.102` maxDD `-2.7703`
- `market_context_high->fx_24h` score `1.0496` n `89` status `ready` deltaP `25.9715` edge `0.082` maxDD `-4.3126`
- `market_context_high->metal_24h` score `0.869` n `89` status `ready` deltaP `1.6268` edge `0.2174` maxDD `-2.6802`
- `market_context_high->commodity_1h` score `0.4353` n `100` status `ready` deltaP `7.6467` edge `0.0269` maxDD `-1.3282`
- `market_context_high->fx_1h` score `0.0143` n `100` status `ready` deltaP `5.9042` edge `-0.0032` maxDD `-0.7973`
- `market_context_high->fx_4h` score `-0.0822` n `98` status `ready` deltaP `10.3441` edge `0.0065` maxDD `-1.8797`
- `market_context_high->metal_1h` score `-0.5226` n `100` status `ready` deltaP `-1.5389` edge `-0.0073` maxDD `-1.6224`
- `market_context_high->index_1h` score `-0.681` n `100` status `ready` deltaP `-2.1317` edge `-0.0197` maxDD `-1.6054`
- `market_context_high->metal_4h` score `-0.8834` n `98` status `ready` deltaP `1.7266` edge `-0.0013` maxDD `-3.211`
- `market_context_high->crypto_alt_1h` score `-1.4995` n `100` status `ready` deltaP `-4.5449` edge `-0.0236` maxDD `-3.0178`
- `market_context_high->crypto_alt_24h` score `-1.5144` n `89` status `ready` deltaP `0.5032` edge `-0.0532` maxDD `-4.5445`
- `market_context_high->crypto_alt_4h` score `-1.7083` n `98` status `ready` deltaP `-2.0284` edge `-0.0665` maxDD `-5.7857`
- `market_context_high->equity_1h` score `-1.7852` n `100` status `ready` deltaP `2.6707` edge `-0.0931` maxDD `-10.619`
- `market_context_high->index_4h` score `-2.0268` n `98` status `ready` deltaP `-11.2805` edge `-0.0592` maxDD `-4.7021`
- `market_context_high->index_24h` score `-2.5932` n `89` status `ready` deltaP `-11.9968` edge `-0.033` maxDD `-7.8922`
- `market_context_high->unknown_1h` score `-3.1071` n `100` status `ready` deltaP `5.4551` edge `-0.2506` maxDD `-1.2421`
- `market_context_high->crypto_major_1h` score `-3.5415` n `100` status `ready` deltaP `-12.4491` edge `-0.0748` maxDD `-7.6533`
- `market_context_high->commodity_24h` score `-5.9983` n `89` status `ready` deltaP `11.1716` edge `-0.0285` maxDD `-50.8663`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
