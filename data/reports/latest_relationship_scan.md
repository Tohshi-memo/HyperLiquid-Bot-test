# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-04T09:52:30.788781+00:00`
- Price records: `672`
- Market context records: `5650`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `72`

- Symbol pattern count: `8684`

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

- `market_context_high->equity_24h` score `2.5414` n `182` status `ready` deltaP `14.652` edge `0.622` maxDD `-31.6316`
- `market_context_high->fx_24h` score `0.8995` n `182` status `ready` deltaP `19.5208` edge `0.0589` maxDD `-1.7932`
- `market_context_high->crypto_major_4h` score `0.7316` n `237` status `ready` deltaP `10.5472` edge `0.2199` maxDD `-14.0065`
- `market_context_high->equity_4h` score `0.4819` n `237` status `ready` deltaP `7.5338` edge `0.1538` maxDD `-7.4425`
- `market_context_high->crypto_alt_4h` score `-0.0713` n `237` status `ready` deltaP `6.2217` edge `0.1375` maxDD `-9.46`
- `market_context_high->fx_1h` score `-0.2632` n `242` status `ready` deltaP `1.9164` edge `0.0011` maxDD `-0.4764`
- `market_context_high->equity_1h` score `-0.3753` n `242` status `ready` deltaP `5.4325` edge `0.0332` maxDD `-5.0555`
- `market_context_high->metal_1h` score `-0.5586` n `242` status `ready` deltaP `-0.5988` edge `-0.0001` maxDD `-2.0682`
- `market_context_high->crypto_alt_1h` score `-0.662` n `242` status `ready` deltaP `1.2879` edge `0.0324` maxDD `-5.0257`
- `market_context_high->crypto_major_1h` score `-0.747` n `242` status `ready` deltaP `3.4196` edge `0.0395` maxDD `-6.9639`
- `market_context_high->index_1h` score `-0.9437` n `242` status `ready` deltaP `0.4194` edge `0.0054` maxDD `-0.9472`
- `market_context_high->commodity_1h` score `-0.9915` n `242` status `ready` deltaP `-0.1918` edge `-0.0048` maxDD `-3.7906`
- `market_context_high->fx_4h` score `-1.2765` n `237` status `ready` deltaP `1.9804` edge `0.0065` maxDD `-1.335`
- `market_context_high->index_4h` score `-2.0233` n `237` status `ready` deltaP `-1.5366` edge `0.0088` maxDD `-3.04`
- `market_context_high->index_24h` score `-2.3227` n `182` status `ready` deltaP `9.8844` edge `0.035` maxDD `-16.8946`
- `market_context_high->metal_4h` score `-3.0607` n `237` status `ready` deltaP `-14.8265` edge `-0.0552` maxDD `-11.7351`
- `market_context_high->commodity_4h` score `-3.8009` n `237` status `ready` deltaP `-2.1875` edge `-0.0346` maxDD `-14.071`
- `market_context_high->crypto_major_24h` score `-4.4811` n `182` status `ready` deltaP `4.1247` edge `0.0531` maxDD `-29.6555`
- `market_context_high->metal_24h` score `-8.3704` n `182` status `ready` deltaP `-12.7251` edge `-0.2522` maxDD `-32.8874`
- `market_context_high->commodity_24h` score `-12.9536` n `182` status `ready` deltaP `-16.1058` edge `-0.1112` maxDD `-45.8715`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
