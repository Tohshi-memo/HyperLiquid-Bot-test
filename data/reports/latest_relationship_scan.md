# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-17T09:37:24.619087+00:00`
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

- `risk_on_high->unknown_1h` score `7.3011` n `35` status `ready` deltaP `2.4893` edge `0.6313` maxDD `-0.8243`
- `risk_on_and_context->unknown_1h` score `7.3011` n `35` status `ready` deltaP `2.4893` edge `0.6313` maxDD `-0.8243`
- `market_context_high->crypto_major_24h` score `2.798` n `91` status `ready` deltaP `9.4533` edge `0.3078` maxDD `-5.6792`
- `market_context_high->index_24h` score `1.3433` n `91` status `ready` deltaP `19.7917` edge `-0.02` maxDD `0.0`
- `risk_on_high->fx_4h` score `1.1633` n `35` status `ready` deltaP `16.1324` edge `0.0035` maxDD `-0.1285`
- `risk_on_and_context->fx_4h` score `1.1633` n `35` status `ready` deltaP `16.1324` edge `0.0035` maxDD `-0.1285`
- `risk_on_high->crypto_major_1h` score `1.1139` n `35` status `ready` deltaP `12.2583` edge `0.0417` maxDD `-1.1144`
- `risk_on_and_context->crypto_major_1h` score `1.1139` n `35` status `ready` deltaP `12.2583` edge `0.0417` maxDD `-1.1144`
- `market_context_high->equity_24h` score `1.0114` n `91` status `ready` deltaP `14.4135` edge `0.0091` maxDD `-0.6726`
- `risk_on_high->equity_1h` score `0.9587` n `35` status `ready` deltaP `13.9564` edge `0.0412` maxDD `-1.6811`
- `risk_on_and_context->equity_1h` score `0.9587` n `35` status `ready` deltaP `13.9564` edge `0.0412` maxDD `-1.6811`
- `risk_on_high->index_1h` score `0.8561` n `35` status `ready` deltaP `14.3927` edge `0.0129` maxDD `-0.3343`
- `risk_on_and_context->index_1h` score `0.8561` n `35` status `ready` deltaP `14.3927` edge `0.0129` maxDD `-0.3343`
- `risk_on_high->commodity_4h` score `0.3069` n `35` status `ready` deltaP `2.4564` edge `0.0721` maxDD `-1.3651`
- `risk_on_and_context->commodity_4h` score `0.3069` n `35` status `ready` deltaP `2.4564` edge `0.0721` maxDD `-1.3651`
- `risk_on_high->crypto_major_4h` score `0.2958` n `35` status `ready` deltaP `3.6759` edge `0.0846` maxDD `-2.0278`
- `risk_on_and_context->crypto_major_4h` score `0.2958` n `35` status `ready` deltaP `3.6759` edge `0.0846` maxDD `-2.0278`
- `market_context_high->commodity_24h` score `0.2704` n `91` status `ready` deltaP `17.6702` edge `0.0956` maxDD `-4.6316`
- `market_context_high->commodity_4h` score `0.1241` n `122` status `ready` deltaP `8.8264` edge `0.0421` maxDD `-2.4692`
- `risk_on_high->fx_1h` score `0.1107` n `35` status `ready` deltaP `5.1839` edge `0.0024` maxDD `-0.1547`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
