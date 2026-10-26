# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-26T16:37:35.043440+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `80`

- Symbol pattern count: `8018`

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

- `market_context_high->unknown_4h` score `64.6412` n `151` status `ready` deltaP `0.499` edge `5.417` maxDD `-1.0178`
- `market_context_high->unknown_1h` score `27.0758` n `154` status `ready` deltaP `1.4309` edge `2.2957` maxDD `-1.5807`
- `market_context_high->metal_24h` score `0.4206` n `113` status `ready` deltaP `26.4075` edge `0.1449` maxDD `-7.3625`
- `market_context_high->fx_1h` score `0.1836` n `154` status `ready` deltaP `7.2926` edge `0.0025` maxDD `-0.1986`
- `market_context_high->fx_4h` score `0.1113` n `151` status `ready` deltaP `9.1687` edge `0.008` maxDD `-0.4545`
- `market_context_high->index_24h` score `-0.0608` n `113` status `ready` deltaP `15.7283` edge `0.0133` maxDD `-4.7426`
- `market_context_high->fx_24h` score `-0.1186` n `113` status `ready` deltaP `17.2697` edge `0.0269` maxDD `-1.2451`
- `market_context_high->metal_1h` score `-0.1482` n `154` status `ready` deltaP `8.0372` edge `0.0066` maxDD `-1.6682`
- `market_context_high->commodity_1h` score `-0.3391` n `154` status `ready` deltaP `1.6506` edge `0.0108` maxDD `-1.0053`
- `market_context_high->index_1h` score `-0.6031` n `154` status `ready` deltaP `-0.3014` edge `-0.0016` maxDD `-1.8971`
- `market_context_high->commodity_4h` score `-0.6862` n `151` status `ready` deltaP `4.3515` edge `0.0367` maxDD `-1.165`
- `market_context_high->crypto_major_1h` score `-0.9148` n `154` status `ready` deltaP `3.9447` edge `0.0145` maxDD `-9.3126`
- `market_context_high->metal_4h` score `-1.0109` n `151` status `ready` deltaP `6.5862` edge `-0.0025` maxDD `-5.3474`
- `market_context_high->equity_1h` score `-1.832` n `154` status `ready` deltaP `1.2948` edge `-0.0159` maxDD `-12.2088`
- `market_context_high->crypto_alt_1h` score `-1.9939` n `154` status `ready` deltaP `-0.5055` edge `-0.0038` maxDD `-13.2099`
- `market_context_high->index_4h` score `-3.4812` n `151` status `ready` deltaP `-6.939` edge `-0.0262` maxDD `-6.7447`
- `market_context_high->crypto_major_24h` score `-4.3975` n `113` status `ready` deltaP `-2.3359` edge `-0.0625` maxDD `-29.1905`
- `market_context_high->crypto_major_4h` score `-4.8012` n `151` status `ready` deltaP `-1.8385` edge `-0.0993` maxDD `-32.9851`
- `market_context_high->equity_24h` score `-6.0496` n `113` status `ready` deltaP `-2.7377` edge `-0.2028` maxDD `-36.3631`
- `market_context_high->commodity_24h` score `-6.3488` n `113` status `ready` deltaP `-17.3433` edge `-0.1394` maxDD `-24.0477`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
