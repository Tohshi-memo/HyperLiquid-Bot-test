# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-22T12:37:37.156281+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9954`

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

- `market_context_high->unknown_4h` score `46.9522` n `46` status `ready` deltaP `7.3171` edge `3.8639` maxDD `0.0`
- `market_context_high->crypto_major_24h` score `31.6329` n `46` status `ready` deltaP `17.0064` edge `2.5383` maxDD `-0.5817`
- `market_context_high->crypto_alt_24h` score `16.7609` n `46` status `ready` deltaP `16.1458` edge `1.2891` maxDD `0.0`
- `market_context_high->equity_24h` score `16.4128` n `46` status `ready` deltaP `12.8397` edge `1.2922` maxDD `-0.1382`
- `market_context_high->index_24h` score `5.562` n `46` status `ready` deltaP `20.1314` edge `0.338` maxDD `-0.03`
- `news_risk_high->crypto_major_24h` score `3.9157` n `101` status `ready` deltaP `-8.3488` edge `1.0678` maxDD `-46.1999`
- `news_risk_high->commodity_24h` score `3.2079` n `101` status `ready` deltaP `38.6482` edge `0.2842` maxDD `-3.4467`
- `news_risk_high->crypto_alt_4h` score `2.3985` n `101` status `ready` deltaP `12.2117` edge `0.2394` maxDD `-7.675`
- `news_risk_high->crypto_alt_1h` score `2.2426` n `101` status `ready` deltaP `13.6865` edge `0.1422` maxDD `-2.058`
- `market_context_high->index_4h` score `2.0319` n `46` status `ready` deltaP `23.7738` edge `0.0242` maxDD `-0.0692`
- `news_risk_high->crypto_major_4h` score `1.7691` n `101` status `ready` deltaP `14.9556` edge `0.1735` maxDD `-8.0625`
- `news_risk_high->crypto_major_1h` score `1.558` n `101` status `ready` deltaP `15.3332` edge `0.0799` maxDD `-2.8494`
- `market_context_high->equity_4h` score `1.204` n `46` status `ready` deltaP `8.4438` edge `0.0747` maxDD `-0.4529`
- `news_risk_high->fx_4h` score `1.0538` n `101` status `ready` deltaP `17.1773` edge `0.0369` maxDD `-0.421`
- `market_context_high->equity_1h` score `1.0008` n `46` status `ready` deltaP `7.9602` edge `0.0546` maxDD `-0.2751`
- `market_context_high->crypto_alt_4h` score `0.8429` n `46` status `ready` deltaP `7.9069` edge `0.077` maxDD `-2.7574`
- `market_context_high->metal_24h` score `0.8365` n `46` status `ready` deltaP `20.8787` edge `-0.0461` maxDD `-0.2042`
- `market_context_high->index_1h` score `0.7358` n `46` status `ready` deltaP `11.2536` edge `0.0116` maxDD `-0.0249`
- `news_risk_high->metal_1h` score `0.6101` n `101` status `ready` deltaP `14.598` edge `0.0137` maxDD `-0.8144`
- `market_context_high->crypto_major_1h` score `0.4702` n `46` status `ready` deltaP `0.7616` edge `0.0864` maxDD `-2.1836`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
