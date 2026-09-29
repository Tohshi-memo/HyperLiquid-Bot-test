# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-29T07:52:37.723146+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `72`

- Symbol pattern count: `7376`

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

- `news_risk_high->unknown_24h` score `2613.6456` n `139` status `ready` deltaP `1.2153` edge `217.7957` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `16.2178` n `139` status `ready` deltaP `32.9349` edge `1.5271` maxDD `-29.2814`
- `news_risk_high->equity_24h` score `9.9837` n `139` status `ready` deltaP `33.2271` edge `0.8661` maxDD `-11.1179`
- `news_risk_high->crypto_major_24h` score `9.1197` n `139` status `ready` deltaP `27.498` edge `1.0201` maxDD `-26.1424`
- `news_risk_high->index_24h` score `4.1404` n `139` status `ready` deltaP `37.6436` edge `0.1636` maxDD `-2.2287`
- `news_risk_high->metal_24h` score `3.8305` n `139` status `ready` deltaP `31.0652` edge `0.2976` maxDD `-6.8392`
- `news_risk_high->equity_4h` score `2.4931` n `139` status `ready` deltaP `27.4785` edge `0.1855` maxDD `-9.2079`
- `news_risk_high->crypto_alt_4h` score `0.9793` n `139` status `ready` deltaP `8.6506` edge `0.2899` maxDD `-15.9436`
- `news_risk_high->crypto_alt_1h` score `0.8952` n `142` status `ready` deltaP `7.7191` edge `0.1142` maxDD `-4.2849`
- `news_risk_high->equity_1h` score `0.6445` n `142` status `ready` deltaP `8.4507` edge `0.0635` maxDD `-1.957`
- `news_risk_high->index_1h` score `0.4574` n `142` status `ready` deltaP `8.6004` edge `0.0098` maxDD `-0.3214`
- `news_risk_high->index_4h` score `-0.0855` n `139` status `ready` deltaP `7.7251` edge `0.0267` maxDD `-1.493`
- `news_risk_high->crypto_major_1h` score `-0.4468` n `142` status `ready` deltaP `1.2419` edge `0.0627` maxDD `-7.2607`
- `news_risk_high->metal_1h` score `-0.5265` n `142` status `ready` deltaP `1.1638` edge `0.0113` maxDD `-0.7016`
- `news_risk_high->fx_4h` score `-1.3311` n `139` status `ready` deltaP `8.61` edge `-0.0067` maxDD `-3.0414`
- `news_risk_high->metal_4h` score `-1.4403` n `139` status `ready` deltaP `-9.0037` edge `0.0248` maxDD `-3.6214`
- `news_risk_high->fx_1h` score `-1.8912` n `142` status `ready` deltaP `-9.8929` edge `-0.0036` maxDD `-1.0436`
- `news_risk_high->crypto_major_4h` score `-1.8926` n `139` status `ready` deltaP `-5.2433` edge `0.0638` maxDD `-13.719`
- `news_risk_high->commodity_1h` score `-2.0645` n `142` status `ready` deltaP `-12.2986` edge `-0.0152` maxDD `-3.3986`
- `news_risk_high->commodity_4h` score `-4.0205` n `139` status `ready` deltaP `-12.2368` edge `-0.0116` maxDD `-8.6825`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
