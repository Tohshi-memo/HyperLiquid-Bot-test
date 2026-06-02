# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-02T21:07:25.884481+00:00`
- Price records: `672`
- Market context records: `2699`
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

- `market_context_high->crypto_alt_24h` score `10.2223` n `111` status `ready` deltaP `16.3523` edge `1.0922` maxDD `-19.9486`
- `market_context_high->unknown_24h` score `8.6743` n `111` status `ready` deltaP `17.652` edge `0.638` maxDD `-1.626`
- `market_context_high->unknown_4h` score `0.8012` n `142` status `ready` deltaP `5.4814` edge `0.1352` maxDD `-3.7312`
- `market_context_high->index_4h` score `0.2359` n `142` status `ready` deltaP `11.8345` edge `0.0355` maxDD `-2.3986`
- `market_context_high->index_1h` score `-0.1511` n `143` status `ready` deltaP `3.2003` edge `0.0087` maxDD `-1.2855`
- `market_context_high->unknown_1h` score `-0.1727` n `143` status `ready` deltaP `2.7491` edge `0.0401` maxDD `-3.1587`
- `market_context_high->crypto_major_24h` score `-0.3958` n `111` status `ready` deltaP `6.1703` edge `0.6644` maxDD `-44.169`
- `market_context_high->commodity_1h` score `-0.4065` n `143` status `ready` deltaP `2.2979` edge `0.0079` maxDD `-4.3601`
- `market_context_high->fx_1h` score `-0.4668` n `143` status `ready` deltaP `0.2513` edge `0.0038` maxDD `-0.2164`
- `market_context_high->crypto_alt_1h` score `-0.5393` n `143` status `ready` deltaP `6.2948` edge `0.0649` maxDD `-10.747`
- `market_context_high->crypto_alt_4h` score `-0.5552` n `142` status `ready` deltaP `16.1671` edge `0.2787` maxDD `-28.6198`
- `market_context_high->fx_24h` score `-0.5716` n `111` status `ready` deltaP `6.6536` edge `-0.0048` maxDD `-0.6418`
- `market_context_high->metal_1h` score `-0.7621` n `143` status `ready` deltaP `-1.5494` edge `-0.0028` maxDD `-3.0996`
- `market_context_high->fx_4h` score `-0.8136` n `142` status `ready` deltaP `-0.7042` edge `0.0106` maxDD `-0.5631`
- `market_context_high->commodity_24h` score `-0.8783` n `111` status `ready` deltaP `6.7474` edge `0.1518` maxDD `-12.4171`
- `market_context_high->crypto_major_1h` score `-0.9986` n `143` status `ready` deltaP `3.3479` edge `0.0366` maxDD `-9.622`
- `market_context_high->commodity_4h` score `-1.0225` n `142` status `ready` deltaP `4.4293` edge `0.0314` maxDD `-10.0279`
- `market_context_high->index_24h` score `-1.0649` n `111` status `ready` deltaP `2.9749` edge `-0.0105` maxDD `-2.5127`
- `market_context_high->equity_1h` score `-1.2451` n `143` status `ready` deltaP `-4.4857` edge `0.01` maxDD `-2.7085`
- `market_context_high->equity_4h` score `-2.0142` n `142` status `ready` deltaP `-1.2753` edge `-0.0189` maxDD `-5.9024`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
