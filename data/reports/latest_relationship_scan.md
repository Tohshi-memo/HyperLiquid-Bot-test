# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-27T05:22:31.575899+00:00`
- Price records: `672`
- Market context records: `8061`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11848`

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

- `market_context_high->equity_24h` score `20.1492` n `75` status `ready` deltaP `35.4338` edge `1.5339` maxDD `-4.9489`
- `market_context_high->equity_4h` score `8.4639` n `87` status `ready` deltaP `32.8778` edge `0.5341` maxDD `-2.5032`
- `market_context_high->metal_24h` score `8.3612` n `75` status `ready` deltaP `35.8752` edge `0.4576` maxDD `0.0`
- `market_context_high->commodity_24h` score `5.3673` n `75` status `ready` deltaP `35.8868` edge `0.3344` maxDD `-6.7764`
- `news_risk_high->unknown_1h` score `5.3435` n `30` status `ready` deltaP `5.7285` edge `0.4348` maxDD `-0.8826`
- `news_risk_high->equity_1h` score `3.5026` n `30` status `ready` deltaP `28.992` edge `0.1302` maxDD `-1.1944`
- `market_context_high->index_4h` score `3.3149` n `87` status `ready` deltaP `31.893` edge `0.0824` maxDD `-0.5022`
- `market_context_high->index_24h` score `2.6089` n `75` status `ready` deltaP `14.7799` edge `0.1859` maxDD `-1.3621`
- `market_context_high->equity_1h` score `2.4785` n `87` status `ready` deltaP `15.7736` edge `0.1447` maxDD `-2.1322`
- `market_context_high->metal_4h` score `2.3436` n `87` status `ready` deltaP `21.606` edge `0.1135` maxDD `-0.979`
- `news_risk_high->crypto_alt_1h` score `1.6242` n `30` status `ready` deltaP `10.2994` edge `0.082` maxDD `-0.2249`
- `news_risk_high->crypto_major_1h` score `1.4617` n `30` status `ready` deltaP `6.2176` edge `0.1037` maxDD `-0.5338`
- `market_context_high->fx_24h` score `1.3781` n `75` status `ready` deltaP `29.1508` edge `0.0527` maxDD `-0.6283`
- `market_context_high->index_1h` score `1.147` n `87` status `ready` deltaP `15.1215` edge `0.0215` maxDD `-0.4716`
- `market_context_high->metal_1h` score `0.8362` n `87` status `ready` deltaP `11.6732` edge `0.0297` maxDD `-0.6936`
- `news_risk_high->index_1h` score `0.5733` n `30` status `ready` deltaP `7.3054` edge `0.0196` maxDD `-0.3089`
- `market_context_high->crypto_major_1h` score `0.5435` n `87` status `ready` deltaP `9.321` edge `0.0242` maxDD `-1.6171`
- `market_context_high->crypto_major_4h` score `0.299` n `87` status `ready` deltaP `7.0385` edge `0.1498` maxDD `-6.7444`
- `market_context_high->crypto_alt_4h` score `0.268` n `87` status `ready` deltaP `3.7427` edge `0.1091` maxDD `-3.9374`
- `news_risk_high->fx_1h` score `0.2175` n `30` status `ready` deltaP `5.5788` edge `0.0067` maxDD `-0.0611`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
