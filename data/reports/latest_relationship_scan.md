# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-27T06:37:27.916175+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `11760`

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

- `news_risk_high->unknown_24h` score `1708.6296` n `118` status `ready` deltaP `1.2153` edge `142.3777` maxDD `0.0`
- `market_context_high->unknown_1h` score `103.7794` n `48` status `ready` deltaP `10.3418` edge `8.584` maxDD `-0.0395`
- `market_context_high->crypto_major_24h` score `52.5585` n `44` status `ready` deltaP `30.1926` edge `4.2137` maxDD `-2.4756`
- `market_context_high->crypto_alt_24h` score `28.6626` n `44` status `ready` deltaP `14.9148` edge `2.3271` maxDD `-2.7051`
- `market_context_high->equity_24h` score `28.0228` n `44` status `ready` deltaP `36.0954` edge `2.126` maxDD `-2.1786`
- `market_context_high->index_24h` score `7.9101` n `44` status `ready` deltaP `33.4912` edge `0.4447` maxDD `-0.3705`
- `market_context_high->metal_24h` score `3.877` n `44` status `ready` deltaP `34.2171` edge `0.1188` maxDD `-0.2401`
- `market_context_high->index_4h` score `3.1556` n `44` status `ready` deltaP `35.2411` edge `0.0351` maxDD `-0.2323`
- `market_context_high->equity_4h` score `2.7449` n `44` status `ready` deltaP `15.6873` edge `0.1618` maxDD `-1.3444`
- `market_context_high->crypto_alt_4h` score `1.0082` n `44` status `ready` deltaP `7.7883` edge `0.0947` maxDD `-3.3417`
- `market_context_high->equity_1h` score `0.9803` n `48` status `ready` deltaP `11.7266` edge `0.0438` maxDD `-1.5564`
- `market_context_high->crypto_major_4h` score `0.8514` n `44` status `ready` deltaP `6.9152` edge `0.1153` maxDD `-5.2359`
- `market_context_high->crypto_major_1h` score `0.8326` n `48` status `ready` deltaP `8.0215` edge `0.1017` maxDD `-4.8632`
- `news_risk_high->metal_24h` score `0.7657` n `118` status `ready` deltaP `16.2664` edge `0.1243` maxDD `-6.8481`
- `news_risk_high->index_24h` score `0.6433` n `118` status `ready` deltaP `13.73` edge `0.0316` maxDD `-2.2287`
- `market_context_high->crypto_alt_1h` score `0.6058` n `48` status `ready` deltaP `7.4102` edge `0.09` maxDD `-5.7799`
- `market_context_high->index_1h` score `0.5953` n `48` status `ready` deltaP `9.7929` edge `0.008` maxDD `-0.2275`
- `market_context_high->fx_1h` score `0.36` n `48` status `ready` deltaP `11.1901` edge `0.0072` maxDD `-0.1854`
- `market_context_high->metal_1h` score `0.1473` n `48` status `ready` deltaP `5.0898` edge `0.0102` maxDD `-0.215`
- `news_risk_high->index_1h` score `-0.191` n `142` status `ready` deltaP `1.5476` edge `0.0029` maxDD `-0.3305`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
