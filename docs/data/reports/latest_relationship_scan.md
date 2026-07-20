# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-20T06:07:27.549343+00:00`
- Price records: `672`
- Market context records: `7326`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `14722`

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

- `risk_on_high->crypto_major_4h` score `7.2705` n `32` status `ready` deltaP `39.7104` edge `0.3604` maxDD `-0.8742`
- `risk_on_and_context->crypto_major_4h` score `7.2705` n `32` status `ready` deltaP `39.7104` edge `0.3604` maxDD `-0.8742`
- `risk_on_high->crypto_alt_4h` score `5.9813` n `32` status `ready` deltaP `32.8506` edge `0.3038` maxDD `-0.9492`
- `risk_on_and_context->crypto_alt_4h` score `5.9813` n `32` status `ready` deltaP `32.8506` edge `0.3038` maxDD `-0.9492`
- `risk_on_high->unknown_4h` score `5.3193` n `32` status `ready` deltaP `18.2927` edge `0.3643` maxDD `-0.4384`
- `risk_on_and_context->unknown_4h` score `5.3193` n `32` status `ready` deltaP `18.2927` edge `0.3643` maxDD `-0.4384`
- `risk_on_high->crypto_major_1h` score `1.3134` n `32` status `ready` deltaP `20.5277` edge `0.056` maxDD `-0.957`
- `risk_on_and_context->crypto_major_1h` score `1.3134` n `32` status `ready` deltaP `20.5277` edge `0.056` maxDD `-0.957`
- `risk_on_high->commodity_1h` score `0.2283` n `32` status `ready` deltaP `4.1479` edge `0.0193` maxDD `-0.2339`
- `risk_on_and_context->commodity_1h` score `0.2283` n `32` status `ready` deltaP `4.1479` edge `0.0193` maxDD `-0.2339`
- `risk_on_high->equity_1h` score `0.2147` n `32` status `ready` deltaP `4.2042` edge `0.0372` maxDD `-1.3497`
- `risk_on_and_context->equity_1h` score `0.2147` n `32` status `ready` deltaP `4.2042` edge `0.0372` maxDD `-1.3497`
- `risk_on_high->crypto_alt_1h` score `0.1991` n `32` status `ready` deltaP `1.0479` edge `0.0556` maxDD `-0.9651`
- `risk_on_and_context->crypto_alt_1h` score `0.1991` n `32` status `ready` deltaP `1.0479` edge `0.0556` maxDD `-0.9651`
- `risk_on_high->metal_4h` score `-0.0156` n `32` status `ready` deltaP `0.4573` edge `0.078` maxDD `-0.5882`
- `risk_on_and_context->metal_4h` score `-0.0156` n `32` status `ready` deltaP `0.4573` edge `0.078` maxDD `-0.5882`
- `market_context_high->fx_1h` score `-0.1605` n `129` status `ready` deltaP `4.2392` edge `0.0001` maxDD `-0.5821`
- `market_context_high->unknown_4h` score `-0.5854` n `129` status `ready` deltaP `6.2287` edge `0.1193` maxDD `-6.2031`
- `market_context_high->commodity_1h` score `-0.7276` n `129` status `ready` deltaP `-3.2649` edge `-0.0143` maxDD `-1.5775`
- `market_context_high->index_1h` score `-0.7703` n `129` status `ready` deltaP `-4.7105` edge `-0.0065` maxDD `-1.868`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
