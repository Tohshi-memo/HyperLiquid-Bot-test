# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-20T14:37:30.242437+00:00`
- Price records: `672`
- Market context records: `7363`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `14631`

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

- `risk_on_high->crypto_major_4h` score `6.8108` n `32` status `ready` deltaP `37.7287` edge `0.3353` maxDD `-0.8742`
- `risk_on_and_context->crypto_major_4h` score `6.8108` n `32` status `ready` deltaP `37.7287` edge `0.3353` maxDD `-0.8742`
- `risk_on_high->crypto_alt_4h` score `5.5587` n `32` status `ready` deltaP `30.8689` edge `0.2818` maxDD `-0.9492`
- `risk_on_and_context->crypto_alt_4h` score `5.5587` n `32` status `ready` deltaP `30.8689` edge `0.2818` maxDD `-0.9492`
- `risk_on_high->unknown_4h` score `5.2221` n `32` status `ready` deltaP `17.378` edge `0.3623` maxDD `-0.4384`
- `risk_on_and_context->unknown_4h` score `5.2221` n `32` status `ready` deltaP `17.378` edge `0.3623` maxDD `-0.4384`
- `risk_on_high->crypto_major_1h` score `1.2448` n `32` status `ready` deltaP `20.2283` edge `0.0492` maxDD `-0.957`
- `risk_on_and_context->crypto_major_1h` score `1.2448` n `32` status `ready` deltaP `20.2283` edge `0.0492` maxDD `-0.957`
- `risk_on_high->commodity_1h` score `0.2596` n `32` status `ready` deltaP `4.298` edge `0.0209` maxDD `-0.2339`
- `risk_on_and_context->commodity_1h` score `0.2596` n `32` status `ready` deltaP `4.298` edge `0.0209` maxDD `-0.2339`
- `risk_on_high->equity_1h` score `0.1804` n `32` status `ready` deltaP `4.0541` edge `0.0338` maxDD `-1.3497`
- `risk_on_and_context->equity_1h` score `0.1804` n `32` status `ready` deltaP `4.0541` edge `0.0338` maxDD `-1.3497`
- `risk_on_high->crypto_alt_1h` score `0.146` n `32` status `ready` deltaP `0.8982` edge `0.0498` maxDD `-0.9651`
- `risk_on_and_context->crypto_alt_1h` score `0.146` n `32` status `ready` deltaP `0.8982` edge `0.0498` maxDD `-0.9651`
- `risk_on_high->metal_4h` score `-0.161` n `32` status `ready` deltaP `-0.6098` edge `0.073` maxDD `-0.5882`
- `risk_on_and_context->metal_4h` score `-0.161` n `32` status `ready` deltaP `-0.6098` edge `0.073` maxDD `-0.5882`
- `market_context_high->fx_1h` score `-0.1629` n `129` status `ready` deltaP `4.2392` edge `-0.0002` maxDD `-0.5821`
- `market_context_high->unknown_4h` score `-0.6485` n `129` status `ready` deltaP `5.314` edge `0.1173` maxDD `-6.2031`
- `market_context_high->commodity_1h` score `-0.7073` n `129` status `ready` deltaP `-3.1148` edge `-0.0127` maxDD `-1.5775`
- `market_context_high->index_1h` score `-0.8156` n `129` status `ready` deltaP `-5.4612` edge `-0.0073` maxDD `-1.868`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
