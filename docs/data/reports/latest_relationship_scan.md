# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-25T21:52:27.339178+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `5054`

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

- `market_context_high->unknown_4h` score `29.7129` n `113` status `ready` deltaP `-0.7487` edge `2.5146` maxDD `-1.016`
- `market_context_high->crypto_major_24h` score `0.5048` n `78` status `ready` deltaP `4.9813` edge `0.1114` maxDD `-4.5369`
- `market_context_high->fx_4h` score `-0.084` n `113` status `ready` deltaP `6.6966` edge `0.0082` maxDD `-0.4545`
- `market_context_high->fx_1h` score `-0.1074` n `113` status `ready` deltaP `2.8112` edge `0.0024` maxDD `-0.1258`
- `market_context_high->fx_24h` score `-0.4166` n `78` status `ready` deltaP `12.8873` edge `0.0179` maxDD `-1.2451`
- `market_context_high->commodity_1h` score `-0.4918` n `113` status `ready` deltaP `-0.0331` edge `0.0093` maxDD `-1.0053`
- `market_context_high->metal_1h` score `-0.6671` n `113` status `ready` deltaP `4.3347` edge `-0.0053` maxDD `-1.6682`
- `market_context_high->index_1h` score `-0.669` n `113` status `ready` deltaP `-2.1859` edge `-0.006` maxDD `-1.2155`
- `market_context_high->commodity_4h` score `-0.7811` n `113` status `ready` deltaP `-1.4759` edge `0.0326` maxDD `-1.165`
- `market_context_high->metal_24h` score `-1.0343` n `78` status `ready` deltaP `7.3985` edge `0.0851` maxDD `-7.3625`
- `market_context_high->index_24h` score `-1.1883` n `78` status `ready` deltaP `7.3318` edge `-0.073` maxDD `-4.925`
- `market_context_high->crypto_major_1h` score `-1.3114` n `113` status `ready` deltaP `3.5464` edge `-0.0337` maxDD `-9.3126`
- `market_context_high->commodity_24h` score `-1.6345` n `78` status `ready` deltaP `-4.3002` edge `-0.0093` maxDD `-4.7271`
- `market_context_high->metal_4h` score `-2.0206` n `113` status `ready` deltaP `3.3941` edge `-0.02` maxDD `-5.3474`
- `market_context_high->index_4h` score `-2.187` n `113` status `ready` deltaP `-8.3774` edge `-0.0371` maxDD `-4.3282`
- `market_context_high->crypto_alt_1h` score `-3.1523` n `113` status `ready` deltaP `-1.2612` edge `-0.0669` maxDD `-11.3243`
- `market_context_high->equity_1h` score `-3.9206` n `113` status `ready` deltaP `-0.9883` edge `-0.0928` maxDD `-12.1865`
- `market_context_high->crypto_alt_24h` score `-6.7288` n `78` status `ready` deltaP `-1.8029` edge `-0.205` maxDD `-42.3182`
- `market_context_high->equity_24h` score `-8.5649` n `78` status `ready` deltaP `-4.7543` edge `-0.538` maxDD `-36.6024`
- `market_context_high->crypto_major_4h` score `-10.1977` n `113` status `ready` deltaP `-14.1147` edge `-0.2559` maxDD `-32.9851`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
