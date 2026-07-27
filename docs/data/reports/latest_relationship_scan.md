# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-27T06:52:26.975341+00:00`
- Price records: `672`
- Market context records: `8067`
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

- `market_context_high->equity_24h` score `20.0352` n `79` status `ready` deltaP `35.9739` edge `1.5208` maxDD `-4.9489`
- `market_context_high->equity_4h` score `8.3542` n `87` status `ready` deltaP `32.4205` edge `0.528` maxDD `-2.5032`
- `market_context_high->metal_24h` score `8.2772` n `79` status `ready` deltaP `35.8752` edge `0.4506` maxDD `0.0`
- `news_risk_high->unknown_1h` score `3.9143` n `36` status `ready` deltaP `5.0233` edge `0.3204` maxDD `-0.8826`
- `market_context_high->commodity_24h` score `3.8319` n `79` status `ready` deltaP `31.4986` edge `0.2843` maxDD `-9.3304`
- `news_risk_high->equity_1h` score `3.7778` n `36` status `ready` deltaP `30.8716` edge `0.1406` maxDD `-1.1944`
- `market_context_high->index_4h` score `3.2797` n `87` status `ready` deltaP `31.5881` edge `0.0815` maxDD `-0.5022`
- `market_context_high->index_24h` score `2.7655` n `79` status `ready` deltaP `16.6027` edge `0.1868` maxDD `-1.3621`
- `market_context_high->metal_4h` score `2.4092` n `87` status `ready` deltaP `22.2158` edge `0.1149` maxDD `-0.979`
- `market_context_high->equity_1h` score `2.3526` n `87` status `ready` deltaP `14.8754` edge `0.1402` maxDD `-2.1322`
- `market_context_high->fx_24h` score `2.2123` n `79` status `ready` deltaP `30.1362` edge `0.0538` maxDD `-0.6283`
- `news_risk_high->crypto_major_1h` score `1.8678` n `36` status `ready` deltaP `9.9135` edge `0.1129` maxDD `-0.5338`
- `news_risk_high->crypto_alt_1h` score `1.596` n `36` status `ready` deltaP `11.1111` edge `0.0784` maxDD `-0.2249`
- `news_risk_high->index_1h` score `1.0888` n `36` status `ready` deltaP `13.2236` edge `0.0231` maxDD `-0.3089`
- `market_context_high->index_1h` score `1.0763` n `87` status `ready` deltaP `14.373` edge `0.0206` maxDD `-0.4716`
- `market_context_high->metal_1h` score `0.7751` n `87` status `ready` deltaP `11.0744` edge `0.0286` maxDD `-0.6936`
- `news_risk_high->fx_1h` score `0.5757` n `36` status `ready` deltaP `9.8303` edge `0.0082` maxDD `-0.0611`
- `market_context_high->crypto_major_1h` score `0.4212` n `87` status `ready` deltaP `8.5725` edge `0.019` maxDD `-1.6171`
- `market_context_high->crypto_alt_4h` score `0.2724` n `87` status `ready` deltaP `3.4378` edge `0.1115` maxDD `-3.9374`
- `market_context_high->crypto_major_4h` score `0.1952` n `87` status `ready` deltaP `6.5812` edge `0.1442` maxDD `-6.7444`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
