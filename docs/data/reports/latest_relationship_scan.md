# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-25T10:37:32.456718+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `112`

- Symbol pattern count: `11286`

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

- `market_context_high->unknown_1h` score `84.7474` n `47` status `ready` deltaP `8.1698` edge `7.0149` maxDD `-0.2334`
- `market_context_high->crypto_major_24h` score `50.2369` n `47` status `ready` deltaP `30.9434` edge `4.0194` maxDD `-2.4756`
- `market_context_high->crypto_alt_24h` score `32.0212` n `47` status `ready` deltaP `24.782` edge `2.5412` maxDD `-2.7051`
- `market_context_high->equity_24h` score `25.5219` n `47` status `ready` deltaP `34.5892` edge `1.9318` maxDD `-2.1786`
- `news_risk_high->unknown_1h` score `11.3373` n `111` status `ready` deltaP `3.4161` edge `0.9359` maxDD `-0.4452`
- `market_context_high->index_24h` score `7.8638` n `47` status `ready` deltaP `35.4573` edge `0.4319` maxDD `-0.3705`
- `market_context_high->metal_24h` score `4.5388` n `47` status `ready` deltaP `38.5306` edge `0.1452` maxDD `-0.2401`
- `news_risk_high->commodity_24h` score `3.7062` n `47` status `ready` deltaP `30.5962` edge `0.1397` maxDD `-1.7857`
- `market_context_high->index_4h` score `2.6702` n `47` status `ready` deltaP `30.9776` edge `0.0314` maxDD `-0.2323`
- `market_context_high->equity_4h` score `2.1004` n `47` status `ready` deltaP `14.7055` edge `0.1188` maxDD `-1.3444`
- `market_context_high->crypto_alt_4h` score `0.942` n `47` status `ready` deltaP `9.5355` edge `0.0817` maxDD `-3.3417`
- `market_context_high->index_1h` score `0.9152` n `47` status `ready` deltaP `14.161` edge `0.0097` maxDD `-0.2275`
- `market_context_high->equity_1h` score `0.9031` n `47` status `ready` deltaP `11.3167` edge `0.0401` maxDD `-1.5564`
- `news_risk_high->crypto_alt_1h` score `0.6726` n `111` status `ready` deltaP `7.682` edge `0.0959` maxDD `-4.2849`
- `market_context_high->fx_1h` score `0.459` n `47` status `ready` deltaP `9.9598` edge `0.0075` maxDD `-0.1854`
- `news_risk_high->index_1h` score `0.0291` n `111` status `ready` deltaP `4.0595` edge `0.0065` maxDD `-0.3863`
- `market_context_high->metal_1h` score `0.0204` n `47` status `ready` deltaP `3.4272` edge `0.0114` maxDD `-0.1976`
- `news_risk_high->metal_1h` score `0.0088` n `111` status `ready` deltaP `8.5451` edge `0.0067` maxDD `-0.7016`
- `news_risk_high->equity_1h` score `-0.0681` n `111` status `ready` deltaP `2.1161` edge `0.0279` maxDD `-2.0595`
- `market_context_high->crypto_major_1h` score `-0.0822` n `47` status `ready` deltaP `3.1055` edge `0.0542` maxDD `-4.5405`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
