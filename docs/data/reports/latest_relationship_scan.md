# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-16T02:37:36.968207+00:00`
- Price records: `672`
- Market context records: `4050`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `10528`

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

- `risk_on_high->unknown_4h` score `144.8917` n `40` status `ready` deltaP `-8.0488` edge `12.3096` maxDD `-10.864`
- `risk_on_and_context->unknown_4h` score `144.8917` n `40` status `ready` deltaP `-8.0488` edge `12.3096` maxDD `-10.864`
- `market_context_high->unknown_24h` score `41.9259` n `139` status `ready` deltaP `-7.9374` edge `3.9496` maxDD `-24.2289`
- `market_context_high->unknown_4h` score `21.4303` n `158` status `ready` deltaP `0.9069` edge `2.3221` maxDD `-35.7161`
- `risk_on_high->equity_24h` score `3.9084` n `40` status `ready` deltaP `33.7955` edge `0.1004` maxDD `0.0`
- `risk_on_and_context->equity_24h` score `3.9084` n `40` status `ready` deltaP `33.7955` edge `0.1004` maxDD `0.0`
- `risk_on_high->equity_4h` score `3.6796` n `40` status `ready` deltaP `38.0488` edge `0.0577` maxDD `-0.0446`
- `risk_on_and_context->equity_4h` score `3.6796` n `40` status `ready` deltaP `38.0488` edge `0.0577` maxDD `-0.0446`
- `market_context_high->index_24h` score `2.2029` n `139` status `ready` deltaP `20.7711` edge `0.0663` maxDD `-1.3629`
- `market_context_high->equity_4h` score `1.7474` n `158` status `ready` deltaP `15.8653` edge `0.1721` maxDD `-6.9137`
- `risk_on_high->crypto_major_4h` score `1.203` n `40` status `ready` deltaP `19.7561` edge `0.0351` maxDD `-2.6576`
- `risk_on_and_context->crypto_major_4h` score `1.203` n `40` status `ready` deltaP `19.7561` edge `0.0351` maxDD `-2.6576`
- `market_context_high->equity_1h` score `0.8495` n `170` status `ready` deltaP `6.6538` edge `0.0824` maxDD `-2.144`
- `risk_on_high->equity_1h` score `0.4496` n `40` status `ready` deltaP `11.2126` edge `0.0018` maxDD `-0.7937`
- `risk_on_and_context->equity_1h` score `0.4496` n `40` status `ready` deltaP `11.2126` edge `0.0018` maxDD `-0.7937`
- `market_context_high->metal_24h` score `0.2525` n `139` status `ready` deltaP `7.8962` edge `0.0671` maxDD `-4.8962`
- `risk_on_high->crypto_major_1h` score `0.1873` n `40` status `ready` deltaP `12.4551` edge `-0.0048` maxDD `-2.3372`
- `risk_on_and_context->crypto_major_1h` score `0.1873` n `40` status `ready` deltaP `12.4551` edge `-0.0048` maxDD `-2.3372`
- `risk_on_high->metal_4h` score `0.1059` n `40` status `ready` deltaP `10.6402` edge `-0.0238` maxDD `-1.3516`
- `risk_on_and_context->metal_4h` score `0.1059` n `40` status `ready` deltaP `10.6402` edge `-0.0238` maxDD `-1.3516`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
