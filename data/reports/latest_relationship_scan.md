# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-30T08:52:31.070320+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `6595`

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

- `market_context_high->unknown_24h` score `1759.9478` n `134` status `ready` deltaP `-2.7908` edge `146.7239` maxDD `-1.1049`
- `market_context_high->unknown_4h` score `34.8045` n `134` status `ready` deltaP `4.0749` edge `2.8865` maxDD `-0.3966`
- `market_context_high->index_24h` score `3.0666` n `134` status `ready` deltaP `33.3541` edge `0.0515` maxDD `-0.1315`
- `market_context_high->equity_24h` score `1.6012` n `134` status `ready` deltaP `16.3117` edge `0.3004` maxDD `-14.0571`
- `market_context_high->metal_1h` score `0.3416` n `134` status `ready` deltaP `10.3048` edge `0.013` maxDD `-0.3659`
- `market_context_high->metal_4h` score `0.2641` n `134` status `ready` deltaP `15.0688` edge `0.023` maxDD `-1.8344`
- `market_context_high->commodity_4h` score `0.2025` n `134` status `ready` deltaP `13.3281` edge `0.0499` maxDD `-1.0837`
- `market_context_high->equity_1h` score `0.137` n `134` status `ready` deltaP `4.4821` edge `0.0691` maxDD `-2.3383`
- `market_context_high->crypto_major_1h` score `0.0001` n `134` status `ready` deltaP `6.8661` edge `0.057` maxDD `-5.2213`
- `market_context_high->fx_1h` score `-0.0964` n `134` status `ready` deltaP `3.7291` edge `-0.0014` maxDD `-0.1986`
- `market_context_high->commodity_1h` score `-0.3308` n `134` status `ready` deltaP `1.6445` edge `0.0129` maxDD `-0.4475`
- `market_context_high->equity_4h` score `-0.4552` n `134` status `ready` deltaP `0.8668` edge `0.0943` maxDD `-6.008`
- `market_context_high->fx_4h` score `-0.5828` n `134` status `ready` deltaP `-1.5403` edge `-0.0046` maxDD `-0.4545`
- `market_context_high->crypto_alt_1h` score `-0.8017` n `134` status `ready` deltaP `3.2979` edge `0.0617` maxDD `-8.251`
- `market_context_high->index_1h` score `-0.8881` n `134` status `ready` deltaP `-2.6946` edge `-0.0002` maxDD `-1.1344`
- `market_context_high->metal_24h` score `-1.3176` n `134` status `ready` deltaP `3.9257` edge `0.0696` maxDD `-10.5088`
- `market_context_high->crypto_major_4h` score `-1.8162` n `134` status `ready` deltaP `7.7039` edge `0.0453` maxDD `-19.0267`
- `market_context_high->fx_24h` score `-1.9063` n `134` status `ready` deltaP `-3.4929` edge `-0.0025` maxDD `-0.9792`
- `market_context_high->index_4h` score `-2.1253` n `134` status `ready` deltaP `-4.4526` edge `-0.0154` maxDD `-3.5621`
- `market_context_high->commodity_24h` score `-3.7515` n `134` status `ready` deltaP `8.5432` edge `0.0211` maxDD `-24.0547`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
