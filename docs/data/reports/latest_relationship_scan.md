# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-14T21:22:30.801350+00:00`
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

- `market_context_high->unknown_24h` score `136.274` n `128` status `ready` deltaP `-31.8577` edge `11.8598` maxDD `-9.6329`
- `risk_on_high->unknown_24h` score `32.8571` n `32` status `ready` deltaP `-45.1389` edge `4.5884` maxDD `-1.6689`
- `risk_on_and_context->unknown_24h` score `32.8571` n `32` status `ready` deltaP `-45.1389` edge `4.5884` maxDD `-1.6689`
- `news_risk_high->equity_24h` score `10.7284` n `36` status `ready` deltaP `14.7569` edge `0.8336` maxDD `-1.0358`
- `news_risk_high->equity_4h` score `7.6837` n `36` status `ready` deltaP `40.3963` edge `0.371` maxDD `0.0`
- `market_context_high->commodity_24h` score `4.931` n `128` status `ready` deltaP `27.8645` edge `0.2309` maxDD `-0.1266`
- `risk_on_high->commodity_24h` score `4.5071` n `32` status `ready` deltaP `30.2083` edge `0.1742` maxDD `0.0`
- `risk_on_and_context->commodity_24h` score `4.5071` n `32` status `ready` deltaP `30.2083` edge `0.1742` maxDD `0.0`
- `risk_on_high->crypto_major_24h` score `3.0314` n `32` status `ready` deltaP `21.0069` edge `0.3642` maxDD `-6.2481`
- `risk_on_and_context->crypto_major_24h` score `3.0314` n `32` status `ready` deltaP `21.0069` edge `0.3642` maxDD `-6.2481`
- `risk_on_high->commodity_4h` score `2.6632` n `32` status `ready` deltaP `18.5213` edge `0.1167` maxDD `-0.1258`
- `risk_on_and_context->commodity_4h` score `2.6632` n `32` status `ready` deltaP `18.5213` edge `0.1167` maxDD `-0.1258`
- `news_risk_high->index_24h` score `2.5157` n `36` status `ready` deltaP `18.5764` edge `0.0858` maxDD `0.0`
- `news_risk_high->index_4h` score `1.8511` n `36` status `ready` deltaP `21.2906` edge `0.0255` maxDD `-0.0546`
- `news_risk_high->equity_1h` score `1.7406` n `36` status `ready` deltaP `8.5829` edge `0.1197` maxDD `-0.5496`
- `market_context_high->commodity_4h` score `1.7154` n `128` status `ready` deltaP `16.9588` edge `0.077` maxDD `-0.7687`
- `risk_on_high->commodity_1h` score `1.2886` n `32` status `ready` deltaP `13.8099` edge `0.0386` maxDD `-0.1957`
- `risk_on_and_context->commodity_1h` score `1.2886` n `32` status `ready` deltaP `13.8099` edge `0.0386` maxDD `-0.1957`
- `risk_on_high->fx_24h` score `1.0839` n `32` status `ready` deltaP `13.1944` edge `0.0208` maxDD `-0.1418`
- `risk_on_and_context->fx_24h` score `1.0839` n `32` status `ready` deltaP `13.1944` edge `0.0208` maxDD `-0.1418`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
