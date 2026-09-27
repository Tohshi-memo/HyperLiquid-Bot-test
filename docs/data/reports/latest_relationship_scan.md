# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-27T20:07:30.125232+00:00`
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

- `news_risk_high->unknown_24h` score `719.6136` n `136` status `ready` deltaP `1.2153` edge `59.9597` maxDD `0.0`
- `news_risk_high->index_24h` score `1.2472` n `136` status `ready` deltaP `17.5143` edge `0.0567` maxDD `-2.2287`
- `news_risk_high->crypto_alt_24h` score `0.7338` n `136` status `ready` deltaP `14.6446` edge `0.3587` maxDD `-29.2814`
- `news_risk_high->metal_24h` score `0.7164` n `136` status `ready` deltaP `18.2088` edge `0.1238` maxDD `-6.8392`
- `news_risk_high->index_1h` score `-0.1115` n `139` status `ready` deltaP `2.4642` edge `0.0033` maxDD `-0.3214`
- `news_risk_high->equity_4h` score `-0.1743` n `139` status `ready` deltaP `15.4358` edge `0.0435` maxDD `-9.2079`
- `news_risk_high->crypto_alt_1h` score `-0.1768` n `139` status `ready` deltaP `3.8739` edge `0.0505` maxDD `-4.2849`
- `news_risk_high->equity_1h` score `-0.3444` n `139` status `ready` deltaP `2.1648` edge `0.023` maxDD `-1.957`
- `news_risk_high->metal_1h` score `-0.776` n `139` status `ready` deltaP `-0.755` edge `0.0033` maxDD `-0.7016`
- `news_risk_high->fx_4h` score `-1.0864` n `139` status `ready` deltaP `12.1161` edge `0.0013` maxDD `-3.0414`
- `news_risk_high->fx_1h` score `-1.0893` n `139` status `ready` deltaP `-7.4711` edge `-0.0018` maxDD `-1.0436`
- `news_risk_high->crypto_major_1h` score `-1.2083` n `139` status `ready` deltaP `-4.4932` edge `0.0033` maxDD `-7.2607`
- `news_risk_high->index_4h` score `-1.229` n `139` status `ready` deltaP `-3.403` edge `0.0056` maxDD `-1.493`
- `news_risk_high->equity_24h` score `-1.4751` n `136` status `ready` deltaP `11.8975` edge `0.0534` maxDD `-11.1179`
- `news_risk_high->commodity_1h` score `-1.8395` n `139` status `ready` deltaP `-8.8722` edge `-0.0092` maxDD `-3.3986`
- `news_risk_high->crypto_alt_4h` score `-1.8921` n `139` status `ready` deltaP `1.3336` edge `0.0994` maxDD `-15.9436`
- `news_risk_high->metal_4h` score `-1.9136` n `139` status `ready` deltaP `-14.3391` edge `-0.0003` maxDD `-3.6214`
- `news_risk_high->commodity_4h` score `-3.4748` n `139` status `ready` deltaP `-8.7307` edge `0.0105` maxDD `-8.6825`
- `news_risk_high->crypto_major_4h` score `-3.6885` n `139` status `ready` deltaP `-13.1701` edge `-0.1136` maxDD `-13.719`
- `news_risk_high->crypto_major_24h` score `-3.9772` n `136` status `ready` deltaP `8.2516` edge `0.057` maxDD `-26.1424`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
