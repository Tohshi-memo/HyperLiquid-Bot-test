# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-20T07:00:17.369972+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9230`

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

- `news_risk_high->crypto_major_24h` score `41.0611` n `81` status `ready` deltaP `17.2839` edge `3.4733` maxDD `-10.3413`
- `news_risk_high->crypto_alt_24h` score `37.3646` n `81` status `ready` deltaP `28.6844` edge `3.0604` maxDD `-9.3661`
- `market_context_high->commodity_24h` score `6.9923` n `74` status `ready` deltaP `35.7921` edge `0.3966` maxDD `-0.8682`
- `news_risk_high->crypto_alt_4h` score `6.2638` n `98` status `ready` deltaP `23.4476` edge `0.4866` maxDD `-7.675`
- `news_risk_high->equity_24h` score `6.1528` n `81` status `ready` deltaP `33.2755` edge `0.3045` maxDD `-0.4217`
- `news_risk_high->crypto_major_4h` score `4.8324` n `98` status `ready` deltaP `23.1427` edge `0.3742` maxDD `-8.0625`
- `market_context_high->commodity_4h` score `4.0246` n `77` status `ready` deltaP `35.641` edge `0.1111` maxDD `-0.0659`
- `news_risk_high->crypto_alt_1h` score `3.414` n `98` status `ready` deltaP `18.9234` edge `0.2049` maxDD `-2.058`
- `news_risk_high->crypto_major_1h` score `2.6081` n `98` status `ready` deltaP `21.0192` edge `0.1295` maxDD `-2.8494`
- `market_context_high->unknown_4h` score `2.3858` n `77` status `ready` deltaP `2.5063` edge `0.1971` maxDD `-0.5326`
- `market_context_high->fx_4h` score `2.3664` n `77` status `ready` deltaP `31.1471` edge `0.0069` maxDD `-0.0543`
- `market_context_high->commodity_1h` score `1.873` n `77` status `ready` deltaP `21.032` edge `0.0369` maxDD `-0.3491`
- `news_risk_high->metal_24h` score `1.3911` n `81` status `ready` deltaP `21.6821` edge `0.0558` maxDD `-2.4203`
- `market_context_high->fx_24h` score `1.0757` n `74` status `ready` deltaP `15.1417` edge `-0.0071` maxDD `-0.0027`
- `news_risk_high->metal_4h` score `0.882` n `98` status `ready` deltaP `19.8917` edge `0.0463` maxDD `-2.0994`
- `market_context_high->fx_1h` score `0.8295` n `77` status `ready` deltaP `13.5917` edge `0.0043` maxDD `-0.063`
- `news_risk_high->metal_1h` score `0.7195` n `98` status `ready` deltaP `15.6055` edge `0.0161` maxDD `-0.8144`
- `news_risk_high->commodity_24h` score `0.352` n `81` status `ready` deltaP `17.2068` edge `0.061` maxDD `-3.4467`
- `news_risk_high->equity_1h` score `0.3408` n `98` status `ready` deltaP `5.7681` edge `0.0305` maxDD `-0.9112`
- `news_risk_high->fx_4h` score `-0.0927` n `98` status `ready` deltaP `5.0803` edge `0.022` maxDD `-0.421`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
