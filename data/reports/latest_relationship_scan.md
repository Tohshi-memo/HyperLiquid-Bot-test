# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-29T23:22:38.003636+00:00`
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

- `news_risk_high->unknown_24h` score `2064.5356` n `138` status `ready` deltaP `1.9097` edge `172.0319` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `14.8514` n `138` status `ready` deltaP `28.4043` edge `1.3904` maxDD `-25.3719`
- `news_risk_high->equity_24h` score `8.8942` n `138` status `ready` deltaP `29.7555` edge `0.7777` maxDD `-9.4579`
- `news_risk_high->crypto_major_24h` score `7.1959` n `138` status `ready` deltaP `24.1999` edge `0.8363` maxDD `-22.5043`
- `news_risk_high->index_24h` score `3.8222` n `138` status `ready` deltaP `35.7865` edge `0.1451` maxDD `-1.8792`
- `news_risk_high->metal_24h` score `3.2017` n `138` status `ready` deltaP `28.51` edge `0.2523` maxDD `-6.0445`
- `news_risk_high->equity_4h` score `2.9193` n `141` status `ready` deltaP `29.3396` edge `0.2078` maxDD `-9.143`
- `news_risk_high->crypto_alt_4h` score `2.239` n `141` status `ready` deltaP `12.3519` edge `0.3702` maxDD `-15.9436`
- `news_risk_high->crypto_alt_1h` score `1.2845` n `141` status `ready` deltaP `9.7953` edge `0.1328` maxDD `-4.2849`
- `news_risk_high->equity_1h` score `0.707` n `141` status `ready` deltaP `8.156` edge `0.0705` maxDD `-1.9431`
- `news_risk_high->index_1h` score `0.4938` n `141` status `ready` deltaP `8.9045` edge `0.0108` maxDD `-0.3214`
- `news_risk_high->index_4h` score `0.0538` n `141` status `ready` deltaP `9.0772` edge `0.0293` maxDD `-1.493`
- `news_risk_high->crypto_major_1h` score `-0.2299` n `141` status `ready` deltaP `3.3879` edge `0.0762` maxDD `-7.2607`
- `news_risk_high->metal_1h` score `-0.574` n `141` status `ready` deltaP `0.3302` edge `0.0129` maxDD `-0.7016`
- `news_risk_high->crypto_major_4h` score `-1.2599` n `141` status `ready` deltaP `-1.866` edge `0.1224` maxDD `-13.719`
- `news_risk_high->metal_4h` score `-1.3448` n `141` status `ready` deltaP `-7.9247` edge `0.029` maxDD `-3.5531`
- `news_risk_high->fx_4h` score `-1.3787` n `141` status `ready` deltaP `7.7841` edge `-0.0073` maxDD `-3.0414`
- `news_risk_high->fx_1h` score `-1.8516` n `141` status `ready` deltaP `-9.3388` edge `-0.004` maxDD `-1.0436`
- `news_risk_high->commodity_1h` score `-1.8635` n `141` status `ready` deltaP `-9.2751` edge `-0.0096` maxDD `-3.3986`
- `news_risk_high->commodity_4h` score `-2.2291` n `141` status `ready` deltaP `-8.5074` edge `0.0128` maxDD `-8.6825`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
