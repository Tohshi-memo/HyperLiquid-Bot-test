# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-22T14:19:04.263357+00:00`
- Price records: `672`
- Market context records: `7572`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `14512`

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

- `market_context_high->commodity_4h` score `0.2658` n `167` status `ready` deltaP `10.1339` edge `0.0306` maxDD `-2.4139`
- `market_context_high->index_1h` score `-0.1016` n `167` status `ready` deltaP `5.3991` edge `0.0075` maxDD `-1.5217`
- `market_context_high->commodity_24h` score `-0.1814` n `154` status `ready` deltaP `12.5594` edge `0.0595` maxDD `-7.0012`
- `market_context_high->commodity_1h` score `-0.2813` n `167` status `ready` deltaP `4.6321` edge `0.0029` maxDD `-1.5775`
- `market_context_high->fx_1h` score `-0.4646` n `167` status `ready` deltaP `1.6526` edge `0.0002` maxDD `-0.6615`
- `market_context_high->index_4h` score `-0.4695` n `167` status `ready` deltaP `11.4221` edge `0.0363` maxDD `-3.4775`
- `market_context_high->metal_1h` score `-0.8281` n `167` status `ready` deltaP `-0.7485` edge `0.0092` maxDD `-1.4971`
- `market_context_high->crypto_alt_1h` score `-0.8348` n `167` status `ready` deltaP `-0.7485` edge `0.0002` maxDD `-5.8454`
- `market_context_high->crypto_major_1h` score `-0.8444` n `167` status `ready` deltaP `4.491` edge `0.0025` maxDD `-7.5892`
- `market_context_high->fx_24h` score `-0.8794` n `154` status `ready` deltaP `8.3465` edge `0.0151` maxDD `-3.8554`
- `market_context_high->unknown_4h` score `-1.1499` n `167` status `ready` deltaP `10.0117` edge `0.0217` maxDD `-6.2031`
- `market_context_high->unknown_24h` score `-1.2479` n `155` status `ready` deltaP `5.9621` edge `0.0706` maxDD `-9.9598`
- `market_context_high->equity_1h` score `-1.3891` n `167` status `ready` deltaP `3.7529` edge `0.0236` maxDD `-13.4699`
- `market_context_high->unknown_1h` score `-1.4012` n `167` status `ready` deltaP `1.0479` edge `-0.0614` maxDD `-1.3217`
- `market_context_high->metal_4h` score `-1.4797` n `167` status `ready` deltaP `0.942` edge `0.0522` maxDD `-4.8549`
- `market_context_high->equity_4h` score `-1.6181` n `167` status `ready` deltaP `3.2046` edge `0.2079` maxDD `-21.9375`
- `market_context_high->crypto_alt_4h` score `-1.7221` n `167` status `ready` deltaP `0.1689` edge `0.0336` maxDD `-13.7735`
- `market_context_high->fx_4h` score `-2.0643` n `167` status `ready` deltaP `-0.7444` edge `0.0014` maxDD `-2.1439`
- `market_context_high->crypto_major_4h` score `-2.4394` n `167` status `ready` deltaP `4.5129` edge `0.0351` maxDD `-22.5675`
- `market_context_high->index_24h` score `-3.8816` n `154` status `ready` deltaP `-18.5302` edge `0.0005` maxDD `-15.3023`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
