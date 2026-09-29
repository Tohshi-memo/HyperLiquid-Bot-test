# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-29T23:07:29.425681+00:00`
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

- `news_risk_high->unknown_24h` score `2116.8916` n `138` status `ready` deltaP `1.9097` edge `176.3949` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `14.9768` n `138` status `ready` deltaP `28.5779` edge `1.3997` maxDD `-25.3719`
- `news_risk_high->equity_24h` score `8.9572` n `138` status `ready` deltaP `29.9291` edge `0.7818` maxDD `-9.4579`
- `news_risk_high->crypto_major_24h` score `7.2715` n `138` status `ready` deltaP `24.1999` edge `0.8426` maxDD `-22.5043`
- `news_risk_high->index_24h` score `3.8445` n `138` status `ready` deltaP `35.9601` edge `0.1458` maxDD `-1.8792`
- `news_risk_high->metal_24h` score `3.2384` n `138` status `ready` deltaP `28.6836` edge `0.2542` maxDD `-6.0445`
- `news_risk_high->equity_4h` score `2.9411` n `141` status `ready` deltaP `29.492` edge `0.2086` maxDD `-9.143`
- `news_risk_high->crypto_alt_4h` score `2.2184` n `141` status `ready` deltaP `12.1994` edge `0.3695` maxDD `-15.9436`
- `news_risk_high->crypto_alt_1h` score `1.2977` n `141` status `ready` deltaP `9.945` edge `0.1329` maxDD `-4.2849`
- `news_risk_high->equity_1h` score `0.707` n `141` status `ready` deltaP `8.156` edge `0.0705` maxDD `-1.9431`
- `news_risk_high->index_1h` score `0.4938` n `141` status `ready` deltaP `8.9045` edge `0.0108` maxDD `-0.3214`
- `news_risk_high->index_4h` score `0.0684` n `141` status `ready` deltaP `9.2296` edge `0.0295` maxDD `-1.493`
- `news_risk_high->crypto_major_1h` score `-0.2314` n `141` status `ready` deltaP `3.3879` edge `0.076` maxDD `-7.2607`
- `news_risk_high->metal_1h` score `-0.5728` n `141` status `ready` deltaP `0.3302` edge `0.013` maxDD `-0.7016`
- `news_risk_high->crypto_major_4h` score `-1.2749` n `141` status `ready` deltaP `-2.0184` edge `0.1215` maxDD `-13.719`
- `news_risk_high->metal_4h` score `-1.3322` n `141` status `ready` deltaP `-7.7722` edge `0.0296` maxDD `-3.5531`
- `news_risk_high->fx_4h` score `-1.37` n `141` status `ready` deltaP `7.9365` edge `-0.0072` maxDD `-3.0414`
- `news_risk_high->fx_1h` score `-1.8385` n `141` status `ready` deltaP `-9.1891` edge `-0.0039` maxDD `-1.0436`
- `news_risk_high->commodity_1h` score `-1.8628` n `141` status `ready` deltaP `-9.2751` edge `-0.0095` maxDD `-3.3986`
- `news_risk_high->commodity_4h` score `-2.2212` n `141` status `ready` deltaP `-8.355` edge `0.0128` maxDD `-8.6825`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
