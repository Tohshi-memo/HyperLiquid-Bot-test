# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-29T05:22:30.797543+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `72`

- Symbol pattern count: `7198`

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

- `news_risk_high->unknown_24h` score `2625.8316` n `139` status `ready` deltaP `1.2153` edge `218.8112` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `15.2309` n `139` status `ready` deltaP `31.8933` edge `1.4518` maxDD `-29.2814`
- `news_risk_high->equity_24h` score `9.3012` n `139` status `ready` deltaP `31.491` edge `0.8208` maxDD `-11.1179`
- `news_risk_high->crypto_major_24h` score `8.7667` n `139` status `ready` deltaP `27.1507` edge `0.993` maxDD `-26.1424`
- `news_risk_high->index_24h` score `3.9451` n `139` status `ready` deltaP `35.9075` edge `0.1589` maxDD `-2.2287`
- `news_risk_high->metal_24h` score `3.5956` n `139` status `ready` deltaP `29.3291` edge `0.2896` maxDD `-6.8392`
- `news_risk_high->equity_4h` score `2.4555` n `139` status `ready` deltaP `27.1736` edge `0.1844` maxDD `-9.2079`
- `news_risk_high->crypto_alt_4h` score `1.3897` n `139` status `ready` deltaP `9.5653` edge `0.318` maxDD `-15.9436`
- `news_risk_high->crypto_alt_1h` score `0.7011` n `139` status `ready` deltaP `7.0176` edge `0.1027` maxDD `-4.2849`
- `news_risk_high->equity_1h` score `0.5955` n `139` status `ready` deltaP `8.3025` edge `0.0604` maxDD `-1.957`
- `news_risk_high->index_1h` score `0.4611` n `139` status `ready` deltaP `8.7516` edge `0.0091` maxDD `-0.3214`
- `news_risk_high->index_4h` score `-0.1269` n `139` status `ready` deltaP `7.2678` edge `0.0263` maxDD `-1.493`
- `news_risk_high->metal_1h` score `-0.5771` n `139` status `ready` deltaP `0.742` edge `0.0099` maxDD `-0.7016`
- `news_risk_high->crypto_major_1h` score `-0.588` n `139` status `ready` deltaP `0.4469` edge `0.0499` maxDD `-7.2607`
- `news_risk_high->fx_1h` score `-1.2255` n `139` status `ready` deltaP `-9.8663` edge `-0.0033` maxDD `-1.0436`
- `news_risk_high->fx_4h` score `-1.3241` n `139` status `ready` deltaP `8.61` edge `-0.0058` maxDD `-3.0414`
- `news_risk_high->metal_4h` score `-1.4656` n `139` status `ready` deltaP `-9.3086` edge `0.0236` maxDD `-3.6214`
- `news_risk_high->crypto_major_4h` score `-1.7612` n `139` status `ready` deltaP `-4.7859` edge `0.0776` maxDD `-13.719`
- `news_risk_high->commodity_1h` score `-2.0108` n `139` status `ready` deltaP `-11.5668` edge `-0.0132` maxDD `-3.3986`
- `news_risk_high->commodity_4h` score `-3.8551` n `139` status `ready` deltaP `-11.4746` edge `-0.0029` maxDD `-8.6825`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
