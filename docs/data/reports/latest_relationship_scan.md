# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-30T04:37:26.954015+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11504`

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

- `risk_on_high->unknown_4h` score `8.401` n `65` status `ready` deltaP `23.03` edge `0.5894` maxDD `-1.0945`
- `risk_on_and_context->unknown_4h` score `8.401` n `65` status `ready` deltaP `23.03` edge `0.5894` maxDD `-1.0945`
- `market_context_high->unknown_4h` score `4.9073` n `167` status `ready` deltaP `19.2529` edge `0.3276` maxDD `-1.0945`
- `market_context_high->metal_24h` score `4.6538` n `103` status `ready` deltaP `34.0547` edge `0.2627` maxDD `-3.1535`
- `risk_on_high->crypto_major_4h` score `3.9735` n `65` status `ready` deltaP `21.7261` edge `0.2146` maxDD `-0.5985`
- `risk_on_and_context->crypto_major_4h` score `3.9735` n `65` status `ready` deltaP `21.7261` edge `0.2146` maxDD `-0.5985`
- `risk_on_high->equity_4h` score `2.7817` n `65` status `ready` deltaP `25.1361` edge `0.0833` maxDD `-0.1918`
- `risk_on_and_context->equity_4h` score `2.7817` n `65` status `ready` deltaP `25.1361` edge `0.0833` maxDD `-0.1918`
- `risk_on_high->crypto_alt_4h` score `2.6293` n `65` status `ready` deltaP `15.0867` edge `0.2848` maxDD `-1.5298`
- `risk_on_and_context->crypto_alt_4h` score `2.6293` n `65` status `ready` deltaP `15.0867` edge `0.2848` maxDD `-1.5298`
- `risk_on_high->unknown_1h` score `2.2881` n `65` status `ready` deltaP `4.2861` edge `0.1997` maxDD `-1.3414`
- `risk_on_and_context->unknown_1h` score `2.2881` n `65` status `ready` deltaP `4.2861` edge `0.1997` maxDD `-1.3414`
- `market_context_high->unknown_1h` score `2.0332` n `167` status `ready` deltaP `9.7306` edge `0.1505` maxDD `-1.3414`
- `risk_on_high->index_4h` score `1.8273` n `65` status `ready` deltaP `25.122` edge `0.0112` maxDD `-0.1125`
- `risk_on_and_context->index_4h` score `1.8273` n `65` status `ready` deltaP `25.122` edge `0.0112` maxDD `-0.1125`
- `risk_on_high->metal_4h` score `1.6728` n `65` status `ready` deltaP `21.311` edge `0.0271` maxDD `-0.0488`
- `risk_on_and_context->metal_4h` score `1.6728` n `65` status `ready` deltaP `21.311` edge `0.0271` maxDD `-0.0488`
- `risk_on_high->metal_1h` score `1.3055` n `65` status `ready` deltaP `17.7752` edge `0.0074` maxDD `-0.0353`
- `risk_on_and_context->metal_1h` score `1.3055` n `65` status `ready` deltaP `17.7752` edge `0.0074` maxDD `-0.0353`
- `news_risk_high->unknown_1h` score `1.2507` n `32` status `ready` deltaP `-13.4543` edge `0.2241` maxDD `-0.7475`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
