# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-25T23:52:24.206818+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `5062`

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

- `market_context_high->unknown_4h` score `29.7429` n `113` status `ready` deltaP `-0.7487` edge `2.5171` maxDD `-1.016`
- `market_context_high->crypto_major_24h` score `0.4526` n `86` status `ready` deltaP `6.8193` edge `0.0948` maxDD `-4.5369`
- `market_context_high->fx_1h` score `-0.0824` n `113` status `ready` deltaP `3.2603` edge `0.0026` maxDD `-0.1258`
- `market_context_high->fx_4h` score `-0.112` n `113` status `ready` deltaP `6.3917` edge `0.0079` maxDD `-0.4545`
- `market_context_high->fx_24h` score `-0.2034` n `86` status `ready` deltaP `16.3881` edge `0.0219` maxDD `-1.2451`
- `market_context_high->commodity_1h` score `-0.4631` n `113` status `ready` deltaP `0.1166` edge `0.0107` maxDD `-1.0053`
- `market_context_high->metal_24h` score `-0.4966` n `86` status `ready` deltaP `13.7193` edge `0.1119` maxDD `-7.3625`
- `market_context_high->index_1h` score `-0.6518` n `113` status `ready` deltaP `-1.8865` edge `-0.0058` maxDD `-1.2155`
- `market_context_high->metal_1h` score `-0.6695` n `113` status `ready` deltaP `4.3347` edge `-0.0055` maxDD `-1.6682`
- `market_context_high->commodity_4h` score `-0.7149` n `113` status `ready` deltaP `-0.7137` edge `0.036` maxDD `-1.165`
- `market_context_high->index_24h` score `-0.8681` n `86` status `ready` deltaP `10.6711` edge `-0.0542` maxDD `-4.925`
- `market_context_high->crypto_major_1h` score `-1.2888` n `113` status `ready` deltaP `3.6961` edge `-0.0318` maxDD `-9.3126`
- `market_context_high->metal_4h` score `-2.029` n `113` status `ready` deltaP `3.3941` edge `-0.0207` maxDD `-5.3474`
- `market_context_high->index_4h` score `-2.1609` n `113` status `ready` deltaP `-7.92` edge `-0.0368` maxDD `-4.3282`
- `market_context_high->commodity_24h` score `-2.7966` n `86` status `ready` deltaP `-8.7128` edge `-0.0498` maxDD `-8.3852`
- `market_context_high->crypto_alt_1h` score `-3.1511` n `113` status `ready` deltaP `-1.4109` edge `-0.0658` maxDD `-11.3243`
- `market_context_high->equity_1h` score `-3.8523` n `113` status `ready` deltaP `-0.3895` edge `-0.0911` maxDD `-12.1865`
- `market_context_high->crypto_alt_24h` score `-7.2588` n `86` status `ready` deltaP `-4.9459` edge `-0.252` maxDD `-42.3182`
- `market_context_high->equity_24h` score `-7.5384` n `86` status `ready` deltaP `0.0162` edge `-0.4382` maxDD `-36.6024`
- `market_context_high->crypto_major_4h` score `-9.9874` n `113` status `ready` deltaP `-12.8952` edge `-0.2465` maxDD `-32.9851`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
