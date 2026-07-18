# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-18T16:15:02.318025+00:00`
- Price records: `672`
- Market context records: `7157`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11762`

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

- `market_context_high->fx_4h` score `0.2483` n `156` status `ready` deltaP `11.6831` edge `0.0128` maxDD `-0.9333`
- `market_context_high->fx_1h` score `-0.2882` n `165` status `ready` deltaP `3.0267` edge `0.0019` maxDD `-0.3545`
- `market_context_high->unknown_1h` score `-0.568` n `165` status `ready` deltaP `-1.7157` edge `0.0283` maxDD `-1.4688`
- `market_context_high->crypto_alt_1h` score `-0.6587` n `165` status `ready` deltaP `-0.7739` edge `0.0246` maxDD `-5.9775`
- `market_context_high->crypto_major_1h` score `-0.6589` n `165` status `ready` deltaP `3.3261` edge `0.0344` maxDD `-7.6171`
- `market_context_high->commodity_1h` score `-0.7043` n `165` status `ready` deltaP `-1.771` edge `-0.0164` maxDD `-1.9668`
- `market_context_high->index_1h` score `-0.7213` n `165` status `ready` deltaP `1.5995` edge `-0.0043` maxDD `-2.3175`
- `market_context_high->metal_1h` score `-1.788` n `165` status `ready` deltaP `-7.0423` edge `-0.0051` maxDD `-2.0897`
- `market_context_high->unknown_4h` score `-1.9788` n `156` status `ready` deltaP `-6.1523` edge `0.0133` maxDD `-6.0783`
- `market_context_high->commodity_4h` score `-2.1101` n `156` status `ready` deltaP `-5.1165` edge `-0.0382` maxDD `-2.9494`
- `market_context_high->metal_4h` score `-2.9428` n `156` status `ready` deltaP `-10.5495` edge `-0.0121` maxDD `-5.2551`
- `market_context_high->equity_1h` score `-3.5968` n `165` status `ready` deltaP `-1.1387` edge `-0.0405` maxDD `-15.4645`
- `market_context_high->index_4h` score `-3.9546` n `156` status `ready` deltaP `-2.482` edge `-0.0431` maxDD `-12.2591`
- `market_context_high->commodity_24h` score `-4.5` n `133` status `ready` deltaP `-13.4581` edge `-0.1544` maxDD `-4.4704`
- `market_context_high->fx_24h` score `-4.897` n `133` status `ready` deltaP `-15.0102` edge `-0.0253` maxDD `-3.9503`
- `market_context_high->crypto_major_4h` score `-4.9394` n `156` status `ready` deltaP `2.3139` edge `0.0083` maxDD `-25.1605`
- `market_context_high->crypto_alt_4h` score `-5.5902` n `156` status `ready` deltaP `-3.6742` edge `-0.0317` maxDD `-24.7723`
- `market_context_high->unknown_24h` score `-10.098` n `133` status `ready` deltaP `-32.7029` edge `-0.1088` maxDD `-23.5076`
- `market_context_high->metal_24h` score `-14.7538` n `133` status `ready` deltaP `-32.1232` edge `-0.1972` maxDD `-40.7836`
- `market_context_high->equity_4h` score `-14.7866` n `156` status `ready` deltaP `-4.3777` edge `-0.2176` maxDD `-66.5013`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
