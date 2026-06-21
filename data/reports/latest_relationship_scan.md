# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-21T20:52:26.669050+00:00`
- Price records: `672`
- Market context records: `4350`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11234`

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

- `risk_on_high->unknown_4h` score `131.0523` n `44` status `ready` deltaP `-0.6791` edge `11.1074` maxDD `-10.8809`
- `risk_on_and_context->unknown_4h` score `131.0523` n `44` status `ready` deltaP `-0.6791` edge `11.1074` maxDD `-10.8809`
- `market_context_high->unknown_1h` score `32.4944` n `220` status `ready` deltaP `3.1683` edge `2.8447` maxDD `-9.6361`
- `market_context_high->unknown_4h` score `12.2845` n `218` status `ready` deltaP `3.5536` edge `1.543` maxDD `-35.7719`
- `risk_on_high->equity_4h` score `3.1508` n `44` status `ready` deltaP `34.6175` edge `0.0365` maxDD `-0.044`
- `risk_on_and_context->equity_4h` score `3.1508` n `44` status `ready` deltaP `34.6175` edge `0.0365` maxDD `-0.044`
- `risk_on_high->metal_24h` score `2.6904` n `44` status `ready` deltaP `-17.44` edge `0.5226` maxDD `-1.9133`
- `risk_on_and_context->metal_24h` score `2.6904` n `44` status `ready` deltaP `-17.44` edge `0.5226` maxDD `-1.9133`
- `risk_on_high->equity_24h` score `1.871` n `44` status `ready` deltaP `20.3125` edge `0.0205` maxDD `0.0`
- `risk_on_and_context->equity_24h` score `1.871` n `44` status `ready` deltaP `20.3125` edge `0.0205` maxDD `0.0`
- `risk_on_high->crypto_major_4h` score `1.6761` n `44` status `ready` deltaP `17.2395` edge `0.0913` maxDD `-2.6576`
- `risk_on_and_context->crypto_major_4h` score `1.6761` n `44` status `ready` deltaP `17.2395` edge `0.0913` maxDD `-2.6576`
- `risk_on_high->fx_1h` score `0.5237` n `44` status `ready` deltaP `9.3903` edge `0.004` maxDD `-0.1704`
- `risk_on_and_context->fx_1h` score `0.5237` n `44` status `ready` deltaP `9.3903` edge `0.004` maxDD `-0.1704`
- `risk_on_high->metal_4h` score `0.4478` n `44` status `ready` deltaP `6.7904` edge `0.0457` maxDD `-1.3516`
- `risk_on_and_context->metal_4h` score `0.4478` n `44` status `ready` deltaP `6.7904` edge `0.0457` maxDD `-1.3516`
- `risk_on_high->index_24h` score `0.4437` n `44` status `ready` deltaP `19.2708` edge `-0.0915` maxDD `0.0`
- `risk_on_and_context->index_24h` score `0.4437` n `44` status `ready` deltaP `19.2708` edge `-0.0915` maxDD `0.0`
- `risk_on_high->equity_1h` score `0.3467` n `44` status `ready` deltaP `9.0229` edge `0.0077` maxDD `-0.7834`
- `risk_on_and_context->equity_1h` score `0.3467` n `44` status `ready` deltaP `9.0229` edge `0.0077` maxDD `-0.7834`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
