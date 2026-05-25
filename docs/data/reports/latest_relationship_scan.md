# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-25T21:21:47.158327+00:00`
- Price records: `672`
- Market context records: `1880`
- Flow alert records: `7313`
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

- `market_context_high->crypto_alt_4h` score `6.9511` n `199` status `ready` deltaP `22.204` edge `0.5457` maxDD `-5.1574`
- `market_context_high->crypto_major_4h` score `6.7119` n `199` status `ready` deltaP `27.4099` edge `0.5012` maxDD `-4.9684`
- `market_context_high->unknown_4h` score `4.3615` n `199` status `ready` deltaP `18.2628` edge `0.4441` maxDD `-9.8581`
- `market_context_high->metal_24h` score `3.6543` n `181` status `ready` deltaP `19.1893` edge `0.4192` maxDD `-12.7414`
- `market_context_high->equity_4h` score `2.3984` n `199` status `ready` deltaP `14.582` edge `0.2121` maxDD `-5.0894`
- `market_context_high->index_24h` score `2.0836` n `181` status `ready` deltaP `12.0712` edge `0.216` maxDD `-4.1604`
- `market_context_high->unknown_24h` score `1.8234` n `181` status `ready` deltaP `12.7187` edge `0.5992` maxDD `-35.8966`
- `market_context_high->crypto_major_1h` score `0.5158` n `199` status `ready` deltaP `6.4951` edge `0.0983` maxDD `-3.2225`
- `market_context_high->index_4h` score `0.4871` n `199` status `ready` deltaP `10.0931` edge `0.0822` maxDD `-3.7119`
- `market_context_high->equity_24h` score `0.2836` n `181` status `ready` deltaP `10.857` edge `0.4411` maxDD `-33.1875`
- `market_context_high->crypto_alt_1h` score `0.2197` n `199` status `ready` deltaP `5.6074` edge `0.0923` maxDD `-4.9097`
- `market_context_high->fx_24h` score `0.2182` n `181` status `ready` deltaP `14.5335` edge `0.0262` maxDD `-1.3925`
- `market_context_high->crypto_major_24h` score `0.0668` n `181` status `ready` deltaP `18.9371` edge `0.7379` maxDD `-62.3533`
- `market_context_high->equity_1h` score `-0.2043` n `199` status `ready` deltaP `4.0886` edge `0.0351` maxDD `-2.6836`
- `market_context_high->unknown_1h` score `-0.4461` n `199` status `ready` deltaP `3.5868` edge `0.0341` maxDD `-3.6151`
- `market_context_high->metal_4h` score `-0.496` n `199` status `ready` deltaP `12.8478` edge `0.1422` maxDD `-12.5349`
- `market_context_high->metal_1h` score `-0.5406` n `199` status `ready` deltaP `6.2814` edge `0.0224` maxDD `-6.3532`
- `market_context_high->fx_1h` score `-0.7017` n `199` status `ready` deltaP `-3.9509` edge `-0.0004` maxDD `-0.3914`
- `market_context_high->index_1h` score `-0.7056` n `199` status `ready` deltaP `-0.7545` edge `0.0094` maxDD `-1.7205`
- `market_context_high->fx_4h` score `-0.9907` n `199` status `ready` deltaP `-5.0389` edge `-0.0046` maxDD `-1.1056`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
