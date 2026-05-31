# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-31T13:07:20.565519+00:00`
- Price records: `672`
- Market context records: `2460`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9222`

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

- `news_risk_high->crypto_alt_24h` score `21.1893` n `36` status `ready` deltaP `45.4861` edge `1.5214` maxDD `-4.3757`
- `news_risk_high->metal_24h` score `20.8021` n `36` status `ready` deltaP `55.5555` edge `1.4071` maxDD `-3.1836`
- `news_risk_high->equity_24h` score `17.4882` n `36` status `ready` deltaP `29.3403` edge `1.2932` maxDD `-2.1831`
- `news_risk_high->crypto_major_24h` score `11.5733` n `36` status `ready` deltaP `21.1806` edge `0.8813` maxDD `-3.3119`
- `news_risk_high->index_24h` score `7.7287` n `36` status `ready` deltaP `21.7014` edge `0.5246` maxDD `-1.3507`
- `news_risk_high->unknown_24h` score `7.362` n `36` status `ready` deltaP `24.4791` edge `0.4729` maxDD `-1.4744`
- `market_context_high->unknown_24h` score `5.8299` n `110` status `ready` deltaP `21.8024` edge `0.3733` maxDD `-1.626`
- `news_risk_high->commodity_4h` score `4.268` n `36` status `ready` deltaP `25.0339` edge `0.2559` maxDD `-3.0367`
- `market_context_high->crypto_alt_4h` score `4.054` n `135` status `ready` deltaP `20.6753` edge `0.4679` maxDD `-15.4319`
- `market_context_high->crypto_major_4h` score `3.9986` n `135` status `ready` deltaP `18.2576` edge `0.3925` maxDD `-10.1468`
- `news_risk_high->fx_24h` score `3.6724` n `36` status `ready` deltaP `37.5` edge `0.0745` maxDD `-0.1442`
- `market_context_high->crypto_major_24h` score `2.4079` n `110` status `ready` deltaP `11.6351` edge `0.6204` maxDD `-25.1408`
- `news_risk_high->fx_4h` score `1.9252` n `36` status `ready` deltaP `24.4241` edge `0.016` maxDD `-0.1382`
- `news_risk_high->unknown_1h` score `1.7027` n `36` status `ready` deltaP `21.0246` edge `0.0449` maxDD `-1.4536`
- `news_risk_high->metal_4h` score `1.6809` n `36` status `ready` deltaP `8.2656` edge `0.2846` maxDD `-5.6032`
- `market_context_high->unknown_4h` score `1.4905` n `135` status `ready` deltaP `9.65` edge `0.1583` maxDD `-3.2074`
- `market_context_high->index_24h` score `1.2588` n `110` status `ready` deltaP `6.3983` edge `0.1087` maxDD `-0.7163`
- `news_risk_high->equity_4h` score `0.9521` n `36` status `ready` deltaP `-13.9566` edge `0.3196` maxDD `-4.0257`
- `market_context_high->crypto_major_1h` score `0.8477` n `136` status `ready` deltaP `9.0833` edge `0.1295` maxDD `-4.2199`
- `market_context_high->crypto_alt_1h` score `0.6577` n `136` status `ready` deltaP `7.3265` edge `0.1247` maxDD `-6.1656`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
