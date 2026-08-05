# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-05T12:52:36.243377+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11664`

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

- `market_context_high->unknown_24h` score `13.9162` n `89` status `ready` deltaP `8.7722` edge `1.1055` maxDD `-0.0103`
- `market_context_high->unknown_4h` score `5.3599` n `93` status `ready` deltaP `2.6259` edge `0.5287` maxDD `-3.6303`
- `market_context_high->commodity_4h` score `1.7771` n `93` status `ready` deltaP `18.1829` edge `0.1115` maxDD `-2.7703`
- `market_context_high->fx_24h` score `1.1401` n `89` status `ready` deltaP `27.1867` edge `0.0855` maxDD `-4.3126`
- `market_context_high->metal_24h` score `0.8768` n `89` status `ready` deltaP `1.6268` edge `0.2184` maxDD `-2.6802`
- `market_context_high->commodity_1h` score `0.4741` n `98` status `ready` deltaP `7.7417` edge `0.0295` maxDD `-1.3282`
- `market_context_high->fx_1h` score `0.0851` n `98` status `ready` deltaP `6.7885` edge `-0.0032` maxDD `-0.7973`
- `market_context_high->fx_4h` score `0.0327` n `93` status `ready` deltaP `12.4935` edge `0.0069` maxDD `-1.8797`
- `market_context_high->metal_1h` score `-0.5739` n `98` status `ready` deltaP `-2.0286` edge `-0.0106` maxDD `-1.6224`
- `market_context_high->index_1h` score `-0.6737` n `98` status `ready` deltaP `-2.1111` edge `-0.0189` maxDD `-1.6054`
- `market_context_high->metal_4h` score `-0.9195` n `93` status `ready` deltaP `1.5424` edge `-0.0047` maxDD `-3.211`
- `market_context_high->crypto_alt_1h` score `-0.9721` n `98` status `ready` deltaP `-4.5857` edge `-0.023` maxDD `-3.0178`
- `market_context_high->crypto_alt_24h` score `-1.4664` n `89` status `ready` deltaP `0.6768` edge `-0.0482` maxDD `-4.5445`
- `market_context_high->crypto_alt_4h` score `-1.5813` n `93` status `ready` deltaP `-0.6655` edge `-0.0593` maxDD `-5.7857`
- `market_context_high->equity_1h` score `-1.7824` n `98` status `ready` deltaP `2.5144` edge `-0.0917` maxDD `-10.619`
- `market_context_high->index_4h` score `-2.1589` n `93` status `ready` deltaP `-13.2065` edge `-0.0633` maxDD `-4.7021`
- `market_context_high->index_24h` score `-2.522` n `89` status `ready` deltaP `-11.3023` edge `-0.0285` maxDD `-7.8922`
- `market_context_high->unknown_1h` score `-3.1385` n `98` status `ready` deltaP `4.7477` edge `-0.2485` maxDD `-1.2421`
- `market_context_high->crypto_major_1h` score `-3.6692` n `98` status `ready` deltaP `-13.5647` edge `-0.078` maxDD `-7.6533`
- `market_context_high->commodity_24h` score `-6.0093` n `89` status `ready` deltaP `11.1716` edge `-0.0299` maxDD `-50.8663`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
