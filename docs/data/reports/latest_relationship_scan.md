# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-25T04:52:29.792802+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `4092`

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

- `market_context_high->unknown_1h` score `32244.0865` n `45` status `ready` deltaP `2.1656` edge `2687.0022` maxDD `-0.4209`
- `market_context_high->unknown_4h` score `21973.8397` n `45` status `ready` deltaP `3.1776` edge `1831.146` maxDD `-0.7765`
- `news_risk_high->unknown_1h` score `1009.1315` n `31` status `ready` deltaP `2.3807` edge `84.096` maxDD `-0.7395`
- `news_risk_high->unknown_4h` score `720.8922` n `31` status `ready` deltaP `4.3962` edge `60.0507` maxDD `-0.1191`
- `news_risk_high->equity_24h` score `39.5388` n `31` status `ready` deltaP `44.4444` edge `2.9986` maxDD `0.0`
- `news_risk_high->crypto_major_24h` score `39.1847` n `31` status `ready` deltaP `50.1736` edge `2.9309` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `35.675` n `31` status `ready` deltaP `49.6528` edge `2.6419` maxDD `0.0`
- `news_risk_high->crypto_alt_4h` score `12.0242` n `31` status `ready` deltaP `28.1323` edge `0.9015` maxDD `-5.2957`
- `news_risk_high->metal_24h` score `11.2442` n `31` status `ready` deltaP `41.2355` edge `0.6896` maxDD `-0.1986`
- `news_risk_high->equity_4h` score `10.7723` n `31` status `ready` deltaP `36.1576` edge `0.7047` maxDD `-2.178`
- `news_risk_high->crypto_major_4h` score `7.5712` n `31` status `ready` deltaP `19.0647` edge `0.9853` maxDD `-7.6714`
- `news_risk_high->index_24h` score `6.0204` n `31` status `ready` deltaP `44.4444` edge `0.2054` maxDD `0.0`
- `news_risk_high->fx_24h` score `5.3352` n `31` status `ready` deltaP `45.1837` edge `0.1562` maxDD `-0.0262`
- `news_risk_high->equity_1h` score `3.7544` n `31` status `ready` deltaP `19.3886` edge `0.2023` maxDD `-0.1621`
- `news_risk_high->index_4h` score `3.2521` n `31` status `ready` deltaP `34.9381` edge `0.0641` maxDD `-0.4146`
- `news_risk_high->crypto_major_1h` score `2.7673` n `31` status `ready` deltaP `12.5555` edge `0.3172` maxDD `-1.6897`
- `news_risk_high->index_1h` score `2.6052` n `31` status `ready` deltaP `30.7949` edge `0.0203` maxDD `-0.0136`
- `market_context_high->fx_4h` score `2.5968` n `45` status `ready` deltaP `31.7649` edge `0.0331` maxDD `-0.2774`
- `news_risk_high->crypto_alt_1h` score `2.3673` n `31` status `ready` deltaP `12.2561` edge `0.2575` maxDD `-1.5232`
- `news_risk_high->metal_1h` score `1.5999` n `31` status `ready` deltaP `30.3312` edge `0.0308` maxDD `-0.2315`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
