# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-26T07:07:36.707043+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `80`

- Symbol pattern count: `8998`

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

- `market_context_high->unknown_4h` score `20.5875` n `121` status `ready` deltaP `-2.7213` edge `1.7673` maxDD `-1.016`
- `market_context_high->metal_24h` score `0.6076` n `113` status `ready` deltaP `28.4445` edge `0.1553` maxDD `-7.3625`
- `market_context_high->fx_24h` score `0.2028` n `113` status `ready` deltaP `22.7446` edge `0.0316` maxDD `-1.2451`
- `market_context_high->fx_4h` score `0.0441` n `121` status `ready` deltaP `8.2682` edge `0.0084` maxDD `-0.4545`
- `market_context_high->fx_1h` score `0.0098` n `131` status `ready` deltaP `5.2612` edge `0.002` maxDD `-0.1986`
- `market_context_high->metal_1h` score `-0.4032` n `131` status `ready` deltaP `4.4236` edge `-0.002` maxDD `-1.6682`
- `market_context_high->commodity_1h` score `-0.4706` n `131` status `ready` deltaP `0.0971` edge `0.0102` maxDD `-1.0053`
- `market_context_high->commodity_4h` score `-0.5767` n `121` status `ready` deltaP `0.999` edge `0.0423` maxDD `-1.165`
- `market_context_high->index_1h` score `-0.6584` n `131` status `ready` deltaP `-2.0878` edge `-0.0053` maxDD `-1.2155`
- `market_context_high->index_24h` score `-0.66` n `113` status `ready` deltaP `10.2615` edge `-0.0248` maxDD `-4.925`
- `market_context_high->metal_4h` score `-1.2207` n `121` status `ready` deltaP `4.5769` edge `-0.016` maxDD `-5.3474`
- `market_context_high->crypto_major_1h` score `-1.3646` n `131` status `ready` deltaP `1.7587` edge `-0.0286` maxDD `-9.3126`
- `market_context_high->index_4h` score `-2.195` n `121` status `ready` deltaP `-8.7419` edge `-0.0357` maxDD `-4.3282`
- `market_context_high->equity_1h` score `-2.388` n `131` status `ready` deltaP `-0.4411` edge `-0.0746` maxDD `-12.2891`
- `market_context_high->crypto_alt_1h` score `-3.8157` n `131` status `ready` deltaP `-2.1621` edge `-0.0551` maxDD `-13.2099`
- `market_context_high->crypto_major_24h` score `-5.0054` n `113` status `ready` deltaP `-2.9406` edge `-0.1364` maxDD `-29.1905`
- `market_context_high->crypto_major_4h` score `-6.311` n `121` status `ready` deltaP `-10.4591` edge `-0.2354` maxDD `-32.9851`
- `market_context_high->commodity_24h` score `-6.5656` n `113` status `ready` deltaP `-18.9927` edge `-0.1562` maxDD `-24.0477`
- `market_context_high->equity_24h` score `-7.3081` n `113` status `ready` deltaP `-5.5955` edge `-0.3421` maxDD `-36.6024`
- `market_context_high->equity_4h` score `-8.9528` n `121` status `ready` deltaP `-8.6298` edge `-0.3641` maxDD `-45.7601`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
