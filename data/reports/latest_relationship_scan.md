# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-31T17:37:27.931704+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `7473`

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

- `market_context_high->unknown_24h` score `2804.1347` n `101` status `ready` deltaP `-9.0192` edge `233.781` maxDD `-1.1049`
- `market_context_high->unknown_4h` score `80.7162` n `101` status `ready` deltaP `0.9961` edge `6.733` maxDD `-0.3966`
- `news_risk_high->unknown_1h` score `77.151` n `108` status `ready` deltaP `-6.0934` edge `6.4985` maxDD `-0.9571`
- `news_risk_high->crypto_alt_24h` score `18.599` n `64` status `ready` deltaP `45.4861` edge `1.2518` maxDD `-0.0763`
- `market_context_high->equity_24h` score `11.0773` n `101` status `ready` deltaP `26.4628` edge `1.0224` maxDD `-14.0571`
- `news_risk_high->crypto_alt_4h` score `4.9582` n `104` status `ready` deltaP `18.0934` edge `0.4312` maxDD `-7.4246`
- `market_context_high->index_24h` score `4.8906` n `101` status `ready` deltaP `43.6744` edge `0.1347` maxDD `-0.1315`
- `market_context_high->metal_4h` score `1.7128` n `101` status `ready` deltaP `21.2131` edge `0.0438` maxDD `-0.7323`
- `market_context_high->equity_4h` score `1.1999` n `101` status `ready` deltaP `6.6635` edge `0.1949` maxDD `-4.48`
- `market_context_high->metal_1h` score `0.8578` n `101` status `ready` deltaP `12.2843` edge `0.0186` maxDD `-0.3209`
- `news_risk_high->crypto_alt_1h` score `0.6418` n `108` status `ready` deltaP `7.8288` edge `0.0967` maxDD `-3.9659`
- `market_context_high->crypto_major_1h` score `0.6162` n `101` status `ready` deltaP `9.7972` edge `0.0888` maxDD `-5.2213`
- `market_context_high->equity_1h` score `0.5214` n `101` status `ready` deltaP `8.1164` edge `0.1003` maxDD `-2.3383`
- `market_context_high->fx_1h` score `0.2393` n `101` status `ready` deltaP `8.6915` edge `-0.0005` maxDD `-0.1407`
- `market_context_high->fx_4h` score `0.2391` n `101` status `ready` deltaP `8.7946` edge `0.0004` maxDD `-0.1285`
- `market_context_high->commodity_4h` score `0.1348` n `101` status `ready` deltaP `12.2283` edge `0.0565` maxDD `-0.9926`
- `market_context_high->metal_24h` score `0.083` n `101` status `ready` deltaP `13.7599` edge `0.1836` maxDD `-10.5088`
- `market_context_high->crypto_major_4h` score `-0.0583` n `101` status `ready` deltaP `16.9433` edge `0.1562` maxDD `-14.5879`
- `market_context_high->index_1h` score `-0.257` n `101` status `ready` deltaP `4.7889` edge `0.0025` maxDD `-1.1344`
- `market_context_high->commodity_1h` score `-0.3688` n `101` status `ready` deltaP `-1.4036` edge `0.0135` maxDD `-0.4475`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
