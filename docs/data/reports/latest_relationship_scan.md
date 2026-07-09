# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-09T19:07:28.804463+00:00`
- Price records: `672`
- Market context records: `6209`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11110`

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

- `news_risk_high->crypto_alt_24h` score `12.9626` n `32` status `ready` deltaP `42.2194` edge `0.8135` maxDD `-0.5131`
- `news_risk_high->fx_24h` score `6.639` n `32` status `ready` deltaP `57.6531` edge `0.1689` maxDD `0.0`
- `news_risk_high->fx_4h` score `4.0454` n `32` status `ready` deltaP `42.3018` edge `0.0597` maxDD `-0.0345`
- `news_risk_high->crypto_major_24h` score `2.3206` n `32` status `ready` deltaP `15.625` edge `0.2713` maxDD `-4.2368`
- `news_risk_high->fx_1h` score `2.2853` n `32` status `ready` deltaP `27.5449` edge `0.0207` maxDD `-0.1113`
- `market_context_high->unknown_1h` score `1.8489` n `192` status `ready` deltaP `1.3629` edge `0.2458` maxDD `-3.7317`
- `news_risk_high->crypto_major_1h` score `1.3743` n `32` status `ready` deltaP `14.128` edge `0.1287` maxDD `-2.0691`
- `news_risk_high->commodity_24h` score `0.8294` n `32` status `ready` deltaP `19.2389` edge `-0.0386` maxDD `-0.3101`
- `news_risk_high->crypto_alt_1h` score `0.7102` n `32` status `ready` deltaP `9.375` edge `0.0747` maxDD `-1.6923`
- `market_context_high->unknown_4h` score `0.2893` n `192` status `ready` deltaP `-2.6042` edge `0.2947` maxDD `-11.925`
- `market_context_high->metal_24h` score `-0.0486` n `192` status `ready` deltaP `19.8023` edge `0.1186` maxDD `-11.8809`
- `news_risk_high->index_24h` score `-0.2619` n `32` status `ready` deltaP `8.801` edge `-0.0051` maxDD `-2.3058`
- `market_context_high->fx_1h` score `-0.3315` n `192` status `ready` deltaP `0.4616` edge `-0.001` maxDD `-0.5659`
- `market_context_high->commodity_1h` score `-0.6122` n `192` status `ready` deltaP `-1.1976` edge `0.0016` maxDD `-0.5708`
- `market_context_high->metal_4h` score `-0.778` n `192` status `ready` deltaP `1.9944` edge `0.0057` maxDD `-3.4996`
- `news_risk_high->metal_1h` score `-0.8057` n `32` status `ready` deltaP `-3.7425` edge `-0.0286` maxDD `-1.6464`
- `market_context_high->metal_1h` score `-0.8988` n `192` status `ready` deltaP `1.4658` edge `-0.0048` maxDD `-2.0564`
- `market_context_high->crypto_major_1h` score `-0.9254` n `192` status `ready` deltaP `4.2322` edge `0.0299` maxDD `-9.807`
- `market_context_high->crypto_alt_1h` score `-0.9535` n `192` status `ready` deltaP `3.6458` edge `0.0287` maxDD `-9.3536`
- `market_context_high->equity_1h` score `-1.1289` n `192` status `ready` deltaP `-3.0127` edge `-0.0131` maxDD `-4.2573`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
