# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-30T01:22:24.999966+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `6714`

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

- `market_context_high->unknown_24h` score `1649.1158` n `134` status `ready` deltaP `-2.7908` edge `137.4879` maxDD `-1.1049`
- `market_context_high->unknown_4h` score `41.3319` n `134` status `ready` deltaP `5.4468` edge `3.4213` maxDD `-0.3966`
- `market_context_high->index_24h` score `2.694` n `134` status `ready` deltaP `31.0971` edge `0.0355` maxDD `-0.1315`
- `market_context_high->metal_1h` score `0.2816` n `134` status `ready` deltaP `9.5563` edge `0.0103` maxDD `-0.3659`
- `market_context_high->commodity_4h` score `0.1765` n `134` status `ready` deltaP `12.7184` edge `0.0518` maxDD `-1.0837`
- `market_context_high->crypto_major_1h` score `0.0685` n `134` status `ready` deltaP `7.0158` edge `0.0617` maxDD `-5.2213`
- `market_context_high->metal_4h` score `0.0649` n `134` status `ready` deltaP `12.7822` edge `0.0127` maxDD `-1.8344`
- `market_context_high->equity_1h` score `-0.0788` n `134` status `ready` deltaP `3.1348` edge `0.0601` maxDD `-2.3383`
- `market_context_high->fx_1h` score `-0.1532` n `134` status `ready` deltaP `2.6812` edge `-0.0017` maxDD `-0.1986`
- `market_context_high->commodity_1h` score `-0.3116` n `134` status `ready` deltaP `1.6445` edge `0.0145` maxDD `-0.4475`
- `market_context_high->equity_24h` score `-0.3515` n `134` status `ready` deltaP `13.5339` edge `0.1562` maxDD `-14.0571`
- `market_context_high->fx_4h` score `-0.6066` n `134` status `ready` deltaP `-1.9976` edge `-0.0046` maxDD `-0.4545`
- `market_context_high->equity_4h` score `-0.6969` n `134` status `ready` deltaP `-0.0478` edge `0.0694` maxDD `-6.008`
- `market_context_high->crypto_alt_1h` score `-0.7058` n `134` status `ready` deltaP `3.8967` edge `0.07` maxDD `-8.251`
- `market_context_high->index_1h` score `-0.8929` n `134` status `ready` deltaP `-2.6946` edge `-0.0006` maxDD `-1.1344`
- `market_context_high->fx_24h` score `-1.3732` n `134` status `ready` deltaP `1.7154` edge `0.0072` maxDD `-0.9792`
- `market_context_high->metal_24h` score `-1.5391` n `134` status `ready` deltaP `3.9257` edge `0.0412` maxDD `-10.5088`
- `market_context_high->crypto_major_4h` score `-1.6946` n `134` status `ready` deltaP `7.5515` edge `0.0619` maxDD `-19.0267`
- `market_context_high->index_4h` score `-2.1847` n `134` status `ready` deltaP `-4.9099` edge `-0.0173` maxDD `-3.5621`
- `market_context_high->commodity_24h` score `-4.0428` n `134` status `ready` deltaP `5.071` edge `0.0069` maxDD `-24.0547`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
