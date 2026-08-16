# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-16T04:07:26.659635+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11734`

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

- `market_context_high->unknown_24h` score `174.4321` n `91` status `ready` deltaP `-23.0636` edge `22.7852` maxDD `-7.8016`
- `risk_on_high->unknown_24h` score `33.5302` n `32` status `ready` deltaP `-39.6501` edge `4.6381` maxDD `-1.6689`
- `risk_on_and_context->unknown_24h` score `33.5302` n `32` status `ready` deltaP `-39.6501` edge `4.6381` maxDD `-1.6689`
- `news_risk_high->equity_24h` score `12.6301` n `36` status `ready` deltaP `23.8879` edge `0.9312` maxDD `-1.0358`
- `news_risk_high->equity_4h` score `7.618` n `36` status `ready` deltaP `38.7195` edge `0.3767` maxDD `0.0`
- `market_context_high->commodity_24h` score `7.1562` n `91` status `ready` deltaP `39.57` edge `0.3383` maxDD `-0.1266`
- `risk_on_high->commodity_24h` score `5.997` n `32` status `ready` deltaP `41.7678` edge `0.2213` maxDD `0.0`
- `risk_on_and_context->commodity_24h` score `5.997` n `32` status `ready` deltaP `41.7678` edge `0.2213` maxDD `0.0`
- `risk_on_high->crypto_major_24h` score `3.9379` n `32` status `ready` deltaP `26.8143` edge `0.4417` maxDD `-6.2481`
- `risk_on_and_context->crypto_major_24h` score `3.9379` n `32` status `ready` deltaP `26.8143` edge `0.4417` maxDD `-6.2481`
- `news_risk_high->index_24h` score `3.6817` n `36` status `ready` deltaP `30.6759` edge `0.1023` maxDD `0.0`
- `risk_on_high->commodity_4h` score `3.0545` n `32` status `ready` deltaP `22.3323` edge `0.1239` maxDD `-0.1258`
- `risk_on_and_context->commodity_4h` score `3.0545` n `32` status `ready` deltaP `22.3323` edge `0.1239` maxDD `-0.1258`
- `market_context_high->commodity_4h` score `2.0409` n `105` status `ready` deltaP `18.493` edge `0.0939` maxDD `-0.7687`
- `news_risk_high->index_4h` score `1.8767` n `36` status `ready` deltaP `21.5955` edge `0.0256` maxDD `-0.0546`
- `news_risk_high->equity_1h` score `1.6879` n `36` status `ready` deltaP `7.6847` edge `0.1213` maxDD `-0.5496`
- `risk_on_high->commodity_1h` score `1.4228` n `32` status `ready` deltaP `15.3069` edge `0.0398` maxDD `-0.1957`
- `risk_on_and_context->commodity_1h` score `1.4228` n `32` status `ready` deltaP `15.3069` edge `0.0398` maxDD `-0.1957`
- `risk_on_high->fx_4h` score `0.8021` n `32` status `ready` deltaP `9.8323` edge `0.0154` maxDD `-0.1285`
- `risk_on_and_context->fx_4h` score `0.8021` n `32` status `ready` deltaP `9.8323` edge `0.0154` maxDD `-0.1285`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
