# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-29T15:52:38.222063+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `72`

- Symbol pattern count: `7160`

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

- `news_risk_high->unknown_24h` score `2584.356` n `139` status `ready` deltaP `1.2153` edge `215.3549` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `16.4519` n `139` status `ready` deltaP `32.0669` edge `1.5524` maxDD `-29.2814`
- `news_risk_high->equity_24h` score `10.1553` n `139` status `ready` deltaP `34.4424` edge `0.8723` maxDD `-11.1179`
- `news_risk_high->crypto_major_24h` score `8.1469` n `139` status `ready` deltaP `24.8938` edge `0.9564` maxDD `-26.1424`
- `news_risk_high->index_24h` score `4.1997` n `139` status `ready` deltaP `38.6853` edge `0.1616` maxDD `-2.2287`
- `news_risk_high->metal_24h` score `3.7822` n `139` status `ready` deltaP `31.586` edge `0.2901` maxDD `-6.8392`
- `news_risk_high->equity_4h` score `2.7542` n `142` status `ready` deltaP `28.1326` edge `0.2029` maxDD `-9.2079`
- `news_risk_high->crypto_alt_4h` score `1.1933` n `142` status `ready` deltaP `9.0906` edge `0.3048` maxDD `-15.9436`
- `news_risk_high->crypto_alt_1h` score `0.8389` n `142` status `ready` deltaP `7.1203` edge `0.1135` maxDD `-4.2849`
- `news_risk_high->equity_1h` score `0.6182` n `142` status `ready` deltaP `7.5525` edge `0.0673` maxDD `-1.957`
- `news_risk_high->index_1h` score `0.4826` n `142` status `ready` deltaP `8.7501` edge `0.0109` maxDD `-0.3214`
- `news_risk_high->index_4h` score `0.0842` n `142` status `ready` deltaP `9.2923` edge `0.0304` maxDD `-1.493`
- `news_risk_high->crypto_major_1h` score `-0.3315` n `142` status `ready` deltaP `2.4395` edge `0.0695` maxDD `-7.2607`
- `news_risk_high->metal_1h` score `-0.5481` n `142` status `ready` deltaP `0.7147` edge `0.0125` maxDD `-0.7016`
- `news_risk_high->fx_4h` score `-1.2858` n `142` status `ready` deltaP `9.4362` edge `-0.0064` maxDD `-3.0414`
- `news_risk_high->metal_4h` score `-1.3028` n `142` status `ready` deltaP `-7.5446` edge `0.0327` maxDD `-3.6214`
- `news_risk_high->crypto_major_4h` score `-1.6861` n `142` status `ready` deltaP `-4.3778` edge `0.0845` maxDD `-13.719`
- `news_risk_high->fx_1h` score `-1.8205` n `142` status `ready` deltaP `-8.9947` edge `-0.0037` maxDD `-1.0436`
- `news_risk_high->commodity_1h` score `-1.9134` n `142` status `ready` deltaP `-10.0531` edge `-0.0108` maxDD `-3.3986`
- `news_risk_high->commodity_4h` score `-2.3536` n `142` status `ready` deltaP `-9.6122` edge `0.0042` maxDD `-8.6825`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
