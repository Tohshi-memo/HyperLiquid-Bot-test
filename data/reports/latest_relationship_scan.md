# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-28T10:07:31.587491+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `72`

- Symbol pattern count: `7910`

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

- `news_risk_high->unknown_24h` score `925.986` n `139` status `ready` deltaP `1.2153` edge `77.1574` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `5.5554` n `139` status `ready` deltaP `19.2196` edge `0.73` maxDD `-29.2814`
- `news_risk_high->crypto_major_24h` score `2.8011` n `139` status `ready` deltaP `14.6507` edge `0.5792` maxDD `-26.1424`
- `news_risk_high->equity_24h` score `2.4022` n `139` status `ready` deltaP `18.123` edge `0.335` maxDD `-11.1179`
- `news_risk_high->index_24h` score `2.3501` n `139` status `ready` deltaP `23.7548` edge `0.107` maxDD `-2.2287`
- `news_risk_high->equity_4h` score `1.5391` n `139` status `ready` deltaP `21.8383` edge `0.1436` maxDD `-9.2079`
- `news_risk_high->metal_24h` score `1.323` n `139` status `ready` deltaP `20.3013` edge `0.1604` maxDD `-6.8392`
- `news_risk_high->crypto_alt_4h` score `0.7256` n `139` status `ready` deltaP `7.2787` edge `0.2779` maxDD `-15.9436`
- `news_risk_high->crypto_alt_1h` score `0.6447` n `139` status `ready` deltaP `7.0176` edge `0.098` maxDD `-4.2849`
- `news_risk_high->equity_1h` score `0.3282` n `139` status `ready` deltaP `6.3564` edge `0.0511` maxDD `-1.957`
- `news_risk_high->index_1h` score `0.2898` n `139` status `ready` deltaP `6.9552` edge `0.0068` maxDD `-0.3214`
- `news_risk_high->index_4h` score `-0.4998` n `139` status `ready` deltaP `3.7617` edge `0.0186` maxDD `-1.493`
- `news_risk_high->metal_1h` score `-0.5867` n `139` status `ready` deltaP `0.742` edge `0.0091` maxDD `-0.7016`
- `news_risk_high->crypto_major_1h` score `-0.7072` n `139` status `ready` deltaP `-0.601` edge `0.0416` maxDD `-7.2607`
- `news_risk_high->fx_1h` score `-1.1485` n `139` status `ready` deltaP `-8.519` edge `-0.0024` maxDD `-1.0436`
- `news_risk_high->fx_4h` score `-1.1906` n `139` status `ready` deltaP `10.5918` edge `-0.0019` maxDD `-3.0414`
- `news_risk_high->metal_4h` score `-1.5038` n `139` status `ready` deltaP `-10.2232` edge `0.0248` maxDD `-3.6214`
- `news_risk_high->commodity_1h` score `-2.0303` n `139` status `ready` deltaP `-11.7165` edge `-0.0147` maxDD `-3.3986`
- `news_risk_high->crypto_major_4h` score `-2.1467` n `139` status `ready` deltaP `-6.9201` edge `0.0424` maxDD `-13.719`
- `news_risk_high->commodity_4h` score `-3.8793` n `139` status `ready` deltaP `-11.6271` edge `-0.0039` maxDD `-8.6825`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
