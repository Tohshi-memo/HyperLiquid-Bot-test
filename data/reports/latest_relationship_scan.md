# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-03T02:37:20.735288+00:00`
- Price records: `672`
- Market context records: `2722`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9250`

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

- `market_context_high->crypto_alt_24h` score `11.1679` n `111` status `ready` deltaP `16.3523` edge `1.171` maxDD `-19.9486`
- `market_context_high->unknown_24h` score `8.7163` n `111` status `ready` deltaP `17.652` edge `0.6415` maxDD `-1.6255`
- `market_context_high->unknown_4h` score `0.9487` n `143` status `ready` deltaP `6.5539` edge `0.1407` maxDD `-3.7602`
- `market_context_high->crypto_major_24h` score `0.8937` n `111` status `ready` deltaP `6.5175` edge `0.8274` maxDD `-44.169`
- `market_context_high->index_4h` score `0.1483` n `143` status `ready` deltaP `10.7038` edge `0.0318` maxDD `-2.3986`
- `market_context_high->index_1h` score `-0.1371` n `143` status `ready` deltaP `3.4997` edge `0.0085` maxDD `-1.2855`
- `market_context_high->unknown_1h` score `-0.1867` n `143` status `ready` deltaP `2.7491` edge `0.0392` maxDD `-3.1801`
- `market_context_high->crypto_alt_4h` score `-0.3959` n `143` status `ready` deltaP `16.3633` edge `0.292` maxDD `-28.7261`
- `market_context_high->fx_1h` score `-0.4692` n `143` status `ready` deltaP `0.2513` edge `0.0036` maxDD `-0.2164`
- `market_context_high->commodity_1h` score `-0.5039` n `143` status `ready` deltaP `1.3997` edge `0.0014` maxDD `-4.3601`
- `market_context_high->crypto_alt_1h` score `-0.533` n `143` status `ready` deltaP `6.2948` edge `0.0657` maxDD `-10.747`
- `market_context_high->metal_1h` score `-0.7278` n `143` status `ready` deltaP `-1.1003` edge `-0.0014` maxDD `-3.0996`
- `market_context_high->crypto_major_1h` score `-0.9245` n `143` status `ready` deltaP `3.6473` edge `0.0441` maxDD `-9.622`
- `market_context_high->fx_24h` score `-0.9407` n `111` status `ready` deltaP `2.8341` edge `-0.0101` maxDD `-0.6418`
- `market_context_high->fx_4h` score `-1.0019` n `143` status `ready` deltaP `-2.2685` edge `0.0095` maxDD `-0.5631`
- `market_context_high->equity_1h` score `-1.1632` n `143` status `ready` deltaP `-3.6367` edge `0.0106` maxDD `-2.6634`
- `market_context_high->commodity_4h` score `-1.3055` n `143` status `ready` deltaP `1.9711` edge `0.0115` maxDD `-10.0279`
- `market_context_high->commodity_24h` score `-1.505` n `111` status `ready` deltaP `3.2752` edge `0.0946` maxDD `-12.4171`
- `market_context_high->equity_4h` score `-1.9981` n `143` status `ready` deltaP `-0.4871` edge `-0.0253` maxDD `-5.7037`
- `market_context_high->index_24h` score `-2.1325` n `111` status `ready` deltaP `-0.8446` edge `-0.074` maxDD `-2.5127`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
