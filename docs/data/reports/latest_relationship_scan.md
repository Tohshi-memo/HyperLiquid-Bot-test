# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-05T23:37:25.916704+00:00`
- Price records: `672`
- Market context records: `5824`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `88`

- Symbol pattern count: `10006`

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

- `market_context_high->equity_4h` score `0.4191` n `279` status `ready` deltaP `6.721` edge `0.1359` maxDD `-6.9958`
- `market_context_high->fx_1h` score `-0.2265` n `279` status `ready` deltaP `2.8062` edge `0.0008` maxDD `-0.5499`
- `market_context_high->equity_24h` score `-0.2323` n `248` status `ready` deltaP `15.3954` edge `0.3859` maxDD `-31.6316`
- `market_context_high->commodity_1h` score `-0.5128` n `279` status `ready` deltaP `-0.5924` edge `-0.0009` maxDD `-2.2045`
- `market_context_high->index_1h` score `-0.583` n `279` status `ready` deltaP `0.8601` edge `0.0043` maxDD `-0.7819`
- `market_context_high->metal_1h` score `-0.6109` n `279` status `ready` deltaP `2.3528` edge `0.0005` maxDD `-2.0339`
- `market_context_high->equity_1h` score `-0.6504` n `279` status `ready` deltaP `2.5487` edge `0.0295` maxDD `-5.0555`
- `market_context_high->crypto_major_1h` score `-0.9208` n `279` status `ready` deltaP `2.92` edge `0.0359` maxDD `-6.2348`
- `market_context_high->crypto_alt_1h` score `-1.0828` n `279` status `ready` deltaP `1.3366` edge `0.0343` maxDD `-6.6758`
- `market_context_high->index_4h` score `-1.1503` n `279` status `ready` deltaP `0.9988` edge `0.0146` maxDD `-3.165`
- `market_context_high->fx_24h` score `-1.4995` n `248` status `ready` deltaP `9.4422` edge `0.0266` maxDD `-5.5435`
- `market_context_high->fx_4h` score `-1.5298` n `279` status `ready` deltaP `-0.4223` edge `0.0016` maxDD `-2.2593`
- `market_context_high->metal_4h` score `-2.1879` n `279` status `ready` deltaP `-4.5301` edge `-0.0444` maxDD `-9.1388`
- `market_context_high->commodity_4h` score `-2.6806` n `279` status `ready` deltaP `-1.0769` edge `-0.0164` maxDD `-8.6511`
- `market_context_high->index_24h` score `-2.8174` n `248` status `ready` deltaP `3.7131` edge `0.0285` maxDD `-18.1572`
- `market_context_high->crypto_major_4h` score `-2.9043` n `279` status `ready` deltaP `7.3515` edge `0.1462` maxDD `-25.6458`
- `market_context_high->crypto_alt_4h` score `-4.6486` n `279` status `ready` deltaP `4.7354` edge `0.0819` maxDD `-28.7346`
- `market_context_high->commodity_24h` score `-5.7714` n `248` status `ready` deltaP `-12.4608` edge `-0.0609` maxDD `-30.3426`
- `market_context_high->metal_24h` score `-7.1322` n `248` status `ready` deltaP `-2.0105` edge `-0.2247` maxDD `-16.1662`
- `market_context_high->crypto_alt_24h` score `-12.502` n `248` status `ready` deltaP `-10.0246` edge `-0.5053` maxDD `-61.7883`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
