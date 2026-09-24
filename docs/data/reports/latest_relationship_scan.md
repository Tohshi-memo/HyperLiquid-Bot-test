# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-24T13:52:30.285780+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `10068`

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

- `market_context_high->unknown_1h` score `97.4047` n `47` status `ready` deltaP `10.116` edge `8.0567` maxDD `-0.2334`
- `market_context_high->crypto_major_24h` score `42.1429` n `47` status `ready` deltaP `29.7281` edge `3.353` maxDD `-2.4756`
- `market_context_high->crypto_alt_24h` score `28.1529` n `47` status `ready` deltaP `24.6084` edge `2.22` maxDD `-2.7051`
- `market_context_high->equity_24h` score `23.8567` n `47` status `ready` deltaP `27.1239` edge `1.8428` maxDD `-2.1786`
- `market_context_high->index_24h` score `7.8245` n `47` status `ready` deltaP `34.9364` edge `0.4321` maxDD `-0.3705`
- `news_risk_high->crypto_alt_24h` score `7.4452` n `101` status `ready` deltaP `0.9935` edge `1.3151` maxDD `-49.7699`
- `news_risk_high->crypto_major_24h` score `6.5946` n `101` status `ready` deltaP `3.4378` edge `1.7268` maxDD `-63.6743`
- `market_context_high->metal_24h` score `3.5255` n `47` status `ready` deltaP `30.5445` edge `0.114` maxDD `-0.2401`
- `market_context_high->index_4h` score `3.0712` n `47` status `ready` deltaP `34.941` edge `0.0384` maxDD `-0.2323`
- `market_context_high->equity_4h` score `2.6539` n `47` status `ready` deltaP `17.7542` edge `0.1446` maxDD `-1.3444`
- `news_risk_high->crypto_alt_1h` score `2.5623` n `120` status `ready` deltaP `12.8344` edge `0.177` maxDD `-1.5895`
- `news_risk_high->crypto_major_1h` score `2.1243` n `120` status `ready` deltaP `15.0799` edge `0.12` maxDD `-1.8141`
- `news_risk_high->fx_4h` score `1.796` n `112` status `ready` deltaP `25.9146` edge `0.0405` maxDD `-0.421`
- `news_risk_high->fx_24h` score `1.333` n `101` status `ready` deltaP `30.5727` edge `0.1302` maxDD `-1.7159`
- `news_risk_high->commodity_24h` score `1.2226` n `101` status `ready` deltaP `17.0362` edge `0.1062` maxDD `-2.431`
- `news_risk_high->metal_24h` score `1.0529` n `101` status `ready` deltaP `23.4031` edge `0.1238` maxDD `-7.2536`
- `market_context_high->index_1h` score `0.9763` n `47` status `ready` deltaP `14.7598` edge `0.0108` maxDD `-0.2275`
- `market_context_high->equity_1h` score `0.9199` n `47` status `ready` deltaP `11.0173` edge `0.0435` maxDD `-1.5564`
- `news_risk_high->crypto_major_4h` score `0.497` n `112` status `ready` deltaP `12.8049` edge `0.1915` maxDD `-13.719`
- `market_context_high->crypto_alt_4h` score `0.4891` n `47` status `ready` deltaP `6.3343` edge `0.0653` maxDD `-3.3417`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
