# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-21T18:22:33.044287+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `24`

- Symbol pattern count: `2658`

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

- `market_context_high->unknown_1h` score `9988.2594` n `126` status `ready` deltaP `0.8649` edge `832.369` maxDD `-0.9188`
- `market_context_high->unknown_4h` score `6051.2849` n `126` status `ready` deltaP `-0.6194` edge `504.3084` maxDD `-0.7759`
- `market_context_high->metal_1h` score `-0.2591` n `126` status `ready` deltaP `3.0534` edge `0.0129` maxDD `-2.6517`
- `market_context_high->index_1h` score `-0.3762` n `126` status `ready` deltaP `1.5112` edge `0.0029` maxDD `-1.2295`
- `market_context_high->metal_4h` score `-0.82` n `126` status `ready` deltaP `7.5275` edge `0.0253` maxDD `-10.1161`
- `market_context_high->fx_1h` score `-1.4513` n `126` status `ready` deltaP `-9.5547` edge `-0.0013` maxDD `-0.4757`
- `market_context_high->fx_4h` score `-1.8859` n `126` status `ready` deltaP `-6.2693` edge `0.0016` maxDD `-1.794`
- `market_context_high->equity_1h` score `-2.108` n `126` status `ready` deltaP `3.8922` edge `0.0043` maxDD `-13.1399`
- `market_context_high->commodity_1h` score `-2.3841` n `126` status `ready` deltaP `-9.4193` edge `-0.0227` maxDD `-4.3877`
- `market_context_high->index_4h` score `-2.7692` n `126` status `ready` deltaP `-7.3001` edge `-0.0188` maxDD `-7.0639`
- `market_context_high->crypto_major_1h` score `-3.2031` n `126` status `ready` deltaP `0.3136` edge `-0.0372` maxDD `-13.8788`
- `market_context_high->crypto_alt_1h` score `-3.8779` n `126` status `ready` deltaP `-6.2898` edge `-0.0535` maxDD `-13.8848`
- `market_context_high->crypto_major_4h` score `-6.1256` n `126` status `ready` deltaP `-5.3765` edge `-0.0566` maxDD `-47.4317`
- `market_context_high->fx_24h` score `-6.4613` n `126` status `ready` deltaP `-13.1697` edge `-0.0047` maxDD `-7.0088`
- `market_context_high->commodity_4h` score `-7.0889` n `126` status `ready` deltaP `-20.9494` edge `-0.0818` maxDD `-15.5426`
- `market_context_high->metal_24h` score `-7.7998` n `126` status `ready` deltaP `7.2173` edge `0.1115` maxDD `-52.1012`
- `market_context_high->crypto_alt_4h` score `-10.2219` n `126` status `ready` deltaP `-6.4436` edge `-0.1276` maxDD `-46.5016`
- `market_context_high->crypto_major_24h` score `-12.4796` n `126` status `ready` deltaP `15.0546` edge `0.3597` maxDD `-152.134`
- `market_context_high->index_24h` score `-14.8329` n `126` status `ready` deltaP `-26.4881` edge `-0.1157` maxDD `-40.1698`
- `market_context_high->crypto_alt_24h` score `-15.7579` n `126` status `ready` deltaP `4.1666` edge `0.0702` maxDD `-156.7906`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
