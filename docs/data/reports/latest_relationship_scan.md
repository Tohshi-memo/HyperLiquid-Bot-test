# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-06T14:07:27.484473+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11781`

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

- `market_context_high->unknown_24h` score `11.5157` n `100` status `ready` deltaP `3.8611` edge `0.9382` maxDD `-0.0104`
- `market_context_high->metal_24h` score `1.3429` n `100` status `ready` deltaP `4.4167` edge `0.1993` maxDD `-2.6802`
- `market_context_high->commodity_4h` score `1.0837` n `110` status `ready` deltaP `12.8908` edge `0.089` maxDD `-2.7703`
- `market_context_high->fx_24h` score `0.472` n `100` status `ready` deltaP `20.3681` edge `0.0453` maxDD `-4.3126`
- `market_context_high->commodity_1h` score `0.328` n `113` status `ready` deltaP `6.8001` edge `0.0236` maxDD `-1.3282`
- `market_context_high->fx_1h` score `0.0439` n `113` status `ready` deltaP `6.461` edge `-0.0044` maxDD `-0.8012`
- `market_context_high->fx_4h` score `-0.3418` n `110` status `ready` deltaP `6.5216` edge `-0.0013` maxDD `-1.8797`
- `market_context_high->metal_1h` score `-0.5627` n `113` status `ready` deltaP `-2.2786` edge `-0.0075` maxDD `-1.6224`
- `market_context_high->metal_4h` score `-0.6933` n `110` status `ready` deltaP `3.7334` edge `0.0097` maxDD `-3.211`
- `market_context_high->index_1h` score `-1.087` n `113` status `ready` deltaP `-3.0271` edge `-0.017` maxDD `-1.6054`
- `market_context_high->index_24h` score `-1.2188` n `100` status `ready` deltaP `-3.8056` edge `0.0886` maxDD `-7.8922`
- `market_context_high->crypto_alt_1h` score `-1.3353` n `113` status `ready` deltaP `-3.8723` edge `-0.0144` maxDD `-3.0178`
- `market_context_high->equity_1h` score `-1.5813` n `113` status `ready` deltaP `2.692` edge `-0.0642` maxDD `-10.5179`
- `market_context_high->index_4h` score `-1.7674` n `110` status `ready` deltaP `-8.6614` edge `-0.0434` maxDD `-4.7021`
- `market_context_high->crypto_alt_4h` score `-1.8158` n `110` status `ready` deltaP `3.326` edge `-0.0345` maxDD `-5.7857`
- `market_context_high->crypto_alt_24h` score `-2.7892` n `100` status `ready` deltaP `-5.0139` edge `-0.0547` maxDD `-4.5445`
- `market_context_high->crypto_major_1h` score `-2.9614` n `113` status `ready` deltaP `-8.9926` edge `-0.0495` maxDD `-7.6533`
- `market_context_high->equity_4h` score `-6.4987` n `110` status `ready` deltaP `-0.6431` edge `-0.3` maxDD `-34.9766`
- `market_context_high->commodity_24h` score `-6.5172` n `100` status `ready` deltaP `7.9306` edge `-0.0119` maxDD `-52.7876`
- `market_context_high->crypto_major_4h` score `-7.5986` n `110` status `ready` deltaP `-7.7134` edge `-0.1606` maxDD `-27.3622`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
