# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-25T12:52:35.241447+00:00`
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

- `market_context_high->unknown_1h` score `84.6178` n `47` status `ready` deltaP `8.1698` edge `7.0041` maxDD `-0.2334`
- `market_context_high->crypto_major_24h` score `50.2873` n `47` status `ready` deltaP `30.9434` edge `4.0236` maxDD `-2.4756`
- `market_context_high->crypto_alt_24h` score `31.7788` n `47` status `ready` deltaP `24.782` edge `2.521` maxDD `-2.7051`
- `market_context_high->equity_24h` score `25.2795` n `47` status `ready` deltaP `34.5892` edge `1.9116` maxDD `-2.1786`
- `news_risk_high->unknown_1h` score `11.2077` n `111` status `ready` deltaP `3.4161` edge `0.9251` maxDD `-0.4452`
- `market_context_high->index_24h` score `7.7717` n `47` status `ready` deltaP `34.9364` edge `0.4277` maxDD `-0.3705`
- `market_context_high->metal_24h` score `4.3382` n `47` status `ready` deltaP `36.9681` edge `0.1389` maxDD `-0.2401`
- `news_risk_high->commodity_24h` score `3.0877` n `55` status `ready` deltaP `26.7645` edge `0.1137` maxDD `-1.7857`
- `market_context_high->index_4h` score `2.5462` n `47` status `ready` deltaP `29.758` edge `0.0292` maxDD `-0.2323`
- `market_context_high->equity_4h` score `2.0074` n `47` status `ready` deltaP `14.2481` edge `0.1141` maxDD `-1.3444`
- `market_context_high->crypto_alt_4h` score `0.8964` n `47` status `ready` deltaP `9.5355` edge `0.0779` maxDD `-3.3417`
- `market_context_high->index_1h` score `0.8744` n `47` status `ready` deltaP `13.7119` edge `0.0093` maxDD `-0.2275`
- `market_context_high->equity_1h` score `0.8623` n `47` status `ready` deltaP `11.0173` edge `0.0387` maxDD `-1.5564`
- `news_risk_high->crypto_alt_1h` score `0.687` n `111` status `ready` deltaP `7.9814` edge `0.0951` maxDD `-4.2849`
- `market_context_high->fx_1h` score `0.4326` n `47` status `ready` deltaP `9.6604` edge `0.0073` maxDD `-0.1854`
- `news_risk_high->index_1h` score `0.0027` n `111` status `ready` deltaP `3.6104` edge `0.0061` maxDD `-0.3863`
- `market_context_high->metal_1h` score `-0.0053` n `47` status `ready` deltaP `3.1278` edge `0.0101` maxDD `-0.1976`
- `news_risk_high->metal_1h` score `-0.0308` n `111` status `ready` deltaP `8.2457` edge `0.0054` maxDD `-0.7016`
- `news_risk_high->equity_1h` score `-0.0946` n `111` status `ready` deltaP `1.8167` edge `0.0265` maxDD `-2.0595`
- `market_context_high->crypto_major_1h` score `-0.0955` n `47` status `ready` deltaP `3.2552` edge `0.0521` maxDD `-4.5405`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
