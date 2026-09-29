# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-29T21:22:34.365622+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `72`

- Symbol pattern count: `7170`

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

- `news_risk_high->unknown_24h` score `2485.4824` n `138` status `ready` deltaP `1.9097` edge `207.1108` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `15.8253` n `138` status `ready` deltaP `29.7932` edge `1.4623` maxDD `-25.3719`
- `news_risk_high->equity_24h` score `9.3953` n `138` status `ready` deltaP `31.1444` edge `0.8102` maxDD `-9.4579`
- `news_risk_high->crypto_major_24h` score `7.8445` n `138` status `ready` deltaP `25.2416` edge `0.8834` maxDD `-22.5043`
- `news_risk_high->index_24h` score `4.0066` n `138` status `ready` deltaP `37.1754` edge `0.1512` maxDD `-1.8792`
- `news_risk_high->metal_24h` score `3.4916` n `138` status `ready` deltaP `29.8989` edge `0.2672` maxDD `-6.0445`
- `news_risk_high->equity_4h` score `3.0889` n `141` status `ready` deltaP `30.5591` edge `0.2138` maxDD `-9.143`
- `news_risk_high->crypto_alt_4h` score `2.1494` n `141` status `ready` deltaP `11.7421` edge `0.3668` maxDD `-15.9436`
- `news_risk_high->crypto_alt_1h` score `1.1358` n `141` status `ready` deltaP `9.0468` edge `0.1254` maxDD `-4.2849`
- `news_risk_high->equity_1h` score `0.7058` n `141` status `ready` deltaP `8.156` edge `0.0704` maxDD `-1.9431`
- `news_risk_high->index_1h` score `0.471` n `141` status `ready` deltaP `8.6051` edge `0.0109` maxDD `-0.3214`
- `news_risk_high->index_4h` score `0.1754` n `141` status `ready` deltaP `10.2967` edge `0.0313` maxDD `-1.493`
- `news_risk_high->crypto_major_1h` score `-0.2299` n `141` status `ready` deltaP `3.5376` edge `0.0752` maxDD `-7.2607`
- `news_risk_high->metal_1h` score `-0.5872` n `141` status `ready` deltaP `0.1805` edge `0.0128` maxDD `-0.7016`
- `news_risk_high->metal_4h` score `-1.244` n `141` status `ready` deltaP `-6.7052` edge `0.0338` maxDD `-3.5531`
- `news_risk_high->crypto_major_4h` score `-1.3001` n `141` status `ready` deltaP `-2.3233` edge `0.1203` maxDD `-13.719`
- `news_risk_high->fx_4h` score `-1.309` n `141` status `ready` deltaP `9.0036` edge `-0.0065` maxDD `-3.0414`
- `news_risk_high->fx_1h` score `-1.8121` n `141` status `ready` deltaP `-8.8897` edge `-0.0037` maxDD `-1.0436`
- `news_risk_high->commodity_1h` score `-1.8441` n `141` status `ready` deltaP `-8.9757` edge `-0.0091` maxDD `-3.3986`
- `news_risk_high->commodity_4h` score `-2.2638` n `141` status `ready` deltaP `-8.9647` edge `0.0114` maxDD `-8.6825`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
