# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-18T21:22:29.773767+00:00`
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

- `market_context_high->crypto_major_4h` score `1.9943` n `106` status `ready` deltaP `19.4001` edge `0.4668` maxDD `-15.2359`
- `market_context_high->commodity_24h` score `1.8887` n `106` status `ready` deltaP `16.9106` edge `0.1298` maxDD `-1.8119`
- `risk_on_high->crypto_major_4h` score `1.5336` n `73` status `ready` deltaP `19.7231` edge `0.3132` maxDD `-11.1788`
- `risk_on_and_context->crypto_major_4h` score `1.5336` n `73` status `ready` deltaP `19.7231` edge `0.3132` maxDD `-11.1788`
- `risk_on_high->commodity_24h` score `1.0314` n `73` status `ready` deltaP `18.0608` edge `0.0916` maxDD `-1.7154`
- `risk_on_and_context->commodity_24h` score `1.0314` n `73` status `ready` deltaP `18.0608` edge `0.0916` maxDD `-1.7154`
- `market_context_high->crypto_major_1h` score `0.837` n `106` status `ready` deltaP `9.2843` edge `0.1343` maxDD `-3.7781`
- `risk_on_high->index_1h` score `0.2891` n `73` status `ready` deltaP `10.4818` edge `0.0056` maxDD `-0.7394`
- `risk_on_and_context->index_1h` score `0.2891` n `73` status `ready` deltaP `10.4818` edge `0.0056` maxDD `-0.7394`
- `market_context_high->crypto_alt_1h` score `-0.1002` n `106` status `ready` deltaP `3.3527` edge `0.1148` maxDD `-7.3329`
- `risk_on_high->crypto_major_1h` score `-0.1128` n `73` status `ready` deltaP `4.6448` edge `0.0465` maxDD `-4.6876`
- `risk_on_and_context->crypto_major_1h` score `-0.1128` n `73` status `ready` deltaP `4.6448` edge `0.0465` maxDD `-4.6876`
- `risk_on_high->equity_1h` score `-0.1758` n `73` status `ready` deltaP `13.1659` edge `0.0272` maxDD `-5.3696`
- `risk_on_and_context->equity_1h` score `-0.1758` n `73` status `ready` deltaP `13.1659` edge `0.0272` maxDD `-5.3696`
- `risk_on_high->fx_1h` score `-0.3463` n `73` status `ready` deltaP `-0.6849` edge `-0.0026` maxDD `-0.3121`
- `risk_on_and_context->fx_1h` score `-0.3463` n `73` status `ready` deltaP `-0.6849` edge `-0.0026` maxDD `-0.3121`
- `market_context_high->index_1h` score `-0.4675` n `106` status `ready` deltaP `5.1703` edge `0.0014` maxDD `-1.3195`
- `market_context_high->metal_4h` score `-0.6116` n `106` status `ready` deltaP `1.1994` edge `0.0473` maxDD `-1.6961`
- `market_context_high->metal_1h` score `-0.8803` n `106` status `ready` deltaP `0.7174` edge `0.0088` maxDD `-0.9556`
- `market_context_high->fx_1h` score `-0.9513` n `106` status `ready` deltaP `-3.7736` edge `-0.002` maxDD `-0.503`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
