# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-30T16:37:31.761205+00:00`
- Price records: `672`
- Market context records: `8428`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `5742`

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

- `news_risk_high->unknown_24h` score `6254.4961` n `52` status `ready` deltaP `42.1341` edge `520.9692` maxDD `-2.0332`
- `news_risk_high->equity_4h` score `5.4575` n `52` status `ready` deltaP `23.3232` edge `0.359` maxDD `-3.4427`
- `news_risk_high->equity_1h` score `2.3139` n `52` status `ready` deltaP `19.1847` edge `0.0958` maxDD `-1.1366`
- `news_risk_high->index_4h` score `2.1244` n `52` status `ready` deltaP `18.5976` edge `0.0721` maxDD `-0.191`
- `news_risk_high->crypto_alt_1h` score `1.574` n `52` status `ready` deltaP `12.4597` edge `0.0915` maxDD `-1.1388`
- `news_risk_high->crypto_major_1h` score `1.2813` n `52` status `ready` deltaP `9.316` edge `0.0844` maxDD `-1.1783`
- `news_risk_high->crypto_major_4h` score `1.255` n `52` status `ready` deltaP `4.796` edge `0.1983` maxDD `-2.8833`
- `news_risk_high->crypto_alt_4h` score `1.0139` n `52` status `ready` deltaP `13.8251` edge `0.177` maxDD `-5.8012`
- `news_risk_high->fx_1h` score `0.1577` n `52` status `ready` deltaP `6.5408` edge `0.0047` maxDD `-0.2475`
- `news_risk_high->metal_4h` score `0.121` n `52` status `ready` deltaP `2.7556` edge `0.0385` maxDD `-0.7433`
- `news_risk_high->index_1h` score `0.0371` n `52` status `ready` deltaP `2.7983` edge `0.0133` maxDD `-0.3089`
- `news_risk_high->fx_4h` score `-0.3716` n `52` status `ready` deltaP `5.4175` edge `0.012` maxDD `-0.6604`
- `news_risk_high->metal_1h` score `-0.4254` n `52` status `ready` deltaP `0.5528` edge `0.0012` maxDD `-0.5599`
- `news_risk_high->commodity_1h` score `-1.9333` n `52` status `ready` deltaP `-6.322` edge `-0.0404` maxDD `-2.9516`
- `news_risk_high->fx_24h` score `-5.7241` n `52` status `ready` deltaP `-27.7244` edge `-0.06` maxDD `-5.2413`
- `news_risk_high->commodity_4h` score `-8.3997` n `52` status `ready` deltaP `-26.2078` edge `-0.1945` maxDD `-13.1269`
- `news_risk_high->metal_24h` score `-8.6896` n `52` status `ready` deltaP `-34.7088` edge `-0.2157` maxDD `-10.8302`
- `news_risk_high->commodity_24h` score `-12.5775` n `52` status `ready` deltaP `-12.6068` edge `-0.3701` maxDD `-33.8515`
- `news_risk_high->index_24h` score `-12.7114` n `52` status `ready` deltaP `-27.3771` edge `-0.3265` maxDD `-28.0214`
- `news_risk_high->equity_24h` score `-36.3796` n `52` status `ready` deltaP `-25.4674` edge `-1.0743` maxDD `-127.0042`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
