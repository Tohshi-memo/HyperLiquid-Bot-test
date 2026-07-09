# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-09T20:37:30.152656+00:00`
- Price records: `672`
- Market context records: `6216`
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

- `news_risk_high->crypto_alt_24h` score `13.1258` n `32` status `ready` deltaP `42.2194` edge `0.8271` maxDD `-0.5131`
- `news_risk_high->fx_24h` score `6.5466` n `32` status `ready` deltaP `56.6327` edge `0.168` maxDD `0.0`
- `news_risk_high->fx_4h` score `4.099` n `32` status `ready` deltaP `42.9116` edge `0.0601` maxDD `-0.0345`
- `news_risk_high->crypto_major_24h` score `2.4399` n `32` status `ready` deltaP `15.625` edge `0.2866` maxDD `-4.2368`
- `news_risk_high->fx_1h` score `2.3212` n `32` status `ready` deltaP `27.994` edge `0.0207` maxDD `-0.1113`
- `market_context_high->unknown_1h` score `1.8597` n `192` status `ready` deltaP `1.5126` edge `0.2457` maxDD `-3.7317`
- `news_risk_high->crypto_major_1h` score `1.4054` n `32` status `ready` deltaP `14.4274` edge `0.1307` maxDD `-2.0691`
- `news_risk_high->commodity_24h` score `1.0826` n `32` status `ready` deltaP `20.2594` edge `-0.0243` maxDD `-0.3101`
- `news_risk_high->crypto_alt_1h` score `0.7631` n `32` status `ready` deltaP `10.1235` edge `0.0765` maxDD `-1.6923`
- `market_context_high->unknown_4h` score `0.3957` n `192` status `ready` deltaP `-1.9944` edge `0.2995` maxDD `-11.925`
- `market_context_high->metal_24h` score `-0.0447` n `192` status `ready` deltaP `19.8023` edge `0.1191` maxDD `-11.8809`
- `news_risk_high->index_24h` score `-0.2424` n `32` status `ready` deltaP `8.801` edge `-0.0026` maxDD `-2.3058`
- `market_context_high->fx_1h` score `-0.3081` n `192` status `ready` deltaP `0.9107` edge `-0.001` maxDD `-0.5659`
- `market_context_high->commodity_1h` score `-0.5703` n `192` status `ready` deltaP `-0.7485` edge `0.0021` maxDD `-0.5708`
- `market_context_high->metal_4h` score `-0.7088` n `192` status `ready` deltaP `2.7566` edge `0.0095` maxDD `-3.4996`
- `news_risk_high->metal_1h` score `-0.7839` n `32` status `ready` deltaP `-3.4431` edge `-0.0278` maxDD `-1.6464`
- `market_context_high->metal_1h` score `-0.8652` n `192` status `ready` deltaP `1.7652` edge `-0.004` maxDD `-2.0564`
- `market_context_high->crypto_major_1h` score `-0.8942` n `192` status `ready` deltaP `4.5316` edge `0.0319` maxDD `-9.807`
- `market_context_high->crypto_alt_1h` score `-0.9006` n `192` status `ready` deltaP `4.3943` edge `0.0305` maxDD `-9.3536`
- `market_context_high->equity_1h` score `-1.1204` n `192` status `ready` deltaP `-2.863` edge `-0.013` maxDD `-4.2573`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
