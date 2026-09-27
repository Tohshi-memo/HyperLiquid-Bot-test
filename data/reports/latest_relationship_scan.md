# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-27T16:07:33.508607+00:00`
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

- `news_risk_high->unknown_24h` score `741.0348` n `136` status `ready` deltaP `1.2153` edge `61.7448` maxDD `0.0`
- `market_context_high->unknown_1h` score `189.8598` n `36` status `ready` deltaP `9.9468` edge `15.76` maxDD `-0.0395`
- `market_context_high->crypto_major_24h` score `57.6035` n `32` status `ready` deltaP `30.5556` edge `4.6317` maxDD `-2.4756`
- `market_context_high->equity_24h` score `31.0663` n `32` status `ready` deltaP `35.2431` edge `2.3853` maxDD `-2.1786`
- `market_context_high->crypto_alt_24h` score `27.4509` n `32` status `ready` deltaP `15.2778` edge `2.2237` maxDD `-2.7051`
- `market_context_high->index_24h` score `8.6528` n `32` status `ready` deltaP `33.1597` edge `0.5088` maxDD `-0.3705`
- `market_context_high->metal_24h` score `4.3333` n `32` status `ready` deltaP `38.5417` edge `0.128` maxDD `-0.2401`
- `market_context_high->equity_4h` score `4.135` n `36` status `ready` deltaP `24.9831` edge `0.2115` maxDD `-1.3444`
- `market_context_high->crypto_alt_4h` score `3.6692` n `36` status `ready` deltaP `19.4613` edge `0.2303` maxDD `-3.3417`
- `market_context_high->index_4h` score `3.322` n `36` status `ready` deltaP `36.0603` edge `0.0435` maxDD `-0.2323`
- `market_context_high->crypto_major_4h` score `1.597` n `36` status `ready` deltaP `8.435` edge `0.1673` maxDD `-5.2359`
- `market_context_high->equity_1h` score `1.5123` n `36` status `ready` deltaP `17.5815` edge `0.0491` maxDD `-1.5564`
- `news_risk_high->index_24h` score `1.0227` n `136` status `ready` deltaP `17.1671` edge `0.0403` maxDD `-2.2287`
- `market_context_high->index_1h` score `0.8264` n `36` status `ready` deltaP `12.026` edge `0.0082` maxDD `-0.2275`
- `news_risk_high->metal_24h` score `0.5516` n `136` status `ready` deltaP `16.2991` edge `0.1228` maxDD `-6.8392`
- `market_context_high->metal_4h` score `0.4906` n `36` status `ready` deltaP `11.0434` edge `0.023` maxDD `-0.3647`
- `market_context_high->fx_1h` score `0.369` n `36` status `ready` deltaP `11.3939` edge `0.007` maxDD `-0.1854`
- `market_context_high->crypto_major_1h` score `0.263` n `36` status `ready` deltaP `8.8656` edge `0.0486` maxDD `-4.8632`
- `news_risk_high->index_1h` score `-0.0755` n `139` status `ready` deltaP `2.9133` edge `0.0033` maxDD `-0.3214`
- `news_risk_high->crypto_alt_1h` score `-0.0761` n `139` status `ready` deltaP `4.6224` edge `0.0539` maxDD `-4.2849`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
