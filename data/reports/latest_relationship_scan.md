# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-25T14:37:31.323189+00:00`
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

- `market_context_high->unknown_4h` score `37.2325` n `113` status `ready` deltaP `-0.4439` edge `3.1392` maxDD `-1.016`
- `market_context_high->commodity_24h` score `0.1109` n `62` status `ready` deltaP `7.9413` edge `0.0472` maxDD `-3.6055`
- `market_context_high->fx_4h` score `0.0085` n `113` status `ready` deltaP `7.7636` edge `0.0088` maxDD `-0.4545`
- `market_context_high->fx_1h` score `-0.0661` n `113` status `ready` deltaP `3.5597` edge `0.0027` maxDD `-0.1258`
- `market_context_high->commodity_1h` score `-0.5314` n `113` status `ready` deltaP `-0.4822` edge `0.009` maxDD `-1.0053`
- `market_context_high->metal_1h` score `-0.6635` n `113` status `ready` deltaP `4.3347` edge `-0.005` maxDD `-1.6682`
- `market_context_high->index_1h` score `-0.6698` n `113` status `ready` deltaP `-2.1859` edge `-0.0061` maxDD `-1.2155`
- `market_context_high->commodity_4h` score `-0.8711` n `113` status `ready` deltaP `-2.8478` edge `0.0302` maxDD `-1.165`
- `market_context_high->crypto_major_24h` score `-1.2996` n `62` status `ready` deltaP `-5.606` edge `-0.0267` maxDD `-4.5369`
- `market_context_high->crypto_major_1h` score `-1.3581` n `113` status `ready` deltaP `2.6482` edge `-0.0337` maxDD `-9.3126`
- `market_context_high->fx_24h` score `-1.5293` n `62` status `ready` deltaP `2.9682` edge `0.01` maxDD `-1.2451`
- `market_context_high->metal_4h` score `-1.8892` n `113` status `ready` deltaP `4.7661` edge `-0.0182` maxDD `-5.3474`
- `market_context_high->index_24h` score `-2.1217` n `62` status `ready` deltaP `-1.9321` edge `-0.1309` maxDD `-4.925`
- `market_context_high->index_4h` score `-2.1862` n `113` status `ready` deltaP `-8.3774` edge `-0.037` maxDD `-4.3282`
- `market_context_high->crypto_alt_1h` score `-3.0983` n `113` status `ready` deltaP `-1.5606` edge `-0.0604` maxDD `-11.3243`
- `market_context_high->metal_24h` score `-3.7561` n `62` status `ready` deltaP `-10.1367` edge `0.0216` maxDD `-7.3625`
- `market_context_high->equity_1h` score `-3.8643` n `113` status `ready` deltaP `-0.3895` edge `-0.0921` maxDD `-12.1865`
- `market_context_high->crypto_alt_24h` score `-7.3377` n `62` status `ready` deltaP `-3.1026` edge `-0.2744` maxDD `-42.3182`
- `market_context_high->crypto_major_4h` score `-9.9752` n `113` status `ready` deltaP `-12.7428` edge `-0.2465` maxDD `-32.9851`
- `market_context_high->equity_24h` score `-11.9448` n `62` status `ready` deltaP `-17.9883` edge `-0.8831` maxDD `-36.6024`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
