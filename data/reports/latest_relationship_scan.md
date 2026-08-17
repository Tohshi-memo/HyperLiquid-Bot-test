# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-17T12:14:22.873425+00:00`
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

- `risk_on_high->unknown_1h` score `7.1176` n `35` status `ready` deltaP `1.8905` edge `0.62` maxDD `-0.8243`
- `risk_on_and_context->unknown_1h` score `7.1176` n `35` status `ready` deltaP `1.8905` edge `0.62` maxDD `-0.8243`
- `market_context_high->crypto_major_24h` score `2.4353` n `92` status `ready` deltaP `8.0993` edge `0.2866` maxDD `-5.6792`
- `market_context_high->index_24h` score `1.2511` n `92` status `ready` deltaP `18.9236` edge `-0.0219` maxDD `0.0`
- `risk_on_high->fx_4h` score `1.2047` n `35` status `ready` deltaP `16.5897` edge `0.0039` maxDD `-0.1285`
- `risk_on_and_context->fx_4h` score `1.2047` n `35` status `ready` deltaP `16.5897` edge `0.0039` maxDD `-0.1285`
- `risk_on_high->crypto_major_1h` score `1.1019` n `35` status `ready` deltaP `12.2583` edge `0.0407` maxDD `-1.1144`
- `risk_on_and_context->crypto_major_1h` score `1.1019` n `35` status `ready` deltaP `12.2583` edge `0.0407` maxDD `-1.1144`
- `risk_on_high->equity_1h` score `0.8832` n `35` status `ready` deltaP `13.3576` edge `0.0389` maxDD `-1.6811`
- `risk_on_and_context->equity_1h` score `0.8832` n `35` status `ready` deltaP `13.3576` edge `0.0389` maxDD `-1.6811`
- `risk_on_high->index_1h` score `0.7902` n `35` status `ready` deltaP `13.6442` edge `0.0124` maxDD `-0.3343`
- `risk_on_and_context->index_1h` score `0.7902` n `35` status `ready` deltaP `13.6442` edge `0.0124` maxDD `-0.3343`
- `market_context_high->equity_24h` score `0.4258` n `92` status `ready` deltaP `12.7491` edge `-0.0286` maxDD `-0.6726`
- `market_context_high->commodity_24h` score `0.4046` n `92` status `ready` deltaP `18.6896` edge `0.1106` maxDD `-4.666`
- `market_context_high->commodity_4h` score `0.3711` n `132` status `ready` deltaP `11.8071` edge `0.0539` maxDD `-2.4692`
- `risk_on_high->commodity_4h` score `0.3537` n `35` status `ready` deltaP `2.4564` edge `0.076` maxDD `-1.3651`
- `risk_on_and_context->commodity_4h` score `0.3537` n `35` status `ready` deltaP `2.4564` edge `0.076` maxDD `-1.3651`
- `risk_on_high->crypto_major_4h` score `0.196` n `35` status `ready` deltaP `2.7613` edge `0.0779` maxDD `-2.0278`
- `risk_on_and_context->crypto_major_4h` score `0.196` n `35` status `ready` deltaP `2.7613` edge `0.0779` maxDD `-2.0278`
- `risk_on_high->fx_1h` score `0.0702` n `35` status `ready` deltaP `4.4354` edge `0.0022` maxDD `-0.1547`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
