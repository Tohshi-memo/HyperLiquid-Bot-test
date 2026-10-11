# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-11T18:52:33.658364+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `88`

- Symbol pattern count: `8206`

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

- `market_context_high->unknown_24h` score `1381.0017` n `40` status `ready` deltaP `-21.3542` edge `115.2622` maxDD `-1.2425`
- `market_context_high->unknown_4h` score `57.3828` n `84` status `ready` deltaP `-5.4515` edge `4.8763` maxDD `-2.3109`
- `market_context_high->unknown_1h` score `8.7976` n `96` status `ready` deltaP `-1.6716` edge `0.7779` maxDD `-1.0231`
- `market_context_high->equity_24h` score `8.7936` n `40` status `ready` deltaP `27.6736` edge `0.5912` maxDD `-1.0977`
- `market_context_high->index_24h` score `6.3892` n `40` status `ready` deltaP `52.4306` edge `0.1829` maxDD `0.0`
- `market_context_high->fx_24h` score `3.2342` n `40` status `ready` deltaP `36.5972` edge `0.0385` maxDD `-0.0374`
- `market_context_high->crypto_major_24h` score `1.5258` n `40` status `ready` deltaP `-20.7639` edge `0.5804` maxDD `-17.8526`
- `market_context_high->fx_4h` score `0.8526` n `84` status `ready` deltaP `13.7122` edge `0.008` maxDD `-0.2692`
- `market_context_high->crypto_alt_1h` score `0.4115` n `96` status `ready` deltaP `5.776` edge `0.0992` maxDD `-4.9401`
- `market_context_high->commodity_4h` score `0.3602` n `84` status `ready` deltaP `10.3876` edge `0.0141` maxDD `-1.6002`
- `market_context_high->crypto_major_4h` score `0.1039` n `84` status `ready` deltaP `0.9727` edge `0.2174` maxDD `-11.1784`
- `market_context_high->commodity_1h` score `0.0246` n `96` status `ready` deltaP `3.8423` edge `0.0048` maxDD `-0.6025`
- `market_context_high->fx_1h` score `-0.0275` n `96` status `ready` deltaP `3.0938` edge `0.0013` maxDD `-0.271`
- `market_context_high->metal_4h` score `-0.117` n `84` status `ready` deltaP `6.1992` edge `0.0212` maxDD `-1.1153`
- `market_context_high->crypto_major_1h` score `-0.1426` n `96` status `ready` deltaP `1.0354` edge `0.0637` maxDD `-3.7778`
- `market_context_high->crypto_alt_4h` score `-0.2194` n `84` status `ready` deltaP `-2.8019` edge `0.2464` maxDD `-13.8008`
- `market_context_high->metal_1h` score `-0.2849` n `96` status `ready` deltaP `4.7468` edge `0.0035` maxDD `-0.7107`
- `market_context_high->index_4h` score `-0.6587` n `84` status `ready` deltaP `-2.8963` edge `0.0049` maxDD `-0.9364`
- `market_context_high->index_1h` score `-0.6902` n `96` status `ready` deltaP `-3.2872` edge `-0.0015` maxDD `-0.5392`
- `market_context_high->equity_1h` score `-0.9572` n `96` status `ready` deltaP `-5.6948` edge `0.0022` maxDD `-2.2898`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
