# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-09T15:07:39.579942+00:00`
- Price records: `672`
- Market context records: `6192`
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

- `news_risk_high->crypto_alt_24h` score `12.7034` n `32` status `ready` deltaP `42.2194` edge `0.7919` maxDD `-0.5131`
- `news_risk_high->fx_24h` score `6.9011` n `32` status `ready` deltaP `60.3741` edge `0.1726` maxDD `0.0`
- `news_risk_high->fx_4h` score `4.0703` n `32` status `ready` deltaP `42.4487` edge `0.0608` maxDD `-0.0345`
- `news_risk_high->fx_1h` score `2.3476` n `32` status `ready` deltaP `28.2934` edge `0.0209` maxDD `-0.1113`
- `news_risk_high->crypto_major_24h` score `2.1045` n `32` status `ready` deltaP `15.625` edge `0.2436` maxDD `-4.2368`
- `market_context_high->unknown_1h` score `1.8441` n `192` status `ready` deltaP `1.2132` edge `0.2464` maxDD `-3.7317`
- `news_risk_high->crypto_major_1h` score `1.3969` n `32` status `ready` deltaP `14.4274` edge `0.1296` maxDD `-2.0691`
- `news_risk_high->crypto_alt_1h` score `0.7406` n `32` status `ready` deltaP `9.375` edge `0.0786` maxDD `-1.6923`
- `market_context_high->unknown_4h` score `0.3479` n `192` status `ready` deltaP `-1.9773` edge `0.2954` maxDD `-11.925`
- `news_risk_high->commodity_24h` score `0.0933` n `32` status `ready` deltaP `16.5179` edge `-0.0818` maxDD `-0.3101`
- `market_context_high->metal_24h` score `0.0692` n `192` status `ready` deltaP `19.8023` edge `0.1337` maxDD `-11.8809`
- `news_risk_high->index_24h` score `-0.1634` n `32` status `ready` deltaP `9.4813` edge `0.003` maxDD `-2.3058`
- `market_context_high->fx_1h` score `-0.291` n `192` status `ready` deltaP `1.2101` edge `-0.0008` maxDD `-0.5659`
- `market_context_high->equity_4h` score `-0.3503` n `192` status `ready` deltaP `1.6242` edge `0.0517` maxDD `-2.671`
- `market_context_high->metal_4h` score `-0.648` n `192` status `ready` deltaP `3.5351` edge `0.0121` maxDD `-3.4996`
- `market_context_high->commodity_1h` score `-0.7644` n `192` status `ready` deltaP `-2.5449` edge `-0.0021` maxDD `-0.5708`
- `news_risk_high->metal_1h` score `-0.8174` n `32` status `ready` deltaP `-3.8922` edge `-0.0291` maxDD `-1.6464`
- `market_context_high->crypto_major_1h` score `-0.9028` n `192` status `ready` deltaP `4.5316` edge `0.0308` maxDD `-9.807`
- `market_context_high->metal_1h` score `-0.9168` n `192` status `ready` deltaP `1.3161` edge `-0.0053` maxDD `-2.0564`
- `market_context_high->crypto_alt_1h` score `-0.9231` n `192` status `ready` deltaP `3.6458` edge `0.0326` maxDD `-9.3536`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
