# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-27T15:52:25.751374+00:00`
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

- `news_risk_high->unknown_24h` score `743.4936` n `136` status `ready` deltaP `1.2153` edge `61.9497` maxDD `0.0`
- `market_context_high->unknown_1h` score `181.7802` n `37` status `ready` deltaP `10.0219` edge `15.0862` maxDD `-0.0395`
- `market_context_high->crypto_major_24h` score `57.7076` n `33` status `ready` deltaP `30.4766` edge `4.6409` maxDD `-2.4756`
- `market_context_high->equity_24h` score `31.0618` n `33` status `ready` deltaP `35.3378` edge `2.3843` maxDD `-2.1786`
- `market_context_high->crypto_alt_24h` score `28.0937` n `33` status `ready` deltaP `15.1989` edge `2.2778` maxDD `-2.7051`
- `market_context_high->index_24h` score `8.6556` n `33` status `ready` deltaP `33.2544` edge `0.5084` maxDD `-0.3705`
- `market_context_high->metal_24h` score `4.3821` n `33` status `ready` deltaP `39.031` edge `0.1288` maxDD `-0.2401`
- `market_context_high->equity_4h` score `4.1084` n `37` status `ready` deltaP `25.206` edge `0.2078` maxDD `-1.3444`
- `market_context_high->crypto_alt_4h` score `4.0723` n `37` status `ready` deltaP `19.7594` edge `0.2619` maxDD `-3.3417`
- `market_context_high->index_4h` score `3.311` n `37` status `ready` deltaP `36.058` edge `0.0426` maxDD `-0.2323`
- `market_context_high->crypto_major_4h` score `1.8657` n `37` status `ready` deltaP `9.1835` edge `0.1847` maxDD `-5.2359`
- `market_context_high->equity_1h` score `1.5915` n `37` status `ready` deltaP `18.3323` edge `0.0507` maxDD `-1.5564`
- `news_risk_high->index_24h` score `1.0107` n `136` status `ready` deltaP `17.1671` edge `0.0393` maxDD `-2.2287`
- `market_context_high->index_1h` score `0.9056` n `37` status `ready` deltaP `12.9269` edge `0.0088` maxDD `-0.2275`
- `market_context_high->fx_1h` score `0.6674` n `37` status `ready` deltaP `12.5951` edge `0.0073` maxDD `-0.1854`
- `market_context_high->crypto_major_1h` score `0.6087` n `37` status `ready` deltaP `9.9167` edge `0.0704` maxDD `-4.8632`
- `news_risk_high->metal_24h` score `0.5366` n `136` status `ready` deltaP `16.1255` edge `0.1227` maxDD `-6.8392`
- `market_context_high->metal_4h` score `0.3777` n `37` status `ready` deltaP `9.5419` edge `0.0227` maxDD `-0.3647`
- `market_context_high->crypto_alt_1h` score `0.2406` n `37` status `ready` deltaP `9.7751` edge `0.0546` maxDD `-5.7799`
- `news_risk_high->index_1h` score `-0.0755` n `139` status `ready` deltaP `2.9133` edge `0.0033` maxDD `-0.3214`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
