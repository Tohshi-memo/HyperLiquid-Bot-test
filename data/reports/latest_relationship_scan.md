# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-25T05:22:26.323001+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `4092`

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

- `market_context_high->unknown_1h` score `32244.0709` n `45` status `ready` deltaP `2.0159` edge `2687.0019` maxDD `-0.4209`
- `market_context_high->unknown_4h` score `21975.9157` n `45` status `ready` deltaP `3.1776` edge `1831.319` maxDD `-0.7765`
- `news_risk_high->unknown_1h` score `1009.116` n `31` status `ready` deltaP `2.231` edge `84.0957` maxDD `-0.7395`
- `news_risk_high->unknown_4h` score `722.9682` n `31` status `ready` deltaP `4.3962` edge `60.2237` maxDD `-0.1191`
- `news_risk_high->equity_24h` score `39.7734` n `31` status `ready` deltaP `44.6181` edge `3.017` maxDD `0.0`
- `news_risk_high->crypto_major_24h` score `39.2915` n `31` status `ready` deltaP `50.1736` edge `2.9398` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `35.8305` n `31` status `ready` deltaP `49.8264` edge `2.6537` maxDD `0.0`
- `news_risk_high->crypto_alt_4h` score `12.0266` n `31` status `ready` deltaP `28.1323` edge `0.9017` maxDD `-5.2957`
- `news_risk_high->metal_24h` score `11.2646` n `31` status `ready` deltaP `41.2355` edge `0.6913` maxDD `-0.1986`
- `news_risk_high->equity_4h` score `10.8615` n `31` status `ready` deltaP `36.4625` edge `0.7101` maxDD `-2.178`
- `news_risk_high->crypto_major_4h` score `7.5979` n `31` status `ready` deltaP `19.2171` edge `0.9877` maxDD `-7.6714`
- `news_risk_high->index_24h` score `6.0733` n `31` status `ready` deltaP `44.7917` edge `0.2075` maxDD `0.0`
- `news_risk_high->fx_24h` score `5.2966` n `31` status `ready` deltaP `44.8365` edge `0.1553` maxDD `-0.0262`
- `news_risk_high->equity_1h` score `3.7867` n `31` status `ready` deltaP `19.5383` edge `0.204` maxDD `-0.1621`
- `news_risk_high->index_4h` score `3.2824` n `31` status `ready` deltaP `35.243` edge `0.0646` maxDD `-0.4146`
- `news_risk_high->crypto_major_1h` score `2.7767` n `31` status `ready` deltaP `12.5555` edge `0.3184` maxDD `-1.6897`
- `news_risk_high->index_1h` score `2.6183` n `31` status `ready` deltaP `30.9446` edge `0.0204` maxDD `-0.0136`
- `market_context_high->fx_4h` score `2.5944` n `45` status `ready` deltaP `31.7649` edge `0.0329` maxDD `-0.2774`
- `news_risk_high->crypto_alt_1h` score `2.3813` n `31` status `ready` deltaP `12.4058` edge `0.2583` maxDD `-1.5232`
- `news_risk_high->metal_1h` score `1.5999` n `31` status `ready` deltaP `30.3312` edge `0.0308` maxDD `-0.2315`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
