# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-13T00:07:25.302153+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11824`

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

- `news_risk_high->equity_4h` score `7.4285` n `36` status `ready` deltaP `39.7866` edge `0.3538` maxDD `0.0`
- `risk_on_high->commodity_4h` score `2.2709` n `32` status `ready` deltaP `15.7774` edge `0.1023` maxDD `-0.1258`
- `risk_on_and_context->commodity_4h` score `2.2709` n `32` status `ready` deltaP `15.7774` edge `0.1023` maxDD `-0.1258`
- `news_risk_high->index_4h` score `2.213` n `36` status `ready` deltaP `24.6443` edge `0.0333` maxDD `-0.0546`
- `risk_on_high->crypto_major_24h` score `2.1698` n `32` status `ready` deltaP `15.9722` edge `0.2873` maxDD `-6.2481`
- `risk_on_and_context->crypto_major_24h` score `2.1698` n `32` status `ready` deltaP `15.9722` edge `0.2873` maxDD `-6.2481`
- `risk_on_high->commodity_24h` score `1.992` n `32` status `ready` deltaP `17.5347` edge `0.0491` maxDD `0.0`
- `risk_on_and_context->commodity_24h` score `1.992` n `32` status `ready` deltaP `17.5347` edge `0.0491` maxDD `0.0`
- `news_risk_high->equity_1h` score `1.7477` n `36` status `ready` deltaP `8.8823` edge `0.1183` maxDD `-0.5496`
- `risk_on_high->fx_24h` score `1.653` n `32` status `ready` deltaP `18.4028` edge `0.0335` maxDD `-0.1418`
- `risk_on_and_context->fx_24h` score `1.653` n `32` status `ready` deltaP `18.4028` edge `0.0335` maxDD `-0.1418`
- `risk_on_high->commodity_1h` score `1.1448` n `32` status `ready` deltaP `12.6123` edge `0.0346` maxDD `-0.1957`
- `risk_on_and_context->commodity_1h` score `1.1448` n `32` status `ready` deltaP `12.6123` edge `0.0346` maxDD `-0.1957`
- `market_context_high->commodity_4h` score `1.0399` n `162` status `ready` deltaP `12.961` edge `0.0641` maxDD `-2.1077`
- `risk_on_high->fx_4h` score `0.9487` n `32` status `ready` deltaP `10.8994` edge `0.0205` maxDD `-0.1285`
- `risk_on_and_context->fx_4h` score `0.9487` n `32` status `ready` deltaP `10.8994` edge `0.0205` maxDD `-0.1285`
- `market_context_high->commodity_1h` score `0.8318` n `162` status `ready` deltaP `10.529` edge `0.0288` maxDD `-0.3742`
- `risk_on_high->index_24h` score `0.349` n `32` status `ready` deltaP `6.4236` edge `0.0167` maxDD `-0.4355`
- `risk_on_and_context->index_24h` score `0.349` n `32` status `ready` deltaP `6.4236` edge `0.0167` maxDD `-0.4355`
- `risk_on_high->index_1h` score `0.2797` n `32` status `ready` deltaP `9.6557` edge `0.009` maxDD `-0.3343`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
