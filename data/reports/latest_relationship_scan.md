# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-28T09:07:31.046015+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `72`

- Symbol pattern count: `7878`

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

- `news_risk_high->unknown_24h` score `832.734` n `139` status `ready` deltaP `1.2153` edge `69.3864` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `5.057` n `139` status `ready` deltaP `18.5252` edge `0.6931` maxDD `-29.2814`
- `news_risk_high->crypto_major_24h` score `2.3339` n `139` status `ready` deltaP `13.9563` edge `0.5449` maxDD `-26.1424`
- `news_risk_high->index_24h` score `2.2489` n `139` status `ready` deltaP `23.0603` edge `0.1032` maxDD `-2.2287`
- `news_risk_high->equity_24h` score `2.0358` n `139` status `ready` deltaP `17.4285` edge `0.3091` maxDD `-11.1179`
- `news_risk_high->equity_4h` score `1.4125` n `139` status `ready` deltaP `21.381` edge `0.1361` maxDD `-9.2079`
- `news_risk_high->metal_24h` score `1.2558` n `139` status `ready` deltaP `20.3013` edge `0.1548` maxDD `-6.8392`
- `news_risk_high->crypto_alt_1h` score `0.5847` n `139` status `ready` deltaP `6.7182` edge `0.095` maxDD `-4.2849`
- `news_risk_high->crypto_alt_4h` score `0.563` n `139` status `ready` deltaP `6.8214` edge `0.2674` maxDD `-15.9436`
- `news_risk_high->equity_1h` score `0.309` n `139` status `ready` deltaP `6.2067` edge `0.0505` maxDD `-1.957`
- `news_risk_high->index_1h` score `0.2647` n `139` status `ready` deltaP `6.6558` edge `0.0067` maxDD `-0.3214`
- `news_risk_high->metal_1h` score `-0.546` n `139` status `ready` deltaP `1.1911` edge `0.0095` maxDD `-0.7016`
- `news_risk_high->index_4h` score `-0.5582` n `139` status `ready` deltaP `3.1519` edge `0.0178` maxDD `-1.493`
- `news_risk_high->crypto_major_1h` score `-0.715` n `139` status `ready` deltaP `-0.7507` edge `0.0416` maxDD `-7.2607`
- `news_risk_high->fx_1h` score `-1.1477` n `139` status `ready` deltaP `-8.519` edge `-0.0023` maxDD `-1.0436`
- `news_risk_high->fx_4h` score `-1.2262` n `139` status `ready` deltaP `9.982` edge `-0.0024` maxDD `-3.0414`
- `news_risk_high->metal_4h` score `-1.5495` n `139` status `ready` deltaP `-10.833` edge `0.023` maxDD `-3.6214`
- `news_risk_high->commodity_1h` score `-1.9867` n `139` status `ready` deltaP `-11.1177` edge `-0.0131` maxDD `-3.3986`
- `news_risk_high->crypto_major_4h` score `-2.2111` n `139` status `ready` deltaP `-7.3774` edge `0.0372` maxDD `-13.719`
- `news_risk_high->commodity_4h` score `-3.7958` n `139` status `ready` deltaP `-11.0173` edge `-0.001` maxDD `-8.6825`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
