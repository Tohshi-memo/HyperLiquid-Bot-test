# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-07T11:37:30.085264+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11739`

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

- `market_context_high->commodity_4h` score `1.1355` n `120` status `ready` deltaP `13.0284` edge `0.0924` maxDD `-2.7703`
- `market_context_high->commodity_1h` score `0.5266` n `120` status `ready` deltaP `8.3982` edge `0.0295` maxDD `-1.3282`
- `market_context_high->fx_24h` score `0.4279` n `113` status `ready` deltaP `19.175` edge `0.0476` maxDD `-4.3126`
- `market_context_high->metal_24h` score `0.2001` n `113` status `ready` deltaP `0.362` edge `0.1311` maxDD `-2.6802`
- `market_context_high->fx_1h` score `0.1122` n `120` status `ready` deltaP `7.7994` edge `-0.0026` maxDD `-0.8012`
- `market_context_high->fx_4h` score `-0.1839` n `120` status `ready` deltaP `8.6585` edge `0.0047` maxDD `-1.8797`
- `market_context_high->metal_1h` score `-0.6456` n `120` status `ready` deltaP `-3.4231` edge `-0.0105` maxDD `-1.6224`
- `market_context_high->crypto_alt_1h` score `-0.8238` n `120` status `ready` deltaP `-3.4431` edge `-0.0116` maxDD `-3.0178`
- `market_context_high->index_1h` score `-0.9976` n `120` status `ready` deltaP `-2.6746` edge `-0.0119` maxDD `-1.6054`
- `market_context_high->equity_1h` score `-1.2742` n `120` status `ready` deltaP `4.0968` edge `-0.0342` maxDD `-10.5179`
- `market_context_high->index_4h` score `-1.5275` n `120` status `ready` deltaP `-6.1484` edge `-0.0294` maxDD `-4.7021`
- `market_context_high->index_24h` score `-1.9077` n `113` status `ready` deltaP `-1.3931` edge `0.0698` maxDD `-7.8922`
- `market_context_high->metal_4h` score `-1.9227` n `120` status `ready` deltaP `-3.3232` edge `-0.0146` maxDD `-3.211`
- `market_context_high->crypto_alt_4h` score `-2.1573` n `120` status `ready` deltaP `0.437` edge `-0.0437` maxDD `-5.7857`
- `market_context_high->crypto_major_1h` score `-2.7053` n `120` status `ready` deltaP `-6.7515` edge `-0.0431` maxDD `-7.6533`
- `market_context_high->crypto_alt_24h` score `-3.6733` n `113` status `ready` deltaP `-9.8556` edge `-0.0961` maxDD `-4.5445`
- `market_context_high->commodity_24h` score `-5.9605` n `113` status `ready` deltaP `11.661` edge `0.0346` maxDD `-52.7876`
- `market_context_high->equity_4h` score `-5.9747` n `120` status `ready` deltaP `0.1931` edge `-0.2384` maxDD `-34.9766`
- `market_context_high->crypto_major_4h` score `-7.7126` n `120` status `ready` deltaP `-7.7134` edge `-0.1701` maxDD `-27.3622`
- `market_context_high->unknown_1h` score `-8.0497` n `120` status `ready` deltaP `1.9212` edge `-0.6389` maxDD `-1.2437`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
