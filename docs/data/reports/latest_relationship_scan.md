# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-16T04:37:26.366237+00:00`
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

- `market_context_high->unknown_24h` score `177.7233` n `90` status `ready` deltaP `-22.6362` edge `23.2043` maxDD `-7.8016`
- `risk_on_high->unknown_24h` score `38.5011` n `31` status `ready` deltaP `-38.9445` edge `5.2707` maxDD `-1.6689`
- `risk_on_and_context->unknown_24h` score `38.5011` n `31` status `ready` deltaP `-38.9445` edge `5.2707` maxDD `-1.6689`
- `news_risk_high->equity_24h` score `12.5855` n `36` status `ready` deltaP `23.5413` edge `0.9298` maxDD `-1.0358`
- `news_risk_high->equity_4h` score `7.6168` n `36` status `ready` deltaP `38.7195` edge `0.3766` maxDD `0.0`
- `market_context_high->commodity_24h` score `7.2096` n `90` status `ready` deltaP `39.8922` edge `0.3406` maxDD `-0.1266`
- `risk_on_high->commodity_24h` score `6.0248` n `31` status `ready` deltaP `42.1144` edge `0.2213` maxDD `0.0`
- `risk_on_and_context->commodity_24h` score `6.0248` n `31` status `ready` deltaP `42.1144` edge `0.2213` maxDD `0.0`
- `risk_on_high->crypto_major_24h` score `4.1898` n `31` status `ready` deltaP `29.3062` edge `0.4531` maxDD `-6.2389`
- `risk_on_and_context->crypto_major_24h` score `4.1898` n `31` status `ready` deltaP `29.3062` edge `0.4531` maxDD `-6.2389`
- `news_risk_high->index_24h` score `3.6817` n `36` status `ready` deltaP `30.6759` edge `0.1023` maxDD `0.0`
- `risk_on_high->commodity_4h` score `3.0437` n `31` status `ready` deltaP `21.6267` edge `0.1277` maxDD `-0.1258`
- `risk_on_and_context->commodity_4h` score `3.0437` n `31` status `ready` deltaP `21.6267` edge `0.1277` maxDD `-0.1258`
- `market_context_high->commodity_4h` score `2.0296` n `104` status `ready` deltaP `18.2458` edge `0.0946` maxDD `-0.7687`
- `news_risk_high->index_4h` score `1.8767` n `36` status `ready` deltaP `21.5955` edge `0.0256` maxDD `-0.0546`
- `news_risk_high->equity_1h` score `1.6879` n `36` status `ready` deltaP `7.6847` edge `0.1213` maxDD `-0.5496`
- `risk_on_high->commodity_1h` score `1.3421` n `31` status `ready` deltaP `14.2988` edge `0.0398` maxDD `-0.1957`
- `risk_on_and_context->commodity_1h` score `1.3421` n `31` status `ready` deltaP `14.2988` edge `0.0398` maxDD `-0.1957`
- `risk_on_high->fx_4h` score `0.9603` n `31` status `ready` deltaP `11.6443` edge `0.0165` maxDD `-0.1285`
- `risk_on_and_context->fx_4h` score `0.9603` n `31` status `ready` deltaP `11.6443` edge `0.0165` maxDD `-0.1285`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
