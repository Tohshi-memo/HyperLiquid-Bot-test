# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-22T15:52:41.489531+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9834`

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

- `market_context_high->unknown_4h` score `46.4946` n `46` status `ready` deltaP `7.0122` edge `3.8278` maxDD `0.0`
- `market_context_high->crypto_major_24h` score `30.4467` n `46` status `ready` deltaP `14.7494` edge `2.4545` maxDD `-0.5817`
- `market_context_high->equity_24h` score `16.2452` n `46` status `ready` deltaP `12.3189` edge `1.2817` maxDD `-0.1382`
- `market_context_high->crypto_alt_24h` score `15.6181` n `46` status `ready` deltaP `14.2361` edge `1.2066` maxDD `0.0`
- `market_context_high->index_24h` score `5.55` n `46` status `ready` deltaP `20.1314` edge `0.337` maxDD `-0.03`
- `news_risk_high->commodity_24h` score `3.1585` n `101` status `ready` deltaP `37.9538` edge `0.2825` maxDD `-3.4467`
- `news_risk_high->crypto_major_24h` score `2.7296` n `101` status `ready` deltaP `-10.6058` edge `0.984` maxDD `-46.1999`
- `news_risk_high->crypto_alt_1h` score `2.0543` n `101` status `ready` deltaP `12.938` edge `0.1315` maxDD `-2.058`
- `news_risk_high->crypto_alt_4h` score `1.9827` n `101` status `ready` deltaP `10.8398` edge `0.2139` maxDD `-7.675`
- `market_context_high->index_4h` score `1.8752` n `46` status `ready` deltaP `22.2494` edge `0.0213` maxDD `-0.0692`
- `news_risk_high->crypto_major_1h` score `1.3218` n `101` status `ready` deltaP `14.1356` edge `0.0682` maxDD `-2.8494`
- `news_risk_high->crypto_major_4h` score `1.3063` n `101` status `ready` deltaP `13.4312` edge `0.1451` maxDD `-8.0625`
- `market_context_high->metal_24h` score `1.1056` n `46` status `ready` deltaP `22.7884` edge `-0.0364` maxDD `-0.2042`
- `news_risk_high->fx_4h` score `1.105` n `101` status `ready` deltaP `17.787` edge `0.0371` maxDD `-0.421`
- `market_context_high->equity_1h` score `0.858` n `46` status `ready` deltaP `7.5111` edge `0.0457` maxDD `-0.2751`
- `market_context_high->equity_4h` score `0.7826` n `46` status `ready` deltaP `6.4621` edge `0.0528` maxDD `-0.4529`
- `market_context_high->index_1h` score `0.671` n `46` status `ready` deltaP `10.6548` edge `0.0102` maxDD `-0.0249`
- `news_risk_high->metal_1h` score `0.628` n `101` status `ready` deltaP `14.8974` edge `0.0132` maxDD `-0.8144`
- `news_risk_high->metal_24h` score `0.5195` n `101` status `ready` deltaP `18.9786` edge `0.0245` maxDD `-2.4203`
- `market_context_high->crypto_alt_4h` score `0.4272` n `46` status `ready` deltaP `6.535` edge `0.0515` maxDD `-2.7574`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
