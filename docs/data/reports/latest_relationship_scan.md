# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-26T07:52:31.841679+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `4007`

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

- `news_risk_high->unknown_4h` score `3248.6287` n `31` status `ready` deltaP `3.4815` edge `270.7015` maxDD `-0.1191`
- `news_risk_high->unknown_1h` score `3220.6237` n `31` status `ready` deltaP `1.6322` edge `268.392` maxDD `-0.7395`
- `market_context_high->unknown_1h` score `90.3318` n `31` status `ready` deltaP `1.6322` edge `7.5262` maxDD `-0.4209`
- `news_risk_high->equity_24h` score `39.8583` n `31` status `ready` deltaP `46.3542` edge `3.0125` maxDD `0.0`
- `news_risk_high->crypto_major_24h` score `38.387` n `31` status `ready` deltaP `47.2222` edge `2.8841` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `32.7694` n `31` status `ready` deltaP `46.5278` edge `2.4206` maxDD `0.0`
- `news_risk_high->crypto_alt_4h` score `10.9733` n `31` status `ready` deltaP `27.3701` edge `0.819` maxDD `-5.2957`
- `news_risk_high->equity_4h` score `10.6062` n `31` status `ready` deltaP `38.5966` edge `0.6746` maxDD `-2.178`
- `news_risk_high->metal_24h` score `9.5864` n `31` status `ready` deltaP `32.9021` edge `0.607` maxDD `-0.1986`
- `news_risk_high->crypto_major_4h` score `6.8998` n `31` status `ready` deltaP `18.3025` edge `0.9043` maxDD `-7.6714`
- `news_risk_high->index_24h` score `6.5602` n `31` status `ready` deltaP `47.7431` edge `0.2284` maxDD `0.0`
- `news_risk_high->fx_24h` score `5.3167` n `31` status `ready` deltaP `45.3573` edge `0.1535` maxDD `-0.0262`
- `news_risk_high->equity_1h` score `3.7554` n `31` status `ready` deltaP `20.4365` edge `0.1954` maxDD `-0.1621`
- `news_risk_high->index_4h` score `3.4906` n `31` status `ready` deltaP `37.5295` edge `0.0667` maxDD `-0.4146`
- `news_risk_high->index_1h` score `2.7333` n `31` status `ready` deltaP `32.2919` edge `0.021` maxDD `-0.0136`
- `news_risk_high->crypto_major_1h` score `2.4992` n `31` status `ready` deltaP `10.1603` edge `0.2988` maxDD `-1.6897`
- `news_risk_high->crypto_alt_1h` score `2.304` n `31` status `ready` deltaP `13.4537` edge `0.2414` maxDD `-1.5232`
- `market_context_high->fx_4h` score `2.1372` n `31` status `ready` deltaP `27.1145` edge `0.0258` maxDD `-0.2774`
- `news_risk_high->metal_1h` score `1.5165` n `31` status `ready` deltaP `29.5827` edge `0.0251` maxDD `-0.2315`
- `news_risk_high->metal_4h` score `1.1078` n `31` status `ready` deltaP `16.7781` edge `0.0859` maxDD `-0.7918`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
