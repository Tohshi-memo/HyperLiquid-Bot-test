# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-27T06:37:28.340877+00:00`
- Price records: `672`
- Market context records: `8066`
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

- `market_context_high->equity_24h` score `20.0292` n `79` status `ready` deltaP `35.9739` edge `1.5203` maxDD `-4.9489`
- `market_context_high->equity_4h` score `8.3542` n `87` status `ready` deltaP `32.4205` edge `0.528` maxDD `-2.5032`
- `market_context_high->metal_24h` score `8.2724` n `79` status `ready` deltaP `35.8752` edge `0.4502` maxDD `0.0`
- `news_risk_high->unknown_1h` score `4.2473` n `35` status `ready` deltaP `6.5312` edge `0.3381` maxDD `-0.8826`
- `market_context_high->commodity_24h` score `3.8199` n `79` status `ready` deltaP `31.4986` edge `0.2833` maxDD `-9.3304`
- `news_risk_high->equity_1h` score `3.7292` n `35` status `ready` deltaP `30.6245` edge `0.1382` maxDD `-1.1944`
- `market_context_high->index_4h` score `3.2785` n `87` status `ready` deltaP `31.5881` edge `0.0814` maxDD `-0.5022`
- `market_context_high->index_24h` score `2.7619` n `79` status `ready` deltaP `16.6027` edge `0.1865` maxDD `-1.3621`
- `market_context_high->metal_4h` score `2.4056` n `87` status `ready` deltaP `22.2158` edge `0.1146` maxDD `-0.979`
- `market_context_high->equity_1h` score `2.3694` n `87` status `ready` deltaP `15.0251` edge `0.1406` maxDD `-2.1322`
- `market_context_high->fx_24h` score `2.2309` n `79` status `ready` deltaP `30.3095` edge `0.0542` maxDD `-0.6283`
- `news_risk_high->crypto_major_1h` score `1.7645` n `35` status `ready` deltaP `8.9521` edge `0.1107` maxDD `-0.5338`
- `news_risk_high->crypto_alt_1h` score `1.7573` n `35` status `ready` deltaP `12.7074` edge `0.0812` maxDD `-0.2249`
- `market_context_high->index_1h` score `1.0883` n `87` status `ready` deltaP `14.5227` edge `0.0206` maxDD `-0.4716`
- `news_risk_high->index_1h` score `1.0269` n `35` status `ready` deltaP `12.4209` edge `0.0233` maxDD `-0.3089`
- `market_context_high->metal_1h` score `0.7763` n `87` status `ready` deltaP `11.0744` edge `0.0287` maxDD `-0.6936`
- `news_risk_high->fx_1h` score `0.4816` n `35` status `ready` deltaP `8.7896` edge `0.0073` maxDD `-0.0611`
- `market_context_high->crypto_major_1h` score `0.4404` n `87` status `ready` deltaP `8.7222` edge `0.0196` maxDD `-1.6171`
- `market_context_high->crypto_alt_4h` score `0.2532` n `87` status `ready` deltaP `3.4378` edge `0.1099` maxDD `-3.9374`
- `market_context_high->crypto_major_4h` score `0.1964` n `87` status `ready` deltaP `6.5812` edge `0.1443` maxDD `-6.7444`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
