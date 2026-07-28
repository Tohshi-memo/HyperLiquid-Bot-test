# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-28T01:07:29.808799+00:00`
- Price records: `672`
- Market context records: `8147`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11842`

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

- `market_context_high->equity_24h` score `24.0687` n `82` status `ready` deltaP `44.0633` edge `1.803` maxDD `-4.9489`
- `market_context_high->equity_4h` score `10.1947` n `83` status `ready` deltaP `36.9637` edge `0.6266` maxDD `-0.5442`
- `market_context_high->metal_24h` score `8.9121` n `82` status `ready` deltaP `38.0208` edge `0.4892` maxDD `0.0`
- `news_risk_high->equity_4h` score `8.056` n `43` status `ready` deltaP `31.3599` edge `0.4828` maxDD `-0.6428`
- `news_risk_high->crypto_major_4h` score `4.8156` n `43` status `ready` deltaP `18.0517` edge `0.3415` maxDD `-2.1767`
- `market_context_high->index_24h` score `4.1984` n `82` status `ready` deltaP `25.7538` edge `0.2452` maxDD `-1.3621`
- `market_context_high->index_4h` score `3.986` n `83` status `ready` deltaP `35.2722` edge `0.1013` maxDD `-0.0092`
- `news_risk_high->equity_1h` score `3.7331` n `43` status `ready` deltaP `29.0802` edge `0.1481` maxDD `-1.1366`
- `market_context_high->equity_1h` score `3.3215` n `83` status `ready` deltaP `17.6485` edge `0.1894` maxDD `-1.088`
- `market_context_high->metal_4h` score `2.6764` n `83` status `ready` deltaP `24.6253` edge `0.1211` maxDD `-0.979`
- `market_context_high->crypto_alt_4h` score `2.5718` n `83` status `ready` deltaP `12.68` edge `0.2415` maxDD `-3.9374`
- `news_risk_high->index_4h` score `2.5439` n `43` status `ready` deltaP `21.4868` edge `0.0878` maxDD `-0.191`
- `market_context_high->crypto_major_4h` score `2.3212` n `83` status `ready` deltaP `14.4652` edge `0.2688` maxDD `-6.7444`
- `market_context_high->fx_24h` score `2.2385` n `82` status `ready` deltaP `30.2549` edge `0.0552` maxDD `-0.6283`
- `market_context_high->commodity_24h` score `1.8503` n `82` status `ready` deltaP `33.4138` edge `0.303` maxDD `-15.7497`
- `market_context_high->index_1h` score `1.725` n `83` status `ready` deltaP `19.8867` edge `0.0308` maxDD `-0.2368`
- `news_risk_high->metal_4h` score `1.3589` n `43` status `ready` deltaP `13.6698` edge `0.0689` maxDD `-0.7433`
- `news_risk_high->crypto_major_1h` score `1.2863` n `43` status `ready` deltaP `5.8836` edge `0.1077` maxDD `-1.1783`
- `market_context_high->metal_1h` score `1.0468` n `83` status `ready` deltaP `13.7202` edge `0.0336` maxDD `-0.6936`
- `market_context_high->crypto_major_1h` score `0.8307` n `83` status `ready` deltaP `12.6362` edge `0.0633` maxDD `-1.6171`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
