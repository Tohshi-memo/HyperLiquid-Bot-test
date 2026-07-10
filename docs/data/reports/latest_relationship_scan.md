# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-10T05:07:34.940336+00:00`
- Price records: `672`
- Market context records: `6251`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11100`

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

- `news_risk_high->crypto_alt_24h` score `14.3709` n `32` status `ready` deltaP `42.4679` edge `0.9292` maxDD `-0.5131`
- `news_risk_high->fx_24h` score `6.0322` n `32` status `ready` deltaP `51.2821` edge `0.1608` maxDD `0.0`
- `news_risk_high->fx_4h` score `4.2083` n `32` status `ready` deltaP `43.9787` edge `0.0621` maxDD `-0.0345`
- `news_risk_high->crypto_major_24h` score `3.397` n `32` status `ready` deltaP `15.8814` edge `0.4076` maxDD `-4.2368`
- `market_context_high->unknown_1h` score `2.3526` n `192` status `ready` deltaP `3.0096` edge `0.2768` maxDD `-3.7317`
- `news_risk_high->commodity_24h` score `2.3025` n `32` status `ready` deltaP `25.7425` edge `0.0408` maxDD `-0.3101`
- `news_risk_high->fx_1h` score `2.2877` n `32` status `ready` deltaP `27.5449` edge `0.0209` maxDD `-0.1113`
- `market_context_high->unknown_4h` score `1.5608` n `192` status `ready` deltaP `-0.1652` edge `0.3844` maxDD `-11.925`
- `news_risk_high->crypto_major_1h` score `1.3244` n `32` status `ready` deltaP `13.8286` edge `0.1243` maxDD `-2.0691`
- `news_risk_high->crypto_alt_1h` score `0.7764` n `32` status `ready` deltaP `10.4229` edge `0.0762` maxDD `-1.6923`
- `market_context_high->metal_24h` score `-0.1584` n `192` status `ready` deltaP `19.4151` edge `0.1071` maxDD `-11.8809`
- `news_risk_high->index_24h` score `-0.1621` n `32` status `ready` deltaP `9.0705` edge `0.0059` maxDD `-2.3058`
- `market_context_high->fx_1h` score `-0.3299` n `192` status `ready` deltaP `0.4616` edge `-0.0008` maxDD `-0.5659`
- `market_context_high->metal_4h` score `-0.5269` n `192` status `ready` deltaP `3.8237` edge `0.0257` maxDD `-3.4996`
- `market_context_high->equity_4h` score `-0.5294` n `192` status `ready` deltaP `2.8201` edge `0.0288` maxDD `-2.671`
- `market_context_high->commodity_1h` score `-0.6266` n `192` status `ready` deltaP `-1.497` edge `0.0024` maxDD `-0.5708`
- `news_risk_high->metal_1h` score `-0.727` n `32` status `ready` deltaP `-2.8443` edge `-0.0245` maxDD `-1.6464`
- `market_context_high->metal_1h` score `-0.7777` n `192` status `ready` deltaP `2.364` edge `-0.0007` maxDD `-2.0564`
- `market_context_high->crypto_alt_1h` score `-0.8873` n `192` status `ready` deltaP `4.6937` edge `0.0302` maxDD `-9.3536`
- `market_context_high->crypto_major_1h` score `-0.9753` n `192` status `ready` deltaP `3.9328` edge `0.0255` maxDD `-9.807`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
