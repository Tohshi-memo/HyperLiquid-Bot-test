# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-21T17:22:27.538423+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `24`

- Symbol pattern count: `2652`

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

- `market_context_high->unknown_1h` score `9992.1426` n `126` status `ready` deltaP `0.8649` edge `832.6926` maxDD `-0.9188`
- `market_context_high->unknown_4h` score `6070.1549` n `126` status `ready` deltaP `-0.6194` edge `505.8809` maxDD `-0.7759`
- `market_context_high->metal_1h` score `-0.2685` n `126` status `ready` deltaP `2.9037` edge `0.0127` maxDD `-2.6517`
- `market_context_high->index_1h` score `-0.4019` n `126` status `ready` deltaP `1.0621` edge `0.0026` maxDD `-1.2295`
- `market_context_high->metal_4h` score `-0.7972` n `126` status `ready` deltaP `7.8324` edge `0.0262` maxDD `-10.1161`
- `market_context_high->fx_1h` score `-1.4394` n `126` status `ready` deltaP `-9.405` edge `-0.0013` maxDD `-0.4757`
- `market_context_high->fx_4h` score `-1.8701` n `126` status `ready` deltaP `-5.9645` edge `0.0016` maxDD `-1.794`
- `market_context_high->equity_1h` score `-2.1308` n `126` status `ready` deltaP `3.7425` edge `0.0034` maxDD `-13.1399`
- `market_context_high->commodity_1h` score `-2.3589` n `126` status `ready` deltaP `-9.1199` edge `-0.0226` maxDD `-4.3877`
- `market_context_high->index_4h` score `-2.8094` n `126` status `ready` deltaP `-7.7574` edge `-0.0191` maxDD `-7.0639`
- `market_context_high->crypto_major_1h` score `-3.2199` n `126` status `ready` deltaP `0.3136` edge `-0.0386` maxDD `-13.8788`
- `market_context_high->crypto_alt_1h` score `-3.8995` n `126` status `ready` deltaP `-6.2898` edge `-0.0553` maxDD `-13.8848`
- `market_context_high->crypto_major_4h` score `-6.0616` n `126` status `ready` deltaP `-5.2241` edge `-0.0494` maxDD `-47.4317`
- `market_context_high->fx_24h` score `-6.4697` n `126` status `ready` deltaP `-13.1697` edge `-0.0054` maxDD `-7.0088`
- `market_context_high->commodity_4h` score `-7.1023` n `126` status `ready` deltaP `-21.1019` edge `-0.0819` maxDD `-15.5426`
- `market_context_high->metal_24h` score `-7.7178` n `126` status `ready` deltaP `7.9117` edge `0.1137` maxDD `-52.1012`
- `market_context_high->crypto_alt_4h` score `-10.0597` n `126` status `ready` deltaP `-6.2912` edge `-0.1151` maxDD `-46.5016`
- `market_context_high->crypto_major_24h` score `-12.3308` n `126` status `ready` deltaP `15.5754` edge `0.3753` maxDD `-152.134`
- `market_context_high->index_24h` score `-14.8691` n `126` status `ready` deltaP `-26.8353` edge `-0.1164` maxDD `-40.1698`
- `market_context_high->crypto_alt_24h` score `-15.6118` n `126` status `ready` deltaP `4.8611` edge `0.0843` maxDD `-156.7906`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
