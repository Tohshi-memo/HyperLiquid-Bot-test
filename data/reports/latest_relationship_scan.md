# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-25T11:07:31.449965+00:00`
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

- `market_context_high->unknown_1h` score `84.7222` n `47` status `ready` deltaP `8.1698` edge `7.0128` maxDD `-0.2334`
- `market_context_high->crypto_major_24h` score `50.2441` n `47` status `ready` deltaP `30.9434` edge `4.02` maxDD `-2.4756`
- `market_context_high->crypto_alt_24h` score `31.9576` n `47` status `ready` deltaP `24.782` edge `2.5359` maxDD `-2.7051`
- `market_context_high->equity_24h` score `25.4607` n `47` status `ready` deltaP `34.5892` edge `1.9267` maxDD `-2.1786`
- `news_risk_high->unknown_1h` score `11.3121` n `111` status `ready` deltaP `3.4161` edge `0.9338` maxDD `-0.4452`
- `market_context_high->index_24h` score `7.8228` n `47` status `ready` deltaP `35.1101` edge `0.4308` maxDD `-0.3705`
- `market_context_high->metal_24h` score `4.4883` n `47` status `ready` deltaP `38.1834` edge `0.1433` maxDD `-0.2401`
- `news_risk_high->commodity_24h` score `3.6575` n `49` status `ready` deltaP `30.8568` edge `0.1339` maxDD `-1.7857`
- `market_context_high->index_4h` score `2.6386` n `47` status `ready` deltaP `30.6727` edge `0.0308` maxDD `-0.2323`
- `market_context_high->equity_4h` score `2.0532` n `47` status `ready` deltaP `14.4006` edge `0.1169` maxDD `-1.3444`
- `market_context_high->crypto_alt_4h` score `0.9084` n `47` status `ready` deltaP `9.5355` edge `0.0789` maxDD `-3.3417`
- `market_context_high->index_1h` score `0.902` n `47` status `ready` deltaP `14.0113` edge `0.0096` maxDD `-0.2275`
- `market_context_high->equity_1h` score `0.8659` n `47` status `ready` deltaP `11.0173` edge `0.039` maxDD `-1.5564`
- `news_risk_high->crypto_alt_1h` score `0.6294` n `111` status `ready` deltaP `7.5323` edge `0.0933` maxDD `-4.2849`
- `market_context_high->fx_1h` score `0.4578` n `47` status `ready` deltaP `9.9598` edge `0.0074` maxDD `-0.1854`
- `news_risk_high->index_1h` score `0.0206` n `111` status `ready` deltaP `3.9098` edge `0.0064` maxDD `-0.3863`
- `market_context_high->metal_1h` score `0.0079` n `47` status `ready` deltaP `3.2775` edge `0.0108` maxDD `-0.1976`
- `news_risk_high->metal_1h` score `-0.0104` n `111` status `ready` deltaP `8.3954` edge `0.0061` maxDD `-0.7016`
- `news_risk_high->equity_1h` score `-0.0923` n `111` status `ready` deltaP `1.8167` edge `0.0268` maxDD `-2.0595`
- `market_context_high->crypto_major_1h` score `-0.1326` n `47` status `ready` deltaP `2.9558` edge `0.051` maxDD `-4.5405`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
