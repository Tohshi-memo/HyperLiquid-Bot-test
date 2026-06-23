# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-23T20:22:46.796048+00:00`
- Price records: `672`
- Market context records: `4551`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `10045`

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

- `market_context_high->unknown_1h` score `59.3247` n `164` status `ready` deltaP `6.4006` edge `4.9511` maxDD `-2.3371`
- `market_context_high->unknown_4h` score `2.1379` n `164` status `ready` deltaP `7.0122` edge `0.288` maxDD `-7.5275`
- `market_context_high->fx_4h` score `-0.4839` n `164` status `ready` deltaP `6.5549` edge `0.0025` maxDD `-1.9927`
- `market_context_high->commodity_1h` score `-0.6116` n `164` status `ready` deltaP `-0.6974` edge `0.0136` maxDD `-2.6555`
- `market_context_high->equity_4h` score `-0.7048` n `164` status `ready` deltaP `2.439` edge `0.0703` maxDD `-8.8203`
- `market_context_high->fx_1h` score `-0.7068` n `164` status `ready` deltaP `-0.0657` edge `-0.003` maxDD `-1.1038`
- `market_context_high->index_4h` score `-0.8185` n `164` status `ready` deltaP `2.2866` edge `-0.0079` maxDD `-5.9823`
- `market_context_high->index_1h` score `-0.9932` n `164` status `ready` deltaP `-2.3952` edge `-0.0105` maxDD `-2.7358`
- `market_context_high->equity_1h` score `-1.079` n `164` status `ready` deltaP `-2.2236` edge `0.0236` maxDD `-5.5624`
- `market_context_high->commodity_4h` score `-1.9156` n `164` status `ready` deltaP `3.0488` edge `0.0308` maxDD `-9.1941`
- `market_context_high->unknown_24h` score `-2.8571` n `162` status `ready` deltaP `2.392` edge `-0.1617` maxDD `-4.7201`
- `market_context_high->metal_1h` score `-4.498` n `164` status `ready` deltaP `-4.4509` edge `-0.08` maxDD `-17.8795`
- `market_context_high->fx_24h` score `-5.506` n `162` status `ready` deltaP `-13.831` edge `-0.0154` maxDD `-6.0982`
- `market_context_high->crypto_alt_1h` score `-5.5251` n `164` status `ready` deltaP `-3.465` edge `-0.1086` maxDD `-22.2982`
- `market_context_high->index_24h` score `-5.7221` n `162` status `ready` deltaP `-9.5872` edge `-0.1322` maxDD `-29.3321`
- `market_context_high->crypto_major_1h` score `-6.5379` n `164` status `ready` deltaP `-5.4659` edge `-0.1331` maxDD `-27.356`
- `market_context_high->commodity_24h` score `-7.0054` n `162` status `ready` deltaP `6.3464` edge `0.0324` maxDD `-40.0127`
- `market_context_high->crypto_alt_4h` score `-8.7097` n `164` status `ready` deltaP `-1.9818` edge `-0.2377` maxDD `-63.9243`
- `market_context_high->equity_24h` score `-13.4137` n `162` status `ready` deltaP `-1.1767` edge `-0.2439` maxDD `-102.1031`
- `market_context_high->metal_4h` score `-15.5707` n `164` status `ready` deltaP `-7.7743` edge `-0.324` maxDD `-67.4051`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
