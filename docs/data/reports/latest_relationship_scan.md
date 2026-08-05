# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-05T07:31:29.966422+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11632`

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

- `market_context_high->unknown_24h` score `14.6418` n `88` status `ready` deltaP `12.2317` edge `1.1429` maxDD `-0.0103`
- `market_context_high->unknown_4h` score `5.6089` n `90` status `ready` deltaP `1.7479` edge `0.5553` maxDD `-3.6303`
- `market_context_high->commodity_4h` score `1.5884` n `90` status `ready` deltaP `17.3849` edge `0.1011` maxDD `-2.7703`
- `market_context_high->fx_24h` score `1.177` n `88` status `ready` deltaP `27.7304` edge `0.0866` maxDD `-4.3126`
- `market_context_high->metal_24h` score `1.0284` n `88` status `ready` deltaP `1.7519` edge `0.237` maxDD `-2.6802`
- `market_context_high->commodity_1h` score `0.2739` n `92` status `ready` deltaP `5.7342` edge `0.0262` maxDD `-1.3282`
- `market_context_high->fx_4h` score `0.0727` n `90` status `ready` deltaP `13.1572` edge `0.0076` maxDD `-1.8797`
- `market_context_high->fx_1h` score `0.0005` n `92` status `ready` deltaP `5.8514` edge `-0.004` maxDD `-0.7973`
- `market_context_high->metal_1h` score `-0.4742` n `92` status `ready` deltaP `-0.5923` edge `-0.0074` maxDD `-1.6224`
- `market_context_high->index_1h` score `-0.6167` n `92` status `ready` deltaP `-0.9242` edge `-0.0195` maxDD `-1.6054`
- `market_context_high->crypto_alt_1h` score `-0.8523` n `92` status `ready` deltaP `-3.1828` edge `-0.017` maxDD `-3.0178`
- `market_context_high->metal_4h` score `-0.86` n `90` status `ready` deltaP `2.1172` edge `-0.0009` maxDD `-3.211`
- `market_context_high->crypto_alt_24h` score `-1.1298` n `88` status `ready` deltaP `3.2197` edge `-0.022` maxDD `-4.5445`
- `market_context_high->crypto_alt_4h` score `-1.3657` n `90` status `ready` deltaP `1.1992` edge `-0.0441` maxDD `-5.7857`
- `market_context_high->equity_1h` score `-1.8141` n `92` status `ready` deltaP `3.0136` edge `-0.0991` maxDD `-10.619`
- `market_context_high->index_24h` score `-2.1033` n `88` status `ready` deltaP `-8.065` edge `0.0036` maxDD `-7.8922`
- `market_context_high->index_4h` score `-2.1052` n `90` status `ready` deltaP `-12.8929` edge `-0.0585` maxDD `-4.7021`
- `market_context_high->unknown_1h` score `-3.2763` n `92` status `ready` deltaP `3.0396` edge `-0.2486` maxDD `-1.2421`
- `market_context_high->crypto_major_1h` score `-3.3132` n `92` status `ready` deltaP `-10.7199` edge `-0.0673` maxDD `-7.6533`
- `market_context_high->commodity_24h` score `-6.3581` n `88` status `ready` deltaP `8.2228` edge `-0.0738` maxDD `-49.6923`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
