# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-06T10:16:21.598968+00:00`
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

- `market_context_high->unknown_24h` score `20.2141` n `98` status `ready` deltaP `3.8407` edge `1.6632` maxDD `-0.0103`
- `market_context_high->metal_24h` score `1.5352` n `98` status `ready` deltaP `4.8256` edge `0.2126` maxDD `-2.6802`
- `market_context_high->commodity_4h` score `1.0214` n `109` status `ready` deltaP `12.5322` edge `0.0862` maxDD `-2.7703`
- `market_context_high->fx_24h` score `0.5044` n `98` status `ready` deltaP `20.7057` edge `0.0472` maxDD `-4.3126`
- `market_context_high->unknown_4h` score `0.3918` n `109` status `ready` deltaP `-0.7356` edge `0.1371` maxDD `-3.6303`
- `market_context_high->commodity_1h` score `0.3892` n `109` status `ready` deltaP `7.4603` edge `0.0243` maxDD `-1.3282`
- `market_context_high->fx_1h` score `-0.0027` n `109` status `ready` deltaP `5.6831` edge `-0.0031` maxDD `-0.8012`
- `market_context_high->fx_4h` score `-0.2923` n `109` status `ready` deltaP `6.7227` edge `0.0037` maxDD `-1.8797`
- `market_context_high->metal_1h` score `-0.523` n `109` status `ready` deltaP `-1.5602` edge `-0.0072` maxDD `-1.6224`
- `market_context_high->index_1h` score `-0.705` n `109` status `ready` deltaP `-2.7578` edge `-0.0186` maxDD `-1.6054`
- `market_context_high->metal_4h` score `-0.7469` n `109` status `ready` deltaP `3.2418` edge `0.0061` maxDD `-3.211`
- `market_context_high->index_24h` score `-1.4487` n `98` status `ready` deltaP `-5.226` edge `0.0686` maxDD `-7.8922`
- `market_context_high->crypto_alt_1h` score `-1.4606` n `109` status `ready` deltaP `-4.8385` edge `-0.0184` maxDD `-3.0178`
- `market_context_high->equity_1h` score `-1.7481` n `109` status `ready` deltaP `1.8679` edge `-0.083` maxDD `-10.619`
- `market_context_high->index_4h` score `-1.9768` n `109` status `ready` deltaP `-11.1435` edge `-0.0537` maxDD `-4.7021`
- `market_context_high->crypto_alt_4h` score `-2.1235` n `109` status `ready` deltaP `1.3845` edge `-0.0472` maxDD `-5.7857`
- `market_context_high->crypto_alt_24h` score `-2.3331` n `98` status `ready` deltaP `-2.0125` edge `-0.0367` maxDD `-4.5445`
- `market_context_high->crypto_major_1h` score `-3.1892` n `109` status `ready` deltaP `-10.7002` edge `-0.0571` maxDD `-7.6533`
- `market_context_high->unknown_1h` score `-5.8779` n `109` status `ready` deltaP `0.9847` edge `-0.4517` maxDD `-1.2421`
- `market_context_high->commodity_24h` score `-6.8279` n `98` status `ready` deltaP `5.0311` edge `-0.0324` maxDD `-52.7876`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
