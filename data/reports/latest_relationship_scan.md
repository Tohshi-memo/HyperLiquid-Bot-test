# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-22T23:52:24.267466+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `5282`

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

- `market_context_high->unknown_1h` score `13296.3632` n `98` status `ready` deltaP `0.8462` edge `1108.0408` maxDD `-0.6271`
- `market_context_high->unknown_4h` score `8870.6609` n `94` status `ready` deltaP `-0.8886` edge `739.2582` maxDD `-0.7759`
- `news_risk_high->unknown_1h` score `1371.9154` n `31` status `ready` deltaP `3.5783` edge `114.32` maxDD `-0.7389`
- `news_risk_high->unknown_4h` score `1211.5194` n `31` status `ready` deltaP `4.3962` edge `100.9363` maxDD `-0.119`
- `news_risk_high->equity_4h` score `12.1372` n `31` status `ready` deltaP `39.9686` edge `0.7932` maxDD `-2.1911`
- `news_risk_high->crypto_alt_4h` score `11.0649` n `31` status `ready` deltaP `25.8457` edge `0.8368` maxDD `-5.2957`
- `news_risk_high->crypto_major_4h` score `6.7488` n `31` status `ready` deltaP `14.9488` edge `0.9073` maxDD `-7.6714`
- `news_risk_high->equity_1h` score `4.0913` n `31` status `ready` deltaP `20.1371` edge `0.2254` maxDD `-0.163`
- `news_risk_high->index_4h` score `3.6592` n `31` status `ready` deltaP `37.9869` edge `0.0777` maxDD `-0.4146`
- `news_risk_high->index_1h` score `2.7717` n `31` status `ready` deltaP `32.2919` edge `0.0242` maxDD `-0.0136`
- `news_risk_high->crypto_major_1h` score `2.5195` n `31` status `ready` deltaP `10.1603` edge `0.3014` maxDD `-1.6897`
- `news_risk_high->crypto_alt_1h` score `2.1235` n `31` status `ready` deltaP `8.813` edge `0.2492` maxDD `-1.5232`
- `news_risk_high->metal_4h` score `1.6781` n `31` status `ready` deltaP `22.5708` edge `0.1204` maxDD `-0.7918`
- `news_risk_high->metal_1h` score `1.582` n `31` status `ready` deltaP `29.7324` edge `0.0325` maxDD `-0.2315`
- `news_risk_high->commodity_4h` score `0.7567` n `31` status `ready` deltaP `17.6682` edge `0.019` maxDD `-0.5151`
- `news_risk_high->commodity_1h` score `-0.0777` n `31` status `ready` deltaP `1.2314` edge `0.0115` maxDD `-0.0947`
- `market_context_high->index_1h` score `-0.438` n `98` status `ready` deltaP `-0.3941` edge `-0.0047` maxDD `-1.2394`
- `market_context_high->metal_1h` score `-0.8384` n `98` status `ready` deltaP `0.4369` edge `-0.0063` maxDD `-2.6517`
- `market_context_high->fx_4h` score `-0.976` n `94` status `ready` deltaP `2.4585` edge `0.0061` maxDD `-1.1427`
- `market_context_high->fx_1h` score `-1.2626` n `98` status `ready` deltaP `-9.2784` edge `-0.0012` maxDD `-0.3731`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
