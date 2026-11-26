# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-26T03:22:37.253566+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `3899`

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

- `market_context_high->unknown_1h` score `36587.078` n `40` status `ready` deltaP `0.5838` edge `3048.9287` maxDD `-0.4209`
- `news_risk_high->unknown_4h` score `3196.5965` n `31` status `ready` deltaP `3.3291` edge `266.3665` maxDD `-0.1191`
- `news_risk_high->unknown_1h` score `886.5769` n `31` status `ready` deltaP `1.6322` edge `73.8881` maxDD `-0.7395`
- `news_risk_high->equity_24h` score `43.4035` n `31` status `ready` deltaP `49.4792` edge `3.2871` maxDD `0.0`
- `news_risk_high->crypto_major_24h` score `40.683` n `31` status `ready` deltaP `50.3472` edge `3.0546` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `35.4086` n `31` status `ready` deltaP `49.6528` edge `2.6197` maxDD `0.0`
- `news_risk_high->crypto_alt_4h` score `10.8163` n `31` status `ready` deltaP `26.6079` edge `0.811` maxDD `-5.2957`
- `news_risk_high->metal_24h` score `10.71` n `31` status `ready` deltaP `36.0271` edge `0.6798` maxDD `-0.1986`
- `news_risk_high->equity_4h` score `10.1857` n `31` status `ready` deltaP `37.2247` edge `0.6487` maxDD `-2.178`
- `news_risk_high->index_24h` score `7.0922` n `31` status `ready` deltaP `50.8681` edge `0.2519` maxDD `0.0`
- `news_risk_high->crypto_major_4h` score `6.7733` n `31` status `ready` deltaP `17.2354` edge `0.8952` maxDD `-7.6714`
- `news_risk_high->fx_24h` score `5.348` n `31` status `ready` deltaP `45.7045` edge `0.1538` maxDD `-0.0262`
- `news_risk_high->equity_1h` score `3.6007` n `31` status `ready` deltaP `19.8377` edge `0.1865` maxDD `-0.1621`
- `news_risk_high->index_4h` score `3.322` n `31` status `ready` deltaP `36.1576` edge `0.0618` maxDD `-0.4146`
- `news_risk_high->index_1h` score `2.6698` n `31` status `ready` deltaP `31.6931` edge `0.0197` maxDD `-0.0136`
- `market_context_high->fx_4h` score `2.4763` n `40` status `ready` deltaP `30.2134` edge `0.0334` maxDD `-0.2774`
- `news_risk_high->crypto_major_1h` score `2.415` n `31` status `ready` deltaP `9.7112` edge `0.291` maxDD `-1.6897`
- `news_risk_high->crypto_alt_1h` score `2.216` n `31` status `ready` deltaP `12.4058` edge `0.2371` maxDD `-1.5232`
- `news_risk_high->metal_1h` score `1.469` n `31` status `ready` deltaP `28.9839` edge `0.023` maxDD `-0.2315`
- `news_risk_high->metal_4h` score `1.129` n `31` status `ready` deltaP `16.9305` edge `0.0876` maxDD `-0.7918`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
