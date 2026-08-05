# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-05T18:37:26.764098+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11684`

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

- `market_context_high->unknown_24h` score `13.0724` n `90` status `ready` deltaP `5.1389` edge `1.0594` maxDD `-0.0103`
- `market_context_high->unknown_4h` score `4.0751` n `100` status `ready` deltaP `0.5` edge `0.4358` maxDD `-3.6303`
- `market_context_high->commodity_4h` score `1.4569` n `100` status `ready` deltaP `15.7256` edge `0.1012` maxDD `-2.7703`
- `market_context_high->metal_24h` score `0.9406` n `90` status `ready` deltaP `2.0139` edge `0.224` maxDD `-2.6802`
- `market_context_high->fx_24h` score `0.9153` n `90` status `ready` deltaP `24.7223` edge `0.0731` maxDD `-4.3126`
- `market_context_high->commodity_1h` score `0.4029` n `107` status `ready` deltaP `7.4221` edge `0.0257` maxDD `-1.3282`
- `market_context_high->fx_1h` score `0.0136` n `107` status `ready` deltaP `5.8117` edge `-0.0026` maxDD `-0.8012`
- `market_context_high->fx_4h` score `-0.0174` n `100` status `ready` deltaP `11.3354` edge `0.0082` maxDD `-1.8797`
- `market_context_high->metal_1h` score `-0.538` n `107` status `ready` deltaP `-1.9685` edge `-0.0064` maxDD `-1.6224`
- `market_context_high->index_1h` score `-0.7718` n `107` status `ready` deltaP `-4.0279` edge `-0.0187` maxDD `-1.6054`
- `market_context_high->metal_4h` score `-0.7864` n `100` status `ready` deltaP `2.4817` edge `0.0061` maxDD `-3.211`
- `market_context_high->crypto_alt_1h` score `-0.9263` n `107` status `ready` deltaP `-4.3959` edge `-0.0184` maxDD `-3.0178`
- `market_context_high->crypto_alt_24h` score `-1.448` n `90` status `ready` deltaP `0.7291` edge `-0.0462` maxDD `-4.5445`
- `market_context_high->equity_1h` score `-1.7469` n `107` status `ready` deltaP `1.802` edge `-0.0824` maxDD `-10.619`
- `market_context_high->index_4h` score `-2.087` n `100` status `ready` deltaP `-11.8232` edge `-0.0633` maxDD `-4.7021`
- `market_context_high->index_24h` score `-2.463` n `90` status `ready` deltaP `-10.9028` edge `-0.0236` maxDD `-7.8922`
- `market_context_high->crypto_alt_4h` score `-2.7709` n `100` status `ready` deltaP `-2.2683` edge `-0.0768` maxDD `-5.7857`
- `market_context_high->crypto_major_1h` score `-3.3113` n `107` status `ready` deltaP `-11.0107` edge `-0.0652` maxDD `-7.6533`
- `market_context_high->unknown_1h` score `-3.5799` n `107` status `ready` deltaP `1.9601` edge `-0.2667` maxDD `-1.2421`
- `market_context_high->commodity_24h` score `-6.0366` n `90` status `ready` deltaP `10.8334` edge `-0.0247` maxDD `-51.0493`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
