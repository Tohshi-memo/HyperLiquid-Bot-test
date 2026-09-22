# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-22T05:52:27.132637+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `10002`

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

- `market_context_high->unknown_4h` score `48.3514` n `46` status `ready` deltaP `7.3171` edge `3.9805` maxDD `0.0`
- `market_context_high->crypto_major_24h` score `34.9059` n `46` status `ready` deltaP `21.6939` edge `2.7798` maxDD `-0.5817`
- `market_context_high->crypto_alt_24h` score `19.5237` n `46` status `ready` deltaP `20.4861` edge `1.4904` maxDD `0.0`
- `market_context_high->equity_24h` score `17.1279` n `46` status `ready` deltaP `14.923` edge `1.3379` maxDD `-0.1382`
- `news_risk_high->crypto_major_24h` score `7.1887` n `101` status `ready` deltaP `-3.6613` edge `1.3093` maxDD `-46.1999`
- `market_context_high->index_24h` score `5.6412` n `46` status `ready` deltaP `20.1314` edge `0.3446` maxDD `-0.03`
- `news_risk_high->crypto_alt_24h` score `3.0427` n `101` status `ready` deltaP `-3.2763` edge `0.7635` maxDD `-32.7147`
- `news_risk_high->commodity_24h` score `2.833` n `101` status `ready` deltaP `34.8288` edge `0.2616` maxDD `-3.4467`
- `news_risk_high->crypto_alt_4h` score `2.6673` n `101` status `ready` deltaP `13.1263` edge `0.2557` maxDD `-7.675`
- `news_risk_high->crypto_alt_1h` score `2.2978` n `101` status `ready` deltaP `13.9859` edge `0.1448` maxDD `-2.058`
- `news_risk_high->crypto_major_4h` score `2.1438` n `101` status `ready` deltaP `16.1751` edge `0.1966` maxDD `-8.0625`
- `market_context_high->index_4h` score `1.9761` n `46` status `ready` deltaP `23.3165` edge `0.0226` maxDD `-0.0692`
- `news_risk_high->crypto_major_1h` score `1.6252` n `101` status `ready` deltaP `15.6326` edge `0.0835` maxDD `-2.8494`
- `market_context_high->crypto_alt_4h` score `1.1117` n `46` status `ready` deltaP `8.8215` edge `0.0933` maxDD `-2.7574`
- `market_context_high->equity_4h` score `1.1064` n `46` status `ready` deltaP `8.1389` edge `0.0686` maxDD `-0.4529`
- `market_context_high->equity_1h` score `0.9516` n `46` status `ready` deltaP `7.5111` edge `0.0535` maxDD `-0.2751`
- `news_risk_high->fx_4h` score `0.8581` n `101` status `ready` deltaP `15.1956` edge `0.0338` maxDD `-0.421`
- `market_context_high->index_1h` score `0.6591` n `46` status `ready` deltaP `10.3554` edge `0.0112` maxDD `-0.0249`
- `news_risk_high->metal_1h` score `0.5442` n `101` status `ready` deltaP `13.8495` edge `0.0132` maxDD `-0.8144`
- `market_context_high->crypto_major_1h` score `0.5373` n `46` status `ready` deltaP `1.061` edge `0.09` maxDD `-2.1836`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
