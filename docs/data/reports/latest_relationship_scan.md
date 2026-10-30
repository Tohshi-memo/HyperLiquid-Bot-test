# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-30T14:52:28.776569+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `7030`

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

- `market_context_high->unknown_24h` score `1614.9444` n `134` status `ready` deltaP `-3.138` edge `134.6426` maxDD `-1.1049`
- `news_risk_high->unknown_1h` score `181.6178` n `53` status `ready` deltaP `-0.3332` edge `15.1496` maxDD `-0.3382`
- `market_context_high->unknown_4h` score `31.9236` n `134` status `ready` deltaP `1.4834` edge `2.6637` maxDD `-0.3966`
- `news_risk_high->crypto_alt_4h` score `7.6238` n `41` status `ready` deltaP `21.4939` edge `0.5317` maxDD `-1.5072`
- `market_context_high->index_24h` score `3.433` n `134` status `ready` deltaP `35.2638` edge `0.0693` maxDD `-0.1315`
- `market_context_high->equity_24h` score `3.4169` n `134` status `ready` deltaP `16.6589` edge `0.4494` maxDD `-14.0571`
- `news_risk_high->crypto_alt_1h` score `0.5823` n `53` status `ready` deltaP `5.7338` edge `0.0814` maxDD `-3.3547`
- `market_context_high->metal_1h` score `0.4047` n `134` status `ready` deltaP `11.203` edge `0.0151` maxDD `-0.3659`
- `market_context_high->metal_4h` score `0.3678` n `134` status `ready` deltaP `15.9834` edge `0.0302` maxDD `-1.8344`
- `market_context_high->equity_1h` score `0.2713` n `134` status `ready` deltaP `5.2306` edge `0.0753` maxDD `-2.3383`
- `market_context_high->commodity_4h` score `0.1699` n `134` status `ready` deltaP `13.1757` edge `0.0482` maxDD `-1.0837`
- `news_risk_high->commodity_4h` score `0.1632` n `41` status `ready` deltaP `0.7622` edge `0.0496` maxDD `-0.7008`
- `market_context_high->crypto_major_1h` score `0.1295` n `134` status `ready` deltaP `7.7643` edge `0.0618` maxDD `-5.2213`
- `market_context_high->equity_4h` score `-0.0553` n `134` status `ready` deltaP `3.3059` edge `0.1293` maxDD `-6.008`
- `market_context_high->fx_1h` score `-0.0598` n `134` status `ready` deltaP `4.3279` edge `-0.0007` maxDD `-0.1986`
- `news_risk_high->index_1h` score `-0.3396` n `53` status `ready` deltaP `4.508` edge `-0.0037` maxDD `-0.5909`
- `market_context_high->commodity_1h` score `-0.3727` n `134` status `ready` deltaP `1.1954` edge `0.0124` maxDD `-0.4475`
- `market_context_high->fx_4h` score `-0.5061` n `134` status `ready` deltaP `-0.3208` edge `-0.0029` maxDD `-0.4545`
- `market_context_high->crypto_alt_1h` score `-0.8173` n `134` status `ready` deltaP `3.2979` edge `0.0597` maxDD `-8.251`
- `market_context_high->index_1h` score `-0.8294` n `134` status `ready` deltaP `-2.0958` edge `0.0007` maxDD `-1.1344`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
