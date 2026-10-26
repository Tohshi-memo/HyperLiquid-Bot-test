# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-26T16:07:28.904479+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `80`

- Symbol pattern count: `7962`

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

- `market_context_high->unknown_4h` score `86.3228` n `151` status `ready` deltaP `0.499` edge `7.2238` maxDD `-1.0178`
- `market_context_high->unknown_1h` score `27.1777` n `154` status `ready` deltaP `1.5806` edge `2.3032` maxDD `-1.5807`
- `market_context_high->metal_24h` score `0.4495` n `113` status `ready` deltaP `26.7541` edge `0.1463` maxDD `-7.3625`
- `market_context_high->fx_1h` score `0.1956` n `154` status `ready` deltaP `7.4423` edge `0.0025` maxDD `-0.1986`
- `market_context_high->fx_4h` score `0.1381` n `151` status `ready` deltaP `9.4731` edge `0.0082` maxDD `-0.4545`
- `market_context_high->index_24h` score `-0.0616` n `113` status `ready` deltaP `15.7283` edge `0.0132` maxDD `-4.7426`
- `market_context_high->fx_24h` score `-0.0966` n `113` status `ready` deltaP `17.6163` edge `0.0274` maxDD `-1.2451`
- `market_context_high->metal_1h` score `-0.1677` n `154` status `ready` deltaP `7.7378` edge `0.0061` maxDD `-1.6682`
- `market_context_high->commodity_1h` score `-0.3164` n `154` status `ready` deltaP `1.8003` edge `0.0117` maxDD `-1.0053`
- `market_context_high->index_1h` score `-0.6218` n `154` status `ready` deltaP `-0.6008` edge `-0.002` maxDD `-1.8971`
- `market_context_high->commodity_4h` score `-0.6439` n `151` status `ready` deltaP `4.6559` edge `0.0382` maxDD `-1.165`
- `market_context_high->crypto_major_1h` score `-0.9537` n `154` status `ready` deltaP `3.6453` edge `0.0115` maxDD `-9.3126`
- `market_context_high->metal_4h` score `-1.0306` n `151` status `ready` deltaP `6.2818` edge `-0.003` maxDD `-5.3474`
- `market_context_high->equity_1h` score `-1.8648` n `154` status `ready` deltaP `0.9954` edge `-0.0181` maxDD `-12.2088`
- `market_context_high->crypto_alt_1h` score `-2.0422` n `154` status `ready` deltaP `-0.8049` edge `-0.008` maxDD `-13.2099`
- `market_context_high->index_4h` score `-3.4824` n `151` status `ready` deltaP `-6.939` edge `-0.0263` maxDD `-6.7447`
- `market_context_high->crypto_major_24h` score `-4.3776` n `113` status `ready` deltaP `-2.1625` edge `-0.0611` maxDD `-29.1905`
- `market_context_high->crypto_major_4h` score `-4.8231` n `151` status `ready` deltaP `-1.9908` edge `-0.1011` maxDD `-32.9851`
- `market_context_high->equity_24h` score `-5.998` n `113` status `ready` deltaP `-2.3911` edge `-0.1985` maxDD `-36.3631`
- `market_context_high->commodity_24h` score `-6.3496` n `113` status `ready` deltaP `-17.3433` edge `-0.1395` maxDD `-24.0477`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
