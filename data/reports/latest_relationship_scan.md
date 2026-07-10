# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-10T04:37:25.209519+00:00`
- Price records: `672`
- Market context records: `6249`
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

- `news_risk_high->crypto_alt_24h` score `14.2784` n `32` status `ready` deltaP `42.302` edge `0.9226` maxDD `-0.5131`
- `news_risk_high->fx_24h` score `6.0502` n `32` status `ready` deltaP `51.448` edge `0.1612` maxDD `0.0`
- `news_risk_high->fx_4h` score `4.2205` n `32` status `ready` deltaP `44.1311` edge `0.0621` maxDD `-0.0345`
- `news_risk_high->crypto_major_24h` score `3.3257` n `32` status `ready` deltaP `15.7102` edge `0.3996` maxDD `-4.2368`
- `market_context_high->unknown_1h` score `2.3155` n `192` status `ready` deltaP `2.7102` edge `0.2757` maxDD `-3.7317`
- `news_risk_high->fx_1h` score `2.2997` n `32` status `ready` deltaP `27.6946` edge `0.0209` maxDD `-0.1113`
- `news_risk_high->commodity_24h` score `2.2936` n `32` status `ready` deltaP `25.6016` edge `0.041` maxDD `-0.3101`
- `market_context_high->unknown_4h` score `1.6834` n `192` status `ready` deltaP `-0.0127` edge `0.3936` maxDD `-11.925`
- `news_risk_high->crypto_major_1h` score `1.3415` n `32` status `ready` deltaP `13.9783` edge `0.1255` maxDD `-2.0691`
- `news_risk_high->crypto_alt_1h` score `0.7888` n `32` status `ready` deltaP `10.5726` edge `0.0768` maxDD `-1.6923`
- `market_context_high->metal_24h` score `-0.1517` n `192` status `ready` deltaP `19.5601` edge `0.107` maxDD `-11.8809`
- `news_risk_high->index_24h` score `-0.1777` n `32` status `ready` deltaP `8.8905` edge `0.0051` maxDD `-2.3058`
- `market_context_high->fx_1h` score `-0.3221` n `192` status `ready` deltaP `0.6113` edge `-0.0008` maxDD `-0.5659`
- `market_context_high->metal_4h` score `-0.5151` n `192` status `ready` deltaP `3.9762` edge `0.0262` maxDD `-3.4996`
- `market_context_high->equity_4h` score `-0.539` n `192` status `ready` deltaP `2.8201` edge `0.028` maxDD `-2.671`
- `market_context_high->commodity_1h` score `-0.6517` n `192` status `ready` deltaP `-1.7964` edge `0.0023` maxDD `-0.5708`
- `news_risk_high->metal_1h` score `-0.7442` n `32` status `ready` deltaP `-3.1437` edge `-0.0247` maxDD `-1.6464`
- `market_context_high->metal_1h` score `-0.8041` n `192` status `ready` deltaP `2.0646` edge `-0.0009` maxDD `-2.0564`
- `market_context_high->crypto_alt_1h` score `-0.8749` n `192` status `ready` deltaP `4.8434` edge `0.0308` maxDD `-9.3536`
- `market_context_high->crypto_major_1h` score `-0.9581` n `192` status `ready` deltaP `4.0825` edge `0.0267` maxDD `-9.807`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
