# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-26T04:52:25.426798+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `64`

- Symbol pattern count: `7162`

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

- `market_context_high->unknown_4h` score `27.0956` n `113` status `ready` deltaP `-2.7304` edge `2.3097` maxDD `-1.016`
- `market_context_high->metal_24h` score `0.3717` n `106` status `ready` deltaP `25.3472` edge `0.1457` maxDD `-7.3625`
- `market_context_high->fx_24h` score `0.1462` n `106` status `ready` deltaP `21.9111` edge `0.0299` maxDD `-1.2451`
- `market_context_high->fx_4h` score `-0.0377` n `113` status `ready` deltaP `7.3063` edge `0.008` maxDD `-0.4545`
- `market_context_high->fx_1h` score `-0.0509` n `124` status `ready` deltaP `4.124` edge `0.0018` maxDD `-0.1986`
- `market_context_high->commodity_1h` score `-0.3569` n `124` status `ready` deltaP `-0.7485` edge `0.0093` maxDD `-1.0053`
- `market_context_high->metal_1h` score `-0.3788` n `124` status `ready` deltaP `4.8484` edge `-0.0017` maxDD `-1.6682`
- `market_context_high->commodity_4h` score `-0.5202` n `113` status `ready` deltaP `1.7253` edge `0.0447` maxDD `-1.165`
- `market_context_high->index_1h` score `-0.6374` n `124` status `ready` deltaP `-1.7288` edge `-0.005` maxDD `-1.2155`
- `market_context_high->index_24h` score `-0.7607` n `106` status `ready` deltaP `9.886` edge `-0.0352` maxDD `-4.925`
- `market_context_high->crypto_major_1h` score `-1.4214` n `124` status `ready` deltaP `2.062` edge `-0.0379` maxDD `-9.3126`
- `market_context_high->metal_4h` score `-2.1179` n `113` status `ready` deltaP `2.3271` edge `-0.021` maxDD `-5.3474`
- `market_context_high->index_4h` score `-2.1632` n `113` status `ready` deltaP `-7.92` edge `-0.0371` maxDD `-4.3282`
- `market_context_high->equity_1h` score `-2.4589` n `124` status `ready` deltaP `-0.5892` edge `-0.0827` maxDD `-12.2891`
- `market_context_high->crypto_alt_1h` score `-4.0223` n `124` status `ready` deltaP `-2.6753` edge `-0.0689` maxDD `-13.2099`
- `market_context_high->crypto_major_24h` score `-4.169` n `106` status `ready` deltaP `-1.4642` edge `-0.1242` maxDD `-24.7088`
- `market_context_high->commodity_24h` score `-5.6577` n `106` status `ready` deltaP `-16.8304` edge `-0.1341` maxDD `-19.9898`
- `market_context_high->equity_24h` score `-7.3998` n `106` status `ready` deltaP `-4.2944` edge `-0.3917` maxDD `-36.6024`
- `market_context_high->crypto_major_4h` score `-10.1684` n `113` status `ready` deltaP `-12.7428` edge `-0.2626` maxDD `-32.9851`
- `market_context_high->crypto_alt_24h` score `-12.4454` n `106` status `ready` deltaP `-12.4148` edge `-0.4697` maxDD `-72.115`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
