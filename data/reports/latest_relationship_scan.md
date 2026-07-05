# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-05T23:22:26.358505+00:00`
- Price records: `672`
- Market context records: `5823`
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

- `market_context_high->equity_4h` score `0.3913` n `280` status `ready` deltaP `6.6289` edge `0.1342` maxDD `-6.9958`
- `market_context_high->equity_24h` score `-0.1987` n `248` status `ready` deltaP `15.3954` edge `0.3887` maxDD `-31.6316`
- `market_context_high->fx_1h` score `-0.2248` n `280` status `ready` deltaP `2.8229` edge `0.0009` maxDD `-0.5499`
- `market_context_high->commodity_1h` score `-0.51` n `280` status `ready` deltaP `-0.5539` edge `-0.0008` maxDD `-2.2045`
- `market_context_high->index_1h` score `-0.5906` n `280` status `ready` deltaP `0.8191` edge `0.0036` maxDD `-0.7819`
- `market_context_high->metal_1h` score `-0.6183` n `280` status `ready` deltaP `2.3054` edge `0.0002` maxDD `-2.0339`
- `market_context_high->equity_1h` score `-0.6954` n `280` status `ready` deltaP `2.3311` edge `0.0272` maxDD `-5.0555`
- `market_context_high->crypto_major_1h` score `-0.9548` n `280` status `ready` deltaP `2.87` edge `0.0334` maxDD `-6.2348`
- `market_context_high->crypto_alt_1h` score `-1.1212` n `280` status `ready` deltaP `1.142` edge `0.0324` maxDD `-6.6758`
- `market_context_high->index_4h` score `-1.1577` n `280` status `ready` deltaP `0.9451` edge `0.014` maxDD `-3.165`
- `market_context_high->fx_24h` score `-1.4956` n `248` status `ready` deltaP `9.4422` edge `0.0271` maxDD `-5.5435`
- `market_context_high->fx_4h` score `-1.5184` n `280` status `ready` deltaP `-0.2482` edge `0.0019` maxDD `-2.2593`
- `market_context_high->metal_4h` score `-2.1752` n `280` status `ready` deltaP `-4.3598` edge `-0.0439` maxDD `-9.1388`
- `market_context_high->commodity_4h` score `-2.6765` n `280` status `ready` deltaP `-1.0104` edge `-0.0165` maxDD `-8.6511`
- `market_context_high->index_24h` score `-2.8167` n `248` status `ready` deltaP `3.7131` edge `0.0286` maxDD `-18.1572`
- `market_context_high->crypto_major_4h` score `-2.8786` n `280` status `ready` deltaP `7.4783` edge `0.1475` maxDD `-25.6458`
- `market_context_high->crypto_alt_4h` score `-4.6123` n `280` status `ready` deltaP `4.8737` edge `0.084` maxDD `-28.7346`
- `market_context_high->commodity_24h` score `-5.7729` n `248` status `ready` deltaP `-12.4608` edge `-0.0611` maxDD `-30.3426`
- `market_context_high->metal_24h` score `-7.2414` n `248` status `ready` deltaP `-2.2401` edge `-0.2256` maxDD `-16.3666`
- `market_context_high->crypto_alt_24h` score `-12.4794` n `248` status `ready` deltaP `-10.0246` edge `-0.5024` maxDD `-61.7883`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
