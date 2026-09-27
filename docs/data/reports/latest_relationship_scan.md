# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-27T14:53:22.617500+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `11964`

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

- `news_risk_high->unknown_24h` score `759.7248` n `136` status `ready` deltaP `1.2153` edge `63.3023` maxDD `0.0`
- `market_context_high->unknown_1h` score `156.4224` n `40` status `ready` deltaP `10.2246` edge `12.9717` maxDD `-0.0395`
- `market_context_high->crypto_major_24h` score `58.1738` n `36` status `ready` deltaP `30.0347` edge `4.6827` maxDD `-2.4756`
- `market_context_high->equity_24h` score `31.0412` n `36` status `ready` deltaP `35.5903` edge `2.3809` maxDD `-2.1786`
- `market_context_high->crypto_alt_24h` score `29.9988` n `36` status `ready` deltaP `14.7569` edge `2.4395` maxDD `-2.7051`
- `market_context_high->index_24h` score `8.6199` n `36` status `ready` deltaP `33.3333` edge `0.5049` maxDD `-0.3705`
- `market_context_high->crypto_alt_4h` score `5.2848` n `40` status `ready` deltaP `20.3659` edge `0.3589` maxDD `-3.3417`
- `market_context_high->metal_24h` score `4.4619` n `36` status `ready` deltaP `40.1042` edge `0.1283` maxDD `-0.2401`
- `market_context_high->equity_4h` score `4.0747` n `40` status `ready` deltaP `25.6098` edge `0.2023` maxDD `-1.3444`
- `market_context_high->index_4h` score `3.2683` n `40` status `ready` deltaP `35.8537` edge `0.0404` maxDD `-0.2323`
- `market_context_high->crypto_major_4h` score `2.8071` n `40` status `ready` deltaP `11.0061` edge `0.251` maxDD `-5.2359`
- `market_context_high->equity_1h` score `1.8341` n `40` status `ready` deltaP `20.0599` edge `0.0594` maxDD `-1.5564`
- `market_context_high->crypto_alt_1h` score `1.7007` n `40` status `ready` deltaP `11.8114` edge `0.1519` maxDD `-5.7799`
- `market_context_high->crypto_major_1h` score `1.5462` n `40` status `ready` deltaP `12.1557` edge `0.1336` maxDD `-4.8632`
- `market_context_high->index_1h` score `1.1158` n `40` status `ready` deltaP `15.3593` edge `0.0101` maxDD `-0.2275`
- `news_risk_high->index_24h` score `0.9512` n `136` status `ready` deltaP `16.9935` edge `0.0355` maxDD `-2.2287`
- `market_context_high->fx_1h` score `0.9508` n `40` status `ready` deltaP `15.988` edge `0.0083` maxDD `-0.1854`
- `news_risk_high->metal_24h` score `0.4762` n `136` status `ready` deltaP `15.431` edge `0.1223` maxDD `-6.8392`
- `market_context_high->metal_4h` score `0.4325` n `40` status `ready` deltaP `7.8354` edge `0.0217` maxDD `-0.3647`
- `news_risk_high->index_1h` score `-0.0755` n `139` status `ready` deltaP `2.9133` edge `0.0033` maxDD `-0.3214`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
