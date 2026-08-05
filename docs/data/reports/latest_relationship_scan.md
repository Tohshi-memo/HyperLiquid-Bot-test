# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-05T18:22:41.161614+00:00`
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

- `market_context_high->unknown_24h` score `13.1031` n `90` status `ready` deltaP `5.3125` edge `1.0608` maxDD `-0.0103`
- `market_context_high->unknown_4h` score `4.0823` n `100` status `ready` deltaP `0.5` edge `0.4364` maxDD `-3.6303`
- `market_context_high->commodity_4h` score `1.4715` n `100` status `ready` deltaP `15.878` edge `0.1014` maxDD `-2.7703`
- `market_context_high->metal_24h` score `0.9445` n `90` status `ready` deltaP `2.0139` edge `0.2245` maxDD `-2.6802`
- `market_context_high->fx_24h` score `0.9207` n `90` status `ready` deltaP `24.7223` edge `0.0738` maxDD `-4.3126`
- `market_context_high->commodity_1h` score `0.4173` n `107` status `ready` deltaP `7.5718` edge `0.0259` maxDD `-1.3282`
- `market_context_high->fx_1h` score `0.0016` n `107` status `ready` deltaP `5.662` edge `-0.0026` maxDD `-0.8012`
- `market_context_high->fx_4h` score `-0.0261` n `100` status `ready` deltaP `11.1829` edge `0.0081` maxDD `-1.8797`
- `market_context_high->metal_1h` score `-0.5395` n `107` status `ready` deltaP `-1.9685` edge `-0.0066` maxDD `-1.6224`
- `market_context_high->index_1h` score `-0.7718` n `107` status `ready` deltaP `-4.0279` edge `-0.0187` maxDD `-1.6054`
- `market_context_high->metal_4h` score `-0.7777` n `100` status `ready` deltaP `2.6341` edge `0.0062` maxDD `-3.211`
- `market_context_high->crypto_alt_1h` score `-0.9162` n `107` status `ready` deltaP `-4.2462` edge `-0.0181` maxDD `-3.0178`
- `market_context_high->crypto_alt_24h` score `-1.441` n `90` status `ready` deltaP `0.7291` edge `-0.0453` maxDD `-4.5445`
- `market_context_high->equity_1h` score `-1.7484` n `107` status `ready` deltaP `1.802` edge `-0.0826` maxDD `-10.619`
- `market_context_high->index_4h` score `-2.0831` n `100` status `ready` deltaP `-11.8232` edge `-0.0628` maxDD `-4.7021`
- `market_context_high->index_24h` score `-2.4783` n `90` status `ready` deltaP `-11.0764` edge `-0.0244` maxDD `-7.8922`
- `market_context_high->crypto_alt_4h` score `-2.7407` n `100` status `ready` deltaP `-2.1159` edge `-0.0753` maxDD `-5.7857`
- `market_context_high->crypto_major_1h` score `-3.2909` n `107` status `ready` deltaP `-10.861` edge `-0.0645` maxDD `-7.6533`
- `market_context_high->unknown_1h` score `-3.5631` n `107` status `ready` deltaP `2.1098` edge `-0.2663` maxDD `-1.2421`
- `market_context_high->commodity_24h` score `-6.0358` n `90` status `ready` deltaP `10.8334` edge `-0.0246` maxDD `-51.0493`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
