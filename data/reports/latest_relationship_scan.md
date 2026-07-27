# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-27T07:07:27.461145+00:00`
- Price records: `672`
- Market context records: `8068`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11784`

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

- `market_context_high->equity_24h` score `20.0424` n `79` status `ready` deltaP `35.9739` edge `1.5214` maxDD `-4.9489`
- `market_context_high->equity_4h` score `8.3494` n `87` status `ready` deltaP `32.4205` edge `0.5276` maxDD `-2.5032`
- `market_context_high->metal_24h` score `8.2796` n `79` status `ready` deltaP `35.8752` edge `0.4508` maxDD `0.0`
- `market_context_high->commodity_24h` score `3.8403` n `79` status `ready` deltaP `31.4986` edge `0.285` maxDD `-9.3304`
- `news_risk_high->equity_1h` score `3.8234` n `37` status `ready` deltaP `31.0973` edge `0.1429` maxDD `-1.1944`
- `news_risk_high->unknown_1h` score `3.5997` n `37` status `ready` deltaP `3.7466` edge `0.3027` maxDD `-0.8826`
- `market_context_high->index_4h` score `3.2797` n `87` status `ready` deltaP `31.5881` edge `0.0815` maxDD `-0.5022`
- `market_context_high->index_24h` score `2.7691` n `79` status `ready` deltaP `16.6027` edge `0.1871` maxDD `-1.3621`
- `market_context_high->metal_4h` score `2.4104` n `87` status `ready` deltaP `22.2158` edge `0.115` maxDD `-0.979`
- `market_context_high->equity_1h` score `2.3346` n `87` status `ready` deltaP `14.7257` edge `0.1397` maxDD `-2.1322`
- `market_context_high->fx_24h` score `2.1948` n `79` status `ready` deltaP `29.9629` edge `0.0535` maxDD `-0.6283`
- `news_risk_high->crypto_major_1h` score `1.6193` n `37` status `ready` deltaP `8.2619` edge `0.1032` maxDD `-0.5338`
- `news_risk_high->crypto_alt_1h` score `1.3298` n `37` status `ready` deltaP `9.6092` edge `0.0677` maxDD `-0.3421`
- `market_context_high->index_1h` score `1.0883` n `87` status `ready` deltaP `14.5227` edge `0.0206` maxDD `-0.4716`
- `news_risk_high->index_1h` score `0.9482` n `37` status `ready` deltaP `11.5715` edge `0.0224` maxDD `-0.3089`
- `market_context_high->metal_1h` score `0.7607` n `87` status `ready` deltaP `10.9247` edge `0.0284` maxDD `-0.6936`
- `news_risk_high->fx_1h` score `0.6718` n `37` status `ready` deltaP `10.9565` edge `0.0087` maxDD `-0.0611`
- `market_context_high->crypto_major_1h` score `0.4212` n `87` status `ready` deltaP `8.5725` edge `0.019` maxDD `-1.6171`
- `market_context_high->crypto_alt_4h` score `0.3014` n `87` status `ready` deltaP `3.5902` edge `0.1129` maxDD `-3.9374`
- `market_context_high->crypto_major_4h` score `0.1904` n `87` status `ready` deltaP `6.5812` edge `0.1438` maxDD `-6.7444`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
