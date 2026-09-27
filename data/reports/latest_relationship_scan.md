# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-27T18:22:29.126334+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `72`

- Symbol pattern count: `8118`

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

- `news_risk_high->unknown_24h` score `733.8012` n `136` status `ready` deltaP `1.2153` edge `61.142` maxDD `0.0`
- `news_risk_high->index_24h` score `1.1572` n `136` status `ready` deltaP `17.5143` edge `0.0492` maxDD `-2.2287`
- `news_risk_high->metal_24h` score `0.6096` n `136` status `ready` deltaP `16.9935` edge `0.123` maxDD `-6.8392`
- `news_risk_high->crypto_alt_24h` score `0.2826` n `136` status `ready` deltaP `14.6446` edge `0.3211` maxDD `-29.2814`
- `news_risk_high->index_1h` score `-0.0995` n `139` status `ready` deltaP `2.6139` edge `0.0033` maxDD `-0.3214`
- `news_risk_high->crypto_alt_1h` score `-0.1912` n `139` status `ready` deltaP `3.8739` edge `0.0493` maxDD `-4.2849`
- `news_risk_high->equity_4h` score `-0.2163` n `139` status `ready` deltaP `15.4358` edge `0.04` maxDD `-9.2079`
- `news_risk_high->equity_1h` score `-0.3468` n `139` status `ready` deltaP `2.1648` edge `0.0228` maxDD `-1.957`
- `news_risk_high->metal_1h` score `-0.7401` n `139` status `ready` deltaP `-0.3059` edge `0.0033` maxDD `-0.7016`
- `news_risk_high->fx_1h` score `-1.0971` n `139` status `ready` deltaP `-7.6208` edge `-0.0018` maxDD `-1.0436`
- `news_risk_high->fx_4h` score `-1.0974` n `139` status `ready` deltaP `11.9637` edge `0.0009` maxDD `-3.0414`
- `news_risk_high->crypto_major_1h` score `-1.2021` n `139` status `ready` deltaP `-4.4932` edge `0.0041` maxDD `-7.2607`
- `news_risk_high->index_4h` score `-1.2398` n `139` status `ready` deltaP `-3.403` edge `0.0047` maxDD `-1.493`
- `news_risk_high->crypto_alt_4h` score `-1.8273` n `139` status `ready` deltaP `1.3336` edge `0.1048` maxDD `-15.9436`
- `news_risk_high->commodity_1h` score `-1.848` n `139` status `ready` deltaP `-9.0219` edge `-0.0093` maxDD `-3.3986`
- `news_risk_high->equity_24h` score `-1.8495` n `136` status `ready` deltaP `11.8975` edge `0.0222` maxDD `-11.1179`
- `news_risk_high->metal_4h` score `-1.9175` n `139` status `ready` deltaP `-14.3391` edge `-0.0008` maxDD `-3.6214`
- `news_risk_high->commodity_4h` score `-3.4132` n `139` status `ready` deltaP `-8.4258` edge `0.0136` maxDD `-8.6825`
- `news_risk_high->crypto_major_4h` score `-3.6823` n `139` status `ready` deltaP `-13.1701` edge `-0.1128` maxDD `-13.719`
- `news_risk_high->commodity_24h` score `-4.2698` n `136` status `ready` deltaP `-2.9514` edge `-0.1727` maxDD `-18.7356`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
