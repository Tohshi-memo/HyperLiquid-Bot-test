# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-28T07:37:28.143187+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `72`

- Symbol pattern count: `7886`

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

- `news_risk_high->unknown_24h` score `692.8872` n `139` status `ready` deltaP `1.2153` edge `57.7325` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `4.1697` n `139` status `ready` deltaP `17.4835` edge `0.6261` maxDD `-29.2814`
- `news_risk_high->index_24h` score `2.108` n `139` status `ready` deltaP `22.0186` edge `0.0984` maxDD `-2.2287`
- `news_risk_high->equity_24h` score `1.5349` n `139` status `ready` deltaP `16.3868` edge `0.2743` maxDD `-11.1179`
- `news_risk_high->crypto_major_24h` score `1.491` n `139` status `ready` deltaP `12.9146` edge `0.4816` maxDD `-26.1424`
- `news_risk_high->equity_4h` score `1.1785` n `139` status `ready` deltaP `20.4663` edge `0.1227` maxDD `-9.2079`
- `news_risk_high->metal_24h` score `1.1646` n `139` status `ready` deltaP `20.3013` edge `0.1472` maxDD `-6.8392`
- `news_risk_high->crypto_alt_1h` score `0.3904` n `139` status `ready` deltaP `5.9697` edge `0.0838` maxDD `-4.2849`
- `news_risk_high->index_1h` score `0.188` n `139` status `ready` deltaP `5.7576` edge `0.0063` maxDD `-0.3214`
- `news_risk_high->equity_1h` score `0.1771` n `139` status `ready` deltaP `5.3085` edge `0.0455` maxDD `-1.957`
- `news_risk_high->crypto_alt_4h` score `0.0854` n `139` status `ready` deltaP `5.9067` edge `0.2337` maxDD `-15.9436`
- `news_risk_high->metal_1h` score `-0.5639` n `139` status `ready` deltaP `1.0414` edge `0.009` maxDD `-0.7016`
- `news_risk_high->index_4h` score `-0.647` n `139` status `ready` deltaP `2.2373` edge `0.0165` maxDD `-1.493`
- `news_risk_high->crypto_major_1h` score `-0.8366` n `139` status `ready` deltaP `-1.3495` edge `0.03` maxDD `-7.2607`
- `news_risk_high->fx_1h` score `-1.1586` n `139` status `ready` deltaP `-8.6687` edge `-0.0027` maxDD `-1.0436`
- `news_risk_high->fx_4h` score `-1.2626` n `139` status `ready` deltaP `9.3722` edge `-0.003` maxDD `-3.0414`
- `news_risk_high->metal_4h` score `-1.6283` n `139` status `ready` deltaP `-11.7476` edge `0.019` maxDD `-3.6214`
- `news_risk_high->commodity_1h` score `-1.9625` n `139` status `ready` deltaP `-10.8183` edge `-0.012` maxDD `-3.3986`
- `news_risk_high->crypto_major_4h` score `-2.4622` n `139` status `ready` deltaP `-8.292` edge `0.0111` maxDD `-13.719`
- `news_risk_high->commodity_4h` score `-3.6854` n `139` status `ready` deltaP `-10.1027` edge `0.0021` maxDD `-8.6825`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
