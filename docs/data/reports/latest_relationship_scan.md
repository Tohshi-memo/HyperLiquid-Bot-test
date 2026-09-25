# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-25T13:22:35.759987+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `112`

- Symbol pattern count: `11258`

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

- `market_context_high->unknown_1h` score `83.5882` n `47` status `ready` deltaP `8.1698` edge `6.9183` maxDD `-0.2334`
- `market_context_high->crypto_major_24h` score `50.3353` n `47` status `ready` deltaP `30.9434` edge `4.0276` maxDD `-2.4756`
- `market_context_high->crypto_alt_24h` score `31.7476` n `47` status `ready` deltaP `24.782` edge `2.5184` maxDD `-2.7051`
- `market_context_high->equity_24h` score `25.2363` n `47` status `ready` deltaP `34.5892` edge `1.908` maxDD `-2.1786`
- `news_risk_high->unknown_1h` score `10.1781` n `111` status `ready` deltaP `3.4161` edge `0.8393` maxDD `-0.4452`
- `market_context_high->index_24h` score `7.7633` n `47` status `ready` deltaP `34.9364` edge `0.427` maxDD `-0.3705`
- `market_context_high->metal_24h` score `4.3045` n `47` status `ready` deltaP `36.6209` edge `0.1384` maxDD `-0.2401`
- `news_risk_high->commodity_24h` score `3.0198` n `57` status `ready` deltaP `26.8001` edge `0.1078` maxDD `-1.7857`
- `market_context_high->index_4h` score `2.545` n `47` status `ready` deltaP `29.758` edge `0.0291` maxDD `-0.2323`
- `market_context_high->equity_4h` score `2.0426` n `47` status `ready` deltaP `14.553` edge `0.115` maxDD `-1.3444`
- `market_context_high->crypto_alt_4h` score `0.9084` n `47` status `ready` deltaP `9.5355` edge `0.0789` maxDD `-3.3417`
- `market_context_high->index_1h` score `0.8732` n `47` status `ready` deltaP `13.7119` edge `0.0092` maxDD `-0.2275`
- `market_context_high->equity_1h` score `0.8551` n `47` status `ready` deltaP `11.0173` edge `0.0381` maxDD `-1.5564`
- `news_risk_high->crypto_alt_1h` score `0.705` n `111` status `ready` deltaP `7.9814` edge `0.0966` maxDD `-4.2849`
- `market_context_high->fx_1h` score `0.447` n `47` status `ready` deltaP `9.8101` edge `0.0075` maxDD `-0.1854`
- `news_risk_high->index_1h` score `0.0019` n `111` status `ready` deltaP `3.6104` edge `0.006` maxDD `-0.3863`
- `market_context_high->metal_1h` score `-0.0061` n `47` status `ready` deltaP `3.1278` edge `0.01` maxDD `-0.1976`
- `market_context_high->crypto_major_1h` score `-0.0091` n `47` status `ready` deltaP `3.4049` edge `0.0583` maxDD `-4.5405`
- `news_risk_high->metal_1h` score `-0.032` n `111` status `ready` deltaP `8.2457` edge `0.0053` maxDD `-0.7016`
- `news_risk_high->equity_1h` score `-0.0993` n `111` status `ready` deltaP `1.8167` edge `0.0259` maxDD `-2.0595`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
