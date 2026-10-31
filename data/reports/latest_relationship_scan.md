# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-31T21:22:27.213427+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `7705`

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

- `market_context_high->unknown_24h` score `3239.3201` n `93` status `ready` deltaP `-10.4671` edge `270.0561` maxDD `-1.1049`
- `market_context_high->unknown_4h` score `116.5415` n `93` status `ready` deltaP `0.5524` edge `9.7214` maxDD `-0.3966`
- `news_risk_high->unknown_1h` score `77.6968` n `108` status `ready` deltaP `-5.0454` edge `6.537` maxDD `-0.9571`
- `news_risk_high->crypto_alt_24h` score `19.1051` n `79` status `ready` deltaP `45.2115` edge `1.2958` maxDD `-0.0763`
- `market_context_high->equity_24h` score `10.7353` n `93` status `ready` deltaP `24.3336` edge `1.0081` maxDD `-14.0571`
- `news_risk_high->crypto_alt_4h` score `5.4473` n `108` status `ready` deltaP `20.4268` edge `0.4564` maxDD `-7.4246`
- `market_context_high->index_24h` score `4.9445` n `93` status `ready` deltaP `43.8676` edge `0.1379` maxDD `-0.1315`
- `market_context_high->metal_4h` score `1.6057` n `93` status `ready` deltaP `19.8597` edge `0.0439` maxDD `-0.7323`
- `market_context_high->metal_1h` score `0.9544` n `93` status `ready` deltaP `13.3861` edge `0.0193` maxDD `-0.3209`
- `news_risk_high->crypto_alt_1h` score `0.8289` n `108` status `ready` deltaP `8.8767` edge `0.1053` maxDD `-3.9659`
- `market_context_high->equity_4h` score `0.5739` n `93` status `ready` deltaP `3.0012` edge `0.1929` maxDD `-4.48`
- `market_context_high->commodity_4h` score `0.5481` n `93` status `ready` deltaP `15.2456` edge `0.0615` maxDD `-0.763`
- `market_context_high->equity_1h` score `0.4893` n `93` status `ready` deltaP `6.9892` edge `0.1037` maxDD `-2.3383`
- `market_context_high->crypto_major_1h` score `0.3632` n `93` status `ready` deltaP `9.2895` edge `0.0874` maxDD `-5.2213`
- `market_context_high->fx_4h` score `0.3405` n `93` status `ready` deltaP `9.9266` edge `0.0013` maxDD `-0.1285`
- `market_context_high->fx_1h` score `0.2996` n `93` status `ready` deltaP `9.1945` edge `-0.0003` maxDD `-0.1407`
- `market_context_high->metal_24h` score `-0.236` n `93` status `ready` deltaP `9.8454` edge `0.1688` maxDD `-10.5088`
- `market_context_high->crypto_major_4h` score `-0.3762` n `93` status `ready` deltaP `14.998` edge `0.1258` maxDD `-14.5879`
- `market_context_high->commodity_1h` score `-0.4048` n `93` status `ready` deltaP `-2.1715` edge `0.014` maxDD `-0.4475`
- `market_context_high->index_1h` score `-0.405` n `93` status `ready` deltaP `3.0149` edge `0.002` maxDD `-1.1344`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
