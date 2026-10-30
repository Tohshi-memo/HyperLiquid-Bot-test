# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-30T00:07:30.087386+00:00`
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

- `market_context_high->unknown_24h` score `1631.6126` n `134` status `ready` deltaP `-2.7908` edge `136.0293` maxDD `-1.1049`
- `market_context_high->unknown_4h` score `51.2778` n `134` status `ready` deltaP `5.7517` edge `4.2481` maxDD `-0.3966`
- `market_context_high->index_24h` score `2.5742` n `134` status `ready` deltaP `30.2291` edge `0.0313` maxDD `-0.1315`
- `market_context_high->metal_1h` score `0.2894` n `134` status `ready` deltaP `9.706` edge `0.0103` maxDD `-0.3659`
- `market_context_high->commodity_4h` score `0.1023` n `134` status `ready` deltaP `11.9562` edge `0.0507` maxDD `-1.0837`
- `market_context_high->metal_4h` score `0.0515` n `134` status `ready` deltaP `12.6297` edge `0.012` maxDD `-1.8344`
- `market_context_high->crypto_major_1h` score `-0.0802` n `134` status `ready` deltaP `6.417` edge `0.0533` maxDD `-5.2213`
- `market_context_high->fx_1h` score `-0.1446` n `134` status `ready` deltaP `2.8309` edge `-0.0016` maxDD `-0.1986`
- `market_context_high->equity_1h` score `-0.2179` n `134` status `ready` deltaP `2.536` edge `0.0525` maxDD `-2.3383`
- `market_context_high->commodity_1h` score `-0.3607` n `134` status `ready` deltaP `1.1954` edge `0.0134` maxDD `-0.4475`
- `market_context_high->fx_4h` score `-0.6161` n `134` status `ready` deltaP `-2.15` edge `-0.0048` maxDD `-0.4545`
- `market_context_high->crypto_alt_1h` score `-0.8509` n `134` status `ready` deltaP `3.2979` edge `0.0554` maxDD `-8.251`
- `market_context_high->equity_4h` score `-0.8895` n `134` status `ready` deltaP `-0.81` edge `0.0498` maxDD `-6.008`
- `market_context_high->index_1h` score `-0.9397` n `134` status `ready` deltaP `-3.1437` edge `-0.0015` maxDD `-1.1344`
- `market_context_high->equity_24h` score `-0.9633` n `134` status `ready` deltaP `12.6659` edge `0.111` maxDD `-14.0571`
- `market_context_high->fx_24h` score `-1.3124` n `134` status `ready` deltaP `2.2362` edge `0.0088` maxDD `-0.9792`
- `market_context_high->metal_24h` score `-1.5734` n `134` status `ready` deltaP `3.9257` edge `0.0368` maxDD `-10.5088`
- `market_context_high->crypto_major_4h` score `-1.9316` n `134` status `ready` deltaP `6.7893` edge `0.0366` maxDD `-19.0267`
- `market_context_high->index_4h` score `-2.2697` n `134` status `ready` deltaP `-5.6721` edge `-0.0193` maxDD `-3.5621`
- `market_context_high->commodity_24h` score `-4.1449` n `134` status `ready` deltaP `4.203` edge `-0.0004` maxDD `-24.0547`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
