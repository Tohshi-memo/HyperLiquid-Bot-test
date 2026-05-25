# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-25T22:07:19.781689+00:00`
- Price records: `672`
- Market context records: `1883`
- Flow alert records: `7322`
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

- `market_context_high->crypto_alt_4h` score `7.0657` n `199` status `ready` deltaP `22.6613` edge `0.5522` maxDD `-5.1574`
- `market_context_high->crypto_major_4h` score `6.7855` n `199` status `ready` deltaP `27.7148` edge `0.5053` maxDD `-4.9684`
- `market_context_high->unknown_4h` score `4.3711` n `199` status `ready` deltaP `18.2628` edge `0.4449` maxDD `-9.8581`
- `market_context_high->metal_24h` score `3.3379` n `181` status `ready` deltaP `18.6685` edge `0.3963` maxDD `-12.7414`
- `market_context_high->equity_4h` score `2.3911` n `199` status `ready` deltaP `14.582` edge `0.2115` maxDD `-5.0894`
- `market_context_high->index_24h` score `1.9592` n `181` status `ready` deltaP `11.5504` edge `0.2091` maxDD `-4.1604`
- `market_context_high->unknown_24h` score `1.7778` n `181` status `ready` deltaP `12.7187` edge `0.5954` maxDD `-35.8966`
- `market_context_high->crypto_major_1h` score `0.5506` n `199` status `ready` deltaP `6.6448` edge `0.1002` maxDD `-3.2225`
- `market_context_high->index_4h` score `0.4507` n `199` status `ready` deltaP `9.7882` edge `0.0812` maxDD `-3.7119`
- `market_context_high->crypto_alt_1h` score `0.2809` n `199` status `ready` deltaP `5.9068` edge `0.0954` maxDD `-4.9097`
- `market_context_high->fx_24h` score `0.2671` n `181` status `ready` deltaP `15.0543` edge `0.0268` maxDD `-1.3925`
- `market_context_high->equity_24h` score `0.1959` n `181` status `ready` deltaP `10.5097` edge `0.4361` maxDD `-33.1875`
- `market_context_high->crypto_major_24h` score `-0.0294` n `181` status `ready` deltaP `18.5898` edge `0.7322` maxDD `-62.3533`
- `market_context_high->equity_1h` score `-0.1659` n `199` status `ready` deltaP `4.388` edge `0.0363` maxDD `-2.6836`
- `market_context_high->unknown_1h` score `-0.4629` n `199` status `ready` deltaP `3.4371` edge `0.0337` maxDD `-3.6151`
- `market_context_high->metal_1h` score `-0.5102` n `199` status `ready` deltaP `6.7305` edge `0.0233` maxDD `-6.3532`
- `market_context_high->metal_4h` score `-0.5336` n `199` status `ready` deltaP `12.5429` edge `0.1411` maxDD `-12.5349`
- `market_context_high->index_1h` score `-0.6877` n `199` status `ready` deltaP `-0.6048` edge `0.0099` maxDD `-1.7205`
- `market_context_high->fx_1h` score `-0.7017` n `199` status `ready` deltaP `-3.9509` edge `-0.0004` maxDD `-0.3914`
- `market_context_high->fx_4h` score `-0.9876` n `199` status `ready` deltaP `-5.0389` edge `-0.0042` maxDD `-1.1056`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
