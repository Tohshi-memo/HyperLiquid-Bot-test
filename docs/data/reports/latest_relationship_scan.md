# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-26T15:52:32.566374+00:00`
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

- `market_context_high->unknown_4h` score `97.268` n `151` status `ready` deltaP `0.499` edge `8.1359` maxDD `-1.0178`
- `market_context_high->unknown_1h` score `27.1741` n `154` status `ready` deltaP `1.5806` edge `2.3029` maxDD `-1.5807`
- `market_context_high->metal_24h` score `0.4632` n `113` status `ready` deltaP `26.9275` edge `0.1469` maxDD `-7.3625`
- `market_context_high->fx_1h` score `0.2088` n `154` status `ready` deltaP `7.592` edge `0.0026` maxDD `-0.1986`
- `market_context_high->fx_4h` score `0.1502` n `151` status `ready` deltaP `9.6253` edge `0.0082` maxDD `-0.4545`
- `market_context_high->index_24h` score `-0.0729` n `113` status `ready` deltaP `15.555` edge `0.0129` maxDD `-4.7426`
- `market_context_high->fx_24h` score `-0.0853` n `113` status `ready` deltaP `17.7896` edge `0.0277` maxDD `-1.2451`
- `market_context_high->metal_1h` score `-0.177` n `154` status `ready` deltaP `7.5881` edge `0.0059` maxDD `-1.6682`
- `market_context_high->commodity_1h` score `-0.3116` n `154` status `ready` deltaP `1.8003` edge `0.0121` maxDD `-1.0053`
- `market_context_high->commodity_4h` score `-0.6245` n `151` status `ready` deltaP `4.8081` edge `0.0388` maxDD `-1.165`
- `market_context_high->index_1h` score `-0.6319` n `154` status `ready` deltaP `-0.7505` edge `-0.0023` maxDD `-1.8971`
- `market_context_high->crypto_major_1h` score `-0.9685` n `154` status `ready` deltaP `3.4956` edge `0.0106` maxDD `-9.3126`
- `market_context_high->metal_4h` score `-1.0409` n `151` status `ready` deltaP `6.1296` edge `-0.0033` maxDD `-5.3474`
- `market_context_high->equity_1h` score `-1.8819` n `154` status `ready` deltaP `0.8457` edge `-0.0193` maxDD `-12.2088`
- `market_context_high->crypto_alt_1h` score `-2.0617` n `154` status `ready` deltaP `-0.9546` edge `-0.0095` maxDD `-13.2099`
- `market_context_high->index_4h` score `-3.4836` n `151` status `ready` deltaP `-6.939` edge `-0.0264` maxDD `-6.7447`
- `market_context_high->crypto_major_24h` score `-4.3655` n `113` status `ready` deltaP `-1.9892` edge `-0.0607` maxDD `-29.1905`
- `market_context_high->crypto_major_4h` score `-4.8263` n `151` status `ready` deltaP `-1.9908` edge `-0.1015` maxDD `-32.9851`
- `market_context_high->equity_24h` score `-5.9918` n `113` status `ready` deltaP `-2.3911` edge `-0.1977` maxDD `-36.3631`
- `market_context_high->commodity_24h` score `-6.3504` n `113` status `ready` deltaP `-17.3433` edge `-0.1396` maxDD `-24.0477`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
