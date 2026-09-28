# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-28T22:31:26.181852+00:00`
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

- `news_risk_high->unknown_24h` score `2666.9064` n `139` status `ready` deltaP `1.2153` edge `222.2341` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `11.1167` n `139` status `ready` deltaP `27.2058` edge `1.1402` maxDD `-29.2814`
- `news_risk_high->equity_24h` score `7.1946` n `139` status `ready` deltaP `26.8035` edge `0.6765` maxDD `-11.1179`
- `news_risk_high->crypto_major_24h` score `6.5953` n `139` status `ready` deltaP `22.4632` edge `0.8433` maxDD `-26.1424`
- `news_risk_high->index_24h` score `3.5101` n `139` status `ready` deltaP `32.4353` edge `0.1458` maxDD `-2.2287`
- `news_risk_high->metal_24h` score `2.7905` n `139` status `ready` deltaP `24.8152` edge `0.2526` maxDD `-6.8392`
- `news_risk_high->equity_4h` score `2.6105` n `139` status `ready` deltaP `27.3261` edge `0.1963` maxDD `-9.2079`
- `news_risk_high->crypto_alt_4h` score `1.0805` n `139` status `ready` deltaP `8.9555` edge `0.2963` maxDD `-15.9436`
- `news_risk_high->crypto_alt_1h` score `0.7598` n `139` status `ready` deltaP `7.4667` edge `0.1046` maxDD `-4.2849`
- `news_risk_high->equity_1h` score `0.5859` n `139` status `ready` deltaP `8.0031` edge `0.0616` maxDD `-1.957`
- `news_risk_high->index_1h` score `0.4707` n `139` status `ready` deltaP `8.9013` edge `0.0089` maxDD `-0.3214`
- `news_risk_high->index_4h` score `-0.0747` n `139` status `ready` deltaP `7.7251` edge `0.0276` maxDD `-1.493`
- `news_risk_high->metal_1h` score `-0.4669` n `139` status `ready` deltaP `1.9396` edge `0.0111` maxDD `-0.7016`
- `news_risk_high->crypto_major_1h` score `-0.4983` n `139` status `ready` deltaP `1.0457` edge `0.0574` maxDD `-7.2607`
- `news_risk_high->fx_1h` score `-1.2123` n `139` status `ready` deltaP `-9.7166` edge `-0.0026` maxDD `-1.0436`
- `news_risk_high->fx_4h` score `-1.3226` n `139` status `ready` deltaP `8.4576` edge `-0.0046` maxDD `-3.0414`
- `news_risk_high->metal_4h` score `-1.3894` n `139` status `ready` deltaP `-8.6988` edge `0.0293` maxDD `-3.6214`
- `news_risk_high->crypto_major_4h` score `-1.8123` n `139` status `ready` deltaP `-5.2433` edge `0.0741` maxDD `-13.719`
- `news_risk_high->commodity_1h` score `-2.0653` n `139` status `ready` deltaP `-12.465` edge `-0.0142` maxDD `-3.3986`
- `news_risk_high->commodity_4h` score `-3.8042` n `139` status `ready` deltaP `-11.0173` edge `-0.0017` maxDD `-8.6825`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
