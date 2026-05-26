# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-26T04:52:17.026869+00:00`
- Price records: `672`
- Market context records: `1913`
- Flow alert records: `7406`
- Minimum samples: `30`
- Pattern count: `64`

- Symbol pattern count: `6052`

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

- `market_context_high->crypto_alt_4h` score `7.8638` n `199` status `ready` deltaP `24.643` edge `0.6055` maxDD `-5.1574`
- `market_context_high->crypto_major_4h` score `7.2869` n `199` status `ready` deltaP `29.3916` edge `0.5359` maxDD `-4.9684`
- `market_context_high->unknown_4h` score `3.9395` n `199` status `ready` deltaP `17.6531` edge `0.413` maxDD `-9.8581`
- `market_context_high->equity_4h` score `2.6677` n `199` status `ready` deltaP `15.954` edge `0.2254` maxDD `-5.0894`
- `market_context_high->metal_24h` score `1.2394` n `190` status `ready` deltaP `14.7277` edge `0.2477` maxDD `-12.7414`
- `market_context_high->unknown_24h` score `1.0942` n `190` status `ready` deltaP `13.3991` edge `0.5339` maxDD `-35.8966`
- `market_context_high->index_24h` score `0.7722` n `190` status `ready` deltaP `6.7635` edge `0.1421` maxDD `-4.1604`
- `market_context_high->crypto_major_1h` score `0.7562` n `205` status `ready` deltaP `8.3146` edge `0.1062` maxDD `-3.2225`
- `market_context_high->crypto_alt_1h` score `0.583` n `205` status `ready` deltaP `7.6435` edge `0.109` maxDD `-4.9097`
- `market_context_high->index_4h` score `0.5588` n `199` status `ready` deltaP `10.8553` edge `0.0831` maxDD `-3.7119`
- `market_context_high->fx_24h` score `-0.0055` n `190` status `ready` deltaP `12.2917` edge `0.0225` maxDD `-1.3925`
- `market_context_high->equity_1h` score `-0.0512` n `205` status `ready` deltaP `5.5966` edge `0.0378` maxDD `-2.6836`
- `market_context_high->metal_1h` score `-0.5946` n `205` status `ready` deltaP `5.6485` edge `0.0197` maxDD `-6.3532`
- `market_context_high->fx_1h` score `-0.6236` n `205` status `ready` deltaP `-2.6442` edge `0.0009` maxDD `-0.3914`
- `market_context_high->index_1h` score `-0.6327` n `205` status `ready` deltaP `0.187` edge `0.0092` maxDD `-1.7205`
- `market_context_high->metal_4h` score `-0.6396` n `199` status `ready` deltaP `12.238` edge `0.1343` maxDD `-12.5349`
- `market_context_high->fx_4h` score `-0.7869` n `199` status `ready` deltaP `-1.9901` edge `0.0012` maxDD `-1.1056`
- `market_context_high->equity_24h` score `-0.907` n `190` status `ready` deltaP `7.1491` edge `0.3666` maxDD `-33.1875`
- `market_context_high->unknown_1h` score `-1.0739` n `205` status `ready` deltaP `1.5292` edge `-0.0045` maxDD `-3.6151`
- `market_context_high->crypto_major_24h` score `-1.6055` n `190` status `ready` deltaP `14.7442` edge `0.6265` maxDD `-62.3533`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
