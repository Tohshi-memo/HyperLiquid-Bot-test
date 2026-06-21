# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-21T18:37:29.837351+00:00`
- Price records: `672`
- Market context records: `4340`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `10810`

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

- `risk_on_high->unknown_4h` score `130.9769` n `44` status `ready` deltaP `-0.5266` edge `11.1001` maxDD `-10.8809`
- `risk_on_and_context->unknown_4h` score `130.9769` n `44` status `ready` deltaP `-0.5266` edge `11.1001` maxDD `-10.8809`
- `market_context_high->unknown_1h` score `30.3058` n `228` status `ready` deltaP `3.5456` edge `2.6598` maxDD `-9.6361`
- `market_context_high->unknown_4h` score `11.0704` n `224` status `ready` deltaP `1.5027` edge `1.4555` maxDD `-35.7719`
- `risk_on_high->equity_4h` score `2.9944` n `44` status `ready` deltaP `33.398` edge `0.0316` maxDD `-0.044`
- `risk_on_and_context->equity_4h` score `2.9944` n `44` status `ready` deltaP `33.398` edge `0.0316` maxDD `-0.044`
- `risk_on_high->metal_24h` score `2.5659` n `44` status `ready` deltaP `-18.8289` edge `0.5159` maxDD `-1.9133`
- `risk_on_and_context->metal_24h` score `2.5659` n `44` status `ready` deltaP `-18.8289` edge `0.5159` maxDD `-1.9133`
- `risk_on_high->equity_24h` score `2.1304` n `44` status `ready` deltaP `21.875` edge `0.0317` maxDD `0.0`
- `risk_on_and_context->equity_24h` score `2.1304` n `44` status `ready` deltaP `21.875` edge `0.0317` maxDD `0.0`
- `risk_on_high->crypto_major_4h` score `1.7197` n `44` status `ready` deltaP `17.5444` edge `0.0929` maxDD `-2.6576`
- `risk_on_and_context->crypto_major_4h` score `1.7197` n `44` status `ready` deltaP `17.5444` edge `0.0929` maxDD `-2.6576`
- `market_context_high->unknown_24h` score `0.5573` n `207` status `ready` deltaP `-6.8085` edge `0.4952` maxDD `-24.2693`
- `risk_on_high->fx_1h` score `0.459` n `44` status `ready` deltaP `8.6418` edge `0.0036` maxDD `-0.1704`
- `risk_on_and_context->fx_1h` score `0.459` n `44` status `ready` deltaP `8.6418` edge `0.0036` maxDD `-0.1704`
- `risk_on_high->metal_4h` score `0.4413` n `44` status `ready` deltaP `6.4856` edge `0.0469` maxDD `-1.3516`
- `risk_on_and_context->metal_4h` score `0.4413` n `44` status `ready` deltaP `6.4856` edge `0.0469` maxDD `-1.3516`
- `risk_on_high->index_24h` score `0.3681` n `44` status `ready` deltaP `19.2708` edge `-0.0978` maxDD `0.0`
- `risk_on_and_context->index_24h` score `0.3681` n `44` status `ready` deltaP `19.2708` edge `-0.0978` maxDD `0.0`
- `risk_on_high->crypto_major_1h` score `0.2626` n `44` status `ready` deltaP `8.5466` edge `0.0309` maxDD `-2.3372`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
