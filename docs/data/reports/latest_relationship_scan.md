# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-19T23:37:50.030462+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8196`

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

- `market_context_high->commodity_24h` score `2.8601` n `75` status `ready` deltaP `22.9791` edge `0.1703` maxDD `-1.8119`
- `risk_on_high->commodity_24h` score `0.872` n `42` status `ready` deltaP `17.9315` edge `0.0329` maxDD `-1.7154`
- `risk_on_and_context->commodity_24h` score `0.872` n `42` status `ready` deltaP `17.9315` edge `0.0329` maxDD `-1.7154`
- `risk_on_high->equity_1h` score `0.7788` n `42` status `ready` deltaP `14.0291` edge `0.0202` maxDD `-1.2396`
- `risk_on_and_context->equity_1h` score `0.7788` n `42` status `ready` deltaP `14.0291` edge `0.0202` maxDD `-1.2396`
- `risk_on_high->index_1h` score `0.5493` n `42` status `ready` deltaP `10.8854` edge `0.0019` maxDD `-0.2956`
- `risk_on_and_context->index_1h` score `0.5493` n `42` status `ready` deltaP `10.8854` edge `0.0019` maxDD `-0.2956`
- `risk_on_high->fx_1h` score `-0.2234` n `42` status `ready` deltaP `1.0337` edge `-0.0009` maxDD `-0.1039`
- `risk_on_and_context->fx_1h` score `-0.2234` n `42` status `ready` deltaP `1.0337` edge `-0.0009` maxDD `-0.1039`
- `risk_on_high->fx_4h` score `-0.2933` n `42` status `ready` deltaP `-0.3049` edge `0.004` maxDD `-0.1126`
- `risk_on_and_context->fx_4h` score `-0.2933` n `42` status `ready` deltaP `-0.3049` edge `0.004` maxDD `-0.1126`
- `market_context_high->metal_1h` score `-0.3558` n `94` status `ready` deltaP `-1.5766` edge `0.0024` maxDD `-0.6669`
- `market_context_high->crypto_major_1h` score `-0.3748` n `94` status `ready` deltaP `0.379` edge `0.0511` maxDD `-4.8007`
- `risk_on_high->equity_4h` score `-0.3794` n `42` status `ready` deltaP `3.869` edge `0.051` maxDD `-4.0351`
- `risk_on_and_context->equity_4h` score `-0.3794` n `42` status `ready` deltaP `3.869` edge `0.051` maxDD `-4.0351`
- `risk_on_high->index_4h` score `-0.3878` n `42` status `ready` deltaP `4.5732` edge `0.0043` maxDD `-0.7604`
- `risk_on_and_context->index_4h` score `-0.3878` n `42` status `ready` deltaP `4.5732` edge `0.0043` maxDD `-0.7604`
- `market_context_high->fx_4h` score `-0.557` n `94` status `ready` deltaP `-1.3687` edge `0.0018` maxDD `-0.7936`
- `market_context_high->commodity_1h` score `-0.6499` n `94` status `ready` deltaP `-0.946` edge `-0.0043` maxDD `-1.4834`
- `market_context_high->metal_4h` score `-0.7352` n `94` status `ready` deltaP `-0.2919` edge `0.0388` maxDD `-1.4893`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
