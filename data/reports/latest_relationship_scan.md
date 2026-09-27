# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-27T21:07:29.943045+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `72`

- Symbol pattern count: `7928`

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

- `news_risk_high->unknown_24h` score `720.0276` n `136` status `ready` deltaP `1.2153` edge `59.9942` maxDD `0.0`
- `news_risk_high->index_24h` score `1.294` n `136` status `ready` deltaP `17.5143` edge `0.0606` maxDD `-2.2287`
- `news_risk_high->crypto_alt_24h` score `0.9618` n `136` status `ready` deltaP `14.6446` edge `0.3777` maxDD `-29.2814`
- `news_risk_high->metal_24h` score `0.7756` n `136` status `ready` deltaP `18.9032` edge `0.1241` maxDD `-6.8392`
- `news_risk_high->index_1h` score `-0.0995` n `139` status `ready` deltaP `2.6139` edge `0.0033` maxDD `-0.3214`
- `news_risk_high->equity_4h` score `-0.1239` n `139` status `ready` deltaP `15.4358` edge `0.0477` maxDD `-9.2079`
- `news_risk_high->crypto_alt_1h` score `-0.1444` n `139` status `ready` deltaP `4.0236` edge `0.0522` maxDD `-4.2849`
- `news_risk_high->equity_1h` score `-0.342` n `139` status `ready` deltaP `2.1648` edge `0.0232` maxDD `-1.957`
- `news_risk_high->metal_1h` score `-0.7629` n `139` status `ready` deltaP `-0.6053` edge `0.0034` maxDD `-0.7016`
- `news_risk_high->fx_4h` score `-1.0602` n `139` status `ready` deltaP `12.5735` edge `0.0016` maxDD `-3.0414`
- `news_risk_high->fx_1h` score `-1.0893` n `139` status `ready` deltaP `-7.4711` edge `-0.0018` maxDD `-1.0436`
- `news_risk_high->crypto_major_1h` score `-1.199` n `139` status `ready` deltaP `-4.3435` edge `0.0035` maxDD `-7.2607`
- `news_risk_high->index_4h` score `-1.2206` n `139` status `ready` deltaP `-3.403` edge `0.0063` maxDD `-1.493`
- `news_risk_high->equity_24h` score `-1.2783` n `136` status `ready` deltaP `11.8975` edge `0.0698` maxDD `-11.1179`
- `news_risk_high->crypto_alt_4h` score `-1.8489` n `139` status `ready` deltaP `1.3336` edge `0.103` maxDD `-15.9436`
- `news_risk_high->commodity_1h` score `-1.8753` n `139` status `ready` deltaP `-9.471` edge `-0.0098` maxDD `-3.3986`
- `news_risk_high->metal_4h` score `-1.9104` n `139` status `ready` deltaP `-14.3391` edge `0.0001` maxDD `-3.6214`
- `news_risk_high->crypto_major_24h` score `-3.514` n `136` status `ready` deltaP `8.2516` edge `0.0956` maxDD `-26.1424`
- `news_risk_high->commodity_4h` score `-3.5668` n `139` status `ready` deltaP `-9.3405` edge `0.0069` maxDD `-8.6825`
- `news_risk_high->crypto_major_4h` score `-3.6292` n `139` status `ready` deltaP `-13.1701` edge `-0.106` maxDD `-13.719`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
