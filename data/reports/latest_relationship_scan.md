# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-25T09:52:32.627073+00:00`
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

- `market_context_high->unknown_1h` score `84.7558` n `47` status `ready` deltaP `8.1698` edge `7.0156` maxDD `-0.2334`
- `market_context_high->crypto_major_24h` score `50.2273` n `47` status `ready` deltaP `30.9434` edge `4.0186` maxDD `-2.4756`
- `market_context_high->crypto_alt_24h` score `32.1616` n `47` status `ready` deltaP `24.782` edge `2.5529` maxDD `-2.7051`
- `market_context_high->equity_24h` score `25.6323` n `47` status `ready` deltaP `34.5892` edge `1.941` maxDD `-2.1786`
- `news_risk_high->unknown_1h` score `11.3457` n `111` status `ready` deltaP `3.4161` edge `0.9366` maxDD `-0.4452`
- `market_context_high->index_24h` score `7.912` n `47` status `ready` deltaP `35.8045` edge `0.4336` maxDD `-0.3705`
- `market_context_high->metal_24h` score `4.6105` n `47` status `ready` deltaP `39.0514` edge `0.1477` maxDD `-0.2401`
- `news_risk_high->commodity_24h` score `3.6828` n `47` status `ready` deltaP `30.4226` edge `0.1389` maxDD `-1.7857`
- `market_context_high->index_4h` score `2.7175` n `47` status `ready` deltaP `31.4349` edge `0.0323` maxDD `-0.2323`
- `market_context_high->equity_4h` score `2.1874` n `47` status `ready` deltaP `15.1628` edge `0.123` maxDD `-1.3444`
- `market_context_high->crypto_alt_4h` score `0.9984` n `47` status `ready` deltaP `9.5355` edge `0.0864` maxDD `-3.3417`
- `market_context_high->equity_1h` score `0.9079` n `47` status `ready` deltaP `11.3167` edge `0.0405` maxDD `-1.5564`
- `market_context_high->index_1h` score `0.9032` n `47` status `ready` deltaP `14.0113` edge `0.0097` maxDD `-0.2275`
- `news_risk_high->crypto_alt_1h` score `0.741` n `111` status `ready` deltaP `7.9814` edge `0.0996` maxDD `-4.2849`
- `market_context_high->fx_1h` score `0.4841` n `47` status `ready` deltaP `10.2592` edge `0.0076` maxDD `-0.1854`
- `news_risk_high->index_1h` score `0.0213` n `111` status `ready` deltaP `3.9098` edge `0.0065` maxDD `-0.3863`
- `market_context_high->metal_1h` score `0.0211` n `47` status `ready` deltaP `3.4272` edge `0.0115` maxDD `-0.1976`
- `news_risk_high->metal_1h` score `0.01` n `111` status `ready` deltaP `8.5451` edge `0.0068` maxDD `-0.7016`
- `market_context_high->crypto_major_1h` score `-0.0535` n `47` status `ready` deltaP `3.2552` edge `0.0556` maxDD `-4.5405`
- `news_risk_high->equity_1h` score `-0.065` n `111` status `ready` deltaP `2.1161` edge `0.0283` maxDD `-2.0595`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
