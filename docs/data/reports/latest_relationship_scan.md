# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-17T14:27:27.196851+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11819`

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

- `risk_on_high->unknown_1h` score `7.114` n `35` status `ready` deltaP `1.7408` edge `0.6207` maxDD `-0.8243`
- `risk_on_and_context->unknown_1h` score `7.114` n `35` status `ready` deltaP `1.7408` edge `0.6207` maxDD `-0.8243`
- `market_context_high->crypto_major_24h` score `2.4821` n `89` status `ready` deltaP `7.7852` edge `0.2873` maxDD `-5.2554`
- `market_context_high->index_24h` score `1.2415` n `89` status `ready` deltaP `18.9236` edge `-0.0227` maxDD `0.0`
- `risk_on_high->fx_4h` score `1.2181` n `35` status `ready` deltaP `16.7421` edge `0.004` maxDD `-0.1285`
- `risk_on_and_context->fx_4h` score `1.2181` n `35` status `ready` deltaP `16.7421` edge `0.004` maxDD `-0.1285`
- `risk_on_high->crypto_major_1h` score `1.0528` n `35` status `ready` deltaP `11.9589` edge `0.0386` maxDD `-1.1144`
- `risk_on_and_context->crypto_major_1h` score `1.0528` n `35` status `ready` deltaP `11.9589` edge `0.0386` maxDD `-1.1144`
- `market_context_high->equity_24h` score `0.8805` n `89` status `ready` deltaP `14.3375` edge `-0.0118` maxDD `-0.1657`
- `risk_on_high->equity_1h` score `0.876` n `35` status `ready` deltaP `13.3576` edge `0.0383` maxDD `-1.6811`
- `risk_on_and_context->equity_1h` score `0.876` n `35` status `ready` deltaP `13.3576` edge `0.0383` maxDD `-1.6811`
- `risk_on_high->index_1h` score `0.8058` n `35` status `ready` deltaP `13.7939` edge `0.0127` maxDD `-0.3343`
- `risk_on_and_context->index_1h` score `0.8058` n `35` status `ready` deltaP `13.7939` edge `0.0127` maxDD `-0.3343`
- `market_context_high->commodity_4h` score `0.4261` n `136` status `ready` deltaP `13.0291` edge `0.0528` maxDD `-2.4692`
- `risk_on_high->commodity_4h` score `0.4199` n `35` status `ready` deltaP `2.6089` edge `0.0805` maxDD `-1.3651`
- `risk_on_and_context->commodity_4h` score `0.4199` n `35` status `ready` deltaP `2.6089` edge `0.0805` maxDD `-1.3651`
- `market_context_high->commodity_24h` score `0.3818` n `89` status `ready` deltaP `18.3852` edge `0.1097` maxDD `-4.666`
- `risk_on_high->fx_1h` score `0.071` n `35` status `ready` deltaP `4.4354` edge `0.0023` maxDD `-0.1547`
- `risk_on_and_context->fx_1h` score `0.071` n `35` status `ready` deltaP `4.4354` edge `0.0023` maxDD `-0.1547`
- `risk_on_high->crypto_major_4h` score `0.0312` n `35` status `ready` deltaP `1.5418` edge `0.0649` maxDD `-2.0278`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
