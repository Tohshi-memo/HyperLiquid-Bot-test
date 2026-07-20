# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-20T15:07:30.053401+00:00`
- Price records: `672`
- Market context records: `7365`
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

- `risk_on_high->crypto_major_4h` score `6.7746` n `32` status `ready` deltaP `37.5762` edge `0.3333` maxDD `-0.8742`
- `risk_on_and_context->crypto_major_4h` score `6.7746` n `32` status `ready` deltaP `37.5762` edge `0.3333` maxDD `-0.8742`
- `risk_on_high->crypto_alt_4h` score `5.4995` n `32` status `ready` deltaP `30.564` edge `0.2789` maxDD `-0.9492`
- `risk_on_and_context->crypto_alt_4h` score `5.4995` n `32` status `ready` deltaP `30.564` edge `0.2789` maxDD `-0.9492`
- `risk_on_high->unknown_4h` score `5.1821` n `32` status `ready` deltaP `17.0732` edge `0.361` maxDD `-0.4384`
- `risk_on_and_context->unknown_4h` score `5.1821` n `32` status `ready` deltaP `17.0732` edge `0.361` maxDD `-0.4384`
- `risk_on_high->crypto_major_1h` score `1.2635` n `32` status `ready` deltaP `20.378` edge `0.0506` maxDD `-0.957`
- `risk_on_and_context->crypto_major_1h` score `1.2635` n `32` status `ready` deltaP `20.378` edge `0.0506` maxDD `-0.957`
- `risk_on_high->commodity_1h` score `0.2788` n `32` status `ready` deltaP `4.4482` edge `0.0215` maxDD `-0.2339`
- `risk_on_and_context->commodity_1h` score `0.2788` n `32` status `ready` deltaP `4.4482` edge `0.0215` maxDD `-0.2339`
- `risk_on_high->equity_1h` score `0.2225` n `32` status `ready` deltaP `4.3544` edge `0.0372` maxDD `-1.3497`
- `risk_on_and_context->equity_1h` score `0.2225` n `32` status `ready` deltaP `4.3544` edge `0.0372` maxDD `-1.3497`
- `risk_on_high->crypto_alt_1h` score `0.164` n `32` status `ready` deltaP `1.0479` edge `0.0511` maxDD `-0.9651`
- `risk_on_and_context->crypto_alt_1h` score `0.164` n `32` status `ready` deltaP `1.0479` edge `0.0511` maxDD `-0.9651`
- `market_context_high->fx_1h` score `-0.1629` n `129` status `ready` deltaP `4.2392` edge `-0.0002` maxDD `-0.5821`
- `risk_on_high->metal_4h` score `-0.184` n `32` status `ready` deltaP `-0.7622` edge `0.0721` maxDD `-0.5882`
- `risk_on_and_context->metal_4h` score `-0.184` n `32` status `ready` deltaP `-0.7622` edge `0.0721` maxDD `-0.5882`
- `market_context_high->unknown_4h` score `-0.6745` n `129` status `ready` deltaP `5.0092` edge `0.116` maxDD `-6.2031`
- `market_context_high->commodity_1h` score `-0.6948` n `129` status `ready` deltaP `-2.9646` edge `-0.0121` maxDD `-1.5775`
- `market_context_high->index_1h` score `-0.7953` n `129` status `ready` deltaP `-5.1609` edge `-0.0067` maxDD `-1.868`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
