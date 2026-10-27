# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-27T15:22:50.134125+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8502`

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

- `market_context_high->unknown_4h` score `80.665` n `135` status `ready` deltaP `4.5472` edge `6.707` maxDD `-0.5521`
- `market_context_high->unknown_1h` score `14.8368` n `135` status `ready` deltaP `0.9193` edge `1.2792` maxDD `-1.5807`
- `market_context_high->index_24h` score `2.0059` n `135` status `ready` deltaP `27.1875` edge `0.0547` maxDD `-2.17`
- `market_context_high->fx_1h` score `0.4943` n `135` status `ready` deltaP `11.0557` edge `0.0033` maxDD `-0.1986`
- `market_context_high->fx_4h` score `0.3434` n `135` status `ready` deltaP `11.8293` edge `0.0096` maxDD `-0.4545`
- `market_context_high->metal_1h` score `-0.0436` n `135` status `ready` deltaP `9.1484` edge `0.0081` maxDD `-1.3073`
- `market_context_high->commodity_1h` score `-0.2255` n `135` status `ready` deltaP `2.8765` edge `0.0121` maxDD `-1.0053`
- `market_context_high->commodity_4h` score `-0.5018` n `135` status `ready` deltaP `5.4697` edge `0.0436` maxDD `-1.0837`
- `market_context_high->crypto_major_1h` score `-0.5285` n `135` status `ready` deltaP `5.4369` edge `0.0243` maxDD `-6.9306`
- `market_context_high->index_1h` score `-0.5944` n `135` status `ready` deltaP `-0.662` edge `-0.0035` maxDD `-1.4631`
- `market_context_high->fx_24h` score `-0.6418` n `135` status `ready` deltaP `8.4375` edge `0.0187` maxDD `-1.2451`
- `market_context_high->metal_4h` score `-0.8148` n `135` status `ready` deltaP `8.0137` edge `-0.0038` maxDD `-4.6603`
- `market_context_high->metal_24h` score `-0.9513` n `135` status `ready` deltaP `16.0995` edge `0.0912` maxDD `-8.2244`
- `market_context_high->equity_1h` score `-1.4963` n `135` status `ready` deltaP `1.5912` edge `-0.0112` maxDD `-9.2993`
- `market_context_high->equity_24h` score `-1.9554` n `135` status `ready` deltaP `8.0671` edge `0.0797` maxDD `-15.7143`
- `market_context_high->crypto_alt_1h` score `-1.9857` n `135` status `ready` deltaP `-1.3407` edge `-0.0093` maxDD `-12.2409`
- `market_context_high->index_4h` score `-2.7727` n `135` status `ready` deltaP `-5.8605` edge `-0.0298` maxDD `-5.6417`
- `market_context_high->crypto_major_4h` score `-3.7689` n `135` status `ready` deltaP `3.2024` edge `-0.0726` maxDD `-27.2215`
- `market_context_high->crypto_major_24h` score `-4.0083` n `135` status `ready` deltaP `0.544` edge `-0.0318` maxDD `-29.1905`
- `market_context_high->equity_4h` score `-5.2264` n `135` status `ready` deltaP `1.023` edge `-0.1535` maxDD `-35.2032`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
