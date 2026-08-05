# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-05T11:22:28.093982+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11648`

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

- `market_context_high->unknown_24h` score `14.0085` n `89` status `ready` deltaP `9.6403` edge `1.1074` maxDD `-0.0103`
- `market_context_high->unknown_4h` score `5.4131` n `92` status `ready` deltaP `2.2402` edge `0.5357` maxDD `-3.6303`
- `market_context_high->commodity_4h` score `1.7335` n `92` status `ready` deltaP `18.1336` edge `0.1082` maxDD `-2.7703`
- `market_context_high->fx_24h` score `1.2029` n `89` status `ready` deltaP `28.2284` edge `0.0866` maxDD `-4.3126`
- `market_context_high->metal_24h` score `0.9033` n `89` status `ready` deltaP `1.6268` edge `0.2218` maxDD `-2.6802`
- `market_context_high->commodity_1h` score `0.4094` n `98` status `ready` deltaP `7.2926` edge `0.0271` maxDD `-1.3282`
- `market_context_high->fx_4h` score `0.0843` n `92` status `ready` deltaP `13.4411` edge `0.0072` maxDD `-1.8797`
- `market_context_high->fx_1h` score `0.0611` n `98` status `ready` deltaP `6.4891` edge `-0.0032` maxDD `-0.7973`
- `market_context_high->metal_1h` score `-0.5458` n `98` status `ready` deltaP `-1.7292` edge `-0.009` maxDD `-1.6224`
- `market_context_high->index_1h` score `-0.6363` n `98` status `ready` deltaP `-1.5123` edge `-0.0181` maxDD `-1.6054`
- `market_context_high->metal_4h` score `-0.8958` n `92` status `ready` deltaP `1.7431` edge `-0.003` maxDD `-3.211`
- `market_context_high->crypto_alt_1h` score `-0.9409` n `98` status `ready` deltaP `-4.2863` edge `-0.021` maxDD `-3.0178`
- `market_context_high->crypto_alt_24h` score `-1.4023` n `89` status `ready` deltaP `1.0241` edge `-0.0423` maxDD `-4.5445`
- `market_context_high->crypto_alt_4h` score `-1.5602` n `92` status `ready` deltaP `-0.8749` edge `-0.0552` maxDD `-5.7857`
- `market_context_high->equity_1h` score `-1.7496` n `98` status `ready` deltaP `2.8138` edge `-0.0895` maxDD `-10.619`
- `market_context_high->index_4h` score `-2.1359` n `92` status `ready` deltaP `-13.1694` edge `-0.0606` maxDD `-4.7021`
- `market_context_high->index_24h` score `-2.4047` n `89` status `ready` deltaP `-10.2607` edge `-0.0204` maxDD `-7.8922`
- `market_context_high->unknown_1h` score `-3.2068` n `98` status `ready` deltaP `4.2986` edge `-0.2512` maxDD `-1.2421`
- `market_context_high->crypto_major_1h` score `-3.602` n `98` status `ready` deltaP `-13.1156` edge `-0.0754` maxDD `-7.6533`
- `market_context_high->commodity_24h` score `-6.1059` n `89` status `ready` deltaP `10.3035` edge `-0.0365` maxDD `-50.8663`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
