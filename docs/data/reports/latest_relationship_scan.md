# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-25T22:37:27.656369+00:00`
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

- `market_context_high->unknown_1h` score `32152.9586` n `45` status `ready` deltaP `1.4171` edge `2679.4132` maxDD `-0.4209`
- `market_context_high->unknown_4h` score `21824.1622` n `45` status `ready` deltaP `1.958` edge `1818.681` maxDD `-0.7765`
- `news_risk_high->unknown_1h` score `918.0037` n `31` status `ready` deltaP `1.6322` edge `76.507` maxDD `-0.7395`
- `news_risk_high->unknown_4h` score `571.2147` n `31` status `ready` deltaP `3.1766` edge `47.5857` maxDD `-0.1191`
- `news_risk_high->unknown_24h` score `295.5589` n `31` status `ready` deltaP `6.0764` edge `24.5894` maxDD `0.0`
- `news_risk_high->equity_24h` score `45.9603` n `31` status `ready` deltaP `52.0833` edge `3.4828` maxDD `0.0`
- `news_risk_high->crypto_major_24h` score `42.0843` n `31` status `ready` deltaP `53.2986` edge `3.1517` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `37.5582` n `31` status `ready` deltaP `52.7778` edge `2.778` maxDD `0.0`
- `news_risk_high->metal_24h` score `11.6315` n `31` status `ready` deltaP `39.3258` edge `0.7346` maxDD `-0.1986`
- `news_risk_high->crypto_alt_4h` score `10.8795` n `31` status `ready` deltaP `26.3031` edge `0.8183` maxDD `-5.2957`
- `news_risk_high->equity_4h` score `10.4421` n `31` status `ready` deltaP `37.8344` edge `0.666` maxDD `-2.178`
- `news_risk_high->index_24h` score `7.4631` n `31` status `ready` deltaP `53.2986` edge `0.2666` maxDD `0.0`
- `news_risk_high->crypto_major_4h` score `6.7104` n `31` status `ready` deltaP `17.5403` edge `0.8851` maxDD `-7.6714`
- `news_risk_high->fx_24h` score `5.2877` n `31` status `ready` deltaP `45.0101` edge `0.1534` maxDD `-0.0262`
- `news_risk_high->equity_1h` score `3.6595` n `31` status `ready` deltaP `19.9874` edge `0.1904` maxDD `-0.1621`
- `news_risk_high->index_4h` score `3.3378` n `31` status `ready` deltaP `36.31` edge `0.0621` maxDD `-0.4146`
- `news_risk_high->index_1h` score `2.671` n `31` status `ready` deltaP `31.6931` edge `0.0198` maxDD `-0.0136`
- `news_risk_high->crypto_major_1h` score `2.4314` n `31` status `ready` deltaP `10.0106` edge `0.2911` maxDD `-1.6897`
- `market_context_high->fx_4h` score `2.3315` n `45` status `ready` deltaP `28.8685` edge `0.0303` maxDD `-0.2774`
- `news_risk_high->crypto_alt_1h` score `2.2354` n `31` status `ready` deltaP `12.7052` edge `0.2376` maxDD `-1.5232`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
