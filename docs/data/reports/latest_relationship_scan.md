# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-29T12:37:33.969085+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `7072`

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

- `market_context_high->unknown_24h` score `1318.9942` n `146` status `ready` deltaP `-2.3664` edge `110.0247` maxDD `-4.7527`
- `market_context_high->unknown_4h` score `38.6178` n `146` status `ready` deltaP `5.2707` edge `3.1963` maxDD `-0.3966`
- `market_context_high->index_24h` score `0.9589` n `146` status `ready` deltaP `19.6442` edge `-0.0025` maxDD `-1.551`
- `market_context_high->fx_1h` score `0.0523` n `146` status `ready` deltaP `5.9511` edge `0.0005` maxDD `-0.1986`
- `market_context_high->commodity_4h` score `0.0389` n `146` status `ready` deltaP `11.6438` edge `0.0475` maxDD `-1.0837`
- `market_context_high->metal_1h` score `-0.1647` n `146` status `ready` deltaP `7.2533` edge `0.0052` maxDD `-1.3073`
- `market_context_high->fx_4h` score `-0.2252` n `146` status `ready` deltaP `5.8616` edge `0.002` maxDD `-0.4545`
- `market_context_high->commodity_1h` score `-0.5365` n `146` status `ready` deltaP `0.7485` edge `0.0087` maxDD `-1.0053`
- `market_context_high->metal_4h` score `-0.6031` n `146` status `ready` deltaP `8.9125` edge `0.0002` maxDD `-4.2878`
- `market_context_high->index_1h` score `-0.7715` n `146` status `ready` deltaP `-3.9783` edge `-0.0041` maxDD `-1.4631`
- `market_context_high->crypto_major_1h` score `-0.8167` n `146` status `ready` deltaP `4.8807` edge `0.0277` maxDD `-6.9306`
- `market_context_high->fx_24h` score `-1.2412` n `146` status `ready` deltaP `4.4473` edge `0.0095` maxDD `-1.0732`
- `market_context_high->equity_1h` score `-1.4001` n `146` status `ready` deltaP `0.2994` edge `0.0025` maxDD `-8.7199`
- `market_context_high->crypto_alt_1h` score `-1.631` n `146` status `ready` deltaP `1.7513` edge `0.01` maxDD `-11.7957`
- `market_context_high->index_4h` score `-3.0687` n `146` status `ready` deltaP `-10.3617` edge `-0.0325` maxDD `-5.3315`
- `market_context_high->crypto_major_4h` score `-3.5141` n `146` status `ready` deltaP `1.9734` edge `-0.0353` maxDD `-26.937`
- `market_context_high->metal_24h` score `-3.6686` n `146` status `ready` deltaP `0.3068` edge `-0.0139` maxDD `-10.5088`
- `market_context_high->crypto_major_24h` score `-3.7126` n `146` status `ready` deltaP `-2.7682` edge `0.0282` maxDD `-29.1905`
- `market_context_high->commodity_24h` score `-4.6698` n `146` status `ready` deltaP `0.1832` edge `-0.0409` maxDD `-24.0547`
- `market_context_high->equity_4h` score `-4.7916` n `146` status `ready` deltaP `-4.4938` edge `-0.1336` maxDD `-29.3937`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
