# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-07T06:51:08.666532+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11736`

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

- `market_context_high->commodity_4h` score `0.9744` n `120` status `ready` deltaP `11.8089` edge `0.0871` maxDD `-2.7703`
- `market_context_high->metal_24h` score `0.622` n `109` status `ready` deltaP `2.3648` edge `0.1529` maxDD `-2.6802`
- `market_context_high->fx_24h` score `0.5729` n `109` status `ready` deltaP `21.3184` edge `0.0519` maxDD `-4.3126`
- `market_context_high->commodity_1h` score `0.4368` n `120` status `ready` deltaP `7.5` edge `0.028` maxDD `-1.3282`
- `market_context_high->fx_1h` score `0.1044` n `120` status `ready` deltaP `7.6497` edge `-0.0026` maxDD `-0.8012`
- `market_context_high->fx_4h` score `-0.1991` n `120` status `ready` deltaP `8.2012` edge `0.0058` maxDD `-1.8797`
- `market_context_high->metal_1h` score `-0.6238` n `120` status `ready` deltaP `-3.1237` edge `-0.0097` maxDD `-1.6224`
- `market_context_high->crypto_alt_1h` score `-0.7731` n `120` status `ready` deltaP `-2.994` edge `-0.0081` maxDD `-3.0178`
- `market_context_high->index_1h` score `-0.9449` n `120` status `ready` deltaP `-2.0758` edge `-0.0115` maxDD `-1.6054`
- `market_context_high->index_24h` score `-1.0726` n `109` status `ready` deltaP `-0.3783` edge `0.0845` maxDD `-7.8922`
- `market_context_high->equity_1h` score `-1.2298` n `120` status `ready` deltaP `4.3962` edge `-0.0305` maxDD `-10.5179`
- `market_context_high->index_4h` score `-1.4888` n `120` status `ready` deltaP `-5.5387` edge `-0.0285` maxDD `-4.7021`
- `market_context_high->metal_4h` score `-1.6722` n `120` status `ready` deltaP `-1.6463` edge `-0.0049` maxDD `-3.211`
- `market_context_high->crypto_alt_4h` score `-1.9383` n `120` status `ready` deltaP `1.8089` edge `-0.0346` maxDD `-5.7857`
- `market_context_high->crypto_major_1h` score `-2.5602` n `120` status `ready` deltaP `-6.1527` edge `-0.035` maxDD `-7.6533`
- `market_context_high->crypto_alt_24h` score `-3.8413` n `109` status `ready` deltaP `-10.3199` edge `-0.107` maxDD `-4.5445`
- `market_context_high->equity_4h` score `-5.8344` n `120` status `ready` deltaP `0.9553` edge `-0.2255` maxDD `-34.9766`
- `market_context_high->commodity_24h` score `-6.3212` n `109` status `ready` deltaP `9.8099` edge `0.0007` maxDD `-52.7876`
- `market_context_high->crypto_major_4h` score `-7.2759` n `120` status `ready` deltaP `-5.8841` edge `-0.1459` maxDD `-27.3622`
- `market_context_high->unknown_1h` score `-8.496` n `120` status `ready` deltaP `1.6218` edge `-0.6741` maxDD `-1.2437`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
