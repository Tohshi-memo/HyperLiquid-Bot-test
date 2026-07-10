# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-10T01:14:47.086805+00:00`
- Price records: `672`
- Market context records: `6235`
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

- `news_risk_high->crypto_alt_24h` score `13.8446` n `32` status `ready` deltaP `42.2194` edge `0.887` maxDD `-0.5131`
- `news_risk_high->fx_24h` score `6.2597` n `32` status `ready` deltaP `53.5714` edge `0.1645` maxDD `0.0`
- `news_risk_high->fx_4h` score `4.1707` n `32` status `ready` deltaP `43.6738` edge `0.061` maxDD `-0.0345`
- `news_risk_high->crypto_major_24h` score `2.9992` n `32` status `ready` deltaP `15.625` edge `0.3583` maxDD `-4.2368`
- `market_context_high->unknown_1h` score `2.3658` n `192` status `ready` deltaP `2.8599` edge `0.2789` maxDD `-3.7317`
- `news_risk_high->fx_1h` score `2.2949` n `32` status `ready` deltaP `27.6946` edge `0.0205` maxDD `-0.1113`
- `news_risk_high->commodity_24h` score `1.7991` n `32` status `ready` deltaP `23.3206` edge `0.015` maxDD `-0.3101`
- `market_context_high->unknown_4h` score `1.7376` n `192` status `ready` deltaP `0.1397` edge `0.3971` maxDD `-11.925`
- `news_risk_high->crypto_major_1h` score `1.3836` n `32` status `ready` deltaP `14.2777` edge `0.1289` maxDD `-2.0691`
- `news_risk_high->crypto_alt_1h` score `0.7943` n `32` status `ready` deltaP `10.5726` edge `0.0775` maxDD `-1.6923`
- `market_context_high->metal_24h` score `-0.0579` n `192` status `ready` deltaP `19.8023` edge `0.1174` maxDD `-11.8809`
- `news_risk_high->index_24h` score `-0.1839` n `32` status `ready` deltaP `8.801` edge `0.0049` maxDD `-2.3058`
- `market_context_high->fx_1h` score `-0.3252` n `192` status `ready` deltaP `0.6113` edge `-0.0012` maxDD `-0.5659`
- `market_context_high->metal_4h` score `-0.5523` n `192` status `ready` deltaP `4.281` edge `0.0194` maxDD `-3.4996`
- `market_context_high->commodity_1h` score `-0.6182` n `192` status `ready` deltaP `-1.3473` edge `0.0021` maxDD `-0.5708`
- `market_context_high->equity_4h` score `-0.7854` n `192` status `ready` deltaP `2.5152` edge `0.0095` maxDD `-2.671`
- `news_risk_high->metal_1h` score `-0.7886` n `32` status `ready` deltaP `-3.5928` edge `-0.0274` maxDD `-1.6464`
- `market_context_high->crypto_alt_1h` score `-0.8694` n `192` status `ready` deltaP `4.8434` edge `0.0315` maxDD `-9.3536`
- `market_context_high->metal_1h` score `-0.8724` n `192` status `ready` deltaP `1.6155` edge `-0.0036` maxDD `-2.0564`
- `market_context_high->crypto_major_1h` score `-0.916` n `192` status `ready` deltaP `4.3819` edge `0.0301` maxDD `-9.807`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
