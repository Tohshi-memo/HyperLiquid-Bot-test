# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-23T11:37:27.521156+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `4482`

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

- `market_context_high->unknown_1h` score `22727.6817` n `62` status `ready` deltaP `0.3525` edge `1893.9873` maxDD `-0.6271`
- `market_context_high->unknown_4h` score `15242.8749` n `62` status `ready` deltaP `4.701` edge `1270.2221` maxDD `-0.7759`
- `news_risk_high->unknown_1h` score `1297.6774` n `31` status `ready` deltaP `3.5783` edge `108.1335` maxDD `-0.7389`
- `news_risk_high->unknown_4h` score `1112.083` n `31` status `ready` deltaP `4.701` edge `92.6479` maxDD `-0.119`
- `news_risk_high->equity_24h` score `45.5678` n `31` status `ready` deltaP `50.8681` edge `3.4582` maxDD `0.0`
- `news_risk_high->crypto_major_24h` score `37.0173` n `31` status `ready` deltaP `48.6111` edge `2.7607` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `32.5924` n `31` status `ready` deltaP `48.7847` edge `2.3908` maxDD `0.0`
- `news_risk_high->metal_24h` score `13.5157` n `31` status `ready` deltaP `51.4785` edge `0.8106` maxDD `-0.1986`
- `news_risk_high->equity_4h` score `10.433` n `31` status `ready` deltaP `33.2612` edge `0.6959` maxDD `-2.1911`
- `news_risk_high->crypto_alt_4h` score `10.1586` n `31` status `ready` deltaP `21.8823` edge `0.7877` maxDD `-5.2957`
- `news_risk_high->index_24h` score `7.1548` n `31` status `ready` deltaP `48.7847` edge `0.271` maxDD `0.0`
- `news_risk_high->fx_24h` score `6.3723` n `31` status `ready` deltaP `54.0379` edge `0.1836` maxDD `-0.0262`
- `news_risk_high->crypto_major_4h` score `6.1968` n `31` status `ready` deltaP `11.4427` edge `0.8599` maxDD `-7.6714`
- `news_risk_high->equity_1h` score `3.6872` n `31` status `ready` deltaP `18.6401` edge `0.2017` maxDD `-0.163`
- `news_risk_high->index_4h` score `3.2949` n `31` status `ready` deltaP `34.6332` edge `0.0697` maxDD `-0.4146`
- `news_risk_high->index_1h` score `2.6232` n `31` status `ready` deltaP `30.7949` edge `0.0218` maxDD `-0.0136`
- `news_risk_high->crypto_major_1h` score `2.3738` n `31` status `ready` deltaP `9.1124` edge `0.2897` maxDD `-1.6897`
- `news_risk_high->crypto_alt_1h` score `1.9684` n `31` status `ready` deltaP `7.7651` edge `0.2363` maxDD `-1.5232`
- `news_risk_high->metal_1h` score `1.5135` n `31` status `ready` deltaP `28.8342` edge `0.0297` maxDD `-0.2315`
- `news_risk_high->metal_4h` score `1.4555` n `31` status `ready` deltaP `20.2842` edge `0.1071` maxDD `-0.7918`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
