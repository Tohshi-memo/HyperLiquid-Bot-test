# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-27T19:37:28.524392+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8770`

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

- `market_context_high->unknown_4h` score `73.0713` n `138` status `ready` deltaP `4.7565` edge `6.0728` maxDD `-0.5521`
- `market_context_high->index_24h` score `1.9735` n `135` status `ready` deltaP `27.1875` edge `0.052` maxDD `-2.17`
- `market_context_high->fx_1h` score `0.3804` n `148` status `ready` deltaP `9.6779` edge `0.003` maxDD `-0.1986`
- `market_context_high->fx_4h` score `0.3292` n `138` status `ready` deltaP `11.592` edge `0.01` maxDD `-0.4545`
- `market_context_high->metal_1h` score `-0.0928` n `148` status `ready` deltaP `8.3225` edge `0.0073` maxDD `-1.3073`
- `market_context_high->crypto_major_1h` score `-0.3369` n `148` status `ready` deltaP `7.8006` edge `0.0331` maxDD `-6.9306`
- `market_context_high->commodity_4h` score `-0.3378` n `138` status `ready` deltaP `6.9039` edge `0.0477` maxDD `-1.0837`
- `market_context_high->fx_24h` score `-0.4822` n `135` status `ready` deltaP `11.0417` edge `0.0218` maxDD `-1.2451`
- `market_context_high->commodity_1h` score `-0.5818` n `148` status `ready` deltaP `0.0769` edge `0.0094` maxDD `-1.0053`
- `market_context_high->index_1h` score `-0.6591` n `148` status `ready` deltaP `-1.8773` edge `-0.0037` maxDD `-1.4631`
- `market_context_high->metal_4h` score `-0.8601` n `138` status `ready` deltaP `7.622` edge `-0.007` maxDD `-4.6603`
- `market_context_high->metal_24h` score `-1.1032` n `135` status `ready` deltaP `14.7106` edge `0.0878` maxDD `-8.2244`
- `market_context_high->equity_1h` score `-1.457` n `148` status `ready` deltaP `1.4929` edge `-0.0055` maxDD `-9.2993`
- `market_context_high->equity_24h` score `-1.6494` n `135` status `ready` deltaP `8.0671` edge `0.1052` maxDD `-15.7143`
- `market_context_high->crypto_alt_1h` score `-1.6742` n `148` status `ready` deltaP `2.4599` edge `0.0053` maxDD `-12.2409`
- `market_context_high->unknown_1h` score `-2.5195` n `148` status `ready` deltaP `0.7` edge `-0.1657` maxDD `-1.5807`
- `market_context_high->index_4h` score `-2.9314` n `138` status `ready` deltaP `-7.2441` edge `-0.0338` maxDD `-5.6417`
- `market_context_high->crypto_major_24h` score `-3.7618` n `135` status `ready` deltaP `0.544` edge `-0.0002` maxDD `-29.1905`
- `market_context_high->crypto_major_4h` score `-3.8135` n `138` status `ready` deltaP `3.3183` edge `-0.0791` maxDD `-27.2215`
- `market_context_high->equity_4h` score `-5.4786` n `138` status `ready` deltaP `-0.1524` edge `-0.178` maxDD `-35.2032`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
