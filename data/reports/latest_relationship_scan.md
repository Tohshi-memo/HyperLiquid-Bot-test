# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-28T10:22:32.016549+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `72`

- Symbol pattern count: `7916`

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

- `news_risk_high->unknown_24h` score `949.4676` n `139` status `ready` deltaP `1.2153` edge `79.1142` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `5.6749` n `139` status `ready` deltaP `19.3933` edge `0.7388` maxDD `-29.2814`
- `news_risk_high->crypto_major_24h` score `2.9182` n `139` status `ready` deltaP `14.8243` edge `0.5878` maxDD `-26.1424`
- `news_risk_high->equity_24h` score `2.4964` n `139` status `ready` deltaP `18.2966` edge `0.3417` maxDD `-11.1179`
- `news_risk_high->index_24h` score `2.376` n `139` status `ready` deltaP `23.9284` edge `0.108` maxDD `-2.2287`
- `news_risk_high->equity_4h` score `1.5765` n `139` status `ready` deltaP `21.9907` edge `0.1457` maxDD `-9.2079`
- `news_risk_high->metal_24h` score `1.3386` n `139` status `ready` deltaP `20.3013` edge `0.1617` maxDD `-6.8392`
- `news_risk_high->crypto_alt_4h` score `0.7617` n `139` status `ready` deltaP `7.4311` edge `0.2799` maxDD `-15.9436`
- `news_risk_high->crypto_alt_1h` score `0.677` n `139` status `ready` deltaP `7.1673` edge `0.0997` maxDD `-4.2849`
- `news_risk_high->equity_1h` score `0.3138` n `139` status `ready` deltaP `6.2067` edge `0.0509` maxDD `-1.957`
- `news_risk_high->index_1h` score `0.303` n `139` status `ready` deltaP `7.1049` edge `0.0069` maxDD `-0.3214`
- `news_risk_high->index_4h` score `-0.484` n `139` status `ready` deltaP `3.9141` edge `0.0189` maxDD `-1.493`
- `news_risk_high->metal_1h` score `-0.5879` n `139` status `ready` deltaP `0.742` edge `0.009` maxDD `-0.7016`
- `news_risk_high->crypto_major_1h` score `-0.6908` n `139` status `ready` deltaP `-0.4513` edge `0.0427` maxDD `-7.2607`
- `news_risk_high->fx_1h` score `-1.1407` n `139` status `ready` deltaP `-8.3693` edge `-0.0024` maxDD `-1.0436`
- `news_risk_high->fx_4h` score `-1.1811` n `139` status `ready` deltaP `10.7442` edge `-0.0017` maxDD `-3.0414`
- `news_risk_high->metal_4h` score `-1.4935` n `139` status `ready` deltaP `-10.0708` edge `0.0251` maxDD `-3.6214`
- `news_risk_high->commodity_1h` score `-2.0396` n `139` status `ready` deltaP `-11.8662` edge `-0.0149` maxDD `-3.3986`
- `news_risk_high->crypto_major_4h` score `-2.1302` n `139` status `ready` deltaP `-6.7677` edge `0.0435` maxDD `-13.719`
- `news_risk_high->commodity_4h` score `-3.9023` n `139` status `ready` deltaP `-11.7795` edge `-0.0048` maxDD `-8.6825`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
