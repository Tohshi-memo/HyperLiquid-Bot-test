# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-29T03:37:28.590507+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `72`

- Symbol pattern count: `7190`

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

- `news_risk_high->unknown_24h` score `2626.9308` n `139` status `ready` deltaP `1.2153` edge `218.9028` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `14.1928` n `139` status `ready` deltaP `30.678` edge `1.3734` maxDD `-29.2814`
- `news_risk_high->equity_24h` score `8.7528` n `139` status `ready` deltaP `30.2757` edge `0.7832` maxDD `-11.1179`
- `news_risk_high->crypto_major_24h` score `8.1583` n `139` status `ready` deltaP `25.9355` edge `0.9504` maxDD `-26.1424`
- `news_risk_high->index_24h` score `3.8011` n `139` status `ready` deltaP `34.6923` edge `0.155` maxDD `-2.2287`
- `news_risk_high->metal_24h` score `3.4012` n `139` status `ready` deltaP `28.1138` edge `0.2815` maxDD `-6.8392`
- `news_risk_high->equity_4h` score `2.4807` n `139` status `ready` deltaP `27.1736` edge `0.1865` maxDD `-9.2079`
- `news_risk_high->crypto_alt_4h` score `1.1717` n `139` status `ready` deltaP `8.9555` edge `0.3039` maxDD `-15.9436`
- `news_risk_high->crypto_alt_1h` score `0.8234` n `139` status `ready` deltaP `7.6164` edge `0.1089` maxDD `-4.2849`
- `news_risk_high->equity_1h` score `0.641` n `139` status `ready` deltaP `8.4522` edge `0.0632` maxDD `-1.957`
- `news_risk_high->index_1h` score `0.4755` n `139` status `ready` deltaP `8.9013` edge `0.0093` maxDD `-0.3214`
- `news_risk_high->index_4h` score `-0.1257` n `139` status `ready` deltaP `7.2678` edge `0.0264` maxDD `-1.493`
- `news_risk_high->crypto_major_1h` score `-0.5443` n `139` status `ready` deltaP `0.5966` edge `0.0545` maxDD `-7.2607`
- `news_risk_high->metal_1h` score `-0.5867` n `139` status `ready` deltaP `0.5923` edge `0.0101` maxDD `-0.7016`
- `news_risk_high->fx_1h` score `-1.2419` n `139` status `ready` deltaP `-10.1657` edge `-0.0034` maxDD `-1.0436`
- `news_risk_high->fx_4h` score `-1.332` n `139` status `ready` deltaP `8.4576` edge `-0.0058` maxDD `-3.0414`
- `news_risk_high->metal_4h` score `-1.4562` n `139` status `ready` deltaP `-9.3086` edge `0.0248` maxDD `-3.6214`
- `news_risk_high->crypto_major_4h` score `-1.8185` n `139` status `ready` deltaP `-5.2433` edge `0.0733` maxDD `-13.719`
- `news_risk_high->commodity_1h` score `-2.0209` n `139` status `ready` deltaP `-11.7165` edge `-0.0135` maxDD `-3.3986`
- `news_risk_high->commodity_4h` score `-3.7412` n `139` status `ready` deltaP `-10.56` edge `0.0005` maxDD `-8.6825`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
