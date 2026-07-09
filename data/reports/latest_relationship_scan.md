# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-09T10:01:12.598730+00:00`
- Price records: `672`
- Market context records: `6171`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11132`

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

- `news_risk_high->crypto_alt_24h` score `12.5558` n `32` status `ready` deltaP `42.3848` edge `0.7785` maxDD `-0.5131`
- `news_risk_high->fx_24h` score `7.2498` n `32` status `ready` deltaP `63.6519` edge `0.1798` maxDD `0.0`
- `news_risk_high->fx_4h` score `4.0453` n `32` status `ready` deltaP `42.1356` edge `0.0608` maxDD `-0.0345`
- `news_risk_high->fx_1h` score `2.3098` n `32` status `ready` deltaP `27.8358` edge `0.0208` maxDD `-0.1113`
- `market_context_high->unknown_1h` score `1.6875` n `194` status `ready` deltaP `0.9202` edge `0.2353` maxDD `-3.7317`
- `news_risk_high->crypto_major_24h` score `1.5869` n `32` status `ready` deltaP `15.7956` edge `0.1761` maxDD `-4.2368`
- `news_risk_high->crypto_major_1h` score `1.2024` n `32` status `ready` deltaP `12.9384` edge `0.1146` maxDD `-2.0691`
- `news_risk_high->crypto_alt_1h` score `0.6145` n `32` status `ready` deltaP `8.181` edge `0.0704` maxDD `-1.6923`
- `market_context_high->unknown_4h` score `0.349` n `194` status `ready` deltaP `-1.2879` edge `0.2909` maxDD `-11.925`
- `market_context_high->metal_24h` score `0.1076` n `194` status `ready` deltaP `20.3916` edge `0.1347` maxDD `-11.8809`
- `news_risk_high->index_24h` score `-0.0783` n `32` status `ready` deltaP `9.663` edge `0.0127` maxDD `-2.3058`
- `market_context_high->equity_4h` score `-0.1845` n `194` status `ready` deltaP `2.392` edge `0.0604` maxDD `-2.671`
- `market_context_high->fx_1h` score `-0.3152` n `194` status `ready` deltaP `0.7739` edge `-0.001` maxDD `-0.5659`
- `news_risk_high->commodity_24h` score `-0.5441` n `32` status `ready` deltaP `13.2146` edge `-0.1129` maxDD `-0.3101`
- `market_context_high->metal_4h` score `-0.6885` n `194` status `ready` deltaP `3.3872` edge `0.0079` maxDD `-3.4996`
- `market_context_high->commodity_1h` score `-0.7047` n `194` status `ready` deltaP `-1.5741` edge `-0.0036` maxDD `-0.5708`
- `news_risk_high->metal_1h` score `-0.8106` n `32` status `ready` deltaP `-3.5821` edge `-0.0303` maxDD `-1.6464`
- `market_context_high->metal_1h` score `-0.9107` n `194` status `ready` deltaP `1.5725` edge `-0.0065` maxDD `-2.0564`
- `market_context_high->crypto_alt_1h` score `-0.9892` n `194` status `ready` deltaP `2.9297` edge `0.0289` maxDD `-9.3536`
- `market_context_high->equity_1h` score `-1.008` n `194` status `ready` deltaP `-2.7281` edge `0.0005` maxDD `-4.2573`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
