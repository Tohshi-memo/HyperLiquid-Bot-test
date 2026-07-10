# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-10T05:37:26.943047+00:00`
- Price records: `672`
- Market context records: `6254`
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

- `news_risk_high->crypto_alt_24h` score `14.4351` n `32` status `ready` deltaP `42.5514` edge `0.934` maxDD `-0.5131`
- `news_risk_high->fx_24h` score `6.0058` n `32` status `ready` deltaP `51.0274` edge `0.1603` maxDD `0.0`
- `news_risk_high->fx_4h` score `4.1937` n `32` status `ready` deltaP `43.8262` edge `0.0619` maxDD `-0.0345`
- `news_risk_high->crypto_major_24h` score `3.4467` n `32` status `ready` deltaP `15.9675` edge `0.4134` maxDD `-4.2368`
- `news_risk_high->commodity_24h` score `2.325` n `32` status `ready` deltaP `25.8134` edge `0.0422` maxDD `-0.3101`
- `market_context_high->unknown_1h` score `2.3215` n `192` status `ready` deltaP `2.7102` edge `0.2762` maxDD `-3.7317`
- `news_risk_high->fx_1h` score `2.314` n `32` status `ready` deltaP `27.8443` edge `0.0211` maxDD `-0.1113`
- `market_context_high->unknown_4h` score `1.4932` n `192` status `ready` deltaP `-0.4701` edge `0.3808` maxDD `-11.925`
- `news_risk_high->crypto_major_1h` score `1.3244` n `32` status `ready` deltaP `13.8286` edge `0.1243` maxDD `-2.0691`
- `news_risk_high->crypto_alt_1h` score `0.7748` n `32` status `ready` deltaP `10.4229` edge `0.076` maxDD `-1.6923`
- `news_risk_high->index_24h` score `-0.1574` n `32` status `ready` deltaP `9.161` edge `0.0059` maxDD `-2.3058`
- `market_context_high->metal_24h` score `-0.1828` n `192` status `ready` deltaP `19.171` edge `0.1056` maxDD `-11.8809`
- `market_context_high->fx_1h` score `-0.3128` n `192` status `ready` deltaP `0.761` edge `-0.0006` maxDD `-0.5659`
- `market_context_high->equity_4h` score `-0.492` n `192` status `ready` deltaP `2.9726` edge `0.0309` maxDD `-2.671`
- `market_context_high->metal_4h` score `-0.5467` n `192` status `ready` deltaP `3.5188` edge `0.0252` maxDD `-3.4996`
- `market_context_high->commodity_1h` score `-0.6134` n `192` status `ready` deltaP `-1.3473` edge `0.0025` maxDD `-0.5708`
- `news_risk_high->metal_1h` score `-0.7185` n `32` status `ready` deltaP `-2.6946` edge `-0.0244` maxDD `-1.6464`
- `market_context_high->metal_1h` score `-0.7646` n `192` status `ready` deltaP `2.5137` edge `-0.0006` maxDD `-2.0564`
- `market_context_high->crypto_alt_1h` score `-0.8889` n `192` status `ready` deltaP `4.6937` edge `0.03` maxDD `-9.3536`
- `market_context_high->crypto_major_1h` score `-0.9753` n `192` status `ready` deltaP `3.9328` edge `0.0255` maxDD `-9.807`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
