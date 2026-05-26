# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-26T12:52:21.397276+00:00`
- Price records: `672`
- Market context records: `1939`
- Flow alert records: `7479`
- Minimum samples: `30`
- Pattern count: `80`

- Symbol pattern count: `7547`

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

- `market_context_high->crypto_alt_4h` score `7.1199` n `225` status `ready` deltaP `22.3487` edge `0.5588` maxDD `-5.1574`
- `market_context_high->crypto_major_4h` score `6.477` n `225` status `ready` deltaP `26.0328` edge `0.4908` maxDD `-4.9684`
- `market_context_high->unknown_4h` score `2.6167` n `225` status `ready` deltaP `14.2275` edge `0.3256` maxDD `-9.8581`
- `market_context_high->equity_4h` score `2.0654` n `225` status `ready` deltaP `13.9297` edge `0.1887` maxDD `-5.0894`
- `market_context_high->crypto_major_1h` score `0.7185` n `232` status `ready` deltaP `7.934` edge `0.1056` maxDD `-3.2225`
- `market_context_high->unknown_24h` score `0.652` n `199` status `ready` deltaP `14.3655` edge `0.4906` maxDD `-35.8966`
- `market_context_high->crypto_alt_1h` score `0.557` n `232` status `ready` deltaP `7.2576` edge `0.1094` maxDD `-4.9097`
- `market_context_high->metal_24h` score `0.2366` n `199` status `ready` deltaP `11.9871` edge `0.1824` maxDD `-12.7414`
- `market_context_high->index_4h` score `0.1578` n `225` status `ready` deltaP `8.4826` edge `0.0655` maxDD `-3.7119`
- `market_context_high->index_24h` score `0.1489` n `199` status `ready` deltaP `4.1922` edge `0.1073` maxDD `-4.1604`
- `market_context_high->equity_1h` score `-0.1376` n `232` status `ready` deltaP `5.1917` edge `0.0333` maxDD `-2.6836`
- `market_context_high->fx_24h` score `-0.2759` n `199` status `ready` deltaP `9.9323` edge `0.0157` maxDD `-1.3925`
- `market_context_high->index_1h` score `-0.6065` n `232` status `ready` deltaP `0.6796` edge `0.0081` maxDD `-1.7205`
- `market_context_high->fx_1h` score `-0.6308` n `232` status `ready` deltaP `-2.6768` edge `0.0002` maxDD `-0.3914`
- `market_context_high->equity_24h` score `-0.9454` n `199` status `ready` deltaP `8.4395` edge `0.3548` maxDD `-33.1875`
- `market_context_high->fx_4h` score `-0.9569` n `225` status `ready` deltaP `-4.8689` edge `-0.0014` maxDD `-1.1056`
- `market_context_high->metal_1h` score `-1.1449` n `232` status `ready` deltaP `3.6558` edge `0.0138` maxDD `-6.3532`
- `market_context_high->unknown_1h` score `-1.416` n `232` status `ready` deltaP `0.8081` edge `-0.0282` maxDD `-3.6151`
- `market_context_high->metal_4h` score `-1.6094` n `225` status `ready` deltaP `6.7751` edge `0.0899` maxDD `-12.5349`
- `market_context_high->commodity_1h` score `-2.0035` n `232` status `ready` deltaP `0.9205` edge `-0.0072` maxDD `-15.7972`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
