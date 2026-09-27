# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-27T19:37:40.243824+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `72`

- Symbol pattern count: `7928`

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

- `news_risk_high->unknown_24h` score `721.8756` n `136` status `ready` deltaP `1.2153` edge `60.1482` maxDD `0.0`
- `news_risk_high->index_24h` score `1.222` n `136` status `ready` deltaP `17.5143` edge `0.0546` maxDD `-2.2287`
- `news_risk_high->metal_24h` score `0.6862` n `136` status `ready` deltaP `17.8616` edge `0.1236` maxDD `-6.8392`
- `news_risk_high->crypto_alt_24h` score `0.615` n `136` status `ready` deltaP `14.6446` edge `0.3488` maxDD `-29.2814`
- `news_risk_high->index_1h` score `-0.1115` n `139` status `ready` deltaP `2.4642` edge `0.0033` maxDD `-0.3214`
- `news_risk_high->crypto_alt_1h` score `-0.1756` n `139` status `ready` deltaP `3.8739` edge `0.0506` maxDD `-4.2849`
- `news_risk_high->equity_4h` score `-0.1899` n `139` status `ready` deltaP `15.4358` edge `0.0422` maxDD `-9.2079`
- `news_risk_high->equity_1h` score `-0.3444` n `139` status `ready` deltaP `2.1648` edge `0.023` maxDD `-1.957`
- `news_risk_high->metal_1h` score `-0.7521` n `139` status `ready` deltaP `-0.4556` edge `0.0033` maxDD `-0.7016`
- `news_risk_high->fx_4h` score `-1.0951` n `139` status `ready` deltaP `11.9637` edge `0.0012` maxDD `-3.0414`
- `news_risk_high->fx_1h` score `-1.0971` n `139` status `ready` deltaP `-7.6208` edge `-0.0018` maxDD `-1.0436`
- `news_risk_high->crypto_major_1h` score `-1.2029` n `139` status `ready` deltaP `-4.4932` edge `0.004` maxDD `-7.2607`
- `news_risk_high->index_4h` score `-1.2338` n `139` status `ready` deltaP `-3.403` edge `0.0052` maxDD `-1.493`
- `news_risk_high->equity_24h` score `-1.5771` n `136` status `ready` deltaP `11.8975` edge `0.0449` maxDD `-11.1179`
- `news_risk_high->commodity_1h` score `-1.8395` n `139` status `ready` deltaP `-8.8722` edge `-0.0092` maxDD `-3.3986`
- `news_risk_high->crypto_alt_4h` score `-1.8717` n `139` status `ready` deltaP `1.3336` edge `0.1011` maxDD `-15.9436`
- `news_risk_high->metal_4h` score `-1.9143` n `139` status `ready` deltaP `-14.3391` edge `-0.0004` maxDD `-3.6214`
- `news_risk_high->commodity_4h` score `-3.4482` n `139` status `ready` deltaP `-8.5783` edge `0.0117` maxDD `-8.6825`
- `news_risk_high->crypto_major_4h` score `-3.6893` n `139` status `ready` deltaP `-13.1701` edge `-0.1137` maxDD `-13.719`
- `news_risk_high->crypto_major_24h` score `-4.1692` n `136` status `ready` deltaP `8.2516` edge `0.041` maxDD `-26.1424`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
