# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-09T13:52:30.038689+00:00`
- Price records: `672`
- Market context records: `6186`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11110`

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

- `news_risk_high->crypto_alt_24h` score `12.6314` n `32` status `ready` deltaP `42.2194` edge `0.7859` maxDD `-0.5131`
- `news_risk_high->fx_24h` score `6.9836` n `32` status `ready` deltaP `61.2245` edge `0.1738` maxDD `0.0`
- `news_risk_high->fx_4h` score `4.0703` n `32` status `ready` deltaP `42.4487` edge `0.0608` maxDD `-0.0345`
- `news_risk_high->fx_1h` score `2.352` n `32` status `ready` deltaP `28.3632` edge `0.0208` maxDD `-0.1113`
- `news_risk_high->crypto_major_24h` score `2.0` n `32` status `ready` deltaP `15.625` edge `0.2302` maxDD `-4.2368`
- `market_context_high->unknown_1h` score `1.8404` n `192` status `ready` deltaP `1.0019` edge `0.2475` maxDD `-3.7317`
- `news_risk_high->crypto_major_1h` score `1.3479` n `32` status `ready` deltaP `13.906` edge `0.1268` maxDD `-2.0691`
- `news_risk_high->crypto_alt_1h` score `0.704` n `32` status `ready` deltaP `9.0013` edge `0.0764` maxDD `-1.6923`
- `market_context_high->unknown_4h` score `0.4241` n `192` status `ready` deltaP `-1.3694` edge `0.2977` maxDD `-11.925`
- `market_context_high->metal_24h` score `0.0575` n `192` status `ready` deltaP `19.8023` edge `0.1322` maxDD `-11.8809`
- `market_context_high->equity_4h` score `-0.1119` n `192` status `ready` deltaP `2.3841` edge `0.0665` maxDD `-2.671`
- `news_risk_high->commodity_24h` score `-0.1295` n `32` status `ready` deltaP `15.6675` edge `-0.0947` maxDD `-0.3101`
- `news_risk_high->index_24h` score `-0.1486` n `32` status `ready` deltaP `9.4813` edge `0.0049` maxDD `-2.3058`
- `market_context_high->fx_1h` score `-0.2881` n `192` status `ready` deltaP `1.2799` edge `-0.0009` maxDD `-0.5659`
- `market_context_high->metal_4h` score `-0.6589` n `192` status `ready` deltaP `3.5351` edge `0.0107` maxDD `-3.4996`
- `market_context_high->commodity_1h` score `-0.8012` n `192` status `ready` deltaP `-2.7653` edge `-0.0037` maxDD `-0.5708`
- `news_risk_high->metal_1h` score `-0.8506` n `32` status `ready` deltaP `-4.1106` edge `-0.0319` maxDD `-1.6464`
- `market_context_high->crypto_major_1h` score `-0.9518` n `192` status `ready` deltaP `4.0102` edge `0.028` maxDD `-9.807`
- `market_context_high->crypto_alt_1h` score `-0.9597` n `192` status `ready` deltaP `3.2721` edge `0.0304` maxDD `-9.3536`
- `market_context_high->metal_1h` score `-0.9678` n `192` status `ready` deltaP `1.0977` edge `-0.0081` maxDD `-2.0564`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
