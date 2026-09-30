# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-30T00:22:31.793338+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `72`

- Symbol pattern count: `7026`

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

- `news_risk_high->unknown_24h` score `1854.9796` n `138` status `ready` deltaP `1.9097` edge `154.5689` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `14.4866` n `138` status `ready` deltaP `28.4043` edge `1.36` maxDD `-25.3719`
- `news_risk_high->equity_24h` score `8.6286` n `138` status `ready` deltaP `29.061` edge `0.7602` maxDD `-9.4579`
- `news_risk_high->crypto_major_24h` score `6.9511` n `138` status `ready` deltaP `24.1999` edge `0.8159` maxDD `-22.5043`
- `news_risk_high->index_24h` score `3.7247` n `138` status `ready` deltaP `35.092` edge `0.1416` maxDD `-1.8792`
- `news_risk_high->metal_24h` score `3.049` n `138` status `ready` deltaP `27.8156` edge `0.2442` maxDD `-6.0445`
- `news_risk_high->equity_4h` score `2.8309` n `141` status `ready` deltaP `28.7298` edge `0.2045` maxDD `-9.143`
- `news_risk_high->crypto_alt_4h` score `2.3814` n `141` status `ready` deltaP `12.9616` edge `0.378` maxDD `-15.9436`
- `news_risk_high->crypto_alt_1h` score `1.3444` n `141` status `ready` deltaP `10.0947` edge `0.1358` maxDD `-4.2849`
- `news_risk_high->equity_1h` score `0.6615` n `141` status `ready` deltaP `7.7069` edge `0.0697` maxDD `-1.9431`
- `news_risk_high->index_1h` score `0.441` n `141` status `ready` deltaP `8.3057` edge `0.0104` maxDD `-0.3214`
- `news_risk_high->index_4h` score `-0.0046` n `141` status `ready` deltaP `8.4674` edge `0.0285` maxDD `-1.493`
- `news_risk_high->crypto_major_1h` score `-0.1691` n `141` status `ready` deltaP `3.9867` edge `0.08` maxDD `-7.2607`
- `news_risk_high->metal_1h` score `-0.6172` n `141` status `ready` deltaP `-0.1189` edge `0.0123` maxDD `-0.7016`
- `news_risk_high->crypto_major_4h` score `-1.1902` n `141` status `ready` deltaP `-1.5611` edge `0.1293` maxDD `-13.719`
- `news_risk_high->fx_4h` score `-1.3874` n `141` status `ready` deltaP `7.6317` edge `-0.0074` maxDD `-3.0414`
- `news_risk_high->metal_4h` score `-1.3921` n `141` status `ready` deltaP `-8.5344` edge `0.027` maxDD `-3.5531`
- `news_risk_high->commodity_1h` score `-1.8363` n `141` status `ready` deltaP `-8.826` edge `-0.0091` maxDD `-3.3986`
- `news_risk_high->fx_1h` score `-1.8397` n `141` status `ready` deltaP `-9.1891` edge `-0.004` maxDD `-1.0436`
- `news_risk_high->commodity_4h` score `-2.2694` n `141` status `ready` deltaP `-9.1172` edge `0.0117` maxDD `-8.6825`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
