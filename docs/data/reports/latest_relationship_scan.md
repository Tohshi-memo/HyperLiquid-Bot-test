# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-25T19:22:16.052483+00:00`
- Price records: `672`
- Market context records: `1871`
- Flow alert records: `7287`
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

- `market_context_high->crypto_alt_4h` score `6.6693` n `199` status `ready` deltaP `21.4418` edge `0.5273` maxDD `-5.1574`
- `market_context_high->crypto_major_4h` score `6.4008` n `199` status `ready` deltaP `26.1904` edge `0.4834` maxDD `-4.9684`
- `market_context_high->unknown_4h` score `4.2769` n `199` status `ready` deltaP `17.8055` edge `0.4401` maxDD `-9.8581`
- `market_context_high->metal_24h` score `4.2123` n `178` status `ready` deltaP `20.2989` edge `0.4583` maxDD `-12.7414`
- `market_context_high->index_24h` score `2.3361` n `178` status `ready` deltaP `13.0072` edge `0.2308` maxDD `-4.1604`
- `market_context_high->equity_4h` score `2.2732` n `199` status `ready` deltaP `14.2771` edge `0.2037` maxDD `-5.0894`
- `market_context_high->unknown_24h` score `1.9936` n `178` status `ready` deltaP `12.4766` edge `0.615` maxDD `-35.8966`
- `market_context_high->index_4h` score `0.4449` n `199` status `ready` deltaP `9.9407` edge `0.0797` maxDD `-3.7119`
- `market_context_high->equity_24h` score `0.4327` n `178` status `ready` deltaP `10.68` edge `0.4547` maxDD `-33.1875`
- `market_context_high->crypto_major_1h` score `0.3624` n `199` status `ready` deltaP `5.5969` edge `0.0915` maxDD `-3.2225`
- `market_context_high->crypto_major_24h` score `0.3127` n `178` status `ready` deltaP `19.2065` edge `0.7566` maxDD `-62.3533`
- `market_context_high->fx_24h` score `0.2275` n `178` status `ready` deltaP `14.56` edge `0.0268` maxDD `-1.3925`
- `market_context_high->crypto_alt_1h` score `0.0806` n `199` status `ready` deltaP `5.0086` edge `0.0847` maxDD `-4.9097`
- `market_context_high->equity_1h` score `-0.2774` n `199` status `ready` deltaP `3.6395` edge `0.032` maxDD `-2.6836`
- `market_context_high->unknown_1h` score `-0.5516` n `199` status `ready` deltaP `2.8383` edge `0.0303` maxDD `-3.6151`
- `market_context_high->metal_1h` score `-0.5671` n `199` status `ready` deltaP `5.982` edge `0.021` maxDD `-6.3532`
- `market_context_high->metal_4h` score `-0.6166` n `199` status `ready` deltaP `12.3905` edge `0.1352` maxDD `-12.5349`
- `market_context_high->fx_1h` score `-0.6846` n `199` status `ready` deltaP `-3.6515` edge `-0.0002` maxDD `-0.3914`
- `market_context_high->index_1h` score `-0.762` n `199` status `ready` deltaP `-1.2036` edge `0.0077` maxDD `-1.7205`
- `market_context_high->fx_4h` score `-0.9828` n `199` status `ready` deltaP `-4.8864` edge `-0.0046` maxDD `-1.1056`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
