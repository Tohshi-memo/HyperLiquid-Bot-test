# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-17T13:37:32.347234+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11803`

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

- `risk_on_high->unknown_1h` score `7.1092` n `35` status `ready` deltaP `1.7408` edge `0.6203` maxDD `-0.8243`
- `risk_on_and_context->unknown_1h` score `7.1092` n `35` status `ready` deltaP `1.7408` edge `0.6203` maxDD `-0.8243`
- `market_context_high->crypto_major_24h` score `2.3851` n `91` status `ready` deltaP `7.7744` edge `0.2817` maxDD `-5.4483`
- `market_context_high->index_24h` score `1.2487` n `91` status `ready` deltaP `18.9236` edge `-0.0221` maxDD `0.0`
- `risk_on_high->fx_4h` score `1.2059` n `35` status `ready` deltaP `16.5897` edge `0.004` maxDD `-0.1285`
- `risk_on_and_context->fx_4h` score `1.2059` n `35` status `ready` deltaP `16.5897` edge `0.004` maxDD `-0.1285`
- `risk_on_high->crypto_major_1h` score `1.0695` n `35` status `ready` deltaP `12.1086` edge `0.039` maxDD `-1.1144`
- `risk_on_and_context->crypto_major_1h` score `1.0695` n `35` status `ready` deltaP `12.1086` edge `0.039` maxDD `-1.1144`
- `risk_on_high->equity_1h` score `0.8784` n `35` status `ready` deltaP `13.3576` edge `0.0385` maxDD `-1.6811`
- `risk_on_and_context->equity_1h` score `0.8784` n `35` status `ready` deltaP `13.3576` edge `0.0385` maxDD `-1.6811`
- `risk_on_high->index_1h` score `0.8046` n `35` status `ready` deltaP `13.7939` edge `0.0126` maxDD `-0.3343`
- `risk_on_and_context->index_1h` score `0.8046` n `35` status `ready` deltaP `13.7939` edge `0.0126` maxDD `-0.3343`
- `market_context_high->equity_24h` score `0.4767` n `91` status `ready` deltaP `12.7347` edge `-0.0307` maxDD `-0.4914`
- `market_context_high->commodity_4h` score `0.4526` n `137` status `ready` deltaP `13.1342` edge `0.0555` maxDD `-2.4692`
- `market_context_high->commodity_24h` score `0.4357` n `91` status `ready` deltaP `19.0019` edge `0.1125` maxDD `-4.666`
- `risk_on_high->commodity_4h` score `0.3897` n `35` status `ready` deltaP `2.4564` edge `0.079` maxDD `-1.3651`
- `risk_on_and_context->commodity_4h` score `0.3897` n `35` status `ready` deltaP `2.4564` edge `0.079` maxDD `-1.3651`
- `risk_on_high->crypto_major_4h` score `0.0768` n `35` status `ready` deltaP `1.9991` edge `0.0677` maxDD `-2.0278`
- `risk_on_and_context->crypto_major_4h` score `0.0768` n `35` status `ready` deltaP `1.9991` edge `0.0677` maxDD `-2.0278`
- `risk_on_high->fx_1h` score `0.0632` n `35` status `ready` deltaP `4.2857` edge `0.0023` maxDD `-0.1547`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
