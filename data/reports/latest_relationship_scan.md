# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-07T12:22:25.925947+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9949`

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

- `risk_on_high->unknown_24h` score `402.0521` n `93` status `ready` deltaP `25.5208` edge `33.3342` maxDD `0.0`
- `risk_on_and_context->unknown_24h` score `402.0521` n `93` status `ready` deltaP `25.5208` edge `33.3342` maxDD `0.0`
- `risk_on_high->crypto_major_24h` score `22.2803` n `93` status `ready` deltaP `38.4129` edge `1.6523` maxDD `-1.4687`
- `risk_on_and_context->crypto_major_24h` score `22.2803` n `93` status `ready` deltaP `38.4129` edge `1.6523` maxDD `-1.4687`
- `risk_on_high->crypto_alt_24h` score `15.1838` n `93` status `ready` deltaP `32.1181` edge `1.0512` maxDD `0.0`
- `risk_on_and_context->crypto_alt_24h` score `15.1838` n `93` status `ready` deltaP `32.1181` edge `1.0512` maxDD `0.0`
- `market_context_high->crypto_alt_24h` score `8.6749` n `193` status `ready` deltaP `24.3461` edge `0.6181` maxDD `-2.5998`
- `market_context_high->equity_24h` score `5.7348` n `193` status `ready` deltaP `19.9653` edge `0.3448` maxDD `0.0`
- `risk_on_high->crypto_alt_4h` score `5.3289` n `117` status `ready` deltaP `28.8058` edge `0.2892` maxDD `-1.9733`
- `risk_on_and_context->crypto_alt_4h` score `5.3289` n `117` status `ready` deltaP `28.8058` edge `0.2892` maxDD `-1.9733`
- `risk_on_high->equity_24h` score `4.8036` n `93` status `ready` deltaP `19.9653` edge `0.2672` maxDD `0.0`
- `risk_on_and_context->equity_24h` score `4.8036` n `93` status `ready` deltaP `19.9653` edge `0.2672` maxDD `0.0`
- `risk_on_high->crypto_major_4h` score `4.3447` n `117` status `ready` deltaP `24.3043` edge `0.2859` maxDD `-3.8693`
- `risk_on_and_context->crypto_major_4h` score `4.3447` n `117` status `ready` deltaP `24.3043` edge `0.2859` maxDD `-3.8693`
- `risk_on_high->index_24h` score `2.4353` n `93` status `ready` deltaP `20.9061` edge `0.0678` maxDD `-0.0051`
- `risk_on_and_context->index_24h` score `2.4353` n `93` status `ready` deltaP `20.9061` edge `0.0678` maxDD `-0.0051`
- `market_context_high->index_24h` score `1.8598` n `193` status `ready` deltaP `15.8417` edge `0.08` maxDD `-0.117`
- `risk_on_high->metal_24h` score `0.8799` n `93` status `ready` deltaP `17.1875` edge `0.1138` maxDD `-0.9131`
- `risk_on_and_context->metal_24h` score `0.8799` n `93` status `ready` deltaP `17.1875` edge `0.1138` maxDD `-0.9131`
- `risk_on_high->crypto_alt_1h` score `0.8661` n `117` status `ready` deltaP `4.097` edge `0.0801` maxDD `-1.1521`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
