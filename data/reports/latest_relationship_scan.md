# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-25T19:52:17.006650+00:00`
- Price records: `672`
- Market context records: `1873`
- Flow alert records: `7293`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `4510`

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

- `market_context_high->crypto_alt_4h` score `6.7379` n `199` status `ready` deltaP `21.5942` edge `0.532` maxDD `-5.1574`
- `market_context_high->crypto_major_4h` score `6.4888` n `199` status `ready` deltaP `26.4953` edge `0.4887` maxDD `-4.9684`
- `market_context_high->unknown_4h` score `4.2975` n `199` status `ready` deltaP `17.958` edge `0.4408` maxDD `-9.8581`
- `market_context_high->metal_24h` score `4.0201` n `178` status `ready` deltaP `19.9517` edge `0.4446` maxDD `-12.7414`
- `market_context_high->equity_4h` score `2.3298` n `199` status `ready` deltaP `14.4296` edge `0.2074` maxDD `-5.0894`
- `market_context_high->index_24h` score `2.2982` n `178` status `ready` deltaP `12.8336` edge `0.2288` maxDD `-4.1604`
- `market_context_high->unknown_24h` score `1.9912` n `178` status `ready` deltaP `12.4766` edge `0.6148` maxDD `-35.8966`
- `market_context_high->index_4h` score `0.4617` n `199` status `ready` deltaP `9.9407` edge `0.0811` maxDD `-3.7119`
- `market_context_high->equity_24h` score `0.4351` n `178` status `ready` deltaP `10.68` edge `0.4549` maxDD `-33.1875`
- `market_context_high->crypto_major_1h` score `0.4223` n `199` status `ready` deltaP `5.8963` edge `0.0945` maxDD `-3.2225`
- `market_context_high->crypto_major_24h` score `0.3295` n `178` status `ready` deltaP `19.2065` edge `0.758` maxDD `-62.3533`
- `market_context_high->fx_24h` score `0.2565` n `178` status `ready` deltaP `14.9072` edge `0.0269` maxDD `-1.3925`
- `market_context_high->crypto_alt_1h` score `0.1454` n `199` status `ready` deltaP `5.308` edge `0.0881` maxDD `-4.9097`
- `market_context_high->equity_1h` score `-0.245` n `199` status `ready` deltaP `3.7892` edge `0.0337` maxDD `-2.6836`
- `market_context_high->metal_1h` score `-0.5554` n `199` status `ready` deltaP `6.1317` edge `0.0215` maxDD `-6.3532`
- `market_context_high->unknown_1h` score `-0.572` n `199` status `ready` deltaP `2.8383` edge `0.0286` maxDD `-3.6151`
- `market_context_high->metal_4h` score `-0.5902` n `199` status `ready` deltaP `12.3905` edge `0.1374` maxDD `-12.5349`
- `market_context_high->fx_1h` score `-0.6924` n `199` status `ready` deltaP `-3.8012` edge `-0.0002` maxDD `-0.3914`
- `market_context_high->index_1h` score `-0.7416` n `199` status `ready` deltaP `-1.0539` edge `0.0084` maxDD `-1.7205`
- `market_context_high->fx_4h` score `-0.9915` n `199` status `ready` deltaP `-5.0389` edge `-0.0047` maxDD `-1.1056`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
