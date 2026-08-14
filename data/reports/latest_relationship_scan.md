# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-14T19:22:25.207213+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11796`

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

- `market_context_high->unknown_24h` score `136.1257` n `128` status `ready` deltaP `-33.2466` edge `11.8567` maxDD `-9.6329`
- `risk_on_high->unknown_24h` score `32.7607` n `32` status `ready` deltaP `-46.5278` edge `4.5853` maxDD `-1.6689`
- `risk_on_and_context->unknown_24h` score `32.7607` n `32` status `ready` deltaP `-46.5278` edge `4.5853` maxDD `-1.6689`
- `news_risk_high->equity_24h` score `10.4289` n `36` status `ready` deltaP `13.368` edge `0.8179` maxDD `-1.0358`
- `news_risk_high->equity_4h` score `7.6741` n `36` status `ready` deltaP `40.3963` edge `0.3702` maxDD `0.0`
- `market_context_high->commodity_24h` score `4.9394` n `128` status `ready` deltaP `27.8645` edge `0.2316` maxDD `-0.1266`
- `risk_on_high->commodity_24h` score `4.5155` n `32` status `ready` deltaP `30.2083` edge `0.1749` maxDD `0.0`
- `risk_on_and_context->commodity_24h` score `4.5155` n `32` status `ready` deltaP `30.2083` edge `0.1749` maxDD `0.0`
- `risk_on_high->crypto_major_24h` score `2.7159` n `32` status `ready` deltaP `19.6181` edge `0.333` maxDD `-6.2481`
- `risk_on_and_context->crypto_major_24h` score `2.7159` n `32` status `ready` deltaP `19.6181` edge `0.333` maxDD `-6.2481`
- `risk_on_high->commodity_4h` score `2.6692` n `32` status `ready` deltaP `18.5213` edge `0.1172` maxDD `-0.1258`
- `risk_on_and_context->commodity_4h` score `2.6692` n `32` status `ready` deltaP `18.5213` edge `0.1172` maxDD `-0.1258`
- `news_risk_high->index_24h` score `2.3866` n `36` status `ready` deltaP `17.1875` edge `0.0843` maxDD `0.0`
- `news_risk_high->index_4h` score `1.9302` n `36` status `ready` deltaP `22.2053` edge `0.026` maxDD `-0.0546`
- `news_risk_high->equity_1h` score `1.7586` n `36` status `ready` deltaP `8.7326` edge `0.1202` maxDD `-0.5496`
- `market_context_high->commodity_4h` score `1.7214` n `128` status `ready` deltaP `16.9588` edge `0.0775` maxDD `-0.7687`
- `risk_on_high->commodity_1h` score `1.2743` n `32` status `ready` deltaP `13.6602` edge `0.0384` maxDD `-0.1957`
- `risk_on_and_context->commodity_1h` score `1.2743` n `32` status `ready` deltaP `13.6602` edge `0.0384` maxDD `-0.1957`
- `risk_on_high->fx_24h` score `1.0947` n `32` status `ready` deltaP `13.1944` edge `0.0217` maxDD `-0.1418`
- `risk_on_and_context->fx_24h` score `1.0947` n `32` status `ready` deltaP `13.1944` edge `0.0217` maxDD `-0.1418`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
