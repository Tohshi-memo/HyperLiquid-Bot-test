# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-17T14:07:32.311078+00:00`
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

- `risk_on_high->unknown_1h` score `7.1116` n `35` status `ready` deltaP `1.7408` edge `0.6205` maxDD `-0.8243`
- `risk_on_and_context->unknown_1h` score `7.1116` n `35` status `ready` deltaP `1.7408` edge `0.6205` maxDD `-0.8243`
- `market_context_high->crypto_major_24h` score `2.4857` n `90` status `ready` deltaP `8.1598` edge `0.2851` maxDD `-5.2554`
- `market_context_high->index_24h` score `1.2427` n `90` status `ready` deltaP `18.9236` edge `-0.0226` maxDD `0.0`
- `risk_on_high->fx_4h` score `1.2181` n `35` status `ready` deltaP `16.7421` edge `0.004` maxDD `-0.1285`
- `risk_on_and_context->fx_4h` score `1.2181` n `35` status `ready` deltaP `16.7421` edge `0.004` maxDD `-0.1285`
- `risk_on_high->crypto_major_1h` score `1.0516` n `35` status `ready` deltaP `11.9589` edge `0.0385` maxDD `-1.1144`
- `risk_on_and_context->crypto_major_1h` score `1.0516` n `35` status `ready` deltaP `11.9589` edge `0.0385` maxDD `-1.1144`
- `risk_on_high->equity_1h` score `0.8784` n `35` status `ready` deltaP `13.3576` edge `0.0385` maxDD `-1.6811`
- `risk_on_and_context->equity_1h` score `0.8784` n `35` status `ready` deltaP `13.3576` edge `0.0385` maxDD `-1.6811`
- `risk_on_high->index_1h` score `0.8046` n `35` status `ready` deltaP `13.7939` edge `0.0126` maxDD `-0.3343`
- `risk_on_and_context->index_1h` score `0.8046` n `35` status `ready` deltaP `13.7939` edge `0.0126` maxDD `-0.3343`
- `market_context_high->equity_24h` score `0.668` n `90` status `ready` deltaP `13.4375` edge `-0.0222` maxDD `-0.271`
- `market_context_high->commodity_4h` score `0.4473` n `137` status `ready` deltaP `13.2867` edge `0.0538` maxDD `-2.4692`
- `risk_on_high->commodity_4h` score `0.4163` n `35` status `ready` deltaP `2.6089` edge `0.0802` maxDD `-1.3651`
- `risk_on_and_context->commodity_4h` score `0.4163` n `35` status `ready` deltaP `2.6089` edge `0.0802` maxDD `-1.3651`
- `market_context_high->commodity_24h` score `0.4072` n `90` status `ready` deltaP `18.7847` edge `0.1103` maxDD `-4.666`
- `risk_on_high->fx_1h` score `0.0632` n `35` status `ready` deltaP `4.2857` edge `0.0023` maxDD `-0.1547`
- `risk_on_and_context->fx_1h` score `0.0632` n `35` status `ready` deltaP `4.2857` edge `0.0023` maxDD `-0.1547`
- `risk_on_high->crypto_major_4h` score `0.0438` n `35` status `ready` deltaP `1.6942` edge `0.0655` maxDD `-2.0278`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
