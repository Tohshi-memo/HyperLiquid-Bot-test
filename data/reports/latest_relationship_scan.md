# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-25T15:37:20.036671+00:00`
- Price records: `672`
- Market context records: `1855`
- Flow alert records: `7240`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `4500`

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

- `market_context_high->crypto_alt_4h` score `6.5023` n `199` status `ready` deltaP `21.2893` edge `0.5144` maxDD `-5.1574`
- `market_context_high->crypto_major_4h` score `5.9248` n `199` status `ready` deltaP `24.666` edge `0.4539` maxDD `-4.9684`
- `market_context_high->metal_24h` score `5.4766` n `178` status `ready` deltaP `22.903` edge `0.5463` maxDD `-12.7414`
- `market_context_high->unknown_4h` score `4.1894` n `199` status `ready` deltaP `16.8909` edge `0.4389` maxDD `-9.8581`
- `market_context_high->index_24h` score `2.7131` n `178` status `ready` deltaP `14.5697` edge `0.2518` maxDD `-4.1604`
- `market_context_high->unknown_24h` score `2.4653` n `178` status `ready` deltaP `13.6919` edge `0.6462` maxDD `-35.8966`
- `market_context_high->equity_4h` score `2.1482` n `199` status `ready` deltaP `14.1247` edge `0.1943` maxDD `-5.0894`
- `market_context_high->equity_24h` score `0.5873` n `178` status `ready` deltaP `11.548` edge `0.4618` maxDD `-33.1875`
- `market_context_high->index_4h` score `0.4321` n `199` status `ready` deltaP `10.2455` edge `0.0766` maxDD `-3.7119`
- `market_context_high->crypto_major_1h` score `0.1933` n `199` status `ready` deltaP `4.549` edge `0.0844` maxDD `-3.2225`
- `market_context_high->crypto_major_24h` score `0.1651` n `178` status `ready` deltaP `19.2065` edge `0.7443` maxDD `-62.3533`
- `market_context_high->fx_24h` score `0.0984` n `178` status `ready` deltaP `13.1711` edge `0.0253` maxDD `-1.3925`
- `market_context_high->crypto_alt_1h` score `-0.02` n `199` status `ready` deltaP `4.2601` edge `0.0813` maxDD `-4.9097`
- `market_context_high->equity_1h` score `-0.2426` n `199` status `ready` deltaP `3.9389` edge `0.0329` maxDD `-2.6836`
- `market_context_high->unknown_1h` score `-0.5144` n `199` status `ready` deltaP `3.1377` edge `0.0314` maxDD `-3.6151`
- `market_context_high->metal_1h` score `-0.6013` n `199` status `ready` deltaP `5.5329` edge `0.0196` maxDD `-6.3532`
- `market_context_high->metal_4h` score `-0.6588` n `199` status `ready` deltaP `12.238` edge `0.1327` maxDD `-12.5349`
- `market_context_high->fx_1h` score `-0.7009` n `199` status `ready` deltaP `-3.9509` edge `-0.0003` maxDD `-0.3914`
- `market_context_high->index_1h` score `-0.7104` n `199` status `ready` deltaP `-0.7545` edge `0.009` maxDD `-1.7205`
- `market_context_high->fx_4h` score `-0.9994` n `199` status `ready` deltaP `-5.1913` edge `-0.0047` maxDD `-1.1056`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
