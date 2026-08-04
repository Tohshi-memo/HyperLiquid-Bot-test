# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-04T02:37:28.364808+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `64`

- Symbol pattern count: `7932`

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

- `market_context_high->unknown_24h` score `37.3791` n `46` status `ready` deltaP `26.2983` edge `2.9439` maxDD `-0.0103`
- `market_context_high->crypto_alt_24h` score `10.1383` n `46` status `ready` deltaP `47.2977` edge `0.5469` maxDD `-0.3889`
- `market_context_high->unknown_4h` score `8.9026` n `79` status `ready` deltaP `7.1203` edge `0.7418` maxDD `-1.4578`
- `market_context_high->commodity_24h` score `8.4129` n `46` status `ready` deltaP `39.8248` edge `0.4535` maxDD `-0.434`
- `market_context_high->commodity_4h` score `1.0417` n `79` status `ready` deltaP `13.596` edge `0.0808` maxDD `-2.7703`
- `news_risk_high->fx_24h` score `1.0114` n `31` status `ready` deltaP `12.0184` edge `0.0694` maxDD `-1.5526`
- `news_risk_high->commodity_1h` score `0.8213` n `31` status `ready` deltaP `18.191` edge `0.0052` maxDD `-0.6947`
- `market_context_high->fx_1h` score `0.3006` n `88` status `ready` deltaP `9.3291` edge `-0.0023` maxDD `-0.7878`
- `market_context_high->fx_4h` score `0.287` n `79` status `ready` deltaP `17.1291` edge `0.0086` maxDD `-1.8797`
- `market_context_high->commodity_1h` score `0.2816` n `88` status `ready` deltaP `6.1309` edge `0.0242` maxDD `-1.3282`
- `news_risk_high->fx_4h` score `0.0497` n `31` status `ready` deltaP `3.3684` edge `0.0342` maxDD `-0.356`
- `news_risk_high->index_1h` score `-0.2175` n `31` status `ready` deltaP `0.0483` edge `-0.0084` maxDD `-0.5845`
- `news_risk_high->crypto_alt_1h` score `-0.2352` n `31` status `ready` deltaP `9.7933` edge `-0.0314` maxDD `-3.1233`
- `news_risk_high->commodity_4h` score `-0.2866` n `31` status `ready` deltaP `8.3694` edge `-0.0296` maxDD `-1.6728`
- `news_risk_high->index_4h` score `-0.2949` n `31` status `ready` deltaP `-3.7225` edge `0.0383` maxDD `-0.3783`
- `news_risk_high->fx_1h` score `-0.3564` n `31` status `ready` deltaP `-2.5111` edge `0.0022` maxDD `-0.1588`
- `market_context_high->index_1h` score `-0.4367` n `88` status `ready` deltaP `2.0278` edge `-0.0161` maxDD `-1.6054`
- `news_risk_high->unknown_4h` score `-0.473` n `31` status `ready` deltaP `-1.2097` edge `-0.0037` maxDD `-1.5766`
- `market_context_high->metal_1h` score `-0.4988` n `88` status `ready` deltaP `-1.0207` edge `-0.0077` maxDD `-1.6224`
- `market_context_high->metal_4h` score `-0.7704` n `79` status `ready` deltaP `2.1901` edge `0.0101` maxDD `-3.211`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
