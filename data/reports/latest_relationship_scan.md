# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-07T18:22:32.427792+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11773`

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

- `market_context_high->metal_24h` score `3.1074` n `96` status `ready` deltaP `13.8664` edge `0.2241` maxDD `-2.2743`
- `market_context_high->equity_24h` score `1.7176` n `96` status `ready` deltaP `-4.0318` edge `0.501` maxDD `-21.1456`
- `market_context_high->commodity_4h` score `1.3739` n `109` status `ready` deltaP `14.0678` edge `0.088` maxDD `-2.7169`
- `market_context_high->fx_24h` score `0.967` n `96` status `ready` deltaP `25.5714` edge `0.0558` maxDD `-2.8511`
- `market_context_high->index_24h` score `0.6201` n `96` status `ready` deltaP `7.7229` edge `0.1515` maxDD `-5.7715`
- `market_context_high->commodity_1h` score `0.4197` n `118` status `ready` deltaP `10.0705` edge `0.026` maxDD `-1.1463`
- `market_context_high->fx_4h` score `0.1274` n `109` status `ready` deltaP `9.3113` edge `0.0072` maxDD `-1.6928`
- `market_context_high->fx_1h` score `-0.2945` n `118` status `ready` deltaP `4.6864` edge `-0.0054` maxDD `-1.0308`
- `market_context_high->index_4h` score `-0.5658` n `109` status `ready` deltaP `-0.9049` edge `-0.006` maxDD `-1.1743`
- `market_context_high->index_1h` score `-0.7195` n `118` status `ready` deltaP `-1.2509` edge `-0.0099` maxDD `-1.3375`
- `market_context_high->metal_4h` score `-0.9301` n `109` status `ready` deltaP `2.9397` edge `0.003` maxDD `-2.6753`
- `market_context_high->metal_1h` score `-1.0076` n `118` status `ready` deltaP `-4.0926` edge `-0.0071` maxDD `-0.9664`
- `market_context_high->equity_1h` score `-1.0659` n `118` status `ready` deltaP `4.2804` edge `-0.0264` maxDD `-9.1031`
- `market_context_high->crypto_alt_1h` score `-1.5141` n `118` status `ready` deltaP `-6.3838` edge `-0.0207` maxDD `-2.3669`
- `market_context_high->crypto_alt_4h` score `-1.5161` n `109` status `ready` deltaP `-0.9076` edge `-0.041` maxDD `-5.7857`
- `market_context_high->equity_4h` score `-1.9218` n `109` status `ready` deltaP `6.2906` edge `-0.0621` maxDD `-8.1993`
- `market_context_high->crypto_major_1h` score `-3.1901` n `118` status `ready` deltaP `-8.0255` edge `-0.0668` maxDD `-8.3095`
- `market_context_high->crypto_major_24h` score `-3.215` n `96` status `ready` deltaP `0.6211` edge `-0.1669` maxDD `-14.2873`
- `market_context_high->crypto_alt_24h` score `-4.4022` n `96` status `ready` deltaP `-15.2612` edge `-0.1208` maxDD `-4.5445`
- `market_context_high->crypto_major_4h` score `-6.665` n `109` status `ready` deltaP `-7.6485` edge `-0.1883` maxDD `-18.9565`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
