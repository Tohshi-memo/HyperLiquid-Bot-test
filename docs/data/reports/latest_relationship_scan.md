# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-26T04:52:29.626376+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `3959`

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

- `market_context_high->unknown_1h` score `41827.6434` n `34` status `ready` deltaP `2.0517` edge `3485.6327` maxDD `-0.4209`
- `news_risk_high->unknown_4h` score `3193.2053` n `31` status `ready` deltaP `3.3291` edge `266.0839` maxDD `-0.1191`
- `news_risk_high->unknown_1h` score `986.7301` n `31` status `ready` deltaP `1.4825` edge `82.2352` maxDD `-0.7395`
- `market_context_high->unknown_4h` score `109.8157` n `34` status `ready` deltaP `0.6725` edge `9.1607` maxDD `-0.7765`
- `news_risk_high->equity_24h` score `42.3194` n `31` status `ready` deltaP `48.4375` edge `3.2037` maxDD `0.0`
- `news_risk_high->crypto_major_24h` score `39.9312` n `31` status `ready` deltaP `49.3056` edge `2.9989` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `34.4433` n `31` status `ready` deltaP `48.6111` edge `2.5462` maxDD `0.0`
- `news_risk_high->crypto_alt_4h` score `10.7403` n `31` status `ready` deltaP `26.3031` edge `0.8067` maxDD `-5.2957`
- `news_risk_high->metal_24h` score `10.3482` n `31` status `ready` deltaP `34.9855` edge `0.6566` maxDD `-0.1986`
- `news_risk_high->equity_4h` score `10.2277` n `31` status `ready` deltaP `37.2247` edge `0.6522` maxDD `-2.178`
- `news_risk_high->index_24h` score `6.9249` n `31` status `ready` deltaP `49.8264` edge `0.2449` maxDD `0.0`
- `news_risk_high->crypto_major_4h` score `6.7726` n `31` status `ready` deltaP `17.2354` edge `0.8951` maxDD `-7.6714`
- `news_risk_high->fx_24h` score `5.3794` n `31` status `ready` deltaP `46.0518` edge `0.1541` maxDD `-0.0262`
- `news_risk_high->equity_1h` score `3.542` n `31` status `ready` deltaP `19.3886` edge `0.1846` maxDD `-0.1621`
- `news_risk_high->index_4h` score `3.3352` n `31` status `ready` deltaP `36.1576` edge `0.0629` maxDD `-0.4146`
- `news_risk_high->index_1h` score `2.6435` n `31` status `ready` deltaP `31.3937` edge `0.0195` maxDD `-0.0136`
- `news_risk_high->crypto_major_1h` score `2.419` n `31` status `ready` deltaP `9.5615` edge `0.2925` maxDD `-1.6897`
- `market_context_high->fx_4h` score `2.2568` n `34` status `ready` deltaP `28.0398` edge `0.0296` maxDD `-0.2774`
- `news_risk_high->crypto_alt_1h` score `2.2121` n `31` status `ready` deltaP `12.4058` edge `0.2366` maxDD `-1.5232`
- `news_risk_high->metal_1h` score `1.5009` n `31` status `ready` deltaP `29.433` edge `0.0241` maxDD `-0.2315`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
