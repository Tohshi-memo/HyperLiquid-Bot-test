# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-27T06:22:27.431374+00:00`
- Price records: `672`
- Market context records: `8065`
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
- `market_context_high->equity_4h` score `8.3602` n `87` status `ready` deltaP `32.4205` edge `0.5285` maxDD `-2.5032`
- `market_context_high->metal_24h` score `8.2688` n `79` status `ready` deltaP `35.8752` edge `0.4499` maxDD `0.0`
- `news_risk_high->unknown_1h` score `4.3665` n `34` status `ready` deltaP `5.3364` edge `0.356` maxDD `-0.8826`
- `market_context_high->commodity_24h` score `3.8091` n `79` status `ready` deltaP `31.4986` edge `0.2824` maxDD `-9.3304`
- `news_risk_high->equity_1h` score `3.668` n `34` status `ready` deltaP `30.354` edge `0.1349` maxDD `-1.1944`
- `market_context_high->index_4h` score `3.2785` n `87` status `ready` deltaP `31.5881` edge `0.0814` maxDD `-0.5022`
- `market_context_high->index_24h` score `2.7607` n `79` status `ready` deltaP `16.6027` edge `0.1864` maxDD `-1.3621`
- `market_context_high->metal_4h` score `2.4032` n `87` status `ready` deltaP `22.2158` edge `0.1144` maxDD `-0.979`
- `market_context_high->equity_1h` score `2.391` n `87` status `ready` deltaP `15.1748` edge `0.1414` maxDD `-2.1322`
- `market_context_high->fx_24h` score `2.2508` n `79` status `ready` deltaP `30.4828` edge `0.0547` maxDD `-0.6283`
- `news_risk_high->crypto_alt_1h` score `1.6662` n `34` status `ready` deltaP `11.7647` edge `0.0799` maxDD `-0.2249`
- `news_risk_high->crypto_major_1h` score `1.6092` n `34` status `ready` deltaP `7.9253` edge `0.1046` maxDD `-0.5338`
- `market_context_high->index_1h` score `1.1015` n `87` status `ready` deltaP `14.6724` edge `0.0207` maxDD `-0.4716`
- `news_risk_high->index_1h` score `0.9618` n `34` status `ready` deltaP `11.5622` edge `0.0236` maxDD `-0.3089`
- `market_context_high->metal_1h` score `0.7895` n `87` status `ready` deltaP `11.2241` edge `0.0288` maxDD `-0.6936`
- `market_context_high->crypto_major_1h` score `0.4668` n `87` status `ready` deltaP `8.8719` edge `0.0208` maxDD `-1.6171`
- `news_risk_high->fx_1h` score `0.3807` n `34` status `ready` deltaP `7.6788` edge `0.0063` maxDD `-0.0611`
- `market_context_high->crypto_alt_4h` score `0.24` n `87` status `ready` deltaP `3.4378` edge `0.1088` maxDD `-3.9374`
- `market_context_high->crypto_major_4h` score `0.2012` n `87` status `ready` deltaP `6.5812` edge `0.1447` maxDD `-6.7444`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
