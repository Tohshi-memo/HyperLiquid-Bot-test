# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-28T20:52:36.875748+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `80`

- Symbol pattern count: `7652`

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

- `news_risk_high->unknown_4h` score `3429.5416` n `30` status `ready` deltaP `5.9451` edge `285.7555` maxDD `0.0`
- `news_risk_high->unknown_1h` score `2906.5915` n `30` status `ready` deltaP `2.0159` edge `242.2201` maxDD `-0.7395`
- `news_risk_high->crypto_major_24h` score `26.5307` n `30` status `ready` deltaP `40.7986` edge `1.9389` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `20.8279` n `30` status `ready` deltaP `38.8889` edge `1.4764` maxDD `0.0`
- `news_risk_high->equity_24h` score `14.0186` n `30` status `ready` deltaP `30.9028` edge `0.9622` maxDD `0.0`
- `news_risk_high->crypto_alt_4h` score `10.1435` n `30` status `ready` deltaP `27.754` edge `0.7464` maxDD `-5.2238`
- `news_risk_high->crypto_major_4h` score `9.8617` n `30` status `ready` deltaP `21.1077` edge `0.8162` maxDD `-7.4756`
- `news_risk_high->equity_4h` score `6.146` n `30` status `ready` deltaP `33.3333` edge `0.338` maxDD `-2.178`
- `news_risk_high->fx_24h` score `5.5765` n `30` status `ready` deltaP `46.4583` edge `0.1635` maxDD `-0.0146`
- `news_risk_high->metal_24h` score `4.206` n `30` status `ready` deltaP `18.4027` edge `0.2506` maxDD `-0.1561`
- `news_risk_high->index_4h` score `2.7163` n `30` status `ready` deltaP `32.876` edge `0.0332` maxDD `-0.4146`
- `news_risk_high->index_24h` score `2.6875` n `30` status `ready` deltaP `28.2986` edge `0.0353` maxDD `0.0`
- `news_risk_high->equity_1h` score `2.5724` n `30` status `ready` deltaP `17.7545` edge `0.1147` maxDD `-0.1621`
- `news_risk_high->crypto_major_1h` score `2.4078` n `30` status `ready` deltaP `9.7006` edge `0.2841` maxDD `-1.5397`
- `news_risk_high->index_1h` score `2.3713` n `30` status `ready` deltaP `28.9521` edge `0.0131` maxDD `-0.0136`
- `news_risk_high->crypto_alt_1h` score `2.2504` n `30` status `ready` deltaP `12.994` edge `0.2342` maxDD `-1.2517`
- `news_risk_high->metal_1h` score `1.309` n `30` status `ready` deltaP `27.1158` edge `0.0106` maxDD `-0.217`
- `market_context_high->fx_1h` score `0.7895` n `72` status `ready` deltaP `12.9491` edge `0.0016` maxDD `-0.1042`
- `market_context_high->fx_4h` score `0.662` n `65` status `ready` deltaP `12.7439` edge `0.0098` maxDD `-0.1673`
- `news_risk_high->commodity_4h` score `0.6443` n `30` status `ready` deltaP `13.9634` edge `0.0291` maxDD `-0.5004`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
