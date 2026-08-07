# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-07T07:52:28.219989+00:00`
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

- `market_context_high->commodity_4h` score `0.9222` n `120` status `ready` deltaP `11.3516` edge `0.0858` maxDD `-2.7703`
- `market_context_high->fx_24h` score `0.5706` n `109` status `ready` deltaP `21.3184` edge `0.0516` maxDD `-4.3126`
- `market_context_high->metal_24h` score `0.5229` n `109` status `ready` deltaP `1.697` edge `0.1491` maxDD `-2.6802`
- `market_context_high->commodity_1h` score `0.42` n `120` status `ready` deltaP `7.3503` edge `0.0276` maxDD `-1.3282`
- `market_context_high->fx_1h` score `0.0888` n `120` status `ready` deltaP `7.3503` edge `-0.0026` maxDD `-0.8012`
- `market_context_high->fx_4h` score `-0.1729` n `120` status `ready` deltaP `8.6585` edge `0.0061` maxDD `-1.8797`
- `market_context_high->metal_1h` score `-0.6417` n `120` status `ready` deltaP `-3.4231` edge `-0.01` maxDD `-1.6224`
- `market_context_high->crypto_alt_1h` score `-0.7957` n `120` status `ready` deltaP `-2.994` edge `-0.011` maxDD `-3.0178`
- `market_context_high->index_1h` score `-1.006` n `120` status `ready` deltaP `-2.6746` edge `-0.0126` maxDD `-1.6054`
- `market_context_high->index_24h` score `-1.0976` n `109` status `ready` deltaP `-0.5453` edge `0.0824` maxDD `-7.8922`
- `market_context_high->equity_1h` score `-1.2999` n `120` status `ready` deltaP `3.7974` edge `-0.0355` maxDD `-10.5179`
- `market_context_high->index_4h` score `-1.5077` n `120` status `ready` deltaP `-5.8435` edge `-0.0289` maxDD `-4.7021`
- `market_context_high->metal_4h` score `-1.7193` n `120` status `ready` deltaP `-1.9512` edge `-0.0068` maxDD `-3.211`
- `market_context_high->crypto_alt_4h` score `-2.0277` n `120` status `ready` deltaP `1.3516` edge `-0.039` maxDD `-5.7857`
- `market_context_high->crypto_major_1h` score `-2.6334` n `120` status `ready` deltaP `-6.4521` edge `-0.0391` maxDD `-7.6533`
- `market_context_high->crypto_alt_24h` score `-3.9367` n `109` status `ready` deltaP `-10.9877` edge `-0.1105` maxDD `-4.5445`
- `market_context_high->equity_4h` score `-5.8628` n `120` status `ready` deltaP `0.6504` edge `-0.2271` maxDD `-34.9766`
- `market_context_high->commodity_24h` score `-6.3033` n `109` status `ready` deltaP `9.8099` edge `0.003` maxDD `-52.7876`
- `market_context_high->crypto_major_4h` score `-7.3277` n `120` status `ready` deltaP `-6.0366` edge `-0.1492` maxDD `-27.3622`
- `market_context_high->unknown_1h` score `-8.3977` n `120` status `ready` deltaP `1.9212` edge `-0.6679` maxDD `-1.2437`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
