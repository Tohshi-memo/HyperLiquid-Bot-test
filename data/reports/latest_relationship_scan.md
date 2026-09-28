# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-28T19:07:31.415432+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `72`

- Symbol pattern count: `7790`

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

- `news_risk_high->unknown_24h` score `2674.728` n `139` status `ready` deltaP `1.2153` edge `222.8859` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `9.1138` n `139` status `ready` deltaP `24.7752` edge `0.9895` maxDD `-29.2814`
- `news_risk_high->equity_24h` score `5.7894` n `139` status `ready` deltaP `24.373` edge `0.5756` maxDD `-11.1179`
- `news_risk_high->crypto_major_24h` score `5.7239` n `139` status `ready` deltaP `20.9007` edge `0.7811` maxDD `-26.1424`
- `news_risk_high->index_24h` score `3.1957` n `139` status `ready` deltaP `30.0048` edge `0.1358` maxDD `-2.2287`
- `news_risk_high->equity_4h` score `2.3746` n `139` status `ready` deltaP `25.8017` edge `0.1868` maxDD `-9.2079`
- `news_risk_high->metal_24h` score `2.1965` n `139` status `ready` deltaP `22.3846` edge `0.2193` maxDD `-6.8392`
- `news_risk_high->crypto_alt_4h` score `0.6885` n `139` status `ready` deltaP `7.4311` edge `0.2738` maxDD `-15.9436`
- `news_risk_high->crypto_alt_1h` score `0.5367` n `139` status `ready` deltaP `6.5685` edge `0.092` maxDD `-4.2849`
- `news_risk_high->equity_1h` score `0.4768` n `139` status `ready` deltaP `7.1049` edge `0.0585` maxDD `-1.957`
- `news_risk_high->index_1h` score `0.4563` n `139` status `ready` deltaP `8.7516` edge `0.0087` maxDD `-0.3214`
- `news_risk_high->index_4h` score `-0.1709` n `139` status `ready` deltaP `6.658` edge `0.0267` maxDD `-1.493`
- `news_risk_high->metal_1h` score `-0.5424` n `139` status `ready` deltaP `1.1911` edge `0.0098` maxDD `-0.7016`
- `news_risk_high->crypto_major_1h` score `-0.6527` n `139` status `ready` deltaP `-0.0022` edge `0.0446` maxDD `-7.2607`
- `news_risk_high->fx_1h` score `-1.1726` n `139` status `ready` deltaP `-8.9681` edge `-0.0025` maxDD `-1.0436`
- `news_risk_high->fx_4h` score `-1.2397` n `139` status `ready` deltaP `9.6771` edge `-0.0021` maxDD `-3.0414`
- `news_risk_high->metal_4h` score `-1.4824` n `139` status `ready` deltaP `-9.9184` edge `0.0255` maxDD `-3.6214`
- `news_risk_high->crypto_major_4h` score `-1.8914` n `139` status `ready` deltaP `-5.7006` edge `0.067` maxDD `-13.719`
- `news_risk_high->commodity_1h` score `-2.031` n `139` status `ready` deltaP `-12.0159` edge `-0.0128` maxDD `-3.3986`
- `news_risk_high->commodity_4h` score `-3.8539` n `139` status `ready` deltaP `-11.4746` edge `-0.0028` maxDD `-8.6825`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
