# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-25T14:52:28.248413+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `5252`

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

- `market_context_high->unknown_4h` score `37.2901` n `113` status `ready` deltaP `-0.4439` edge `3.144` maxDD `-1.016`
- `market_context_high->commodity_24h` score `0.1061` n `62` status `ready` deltaP `7.9413` edge `0.0468` maxDD `-3.6055`
- `market_context_high->fx_4h` score `-0.0049` n `113` status `ready` deltaP `7.6112` edge `0.0087` maxDD `-0.4545`
- `market_context_high->fx_1h` score `-0.0583` n `113` status `ready` deltaP `3.7094` edge `0.0027` maxDD `-0.1258`
- `market_context_high->commodity_1h` score `-0.5445` n `113` status `ready` deltaP `-0.6319` edge `0.0089` maxDD `-1.0053`
- `market_context_high->metal_1h` score `-0.6635` n `113` status `ready` deltaP `4.3347` edge `-0.005` maxDD `-1.6682`
- `market_context_high->index_1h` score `-0.6783` n `113` status `ready` deltaP `-2.3356` edge `-0.0062` maxDD `-1.2155`
- `market_context_high->commodity_4h` score `-0.8616` n `113` status `ready` deltaP `-2.6954` edge `0.0304` maxDD `-1.165`
- `market_context_high->crypto_major_24h` score `-1.2996` n `62` status `ready` deltaP `-5.606` edge `-0.0267` maxDD `-4.5369`
- `market_context_high->crypto_major_1h` score `-1.3581` n `113` status `ready` deltaP `2.6482` edge `-0.0337` maxDD `-9.3126`
- `market_context_high->fx_24h` score `-1.5444` n `62` status `ready` deltaP `2.7946` edge `0.0099` maxDD `-1.2451`
- `market_context_high->metal_4h` score `-1.8892` n `113` status `ready` deltaP `4.7661` edge `-0.0182` maxDD `-5.3474`
- `market_context_high->index_24h` score `-2.1201` n `62` status `ready` deltaP `-1.9321` edge `-0.1307` maxDD `-4.925`
- `market_context_high->index_4h` score `-2.1862` n `113` status `ready` deltaP `-8.3774` edge `-0.037` maxDD `-4.3282`
- `market_context_high->crypto_alt_1h` score `-3.1127` n `113` status `ready` deltaP `-1.7103` edge `-0.0606` maxDD `-11.3243`
- `market_context_high->metal_24h` score `-3.7537` n `62` status `ready` deltaP `-10.1367` edge `0.0218` maxDD `-7.3625`
- `market_context_high->equity_1h` score `-3.8799` n `113` status `ready` deltaP `-0.5392` edge `-0.0924` maxDD `-12.1865`
- `market_context_high->crypto_alt_24h` score `-7.3556` n `62` status `ready` deltaP `-3.1026` edge `-0.2767` maxDD `-42.3182`
- `market_context_high->crypto_major_4h` score `-9.9716` n `113` status `ready` deltaP `-12.7428` edge `-0.2462` maxDD `-32.9851`
- `market_context_high->equity_24h` score `-11.9362` n `62` status `ready` deltaP `-17.9883` edge `-0.882` maxDD `-36.6024`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
