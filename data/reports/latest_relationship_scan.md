# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-17T17:22:28.786347+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11835`

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

- `risk_on_high->unknown_1h` score `7.2496` n `35` status `ready` deltaP `1.8905` edge `0.631` maxDD `-0.8243`
- `risk_on_and_context->unknown_1h` score `7.2496` n `35` status `ready` deltaP `1.8905` edge `0.631` maxDD `-0.8243`
- `market_context_high->crypto_major_24h` score `3.8333` n `84` status `ready` deltaP `13.2192` edge `0.3521` maxDD `-4.9964`
- `market_context_high->equity_24h` score `2.1922` n `84` status `ready` deltaP `17.1875` edge `0.0681` maxDD `0.0`
- `market_context_high->index_24h` score `1.2619` n `84` status `ready` deltaP `18.9236` edge `-0.021` maxDD `0.0`
- `risk_on_high->fx_4h` score `1.2047` n `35` status `ready` deltaP `16.5897` edge `0.0039` maxDD `-0.1285`
- `risk_on_and_context->fx_4h` score `1.2047` n `35` status `ready` deltaP `16.5897` edge `0.0039` maxDD `-0.1285`
- `risk_on_high->crypto_major_1h` score `0.9161` n `35` status `ready` deltaP `11.0607` edge `0.0332` maxDD `-1.1144`
- `risk_on_and_context->crypto_major_1h` score `0.9161` n `35` status `ready` deltaP `11.0607` edge `0.0332` maxDD `-1.1144`
- `risk_on_high->index_1h` score `0.7866` n `35` status `ready` deltaP `13.6442` edge `0.0121` maxDD `-0.3343`
- `risk_on_and_context->index_1h` score `0.7866` n `35` status `ready` deltaP `13.6442` edge `0.0121` maxDD `-0.3343`
- `risk_on_high->equity_1h` score `0.7322` n `35` status `ready` deltaP `12.4594` edge `0.0323` maxDD `-1.6811`
- `risk_on_and_context->equity_1h` score `0.7322` n `35` status `ready` deltaP `12.4594` edge `0.0323` maxDD `-1.6811`
- `market_context_high->commodity_4h` score `0.5128` n `132` status `ready` deltaP `12.2644` edge `0.046` maxDD `-2.4692`
- `risk_on_high->commodity_4h` score `0.4695` n `35` status `ready` deltaP `2.9137` edge `0.0826` maxDD `-1.3651`
- `risk_on_and_context->commodity_4h` score `0.4695` n `35` status `ready` deltaP `2.9137` edge `0.0826` maxDD `-1.3651`
- `market_context_high->commodity_24h` score `0.2427` n `84` status `ready` deltaP `17.2867` edge `0.0992` maxDD `-4.666`
- `risk_on_high->fx_1h` score `0.071` n `35` status `ready` deltaP `4.4354` edge `0.0023` maxDD `-0.1547`
- `risk_on_and_context->fx_1h` score `0.071` n `35` status `ready` deltaP `4.4354` edge `0.0023` maxDD `-0.1547`
- `risk_on_high->crypto_major_4h` score `-0.0277` n `35` status `ready` deltaP `1.0845` edge `0.0604` maxDD `-2.0278`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
