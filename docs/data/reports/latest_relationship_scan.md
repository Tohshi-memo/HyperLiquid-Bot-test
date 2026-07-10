# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-10T00:52:30.828126+00:00`
- Price records: `672`
- Market context records: `6233`
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

- `news_risk_high->crypto_alt_24h` score `13.793` n `32` status `ready` deltaP `42.2194` edge `0.8827` maxDD `-0.5131`
- `news_risk_high->fx_24h` score `6.2757` n `32` status `ready` deltaP `53.7415` edge `0.1647` maxDD `0.0`
- `news_risk_high->fx_4h` score `4.1573` n `32` status `ready` deltaP `43.5213` edge `0.0609` maxDD `-0.0345`
- `news_risk_high->crypto_major_24h` score `2.9547` n `32` status `ready` deltaP `15.625` edge `0.3526` maxDD `-4.2368`
- `market_context_high->unknown_1h` score `2.3802` n `192` status `ready` deltaP `3.0096` edge `0.2791` maxDD `-3.7317`
- `news_risk_high->fx_1h` score `2.2949` n `32` status `ready` deltaP `27.6946` edge `0.0205` maxDD `-0.1113`
- `news_risk_high->commodity_24h` score `1.7615` n `32` status `ready` deltaP `23.1505` edge `0.013` maxDD `-0.3101`
- `market_context_high->unknown_4h` score `1.711` n `192` status `ready` deltaP `-0.0127` edge `0.3959` maxDD `-11.925`
- `news_risk_high->crypto_major_1h` score `1.3945` n `32` status `ready` deltaP `14.4274` edge `0.1293` maxDD `-2.0691`
- `news_risk_high->crypto_alt_1h` score `0.8036` n `32` status `ready` deltaP `10.7223` edge `0.0777` maxDD `-1.6923`
- `market_context_high->metal_24h` score `-0.0548` n `192` status `ready` deltaP `19.8023` edge `0.1178` maxDD `-11.8809`
- `news_risk_high->index_24h` score `-0.1871` n `32` status `ready` deltaP `8.801` edge `0.0045` maxDD `-2.3058`
- `market_context_high->fx_1h` score `-0.3252` n `192` status `ready` deltaP `0.6113` edge `-0.0012` maxDD `-0.5659`
- `market_context_high->metal_4h` score `-0.5585` n `192` status `ready` deltaP `4.281` edge `0.0186` maxDD `-3.4996`
- `market_context_high->commodity_1h` score `-0.6182` n `192` status `ready` deltaP `-1.3473` edge `0.0021` maxDD `-0.5708`
- `news_risk_high->metal_1h` score `-0.7878` n `32` status `ready` deltaP `-3.5928` edge `-0.0273` maxDD `-1.6464`
- `market_context_high->equity_4h` score `-0.8216` n `192` status `ready` deltaP `2.3628` edge `0.0075` maxDD `-2.671`
- `market_context_high->crypto_alt_1h` score `-0.8601` n `192` status `ready` deltaP `4.9931` edge `0.0317` maxDD `-9.3536`
- `market_context_high->metal_1h` score `-0.8712` n `192` status `ready` deltaP `1.6155` edge `-0.0035` maxDD `-2.0564`
- `market_context_high->crypto_major_1h` score `-0.9051` n `192` status `ready` deltaP `4.5316` edge `0.0305` maxDD `-9.807`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
