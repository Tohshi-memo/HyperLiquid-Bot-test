# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-09T20:27:24.217232+00:00`
- Price records: `672`
- Market context records: `6215`
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

- `news_risk_high->crypto_alt_24h` score `13.0982` n `32` status `ready` deltaP `42.2194` edge `0.8248` maxDD `-0.5131`
- `news_risk_high->fx_24h` score `6.5614` n `32` status `ready` deltaP `56.8027` edge `0.1681` maxDD `0.0`
- `news_risk_high->fx_4h` score `4.0856` n `32` status `ready` deltaP `42.7591` edge `0.06` maxDD `-0.0345`
- `news_risk_high->crypto_major_24h` score `2.4204` n `32` status `ready` deltaP `15.625` edge `0.2841` maxDD `-4.2368`
- `news_risk_high->fx_1h` score `2.308` n `32` status `ready` deltaP `27.8443` edge `0.0206` maxDD `-0.1113`
- `market_context_high->unknown_1h` score `1.8585` n `192` status `ready` deltaP `1.5126` edge `0.2456` maxDD `-3.7317`
- `news_risk_high->crypto_major_1h` score `1.4023` n `32` status `ready` deltaP `14.4274` edge `0.1303` maxDD `-2.0691`
- `news_risk_high->commodity_24h` score `1.0378` n `32` status `ready` deltaP `20.0893` edge `-0.0269` maxDD `-0.3101`
- `news_risk_high->crypto_alt_1h` score `0.753` n `32` status `ready` deltaP `9.9738` edge `0.0762` maxDD `-1.6923`
- `market_context_high->unknown_4h` score `0.4127` n `192` status `ready` deltaP `-1.842` edge `0.2999` maxDD `-11.925`
- `market_context_high->metal_24h` score `-0.0447` n `192` status `ready` deltaP `19.8023` edge `0.1191` maxDD `-11.8809`
- `news_risk_high->index_24h` score `-0.2471` n `32` status `ready` deltaP `8.801` edge `-0.0032` maxDD `-2.3058`
- `market_context_high->fx_1h` score `-0.3167` n `192` status `ready` deltaP `0.761` edge `-0.0011` maxDD `-0.5659`
- `market_context_high->commodity_1h` score `-0.5835` n `192` status `ready` deltaP `-0.8982` edge `0.002` maxDD `-0.5708`
- `market_context_high->metal_4h` score `-0.7222` n `192` status `ready` deltaP `2.6042` edge `0.0088` maxDD `-3.4996`
- `news_risk_high->metal_1h` score `-0.7862` n `32` status `ready` deltaP `-3.4431` edge `-0.0281` maxDD `-1.6464`
- `market_context_high->metal_1h` score `-0.8688` n `192` status `ready` deltaP `1.7652` edge `-0.0043` maxDD `-2.0564`
- `market_context_high->crypto_major_1h` score `-0.8973` n `192` status `ready` deltaP `4.5316` edge `0.0315` maxDD `-9.807`
- `market_context_high->crypto_alt_1h` score `-0.9107` n `192` status `ready` deltaP `4.2446` edge `0.0302` maxDD `-9.3536`
- `market_context_high->equity_1h` score `-1.1328` n `192` status `ready` deltaP `-3.0127` edge `-0.0136` maxDD `-4.2573`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
