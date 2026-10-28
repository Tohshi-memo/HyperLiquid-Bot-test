# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-28T02:52:25.273275+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8807`

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

- `market_context_high->unknown_24h` score `949.8046` n `135` status `ready` deltaP `-3.7616` edge `79.2682` maxDD `-4.7527`
- `market_context_high->unknown_4h` score `44.3242` n `148` status `ready` deltaP `5.0882` edge `3.675` maxDD `-0.5521`
- `market_context_high->index_24h` score `1.9327` n `135` status `ready` deltaP `27.1875` edge `0.0486` maxDD `-2.17`
- `market_context_high->fx_1h` score `0.2762` n `148` status `ready` deltaP `8.4803` edge `0.0023` maxDD `-0.1986`
- `market_context_high->fx_4h` score `0.0834` n `148` status `ready` deltaP `8.7591` edge `0.0084` maxDD `-0.4545`
- `market_context_high->metal_1h` score `-0.1465` n `148` status `ready` deltaP `7.4243` edge `0.0064` maxDD `-1.3073`
- `market_context_high->commodity_4h` score `-0.3325` n `148` status `ready` deltaP `7.3912` edge `0.0449` maxDD `-1.0837`
- `market_context_high->fx_24h` score `-0.372` n `135` status `ready` deltaP `12.9514` edge `0.0232` maxDD `-1.2451`
- `market_context_high->crypto_major_1h` score `-0.4554` n `148` status `ready` deltaP `6.603` edge `0.0259` maxDD `-6.9306`
- `market_context_high->commodity_1h` score `-0.5711` n `148` status `ready` deltaP `0.2266` edge `0.0093` maxDD `-1.0053`
- `market_context_high->index_1h` score `-0.7487` n `148` status `ready` deltaP `-3.3743` edge `-0.0052` maxDD `-1.4631`
- `market_context_high->metal_4h` score `-0.7992` n `148` status `ready` deltaP `8.3429` edge `-0.004` maxDD `-4.6603`
- `market_context_high->equity_24h` score `-1.0842` n `135` status `ready` deltaP `8.0671` edge `0.1523` maxDD `-15.7143`
- `market_context_high->equity_1h` score `-1.6097` n `148` status `ready` deltaP `-0.0041` edge `-0.0151` maxDD `-9.2993`
- `market_context_high->metal_24h` score `-1.6748` n `135` status `ready` deltaP `10.3704` edge `0.0691` maxDD `-8.2244`
- `market_context_high->crypto_alt_1h` score `-1.7904` n `148` status `ready` deltaP `1.5617` edge `-0.0036` maxDD `-12.2409`
- `market_context_high->index_4h` score `-3.042` n `148` status `ready` deltaP `-8.6273` edge `-0.0338` maxDD `-5.6417`
- `market_context_high->crypto_major_24h` score `-3.421` n `135` status `ready` deltaP `0.544` edge `0.0435` maxDD `-29.1905`
- `market_context_high->crypto_major_4h` score `-3.6576` n `148` status `ready` deltaP `3.2713` edge `-0.0588` maxDD `-27.2215`
- `market_context_high->equity_4h` score `-5.7277` n `148` status `ready` deltaP `-3.9222` edge `-0.1848` maxDD `-35.2032`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
