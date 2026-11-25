# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-25T21:52:33.051785+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `3696`

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

- `market_context_high->unknown_1h` score `32154.515` n `45` status `ready` deltaP `1.4171` edge `2679.5429` maxDD `-0.4209`
- `market_context_high->unknown_4h` score `21827.6614` n `45` status `ready` deltaP `1.958` edge `1818.9726` maxDD `-0.7765`
- `news_risk_high->unknown_1h` score `919.5601` n `31` status `ready` deltaP `1.6322` edge `76.6367` maxDD `-0.7395`
- `news_risk_high->unknown_4h` score `574.7139` n `31` status `ready` deltaP `3.1766` edge `47.8773` maxDD `-0.1191`
- `news_risk_high->unknown_24h` score `295.1034` n `31` status `ready` deltaP `5.9028` edge `24.5526` maxDD `0.0`
- `news_risk_high->equity_24h` score `46.0971` n `31` status `ready` deltaP `52.0833` edge `3.4942` maxDD `0.0`
- `news_risk_high->crypto_major_24h` score `42.1877` n `31` status `ready` deltaP `53.6458` edge `3.158` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `37.7552` n `31` status `ready` deltaP `53.125` edge `2.7921` maxDD `0.0`
- `news_risk_high->metal_24h` score `11.7403` n `31` status `ready` deltaP `39.8466` edge `0.7402` maxDD `-0.1986`
- `news_risk_high->crypto_alt_4h` score `10.8963` n `31` status `ready` deltaP `26.3031` edge `0.8197` maxDD `-5.2957`
- `news_risk_high->equity_4h` score `10.4781` n `31` status `ready` deltaP `37.8344` edge `0.669` maxDD `-2.178`
- `news_risk_high->index_24h` score `7.4679` n `31` status `ready` deltaP `53.2986` edge `0.267` maxDD `0.0`
- `news_risk_high->crypto_major_4h` score `6.7338` n `31` status `ready` deltaP `17.5403` edge `0.8881` maxDD `-7.6714`
- `news_risk_high->fx_24h` score `5.3341` n `31` status `ready` deltaP `45.5309` edge `0.1538` maxDD `-0.0262`
- `news_risk_high->equity_1h` score `3.5851` n `31` status `ready` deltaP `19.688` edge `0.1862` maxDD `-0.1621`
- `news_risk_high->index_4h` score `3.339` n `31` status `ready` deltaP `36.31` edge `0.0622` maxDD `-0.4146`
- `news_risk_high->index_1h` score `2.6279` n `31` status `ready` deltaP `31.244` edge `0.0192` maxDD `-0.0136`
- `news_risk_high->crypto_major_1h` score `2.3831` n `31` status `ready` deltaP `9.5615` edge `0.2879` maxDD `-1.6897`
- `market_context_high->fx_4h` score `2.3327` n `45` status `ready` deltaP `28.8685` edge `0.0304` maxDD `-0.2774`
- `news_risk_high->crypto_alt_1h` score `2.1957` n `31` status `ready` deltaP `12.2561` edge `0.2355` maxDD `-1.5232`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
