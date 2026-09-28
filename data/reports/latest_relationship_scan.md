# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-28T20:07:32.715761+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `72`

- Symbol pattern count: `7386`

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

- `news_risk_high->unknown_24h` score `2672.8392` n `139` status `ready` deltaP `1.2153` edge `222.7285` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `9.7046` n `139` status `ready` deltaP `25.4696` edge `1.0341` maxDD `-29.2814`
- `news_risk_high->equity_24h` score `6.1905` n `139` status `ready` deltaP `25.0674` edge `0.6044` maxDD `-11.1179`
- `news_risk_high->crypto_major_24h` score `6.0567` n `139` status `ready` deltaP `21.5952` edge `0.8042` maxDD `-26.1424`
- `news_risk_high->index_24h` score `3.2872` n `139` status `ready` deltaP `30.6992` edge `0.1388` maxDD `-2.2287`
- `news_risk_high->equity_4h` score `2.3662` n `139` status `ready` deltaP `25.8017` edge `0.1861` maxDD `-9.2079`
- `news_risk_high->metal_24h` score `2.366` n `139` status `ready` deltaP `23.0791` edge `0.2288` maxDD `-6.8392`
- `news_risk_high->crypto_alt_4h` score `0.7223` n `139` status `ready` deltaP `7.5836` edge `0.2756` maxDD `-15.9436`
- `news_risk_high->crypto_alt_1h` score `0.6675` n `139` status `ready` deltaP `7.0176` edge `0.0999` maxDD `-4.2849`
- `news_risk_high->equity_1h` score `0.4888` n `139` status `ready` deltaP `7.1049` edge `0.0595` maxDD `-1.957`
- `news_risk_high->index_1h` score `0.4683` n `139` status `ready` deltaP `8.9013` edge `0.0087` maxDD `-0.3214`
- `news_risk_high->index_4h` score `-0.1879` n `139` status `ready` deltaP `6.5056` edge `0.0263` maxDD `-1.493`
- `news_risk_high->metal_1h` score `-0.528` n `139` status `ready` deltaP `1.3408` edge `0.01` maxDD `-0.7016`
- `news_risk_high->crypto_major_1h` score `-0.5537` n `139` status `ready` deltaP `0.5966` edge `0.0533` maxDD `-7.2607`
- `news_risk_high->fx_1h` score `-1.1889` n `139` status `ready` deltaP `-9.2675` edge `-0.0026` maxDD `-1.0436`
- `news_risk_high->fx_4h` score `-1.2492` n `139` status `ready` deltaP `9.5247` edge `-0.0023` maxDD `-3.0414`
- `news_risk_high->metal_4h` score `-1.4706` n `139` status `ready` deltaP `-9.7659` edge `0.026` maxDD `-3.6214`
- `news_risk_high->crypto_major_4h` score `-1.8545` n `139` status `ready` deltaP `-5.3957` edge `0.0697` maxDD `-13.719`
- `news_risk_high->commodity_1h` score `-2.0474` n `139` status `ready` deltaP `-12.1656` edge `-0.0139` maxDD `-3.3986`
- `news_risk_high->commodity_4h` score `-3.7958` n `139` status `ready` deltaP `-11.0173` edge `-0.001` maxDD `-8.6825`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
