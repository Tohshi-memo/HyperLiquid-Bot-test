# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-12T20:22:33.582694+00:00`
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

- `news_risk_high->equity_4h` score `7.5157` n `36` status `ready` deltaP `39.4817` edge `0.3631` maxDD `0.0`
- `news_risk_high->index_4h` score `2.3565` n `36` status `ready` deltaP `26.1687` edge `0.0351` maxDD `-0.0546`
- `risk_on_high->crypto_major_24h` score `2.3111` n `32` status `ready` deltaP `16.3194` edge `0.3031` maxDD `-6.2481`
- `risk_on_and_context->crypto_major_24h` score `2.3111` n `32` status `ready` deltaP `16.3194` edge `0.3031` maxDD `-6.2481`
- `risk_on_high->commodity_4h` score `2.1262` n `32` status `ready` deltaP `14.253` edge `0.1004` maxDD `-0.1258`
- `risk_on_and_context->commodity_4h` score `2.1262` n `32` status `ready` deltaP `14.253` edge `0.1004` maxDD `-0.1258`
- `news_risk_high->equity_1h` score `1.7669` n `36` status `ready` deltaP `9.032` edge `0.1189` maxDD `-0.5496`
- `risk_on_high->commodity_24h` score `1.7175` n `32` status `ready` deltaP `15.7986` edge `0.0378` maxDD `0.0`
- `risk_on_and_context->commodity_24h` score `1.7175` n `32` status `ready` deltaP `15.7986` edge `0.0378` maxDD `0.0`
- `risk_on_high->fx_24h` score `1.6343` n `32` status `ready` deltaP `18.2292` edge `0.0331` maxDD `-0.1418`
- `risk_on_and_context->fx_24h` score `1.6343` n `32` status `ready` deltaP `18.2292` edge `0.0331` maxDD `-0.1418`
- `risk_on_high->commodity_1h` score `1.0873` n `32` status `ready` deltaP `12.0135` edge `0.0338` maxDD `-0.1957`
- `risk_on_and_context->commodity_1h` score `1.0873` n `32` status `ready` deltaP `12.0135` edge `0.0338` maxDD `-0.1957`
- `risk_on_high->fx_4h` score `0.8719` n `32` status `ready` deltaP `9.9848` edge `0.0202` maxDD `-0.1285`
- `risk_on_and_context->fx_4h` score `0.8719` n `32` status `ready` deltaP `9.9848` edge `0.0202` maxDD `-0.1285`
- `market_context_high->commodity_4h` score `0.7714` n `170` status `ready` deltaP `10.8339` edge `0.0559` maxDD `-2.1077`
- `risk_on_high->index_24h` score `0.7565` n `32` status `ready` deltaP `9.0278` edge `0.0333` maxDD `-0.4355`
- `risk_on_and_context->index_24h` score `0.7565` n `32` status `ready` deltaP `9.0278` edge `0.0333` maxDD `-0.4355`
- `market_context_high->commodity_1h` score `0.7104` n `170` status `ready` deltaP `9.7341` edge `0.0265` maxDD `-0.5752`
- `risk_on_high->index_1h` score `0.3147` n `32` status `ready` deltaP `10.2545` edge `0.0095` maxDD `-0.3343`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
