# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-13T02:37:30.190174+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11840`

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

- `news_risk_high->equity_4h` score `7.1088` n `36` status `ready` deltaP `38.4146` edge `0.3363` maxDD `0.0`
- `risk_on_high->commodity_24h` score `2.2893` n `32` status `ready` deltaP `19.2708` edge `0.0623` maxDD `0.0`
- `risk_on_and_context->commodity_24h` score `2.2893` n `32` status `ready` deltaP `19.2708` edge `0.0623` maxDD `0.0`
- `risk_on_high->commodity_4h` score `2.2865` n `32` status `ready` deltaP `15.7774` edge `0.1036` maxDD `-0.1258`
- `risk_on_and_context->commodity_4h` score `2.2865` n `32` status `ready` deltaP `15.7774` edge `0.1036` maxDD `-0.1258`
- `news_risk_high->index_4h` score `2.0804` n `36` status `ready` deltaP `23.2723` edge `0.0314` maxDD `-0.0546`
- `risk_on_high->crypto_major_24h` score `2.0341` n `32` status `ready` deltaP `15.9722` edge `0.2699` maxDD `-6.2481`
- `risk_on_and_context->crypto_major_24h` score `2.0341` n `32` status `ready` deltaP `15.9722` edge `0.2699` maxDD `-6.2481`
- `risk_on_high->fx_24h` score `1.8074` n `32` status `ready` deltaP `20.1389` edge `0.0348` maxDD `-0.1418`
- `risk_on_and_context->fx_24h` score `1.8074` n `32` status `ready` deltaP `20.1389` edge `0.0348` maxDD `-0.1418`
- `news_risk_high->equity_1h` score `1.6003` n `36` status `ready` deltaP `8.1338` edge `0.111` maxDD `-0.5496`
- `risk_on_high->commodity_1h` score `1.1772` n `32` status `ready` deltaP `12.9117` edge `0.0353` maxDD `-0.1957`
- `risk_on_and_context->commodity_1h` score `1.1772` n `32` status `ready` deltaP `12.9117` edge `0.0353` maxDD `-0.1957`
- `market_context_high->commodity_4h` score `1.1049` n `161` status `ready` deltaP `13.4288` edge `0.0664` maxDD `-2.1077`
- `risk_on_high->fx_4h` score `1.0814` n `32` status `ready` deltaP `12.4238` edge `0.0214` maxDD `-0.1285`
- `risk_on_and_context->fx_4h` score `1.0814` n `32` status `ready` deltaP `12.4238` edge `0.0214` maxDD `-0.1285`
- `market_context_high->commodity_1h` score `0.9033` n `161` status `ready` deltaP `11.2424` edge `0.03` maxDD `-0.3742`
- `market_context_high->commodity_24h` score `0.3203` n `161` status `ready` deltaP `9.3329` edge `0.0448` maxDD `-2.4263`
- `risk_on_high->index_1h` score `0.2423` n `32` status `ready` deltaP `9.0569` edge `0.0082` maxDD `-0.3343`
- `risk_on_and_context->index_1h` score `0.2423` n `32` status `ready` deltaP `9.0569` edge `0.0082` maxDD `-0.3343`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
