# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-11T09:37:24.204484+00:00`
- Price records: `672`
- Market context records: `6378`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11072`

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

- `news_risk_high->crypto_alt_24h` score `14.2407` n `32` status `ready` deltaP `38.0208` edge `0.948` maxDD `-0.5131`
- `news_risk_high->fx_24h` score `6.3383` n `32` status `ready` deltaP `52.6042` edge `0.1775` maxDD `0.0`
- `news_risk_high->crypto_major_24h` score `4.2934` n `32` status `ready` deltaP `17.5347` edge `0.5115` maxDD `-4.2368`
- `news_risk_high->commodity_24h` score `4.158` n `32` status `ready` deltaP `36.1111` edge `0.1263` maxDD `-0.3101`
- `news_risk_high->fx_4h` score `3.923` n `32` status `ready` deltaP `40.4726` edge `0.0617` maxDD `-0.0345`
- `news_risk_high->fx_1h` score `2.3859` n `32` status `ready` deltaP `28.7425` edge `0.0211` maxDD `-0.1113`
- `news_risk_high->crypto_major_1h` score `1.4842` n `32` status `ready` deltaP `14.2777` edge `0.1418` maxDD `-2.0691`
- `news_risk_high->crypto_alt_1h` score `0.8676` n `32` status `ready` deltaP `10.872` edge `0.0849` maxDD `-1.6923`
- `market_context_high->metal_4h` score `0.463` n `220` status `ready` deltaP `14.6563` edge `0.0413` maxDD `-2.7056`
- `market_context_high->unknown_1h` score `0.2564` n `224` status `ready` deltaP `-5.6726` edge `0.16` maxDD `-3.7317`
- `market_context_high->index_4h` score `0.1934` n `220` status `ready` deltaP `9.3376` edge `0.0215` maxDD `-0.4108`
- `news_risk_high->unknown_1h` score `-0.2944` n `32` status `ready` deltaP `6.381` edge `-0.0326` maxDD `-0.7581`
- `market_context_high->metal_24h` score `-0.3371` n `142` status `ready` deltaP `18.5593` edge `0.0899` maxDD `-11.8809`
- `market_context_high->metal_1h` score `-0.392` n `224` status `ready` deltaP `3.7051` edge `0.0028` maxDD `-1.8877`
- `market_context_high->index_1h` score `-0.6397` n `224` status `ready` deltaP `-1.9434` edge `0.0029` maxDD `-0.7564`
- `market_context_high->fx_1h` score `-0.7152` n `224` status `ready` deltaP `-0.7218` edge `-0.0014` maxDD `-0.9376`
- `news_risk_high->metal_1h` score `-0.7169` n `32` status `ready` deltaP `-2.5449` edge `-0.0252` maxDD `-1.6464`
- `news_risk_high->index_24h` score `-0.7307` n `32` status `ready` deltaP `0.5208` edge `-0.01` maxDD `-2.3058`
- `market_context_high->commodity_24h` score `-0.7611` n `142` status `ready` deltaP `-5.3062` edge `0.1242` maxDD `-6.2457`
- `market_context_high->equity_4h` score `-0.8416` n `220` status `ready` deltaP `7.403` edge `0.0504` maxDD `-8.2573`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
