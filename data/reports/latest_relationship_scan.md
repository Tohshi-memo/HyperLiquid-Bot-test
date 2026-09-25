# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-25T10:22:31.941268+00:00`
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

- `market_context_high->unknown_1h` score `84.745` n `47` status `ready` deltaP `8.1698` edge `7.0147` maxDD `-0.2334`
- `market_context_high->crypto_major_24h` score `50.2429` n `47` status `ready` deltaP `30.9434` edge `4.0199` maxDD `-2.4756`
- `market_context_high->crypto_alt_24h` score `32.074` n `47` status `ready` deltaP `24.782` edge `2.5456` maxDD `-2.7051`
- `market_context_high->equity_24h` score `25.5591` n `47` status `ready` deltaP `34.5892` edge `1.9349` maxDD `-2.1786`
- `news_risk_high->unknown_1h` score `11.3349` n `111` status `ready` deltaP `3.4161` edge `0.9357` maxDD `-0.4452`
- `market_context_high->index_24h` score `7.8849` n `47` status `ready` deltaP `35.6309` edge `0.4325` maxDD `-0.3705`
- `market_context_high->metal_24h` score `4.5623` n `47` status `ready` deltaP `38.7042` edge `0.146` maxDD `-0.2401`
- `news_risk_high->commodity_24h` score `3.7026` n `47` status `ready` deltaP `30.5962` edge `0.1394` maxDD `-1.7857`
- `market_context_high->index_4h` score `2.686` n `47` status `ready` deltaP `31.13` edge `0.0317` maxDD `-0.2323`
- `market_context_high->equity_4h` score `2.1294` n `47` status `ready` deltaP `14.8579` edge `0.1202` maxDD `-1.3444`
- `market_context_high->crypto_alt_4h` score `0.9684` n `47` status `ready` deltaP `9.5355` edge `0.0839` maxDD `-3.3417`
- `market_context_high->index_1h` score `0.9152` n `47` status `ready` deltaP `14.161` edge `0.0097` maxDD `-0.2275`
- `market_context_high->equity_1h` score `0.9067` n `47` status `ready` deltaP `11.3167` edge `0.0404` maxDD `-1.5564`
- `news_risk_high->crypto_alt_1h` score `0.7002` n `111` status `ready` deltaP `7.8317` edge `0.0972` maxDD `-4.2849`
- `market_context_high->fx_1h` score `0.459` n `47` status `ready` deltaP `9.9598` edge `0.0075` maxDD `-0.1854`
- `news_risk_high->index_1h` score `0.0291` n `111` status `ready` deltaP `4.0595` edge `0.0065` maxDD `-0.3863`
- `market_context_high->metal_1h` score `0.0211` n `47` status `ready` deltaP `3.4272` edge `0.0115` maxDD `-0.1976`
- `news_risk_high->metal_1h` score `0.01` n `111` status `ready` deltaP `8.5451` edge `0.0068` maxDD `-0.7016`
- `market_context_high->crypto_major_1h` score `-0.0619` n `47` status `ready` deltaP `3.2552` edge `0.0549` maxDD `-4.5405`
- `news_risk_high->equity_1h` score `-0.0658` n `111` status `ready` deltaP `2.1161` edge `0.0282` maxDD `-2.0595`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
