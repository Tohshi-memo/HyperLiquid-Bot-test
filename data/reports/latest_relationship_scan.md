# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-26T04:37:22.512084+00:00`
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

- `market_context_high->unknown_1h` score `42326.8172` n `35` status `ready` deltaP `2.2198` edge `3527.2294` maxDD `-0.4209`
- `news_risk_high->unknown_4h` score `3192.9581` n `31` status `ready` deltaP `3.3291` edge `266.0633` maxDD `-0.1191`
- `news_risk_high->unknown_1h` score `887.3329` n `31` status `ready` deltaP `1.4825` edge `73.9521` maxDD `-0.7395`
- `market_context_high->unknown_4h` score `77.3368` n `35` status `ready` deltaP `0.8406` edge `6.453` maxDD `-0.7765`
- `news_risk_high->equity_24h` score `42.5109` n `31` status `ready` deltaP `48.6111` edge `3.2185` maxDD `0.0`
- `news_risk_high->crypto_major_24h` score `40.0795` n `31` status `ready` deltaP `49.4792` edge `3.0101` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `34.6072` n `31` status `ready` deltaP `48.7847` edge `2.5587` maxDD `0.0`
- `news_risk_high->crypto_alt_4h` score `10.7391` n `31` status `ready` deltaP `26.3031` edge `0.8066` maxDD `-5.2957`
- `news_risk_high->metal_24h` score `10.4113` n `31` status `ready` deltaP `35.1591` edge `0.6607` maxDD `-0.1986`
- `news_risk_high->equity_4h` score `10.2097` n `31` status `ready` deltaP `37.2247` edge `0.6507` maxDD `-2.178`
- `news_risk_high->index_24h` score `6.9532` n `31` status `ready` deltaP `50.0` edge `0.2461` maxDD `0.0`
- `news_risk_high->crypto_major_4h` score `6.7765` n `31` status `ready` deltaP `17.2354` edge `0.8956` maxDD `-7.6714`
- `news_risk_high->fx_24h` score `5.3794` n `31` status `ready` deltaP `46.0518` edge `0.1541` maxDD `-0.0262`
- `news_risk_high->equity_1h` score `3.5468` n `31` status `ready` deltaP `19.3886` edge `0.185` maxDD `-0.1621`
- `news_risk_high->index_4h` score `3.3316` n `31` status `ready` deltaP `36.1576` edge `0.0626` maxDD `-0.4146`
- `news_risk_high->index_1h` score `2.6435` n `31` status `ready` deltaP `31.3937` edge `0.0195` maxDD `-0.0136`
- `news_risk_high->crypto_major_1h` score `2.4275` n `31` status `ready` deltaP `9.7112` edge `0.2926` maxDD `-1.6897`
- `market_context_high->fx_4h` score `2.3` n `35` status `ready` deltaP `28.4756` edge `0.0303` maxDD `-0.2774`
- `news_risk_high->crypto_alt_1h` score `2.2144` n `31` status `ready` deltaP `12.4058` edge `0.2369` maxDD `-1.5232`
- `news_risk_high->metal_1h` score `1.5001` n `31` status `ready` deltaP `29.433` edge `0.024` maxDD `-0.2315`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
