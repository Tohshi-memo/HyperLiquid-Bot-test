# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-28T15:37:36.889801+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `72`

- Symbol pattern count: `7782`

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

- `news_risk_high->unknown_24h` score `2431.0176` n `139` status `ready` deltaP `1.2153` edge `202.5767` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `7.5058` n `139` status `ready` deltaP `22.3446` edge `0.8717` maxDD `-29.2814`
- `news_risk_high->crypto_major_24h` score `4.7735` n `139` status `ready` deltaP `18.4702` edge `0.7181` maxDD `-26.1424`
- `news_risk_high->equity_24h` score `4.4789` n `139` status `ready` deltaP `21.9424` edge `0.4826` maxDD `-11.1179`
- `news_risk_high->index_24h` score `2.8884` n `139` status `ready` deltaP `27.5742` edge `0.1264` maxDD `-2.2287`
- `news_risk_high->equity_4h` score `2.1252` n `139` status `ready` deltaP `24.1249` edge `0.1772` maxDD `-9.2079`
- `news_risk_high->metal_24h` score `1.7396` n `139` status `ready` deltaP `20.6485` edge `0.1928` maxDD `-6.8392`
- `news_risk_high->crypto_alt_1h` score `0.755` n `139` status `ready` deltaP `7.4667` edge `0.1042` maxDD `-4.2849`
- `news_risk_high->equity_1h` score `0.514` n `139` status `ready` deltaP `7.1049` edge `0.0616` maxDD `-1.957`
- `news_risk_high->crypto_alt_4h` score `0.4836` n `139` status `ready` deltaP `6.6689` edge `0.2618` maxDD `-15.9436`
- `news_risk_high->index_1h` score `0.4479` n `139` status `ready` deltaP `8.6019` edge `0.009` maxDD `-0.3214`
- `news_risk_high->index_4h` score `-0.2841` n `139` status `ready` deltaP `5.4385` edge `0.0254` maxDD `-1.493`
- `news_risk_high->metal_1h` score `-0.498` n `139` status `ready` deltaP `1.6402` edge `0.0105` maxDD `-0.7016`
- `news_risk_high->crypto_major_1h` score `-0.5981` n `139` status `ready` deltaP `0.2972` edge `0.0496` maxDD `-7.2607`
- `news_risk_high->fx_1h` score `-1.1812` n `139` status `ready` deltaP `-9.1178` edge `-0.0026` maxDD `-1.0436`
- `news_risk_high->fx_4h` score `-1.1875` n `139` status `ready` deltaP `10.5918` edge `-0.0015` maxDD `-3.0414`
- `news_risk_high->metal_4h` score `-1.5346` n `139` status `ready` deltaP `-10.6806` edge `0.0239` maxDD `-3.6214`
- `news_risk_high->commodity_1h` score `-2.0638` n `139` status `ready` deltaP `-12.1656` edge `-0.016` maxDD `-3.3986`
- `news_risk_high->crypto_major_4h` score `-2.0706` n `139` status `ready` deltaP `-6.3103` edge `0.0481` maxDD `-13.719`
- `news_risk_high->commodity_4h` score `-4.0051` n `139` status `ready` deltaP `-12.3893` edge `-0.0093` maxDD `-8.6825`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
