# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-22T05:07:34.019085+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9986`

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

- `market_context_high->unknown_4h` score `49.8094` n `46` status `ready` deltaP `7.3171` edge `4.102` maxDD `0.0`
- `market_context_high->crypto_major_24h` score `35.3723` n `46` status `ready` deltaP `22.2147` edge `2.8152` maxDD `-0.5817`
- `market_context_high->crypto_alt_24h` score `19.9158` n `46` status `ready` deltaP `21.0069` edge `1.5196` maxDD `0.0`
- `market_context_high->equity_24h` score `17.286` n `46` status `ready` deltaP `15.4439` edge `1.3476` maxDD `-0.1382`
- `news_risk_high->crypto_major_24h` score `7.6552` n `101` status `ready` deltaP `-3.1405` edge `1.3447` maxDD `-46.1999`
- `market_context_high->index_24h` score `5.6616` n `46` status `ready` deltaP `20.1314` edge `0.3463` maxDD `-0.03`
- `news_risk_high->crypto_alt_24h` score `3.4348` n `101` status `ready` deltaP `-2.7555` edge `0.7927` maxDD `-32.7147`
- `news_risk_high->commodity_24h` score `2.7911` n `101` status `ready` deltaP `34.3079` edge `0.2597` maxDD `-3.4467`
- `news_risk_high->crypto_alt_4h` score `2.6759` n `101` status `ready` deltaP `13.2788` edge `0.2554` maxDD `-7.675`
- `news_risk_high->crypto_alt_1h` score `2.2702` n `101` status `ready` deltaP `13.8362` edge `0.1435` maxDD `-2.058`
- `news_risk_high->crypto_major_4h` score `2.1536` n `101` status `ready` deltaP `16.3276` edge `0.1964` maxDD `-8.0625`
- `market_context_high->index_4h` score `1.9725` n `46` status `ready` deltaP `23.3165` edge `0.0223` maxDD `-0.0692`
- `news_risk_high->crypto_major_1h` score `1.5928` n `101` status `ready` deltaP `15.4829` edge `0.0818` maxDD `-2.8494`
- `market_context_high->crypto_alt_4h` score `1.1203` n `46` status `ready` deltaP `8.974` edge `0.093` maxDD `-2.7574`
- `market_context_high->equity_4h` score `1.0776` n `46` status `ready` deltaP `8.1389` edge `0.0662` maxDD `-0.4529`
- `market_context_high->equity_1h` score `0.9085` n `46` status `ready` deltaP `7.2117` edge `0.0519` maxDD `-0.2751`
- `news_risk_high->fx_4h` score `0.8155` n `101` status `ready` deltaP `14.7383` edge `0.0333` maxDD `-0.421`
- `market_context_high->index_1h` score `0.6327` n `46` status `ready` deltaP `10.056` edge `0.011` maxDD `-0.0249`
- `news_risk_high->metal_1h` score `0.543` n `101` status `ready` deltaP `13.8495` edge `0.0131` maxDD `-0.8144`
- `market_context_high->crypto_major_1h` score `0.505` n `46` status `ready` deltaP `0.9113` edge `0.0883` maxDD `-2.1836`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
