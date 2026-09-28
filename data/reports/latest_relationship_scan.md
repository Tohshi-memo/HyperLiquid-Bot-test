# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-28T01:52:30.039927+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `72`

- Symbol pattern count: `7602`

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

- `news_risk_high->unknown_24h` score `633.7764` n `138` status `ready` deltaP `1.2153` edge `52.8066` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `1.8488` n `138` status `ready` deltaP `14.1682` edge `0.4548` maxDD `-29.2814`
- `news_risk_high->index_24h` score `1.58` n `138` status `ready` deltaP `18.599` edge `0.0772` maxDD `-2.2287`
- `news_risk_high->metal_24h` score `0.9335` n `138` status `ready` deltaP `20.6975` edge `0.1253` maxDD `-6.8392`
- `news_risk_high->equity_4h` score `0.2488` n `139` status `ready` deltaP `16.9602` edge `0.0686` maxDD `-9.2079`
- `news_risk_high->index_1h` score `-0.0096` n `139` status `ready` deltaP `3.5121` edge `0.0048` maxDD `-0.3214`
- `news_risk_high->equity_1h` score `-0.0974` n `139` status `ready` deltaP `3.6618` edge `0.0336` maxDD `-1.957`
- `news_risk_high->crypto_alt_1h` score `-0.1061` n `139` status `ready` deltaP `4.1733` edge `0.0544` maxDD `-4.2849`
- `news_risk_high->equity_24h` score `-0.2981` n `138` status `ready` deltaP `12.9152` edge `0.1447` maxDD `-11.1179`
- `news_risk_high->metal_1h` score `-0.6346` n `139` status `ready` deltaP `0.4426` edge `0.0071` maxDD `-0.7016`
- `news_risk_high->index_4h` score `-1.0043` n `139` status `ready` deltaP `-1.2688` edge `0.0101` maxDD `-1.493`
- `news_risk_high->crypto_major_1h` score `-1.0704` n `139` status `ready` deltaP `-3.2956` edge `0.013` maxDD `-7.2607`
- `news_risk_high->fx_4h` score `-1.1044` n `139` status `ready` deltaP `11.9637` edge `0.0` maxDD `-3.0414`
- `news_risk_high->fx_1h` score `-1.1329` n `139` status `ready` deltaP `-8.2196` edge `-0.0024` maxDD `-1.0436`
- `news_risk_high->crypto_major_24h` score `-1.4459` n `138` status `ready` deltaP `9.443` edge `0.26` maxDD `-26.1424`
- `news_risk_high->crypto_alt_4h` score `-1.5619` n `139` status `ready` deltaP `2.4006` edge `0.1198` maxDD `-15.9436`
- `news_risk_high->metal_4h` score `-1.8004` n `139` status `ready` deltaP `-13.272` edge `0.0071` maxDD `-3.6214`
- `news_risk_high->commodity_1h` score `-1.943` n `139` status `ready` deltaP `-10.5189` edge `-0.0115` maxDD `-3.3986`
- `news_risk_high->crypto_major_4h` score `-3.4027` n `139` status `ready` deltaP `-11.7981` edge `-0.0861` maxDD `-13.719`
- `news_risk_high->commodity_4h` score `-3.5642` n `139` status `ready` deltaP `-9.188` edge `0.0061` maxDD `-8.6825`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
