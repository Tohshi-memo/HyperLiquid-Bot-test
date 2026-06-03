# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-03T04:37:21.088895+00:00`
- Price records: `672`
- Market context records: `2730`
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

- `market_context_high->crypto_alt_24h` score `11.4379` n `111` status `ready` deltaP `16.3523` edge `1.1935` maxDD `-19.9486`
- `market_context_high->unknown_24h` score `8.6448` n `111` status `ready` deltaP `17.4784` edge `0.6367` maxDD `-1.6255`
- `market_context_high->crypto_major_24h` score `1.3164` n `111` status `ready` deltaP `6.5175` edge `0.8816` maxDD `-44.169`
- `market_context_high->unknown_4h` score `1.1902` n `143` status `ready` deltaP `7.7734` edge `0.1527` maxDD `-3.7602`
- `market_context_high->index_4h` score `0.0396` n `143` status `ready` deltaP `9.4843` edge `0.026` maxDD `-2.3986`
- `market_context_high->unknown_1h` score `-0.1711` n `143` status `ready` deltaP `2.7491` edge `0.0405` maxDD `-3.1801`
- `market_context_high->index_1h` score `-0.1853` n `143` status `ready` deltaP `2.7512` edge `0.0073` maxDD `-1.2855`
- `market_context_high->crypto_alt_4h` score `-0.3665` n `143` status `ready` deltaP `16.8206` edge `0.2914` maxDD `-28.7261`
- `market_context_high->fx_1h` score `-0.5326` n `143` status `ready` deltaP `-0.4972` edge `0.0033` maxDD `-0.2164`
- `market_context_high->commodity_1h` score `-0.5358` n `143` status `ready` deltaP `0.9506` edge `0.0003` maxDD `-4.3601`
- `market_context_high->crypto_alt_1h` score `-0.5424` n `143` status `ready` deltaP `6.1451` edge `0.0655` maxDD `-10.747`
- `market_context_high->metal_1h` score `-0.7559` n `143` status `ready` deltaP `-1.3997` edge `-0.003` maxDD `-3.0996`
- `market_context_high->crypto_major_1h` score `-0.9112` n `143` status `ready` deltaP `3.6473` edge `0.0458` maxDD `-9.622`
- `market_context_high->fx_4h` score `-1.0177` n `143` status `ready` deltaP `-2.421` edge `0.0092` maxDD `-0.5631`
- `market_context_high->fx_24h` score `-1.0687` n `111` status `ready` deltaP `1.4452` edge `-0.0115` maxDD `-0.6418`
- `market_context_high->equity_1h` score `-1.2807` n `143` status `ready` deltaP `-4.6846` edge `0.0078` maxDD `-2.6634`
- `market_context_high->commodity_4h` score `-1.3692` n `143` status `ready` deltaP `1.3613` edge `0.0074` maxDD `-10.0279`
- `market_context_high->commodity_24h` score `-1.6308` n `111` status `ready` deltaP `2.5807` edge `0.0831` maxDD `-12.4171`
- `market_context_high->equity_4h` score `-2.0963` n `143` status `ready` deltaP `-1.2493` edge `-0.0284` maxDD `-5.7037`
- `market_context_high->crypto_major_4h` score `-2.2657` n `143` status `ready` deltaP `6.7521` edge `0.1551` maxDD `-32.2466`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
