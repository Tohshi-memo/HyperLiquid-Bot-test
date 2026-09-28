# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-28T23:52:33.279943+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `72`

- Symbol pattern count: `7166`

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

- `news_risk_high->unknown_24h` score `2657.5824` n `139` status `ready` deltaP `1.2153` edge `221.4571` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `11.8341` n `139` status `ready` deltaP `28.0738` edge `1.1942` maxDD `-29.2814`
- `news_risk_high->equity_24h` score `7.648` n `139` status `ready` deltaP `27.6716` edge `0.7085` maxDD `-11.1179`
- `news_risk_high->crypto_major_24h` score `6.8843` n `139` status `ready` deltaP `23.3313` edge `0.8616` maxDD `-26.1424`
- `news_risk_high->index_24h` score `3.6132` n `139` status `ready` deltaP `33.3034` edge `0.1486` maxDD `-2.2287`
- `news_risk_high->metal_24h` score `2.98` n `139` status `ready` deltaP `25.6832` edge `0.2626` maxDD `-6.8392`
- `news_risk_high->equity_4h` score `2.6565` n `139` status `ready` deltaP `27.631` edge `0.1981` maxDD `-9.2079`
- `news_risk_high->crypto_alt_4h` score `1.0179` n `139` status `ready` deltaP `8.8031` edge `0.2921` maxDD `-15.9436`
- `news_risk_high->crypto_alt_1h` score `0.6938` n `139` status `ready` deltaP `7.317` edge `0.1001` maxDD `-4.2849`
- `news_risk_high->equity_1h` score `0.6027` n `139` status `ready` deltaP `8.0031` edge `0.063` maxDD `-1.957`
- `news_risk_high->index_1h` score `0.4851` n `139` status `ready` deltaP `9.051` edge `0.0091` maxDD `-0.3214`
- `news_risk_high->index_4h` score `-0.0857` n `139` status `ready` deltaP `7.5726` edge `0.0277` maxDD `-1.493`
- `news_risk_high->metal_1h` score `-0.4657` n `139` status `ready` deltaP `1.9396` edge `0.0112` maxDD `-0.7016`
- `news_risk_high->crypto_major_1h` score `-0.5568` n `139` status `ready` deltaP `0.5966` edge `0.0529` maxDD `-7.2607`
- `news_risk_high->fx_1h` score `-1.2248` n `139` status `ready` deltaP `-9.8663` edge `-0.0032` maxDD `-1.0436`
- `news_risk_high->fx_4h` score `-1.3471` n `139` status `ready` deltaP `8.1527` edge `-0.0057` maxDD `-3.0414`
- `news_risk_high->metal_4h` score `-1.3933` n `139` status `ready` deltaP `-8.6988` edge `0.0288` maxDD `-3.6214`
- `news_risk_high->crypto_major_4h` score `-1.8905` n `139` status `ready` deltaP `-5.5481` edge `0.0661` maxDD `-13.719`
- `news_risk_high->commodity_1h` score `-2.0209` n `139` status `ready` deltaP `-11.7165` edge `-0.0135` maxDD `-3.3986`
- `news_risk_high->commodity_4h` score `-3.7848` n `139` status `ready` deltaP `-10.8649` edge `-0.0011` maxDD `-8.6825`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
