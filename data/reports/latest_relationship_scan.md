# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-29T19:22:30.666506+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `72`

- Symbol pattern count: `7160`

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

- `news_risk_high->unknown_24h` score `2590.8679` n `139` status `ready` deltaP `1.3889` edge `215.8964` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `15.5301` n `139` status `ready` deltaP `30.5044` edge `1.486` maxDD `-29.2814`
- `news_risk_high->equity_24h` score `9.4579` n `139` status `ready` deltaP `32.0118` edge `0.8294` maxDD `-11.039`
- `news_risk_high->crypto_major_24h` score `7.4557` n `139` status `ready` deltaP `24.8938` edge `0.8988` maxDD `-26.1424`
- `news_risk_high->index_24h` score `4.0566` n `139` status `ready` deltaP `37.9909` edge `0.1543` maxDD `-2.2287`
- `news_risk_high->metal_24h` score `3.5586` n `139` status `ready` deltaP `30.8916` edge `0.2761` maxDD `-6.8392`
- `news_risk_high->equity_4h` score `3.0389` n `142` status `ready` deltaP `30.1143` edge `0.2126` maxDD `-9.143`
- `news_risk_high->crypto_alt_4h` score `2.0108` n `142` status `ready` deltaP `11.2247` edge `0.3587` maxDD `-15.9436`
- `news_risk_high->crypto_alt_1h` score `1.0031` n `142` status `ready` deltaP `8.0185` edge `0.1212` maxDD `-4.2849`
- `news_risk_high->equity_1h` score `0.7186` n `142` status `ready` deltaP `8.301` edge `0.0705` maxDD `-1.9431`
- `news_risk_high->index_1h` score `0.5221` n `142` status `ready` deltaP `9.1992` edge `0.0112` maxDD `-0.3214`
- `news_risk_high->index_4h` score `0.2534` n `142` status `ready` deltaP `11.1216` edge `0.0323` maxDD `-1.493`
- `news_risk_high->crypto_major_1h` score `-0.2761` n `142` status `ready` deltaP `3.0383` edge `0.0726` maxDD `-7.2607`
- `news_risk_high->metal_1h` score `-0.4738` n `142` status `ready` deltaP `1.4632` edge `0.0137` maxDD `-0.7016`
- `news_risk_high->metal_4h` score `-1.2059` n `142` status `ready` deltaP `-6.3251` edge `0.037` maxDD `-3.6214`
- `news_risk_high->fx_4h` score `-1.2827` n `142` status `ready` deltaP `9.4362` edge `-0.006` maxDD `-3.0414`
- `news_risk_high->crypto_major_4h` score `-1.3119` n `142` status `ready` deltaP `-2.701` edge `0.1213` maxDD `-13.719`
- `news_risk_high->fx_1h` score `-1.8061` n `142` status `ready` deltaP `-8.845` edge `-0.0035` maxDD `-1.0436`
- `news_risk_high->commodity_1h` score `-1.8752` n `142` status `ready` deltaP `-9.4543` edge `-0.0099` maxDD `-3.3986`
- `news_risk_high->commodity_4h` score `-2.3405` n `142` status `ready` deltaP `-9.7647` edge `0.0069` maxDD `-8.6825`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
