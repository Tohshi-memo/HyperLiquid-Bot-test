# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-25T21:37:20.483277+00:00`
- Price records: `672`
- Market context records: `1881`
- Flow alert records: `7316`
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

- `market_context_high->crypto_alt_4h` score `6.9993` n `199` status `ready` deltaP `22.3564` edge `0.5487` maxDD `-5.1574`
- `market_context_high->crypto_major_4h` score `6.7529` n `199` status `ready` deltaP `27.5623` edge `0.5036` maxDD `-4.9684`
- `market_context_high->unknown_4h` score `4.3687` n `199` status `ready` deltaP `18.2628` edge `0.4447` maxDD `-9.8581`
- `market_context_high->metal_24h` score `3.542` n `181` status `ready` deltaP `19.0157` edge `0.411` maxDD `-12.7414`
- `market_context_high->equity_4h` score `2.4008` n `199` status `ready` deltaP `14.582` edge `0.2123` maxDD `-5.0894`
- `market_context_high->index_24h` score `2.0421` n `181` status `ready` deltaP `11.8976` edge `0.2137` maxDD `-4.1604`
- `market_context_high->unknown_24h` score `1.8114` n `181` status `ready` deltaP `12.7187` edge `0.5982` maxDD `-35.8966`
- `market_context_high->crypto_major_1h` score `0.5434` n `199` status `ready` deltaP `6.6448` edge `0.0996` maxDD `-3.2225`
- `market_context_high->index_4h` score `0.4737` n `199` status `ready` deltaP `9.9407` edge `0.0821` maxDD `-3.7119`
- `market_context_high->equity_24h` score `0.2668` n `181` status `ready` deltaP `10.857` edge `0.4397` maxDD `-33.1875`
- `market_context_high->crypto_alt_1h` score `0.2521` n `199` status `ready` deltaP `5.7571` edge `0.094` maxDD `-4.9097`
- `market_context_high->fx_24h` score `0.2345` n `181` status `ready` deltaP `14.7071` edge `0.0264` maxDD `-1.3925`
- `market_context_high->crypto_major_24h` score `0.05` n `181` status `ready` deltaP `18.9371` edge `0.7365` maxDD `-62.3533`
- `market_context_high->equity_1h` score `-0.1863` n `199` status `ready` deltaP `4.2383` edge `0.0356` maxDD `-2.6836`
- `market_context_high->unknown_1h` score `-0.4281` n `199` status `ready` deltaP `3.7365` edge `0.0346` maxDD `-3.6151`
- `market_context_high->metal_4h` score `-0.496` n `199` status `ready` deltaP `12.8478` edge `0.1422` maxDD `-12.5349`
- `market_context_high->metal_1h` score `-0.532` n `199` status `ready` deltaP `6.4311` edge `0.0225` maxDD `-6.3532`
- `market_context_high->index_1h` score `-0.7032` n `199` status `ready` deltaP `-0.7545` edge `0.0096` maxDD `-1.7205`
- `market_context_high->fx_1h` score `-0.7095` n `199` status `ready` deltaP `-4.1006` edge `-0.0004` maxDD `-0.3914`
- `market_context_high->fx_4h` score `-0.9899` n `199` status `ready` deltaP `-5.0389` edge `-0.0045` maxDD `-1.1056`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
