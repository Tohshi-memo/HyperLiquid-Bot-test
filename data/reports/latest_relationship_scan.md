# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-30T00:07:27.993165+00:00`
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

- `news_risk_high->unknown_24h` score `1907.3752` n `138` status `ready` deltaP `1.9097` edge `158.9352` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `14.5802` n `138` status `ready` deltaP `28.4043` edge `1.3678` maxDD `-25.3719`
- `news_risk_high->equity_24h` score `8.6953` n `138` status `ready` deltaP `29.2346` edge `0.7646` maxDD `-9.4579`
- `news_risk_high->crypto_major_24h` score `7.0171` n `138` status `ready` deltaP `24.1999` edge `0.8214` maxDD `-22.5043`
- `news_risk_high->index_24h` score `3.7482` n `138` status `ready` deltaP `35.2657` edge `0.1424` maxDD `-1.8792`
- `news_risk_high->metal_24h` score `3.0881` n `138` status `ready` deltaP `27.9892` edge `0.2463` maxDD `-6.0445`
- `news_risk_high->equity_4h` score `2.8491` n `141` status `ready` deltaP `28.8823` edge `0.205` maxDD `-9.143`
- `news_risk_high->crypto_alt_4h` score `2.3452` n `141` status `ready` deltaP `12.8092` edge `0.376` maxDD `-15.9436`
- `news_risk_high->crypto_alt_1h` score `1.3336` n `141` status `ready` deltaP `10.0947` edge `0.1349` maxDD `-4.2849`
- `news_risk_high->equity_1h` score `0.6627` n `141` status `ready` deltaP `7.7069` edge `0.0698` maxDD `-1.9431`
- `news_risk_high->index_1h` score `0.4542` n `141` status `ready` deltaP `8.4554` edge `0.0105` maxDD `-0.3214`
- `news_risk_high->index_4h` score `0.0088` n `141` status `ready` deltaP `8.6199` edge `0.0286` maxDD `-1.493`
- `news_risk_high->crypto_major_1h` score `-0.1831` n `141` status `ready` deltaP `3.837` edge `0.0792` maxDD `-7.2607`
- `news_risk_high->metal_1h` score `-0.6136` n `141` status `ready` deltaP `-0.1189` edge `0.0126` maxDD `-0.7016`
- `news_risk_high->crypto_major_4h` score `-1.2138` n `141` status `ready` deltaP `-1.7136` edge `0.1273` maxDD `-13.719`
- `news_risk_high->fx_4h` score `-1.3795` n `141` status `ready` deltaP `7.7841` edge `-0.0074` maxDD `-3.0414`
- `news_risk_high->metal_4h` score `-1.3811` n `141` status `ready` deltaP `-8.382` edge `0.0274` maxDD `-3.5531`
- `news_risk_high->fx_1h` score `-1.8397` n `141` status `ready` deltaP `-9.1891` edge `-0.004` maxDD `-1.0436`
- `news_risk_high->commodity_1h` score `-1.8441` n `141` status `ready` deltaP `-8.9757` edge `-0.0091` maxDD `-3.3986`
- `news_risk_high->commodity_4h` score `-2.2583` n `141` status `ready` deltaP `-8.9647` edge `0.0121` maxDD `-8.6825`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
