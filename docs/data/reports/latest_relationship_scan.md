# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-29T14:52:31.371065+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `72`

- Symbol pattern count: `7430`

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

- `news_risk_high->unknown_24h` score `2584.2132` n `139` status `ready` deltaP `1.2153` edge `215.343` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `16.7943` n `139` status `ready` deltaP `32.7613` edge `1.5763` maxDD `-29.2814`
- `news_risk_high->equity_24h` score `10.3597` n `139` status `ready` deltaP `35.1368` edge `0.8847` maxDD `-11.1179`
- `news_risk_high->crypto_major_24h` score `8.4231` n `139` status `ready` deltaP `25.241` edge `0.9771` maxDD `-26.1424`
- `news_risk_high->index_24h` score `4.2805` n `139` status `ready` deltaP `39.3798` edge `0.1637` maxDD `-2.2287`
- `news_risk_high->metal_24h` score `3.8369` n `139` status `ready` deltaP `31.7596` edge `0.2935` maxDD `-6.8392`
- `news_risk_high->equity_4h` score `2.712` n `142` status `ready` deltaP `27.9801` edge `0.2004` maxDD `-9.2079`
- `news_risk_high->crypto_alt_4h` score `1.0475` n `142` status `ready` deltaP `8.6332` edge `0.2957` maxDD `-15.9436`
- `news_risk_high->crypto_alt_1h` score `0.7477` n `142` status `ready` deltaP `6.8209` edge `0.1079` maxDD `-4.2849`
- `news_risk_high->equity_1h` score `0.5799` n `142` status `ready` deltaP `7.4028` edge `0.0651` maxDD `-1.957`
- `news_risk_high->index_1h` score `0.4658` n `142` status `ready` deltaP `8.6004` edge `0.0105` maxDD `-0.3214`
- `news_risk_high->index_4h` score `0.0223` n `142` status `ready` deltaP `8.6826` edge `0.0293` maxDD `-1.493`
- `news_risk_high->crypto_major_1h` score `-0.3782` n `142` status `ready` deltaP `2.2898` edge `0.0645` maxDD `-7.2607`
- `news_risk_high->metal_1h` score `-0.5517` n `142` status `ready` deltaP `0.7147` edge `0.0122` maxDD `-0.7016`
- `news_risk_high->fx_4h` score `-1.3024` n `142` status `ready` deltaP `9.1313` edge `-0.0065` maxDD `-3.0414`
- `news_risk_high->metal_4h` score `-1.3587` n `142` status `ready` deltaP `-8.1544` edge `0.0296` maxDD `-3.6214`
- `news_risk_high->crypto_major_4h` score `-1.7818` n `142` status `ready` deltaP `-4.9876` edge `0.0763` maxDD `-13.719`
- `news_risk_high->fx_1h` score `-1.8325` n `142` status `ready` deltaP `-9.1444` edge `-0.0037` maxDD `-1.0436`
- `news_risk_high->commodity_1h` score `-1.9227` n `142` status `ready` deltaP `-10.2028` edge `-0.011` maxDD `-3.3986`
- `news_risk_high->commodity_4h` score `-2.3734` n `142` status `ready` deltaP `-9.9171` edge `0.0037` maxDD `-8.6825`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
