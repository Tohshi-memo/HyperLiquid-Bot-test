# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-05T22:07:26.137770+00:00`
- Price records: `672`
- Market context records: `5817`
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

- `market_context_high->equity_4h` score `0.2834` n `285` status `ready` deltaP `6.1943` edge `0.1281` maxDD `-6.9958`
- `market_context_high->equity_24h` score `-0.0283` n `248` status `ready` deltaP `15.3954` edge `0.4029` maxDD `-31.6316`
- `market_context_high->fx_1h` score `-0.1898` n `285` status `ready` deltaP `3.4363` edge `0.0013` maxDD `-0.5499`
- `market_context_high->commodity_1h` score `-0.5695` n `285` status `ready` deltaP `-1.3872` edge `-0.0027` maxDD `-2.2187`
- `market_context_high->metal_1h` score `-0.6171` n `285` status `ready` deltaP `2.2902` edge `0.0004` maxDD `-2.0339`
- `market_context_high->index_1h` score `-0.6401` n `285` status `ready` deltaP `0.1849` edge `0.003` maxDD `-0.9038`
- `market_context_high->equity_1h` score `-0.6982` n `285` status `ready` deltaP `2.4168` edge `0.0264` maxDD `-5.0555`
- `market_context_high->crypto_major_1h` score `-0.8577` n `285` status `ready` deltaP `3.2446` edge `0.039` maxDD `-6.2348`
- `market_context_high->crypto_alt_1h` score `-1.0359` n `285` status `ready` deltaP `1.7428` edge `0.0355` maxDD `-6.6758`
- `market_context_high->index_4h` score `-1.2107` n `285` status `ready` deltaP `0.2412` edge `0.0119` maxDD `-3.165`
- `market_context_high->fx_4h` score `-1.4608` n `285` status `ready` deltaP `0.6039` edge `0.0036` maxDD `-2.2593`
- `market_context_high->fx_24h` score `-1.4785` n `248` status `ready` deltaP `9.4422` edge `0.0293` maxDD `-5.5435`
- `market_context_high->metal_4h` score `-2.1369` n `285` status `ready` deltaP `-3.9233` edge `-0.0419` maxDD `-9.1388`
- `market_context_high->crypto_major_4h` score `-2.6742` n `285` status `ready` deltaP `8.0986` edge `0.1604` maxDD `-25.6458`
- `market_context_high->commodity_4h` score `-2.7249` n `285` status `ready` deltaP `-1.495` edge `-0.0173` maxDD `-8.6511`
- `market_context_high->index_24h` score `-2.8159` n `248` status `ready` deltaP `3.7131` edge `0.0287` maxDD `-18.1572`
- `market_context_high->crypto_alt_4h` score `-4.4106` n `285` status `ready` deltaP `5.5504` edge `0.0963` maxDD `-28.7346`
- `market_context_high->commodity_24h` score `-5.8431` n `248` status `ready` deltaP `-12.4608` edge `-0.0624` maxDD `-30.958`
- `market_context_high->metal_24h` score `-7.8525` n `248` status `ready` deltaP `-3.3883` edge `-0.2306` maxDD `-17.7616`
- `market_context_high->crypto_major_24h` score `-12.2673` n `248` status `ready` deltaP `-3.3714` edge `-0.301` maxDD `-36.5708`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
