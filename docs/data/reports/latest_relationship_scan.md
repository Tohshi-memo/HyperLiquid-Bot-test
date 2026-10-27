# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-27T04:37:32.998730+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9688`

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

- `market_context_high->unknown_4h` score `82.8062` n `149` status `ready` deltaP `2.126` edge `6.9199` maxDD `-1.0178`
- `market_context_high->unknown_1h` score `12.2734` n `149` status `ready` deltaP `1.0359` edge `1.0648` maxDD `-1.5807`
- `market_context_high->fx_4h` score `0.3744` n `149` status `ready` deltaP `12.232` edge `0.0095` maxDD `-0.4545`
- `market_context_high->fx_1h` score `0.3005` n `149` status `ready` deltaP `8.6937` edge `0.0029` maxDD `-0.1986`
- `market_context_high->index_24h` score `0.2755` n `122` status `ready` deltaP `18.9718` edge `0.0184` maxDD `-3.4316`
- `market_context_high->metal_24h` score `0.1306` n `122` status `ready` deltaP `21.0898` edge `0.1287` maxDD `-6.204`
- `market_context_high->metal_1h` score `-0.0188` n `149` status `ready` deltaP `9.6019` edge `0.0084` maxDD `-1.3188`
- `market_context_high->commodity_1h` score `-0.0913` n `149` status `ready` deltaP `3.7586` edge `0.0174` maxDD `-1.0053`
- `market_context_high->fx_24h` score `-0.1394` n `122` status `ready` deltaP `17.0938` edge `0.0254` maxDD `-1.2451`
- `market_context_high->commodity_4h` score `-0.3252` n `149` status `ready` deltaP `7.049` edge `0.0488` maxDD `-1.165`
- `market_context_high->index_1h` score `-0.5875` n `149` status `ready` deltaP `-0.0312` edge `-0.0014` maxDD `-1.8971`
- `market_context_high->crypto_major_1h` score `-0.6601` n `149` status `ready` deltaP `5.0436` edge `0.0216` maxDD `-7.8544`
- `market_context_high->metal_4h` score `-0.8037` n `149` status `ready` deltaP `9.1156` edge `0.0004` maxDD `-4.8031`
- `market_context_high->equity_1h` score `-1.7107` n `149` status `ready` deltaP `1.8426` edge `-0.004` maxDD `-12.2088`
- `market_context_high->crypto_alt_1h` score `-1.9087` n `149` status `ready` deltaP `-0.0111` edge `-0.0002` maxDD `-12.8878`
- `market_context_high->index_4h` score `-3.4546` n `149` status `ready` deltaP `-6.6214` edge `-0.0268` maxDD `-6.6889`
- `market_context_high->crypto_major_24h` score `-3.9125` n `122` status `ready` deltaP `1.4121` edge `-0.0253` maxDD `-29.1905`
- `market_context_high->crypto_major_4h` score `-4.3268` n `149` status `ready` deltaP `0.0604` edge `-0.0803` maxDD `-30.6525`
- `market_context_high->equity_24h` score `-4.3405` n `122` status `ready` deltaP `-2.7801` edge `-0.1132` maxDD `-25.9791`
- `market_context_high->equity_4h` score `-6.7314` n `149` status `ready` deltaP `-0.6742` edge `-0.1647` maxDD `-44.1713`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
