# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-23T18:37:28.956736+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `4518`

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

- `market_context_high->unknown_1h` score `32455.1761` n `45` status `ready` deltaP `2.7644` edge `2704.589` maxDD `-0.4206`
- `market_context_high->unknown_4h` score `22296.9954` n `45` status `ready` deltaP `3.4824` edge `1858.0736` maxDD `-0.7759`
- `news_risk_high->unknown_1h` score `1245.6467` n `31` status `ready` deltaP `2.9795` edge `103.8016` maxDD `-0.7389`
- `news_risk_high->unknown_4h` score `1061.6422` n `31` status `ready` deltaP `4.701` edge `88.4445` maxDD `-0.119`
- `news_risk_high->equity_24h` score `41.219` n `31` status `ready` deltaP `46.0069` edge `3.1282` maxDD `0.0`
- `news_risk_high->crypto_major_24h` score `35.609` n `31` status `ready` deltaP `47.2222` edge `2.6526` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `31.5117` n `31` status `ready` deltaP `47.3958` edge `2.31` maxDD `0.0`
- `news_risk_high->metal_24h` score `12.7528` n `31` status `ready` deltaP `47.3119` edge `0.7748` maxDD `-0.1986`
- `news_risk_high->crypto_alt_4h` score `9.7472` n `31` status `ready` deltaP `22.0348` edge `0.7524` maxDD `-5.2957`
- `news_risk_high->equity_4h` score `8.5733` n `31` status `ready` deltaP `30.6698` edge `0.5582` maxDD `-2.1911`
- `news_risk_high->index_24h` score `6.4157` n `31` status `ready` deltaP `44.2708` edge `0.2395` maxDD `0.0`
- `news_risk_high->fx_24h` score `6.2451` n `31` status `ready` deltaP `52.8226` edge `0.1811` maxDD `-0.0262`
- `news_risk_high->crypto_major_4h` score `5.8732` n `31` status `ready` deltaP `11.5952` edge `0.8174` maxDD `-7.6714`
- `news_risk_high->equity_1h` score `3.2397` n `31` status `ready` deltaP `18.0413` edge `0.1684` maxDD `-0.163`
- `market_context_high->fx_4h` score `3.1552` n `45` status `ready` deltaP `37.71` edge `0.04` maxDD `-0.2774`
- `news_risk_high->index_4h` score `2.9223` n `31` status `ready` deltaP `32.3466` edge `0.0539` maxDD `-0.4146`
- `news_risk_high->index_1h` score `2.5452` n `31` status `ready` deltaP `30.3458` edge `0.0183` maxDD `-0.0136`
- `news_risk_high->crypto_major_1h` score `2.3713` n `31` status `ready` deltaP `10.31` edge `0.2814` maxDD `-1.6897`
- `news_risk_high->crypto_alt_1h` score `1.9901` n `31` status `ready` deltaP `9.2621` edge `0.2291` maxDD `-1.5232`
- `market_context_high->commodity_24h` score `1.905` n `38` status `ready` deltaP `4.5413` edge `0.296` maxDD `-2.5636`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
