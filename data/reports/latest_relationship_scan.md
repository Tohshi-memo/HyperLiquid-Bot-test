# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-30T00:37:26.796768+00:00`
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

- `news_risk_high->unknown_24h` score `1802.5636` n `138` status `ready` deltaP `1.9097` edge `150.2009` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `14.4014` n `138` status `ready` deltaP `28.4043` edge `1.3529` maxDD `-25.3719`
- `news_risk_high->equity_24h` score `8.5631` n `138` status `ready` deltaP `28.8874` edge `0.7559` maxDD `-9.4579`
- `news_risk_high->crypto_major_24h` score `6.8911` n `138` status `ready` deltaP `24.1999` edge `0.8109` maxDD `-22.5043`
- `news_risk_high->index_24h` score `3.7012` n `138` status `ready` deltaP `34.9184` edge `0.1408` maxDD `-1.8792`
- `news_risk_high->metal_24h` score `3.0123` n `138` status `ready` deltaP `27.6419` edge `0.2423` maxDD `-6.0445`
- `news_risk_high->equity_4h` score `2.8151` n `141` status `ready` deltaP `28.5774` edge `0.2042` maxDD `-9.143`
- `news_risk_high->crypto_alt_4h` score `2.4224` n `141` status `ready` deltaP `13.1141` edge `0.3804` maxDD `-15.9436`
- `news_risk_high->crypto_alt_1h` score `1.3432` n `141` status `ready` deltaP `10.0947` edge `0.1357` maxDD `-4.2849`
- `news_risk_high->equity_1h` score `0.6579` n `141` status `ready` deltaP `7.7069` edge `0.0694` maxDD `-1.9431`
- `news_risk_high->index_1h` score `0.441` n `141` status `ready` deltaP `8.3057` edge `0.0104` maxDD `-0.3214`
- `news_risk_high->index_4h` score `-0.018` n `141` status `ready` deltaP `8.315` edge `0.0284` maxDD `-1.493`
- `news_risk_high->crypto_major_1h` score `-0.1675` n `141` status `ready` deltaP `3.9867` edge `0.0802` maxDD `-7.2607`
- `news_risk_high->metal_1h` score `-0.6184` n `141` status `ready` deltaP `-0.1189` edge `0.0122` maxDD `-0.7016`
- `news_risk_high->crypto_major_4h` score `-1.1644` n `141` status `ready` deltaP `-1.4087` edge `0.1316` maxDD `-13.719`
- `news_risk_high->fx_4h` score `-1.3961` n `141` status `ready` deltaP `7.4792` edge `-0.0075` maxDD `-3.0414`
- `news_risk_high->metal_4h` score `-1.4024` n `141` status `ready` deltaP `-8.6869` edge `0.0267` maxDD `-3.5531`
- `news_risk_high->commodity_1h` score `-1.8363` n `141` status `ready` deltaP `-8.826` edge `-0.0091` maxDD `-3.3986`
- `news_risk_high->fx_1h` score `-1.8528` n `141` status `ready` deltaP `-9.3388` edge `-0.0041` maxDD `-1.0436`
- `news_risk_high->commodity_4h` score `-2.2804` n `141` status `ready` deltaP `-9.2696` edge `0.0113` maxDD `-8.6825`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
