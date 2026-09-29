# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-29T23:52:29.961429+00:00`
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

- `news_risk_high->unknown_24h` score `1959.778` n `138` status `ready` deltaP `1.9097` edge `163.3021` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `14.6654` n `138` status `ready` deltaP `28.4043` edge `1.3749` maxDD `-25.3719`
- `news_risk_high->equity_24h` score `8.762` n `138` status `ready` deltaP `29.4082` edge `0.769` maxDD `-9.4579`
- `news_risk_high->crypto_major_24h` score `7.0735` n `138` status `ready` deltaP `24.1999` edge `0.8261` maxDD `-22.5043`
- `news_risk_high->index_24h` score `3.7729` n `138` status `ready` deltaP `35.4393` edge `0.1433` maxDD `-1.8792`
- `news_risk_high->metal_24h` score `3.1259` n `138` status `ready` deltaP `28.1628` edge `0.2483` maxDD `-6.0445`
- `news_risk_high->equity_4h` score `2.8709` n `141` status `ready` deltaP `29.0347` edge `0.2058` maxDD `-9.143`
- `news_risk_high->crypto_alt_4h` score `2.315` n `141` status `ready` deltaP `12.6567` edge `0.3745` maxDD `-15.9436`
- `news_risk_high->crypto_alt_1h` score `1.3073` n `141` status `ready` deltaP `9.945` edge `0.1337` maxDD `-4.2849`
- `news_risk_high->equity_1h` score `0.6783` n `141` status `ready` deltaP `7.8566` edge `0.0701` maxDD `-1.9431`
- `news_risk_high->index_1h` score `0.4674` n `141` status `ready` deltaP `8.6051` edge `0.0106` maxDD `-0.3214`
- `news_risk_high->index_4h` score `0.0234` n `141` status `ready` deltaP `8.7723` edge `0.0288` maxDD `-1.493`
- `news_risk_high->crypto_major_1h` score `-0.2026` n `141` status `ready` deltaP `3.6873` edge `0.0777` maxDD `-7.2607`
- `news_risk_high->metal_1h` score `-0.5992` n `141` status `ready` deltaP `0.0308` edge `0.0128` maxDD `-0.7016`
- `news_risk_high->crypto_major_4h` score `-1.2262` n `141` status `ready` deltaP `-1.7136` edge `0.1257` maxDD `-13.719`
- `news_risk_high->metal_4h` score `-1.3692` n `141` status `ready` deltaP `-8.2296` edge `0.0279` maxDD `-3.5531`
- `news_risk_high->fx_4h` score `-1.3795` n `141` status `ready` deltaP `7.7841` edge `-0.0074` maxDD `-3.0414`
- `news_risk_high->commodity_1h` score `-1.8449` n `141` status `ready` deltaP `-8.9757` edge `-0.0092` maxDD `-3.3986`
- `news_risk_high->fx_1h` score `-1.8516` n `141` status `ready` deltaP `-9.3388` edge `-0.004` maxDD `-1.0436`
- `news_risk_high->commodity_4h` score `-2.2473` n `141` status `ready` deltaP `-8.8123` edge `0.0125` maxDD `-8.6825`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
