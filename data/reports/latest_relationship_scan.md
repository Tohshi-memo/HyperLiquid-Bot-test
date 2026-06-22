# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-22T09:22:32.840576+00:00`
- Price records: `672`
- Market context records: `4402`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11123`

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

- `risk_on_high->unknown_4h` score `125.07` n `47` status `ready` deltaP `2.092` edge `10.5904` maxDD `-10.8809`
- `risk_on_and_context->unknown_4h` score `125.07` n `47` status `ready` deltaP `2.092` edge `10.5904` maxDD `-10.8809`
- `market_context_high->unknown_1h` score `31.5441` n `228` status `ready` deltaP `2.5187` edge `2.7615` maxDD `-9.6361`
- `market_context_high->unknown_4h` score `12.4575` n `219` status `ready` deltaP `5.3855` edge `1.5452` maxDD `-35.7719`
- `risk_on_high->equity_4h` score `3.2058` n `47` status `ready` deltaP `34.0003` edge `0.0452` maxDD `-0.044`
- `risk_on_and_context->equity_4h` score `3.2058` n `47` status `ready` deltaP `34.0003` edge `0.0452` maxDD `-0.044`
- `risk_on_high->metal_24h` score `2.9835` n `44` status `ready` deltaP `-15.3567` edge `0.5463` maxDD `-1.9133`
- `risk_on_and_context->metal_24h` score `2.9835` n `44` status `ready` deltaP `-15.3567` edge `0.5463` maxDD `-1.9133`
- `risk_on_high->crypto_major_4h` score `2.3842` n `47` status `ready` deltaP `19.8949` edge `0.1326` maxDD `-2.6576`
- `risk_on_and_context->crypto_major_4h` score `2.3842` n `47` status `ready` deltaP `19.8949` edge `0.1326` maxDD `-2.6576`
- `risk_on_high->equity_24h` score `1.7121` n `44` status `ready` deltaP `20.4861` edge `0.0061` maxDD `0.0`
- `risk_on_and_context->equity_24h` score `1.7121` n `44` status `ready` deltaP `20.4861` edge `0.0061` maxDD `0.0`
- `risk_on_high->index_24h` score `1.5018` n `44` status `ready` deltaP `23.4375` edge `-0.0311` maxDD `0.0`
- `risk_on_and_context->index_24h` score `1.5018` n `44` status `ready` deltaP `23.4375` edge `-0.0311` maxDD `0.0`
- `risk_on_high->equity_1h` score `0.7894` n `49` status `ready` deltaP `12.6513` edge `0.0204` maxDD `-0.7834`
- `risk_on_and_context->equity_1h` score `0.7894` n `49` status `ready` deltaP `12.6513` edge `0.0204` maxDD `-0.7834`
- `risk_on_high->metal_4h` score `0.4505` n `47` status `ready` deltaP `7.4274` edge `0.0418` maxDD `-1.3516`
- `risk_on_and_context->metal_4h` score `0.4505` n `47` status `ready` deltaP `7.4274` edge `0.0418` maxDD `-1.3516`
- `risk_on_high->fx_4h` score `0.2534` n `47` status `ready` deltaP `13.0741` edge `0.0044` maxDD `-0.3925`
- `risk_on_and_context->fx_4h` score `0.2534` n `47` status `ready` deltaP `13.0741` edge `0.0044` maxDD `-0.3925`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
