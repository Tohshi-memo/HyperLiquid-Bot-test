# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-05T23:51:30.542929+00:00`
- Price records: `672`
- Market context records: `5825`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `88`

- Symbol pattern count: `10024`

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

- `market_context_high->equity_4h` score `0.4434` n `278` status `ready` deltaP `6.8148` edge `0.1373` maxDD `-6.9958`
- `market_context_high->fx_1h` score `-0.2359` n `278` status `ready` deltaP `2.6386` edge `0.0007` maxDD `-0.5499`
- `market_context_high->equity_24h` score `-0.2671` n `248` status `ready` deltaP `15.3954` edge `0.383` maxDD `-31.6316`
- `market_context_high->commodity_1h` score `-0.5148` n `278` status `ready` deltaP `-0.6322` edge `-0.0009` maxDD `-2.2045`
- `market_context_high->index_1h` score `-0.5784` n `278` status `ready` deltaP `0.9025` edge `0.0046` maxDD `-0.7819`
- `market_context_high->metal_1h` score `-0.5914` n `278` status `ready` deltaP `2.5514` edge `0.0008` maxDD `-2.0339`
- `market_context_high->equity_1h` score `-0.6089` n `278` status `ready` deltaP `2.7679` edge `0.0315` maxDD `-5.0555`
- `market_context_high->crypto_major_1h` score `-0.8903` n `278` status `ready` deltaP `3.1211` edge `0.0371` maxDD `-6.2348`
- `market_context_high->crypto_alt_1h` score `-1.0588` n `278` status `ready` deltaP `1.5326` edge `0.035` maxDD `-6.6758`
- `market_context_high->index_4h` score `-1.1458` n `278` status `ready` deltaP `1.0539` edge `0.0148` maxDD `-3.165`
- `market_context_high->fx_24h` score `-1.5026` n `248` status `ready` deltaP `9.4422` edge `0.0262` maxDD `-5.5435`
- `market_context_high->fx_4h` score `-1.5412` n `278` status `ready` deltaP `-0.5977` edge `0.0013` maxDD `-2.2593`
- `market_context_high->metal_4h` score `-2.2` n `278` status `ready` deltaP `-4.7015` edge `-0.0448` maxDD `-9.1388`
- `market_context_high->commodity_4h` score `-2.6861` n `278` status `ready` deltaP `-1.1449` edge `-0.0164` maxDD `-8.6511`
- `market_context_high->index_24h` score `-2.8167` n `248` status `ready` deltaP `3.7131` edge `0.0286` maxDD `-18.1572`
- `market_context_high->crypto_major_4h` score `-2.9338` n `278` status `ready` deltaP `7.2239` edge `0.1446` maxDD `-25.6458`
- `market_context_high->crypto_alt_4h` score `-4.6885` n `278` status `ready` deltaP `4.5962` edge `0.0795` maxDD `-28.7346`
- `market_context_high->commodity_24h` score `-5.7729` n `248` status `ready` deltaP `-12.4608` edge `-0.0611` maxDD `-30.3426`
- `market_context_high->metal_24h` score `-7.0142` n `248` status `ready` deltaP `-1.7809` edge `-0.2239` maxDD `-15.8997`
- `market_context_high->crypto_alt_24h` score `-12.5238` n `248` status `ready` deltaP `-10.0246` edge `-0.5081` maxDD `-61.7883`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
