# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-18T20:07:30.134732+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9318`

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

- `market_context_high->crypto_major_4h` score `1.9486` n `111` status `ready` deltaP `20.3802` edge `0.4544` maxDD `-15.2359`
- `market_context_high->commodity_24h` score `1.8853` n `111` status `ready` deltaP `17.888` edge `0.123` maxDD `-1.8119`
- `risk_on_high->commodity_24h` score `1.6117` n `78` status `ready` deltaP `19.3779` edge `0.0849` maxDD `-1.7154`
- `risk_on_and_context->commodity_24h` score `1.6117` n `78` status `ready` deltaP `19.3779` edge `0.0849` maxDD `-1.7154`
- `risk_on_high->crypto_major_4h` score `1.5821` n `78` status `ready` deltaP `21.4197` edge `0.3081` maxDD `-11.1788`
- `risk_on_and_context->crypto_major_4h` score `1.5821` n `78` status `ready` deltaP `21.4197` edge `0.3081` maxDD `-11.1788`
- `market_context_high->crypto_major_1h` score `0.6064` n `111` status `ready` deltaP `7.0562` edge `0.1196` maxDD `-3.7781`
- `risk_on_high->index_1h` score `0.1941` n `78` status `ready` deltaP `8.6395` edge `0.0057` maxDD `-0.7394`
- `risk_on_and_context->index_1h` score `0.1941` n `78` status `ready` deltaP `8.6395` edge `0.0057` maxDD `-0.7394`
- `risk_on_high->equity_1h` score `-0.2636` n `78` status `ready` deltaP `10.1293` edge `0.0283` maxDD `-5.3696`
- `risk_on_and_context->equity_1h` score `-0.2636` n `78` status `ready` deltaP `10.1293` edge `0.0283` maxDD `-5.3696`
- `market_context_high->crypto_alt_1h` score `-0.351` n `111` status `ready` deltaP `1.4848` edge `0.0951` maxDD `-7.3329`
- `risk_on_high->fx_1h` score `-0.5169` n `78` status `ready` deltaP `-3.696` edge `-0.0036` maxDD `-0.376`
- `risk_on_and_context->fx_1h` score `-0.5169` n `78` status `ready` deltaP `-3.696` edge `-0.0036` maxDD `-0.376`
- `market_context_high->index_1h` score `-0.5412` n `111` status `ready` deltaP `4.2042` edge `0.0017` maxDD `-1.3195`
- `risk_on_high->crypto_major_1h` score `-0.613` n `78` status `ready` deltaP `1.5815` edge `0.0303` maxDD `-4.6876`
- `risk_on_and_context->crypto_major_1h` score `-0.613` n `78` status `ready` deltaP `1.5815` edge `0.0303` maxDD `-4.6876`
- `risk_on_high->metal_1h` score `-0.719` n `78` status `ready` deltaP `-3.351` edge `0.0033` maxDD `-0.8513`
- `risk_on_and_context->metal_1h` score `-0.719` n `78` status `ready` deltaP `-3.351` edge `0.0033` maxDD `-0.8513`
- `market_context_high->fx_1h` score `-0.7243` n `111` status `ready` deltaP `-5.7057` edge `-0.0027` maxDD `-0.503`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
