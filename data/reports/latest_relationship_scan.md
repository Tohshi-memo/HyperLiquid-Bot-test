# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-20T11:52:29.046865+00:00`
- Price records: `672`
- Market context records: `7351`
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

- `risk_on_high->crypto_major_4h` score `7.1125` n `32` status `ready` deltaP `39.1006` edge `0.3513` maxDD `-0.8742`
- `risk_on_and_context->crypto_major_4h` score `7.1125` n `32` status `ready` deltaP `39.1006` edge `0.3513` maxDD `-0.8742`
- `risk_on_high->crypto_alt_4h` score `5.8281` n `32` status `ready` deltaP `32.2409` edge `0.2951` maxDD `-0.9492`
- `risk_on_and_context->crypto_alt_4h` score `5.8281` n `32` status `ready` deltaP `32.2409` edge `0.2951` maxDD `-0.9492`
- `risk_on_high->unknown_4h` score `5.3968` n `32` status `ready` deltaP `18.9024` edge `0.3667` maxDD `-0.4384`
- `risk_on_and_context->unknown_4h` score `5.3968` n `32` status `ready` deltaP `18.9024` edge `0.3667` maxDD `-0.4384`
- `risk_on_high->crypto_major_1h` score `1.2589` n `32` status `ready` deltaP `20.2283` edge `0.051` maxDD `-0.957`
- `risk_on_and_context->crypto_major_1h` score `1.2589` n `32` status `ready` deltaP `20.2283` edge `0.051` maxDD `-0.957`
- `risk_on_high->commodity_1h` score `0.2571` n `32` status `ready` deltaP `4.1479` edge `0.0217` maxDD `-0.2339`
- `risk_on_and_context->commodity_1h` score `0.2571` n `32` status `ready` deltaP `4.1479` edge `0.0217` maxDD `-0.2339`
- `risk_on_high->equity_1h` score `0.1991` n `32` status `ready` deltaP `4.3544` edge `0.0342` maxDD `-1.3497`
- `risk_on_and_context->equity_1h` score `0.1991` n `32` status `ready` deltaP `4.3544` edge `0.0342` maxDD `-1.3497`
- `risk_on_high->crypto_alt_1h` score `0.1531` n `32` status `ready` deltaP `0.8982` edge `0.0507` maxDD `-0.9651`
- `risk_on_and_context->crypto_alt_1h` score `0.1531` n `32` status `ready` deltaP `0.8982` edge `0.0507` maxDD `-0.9651`
- `risk_on_high->metal_4h` score `-0.1238` n `32` status `ready` deltaP `-0.6098` edge `0.0761` maxDD `-0.5882`
- `risk_on_and_context->metal_4h` score `-0.1238` n `32` status `ready` deltaP `-0.6098` edge `0.0761` maxDD `-0.5882`
- `market_context_high->fx_1h` score `-0.1801` n `129` status `ready` deltaP `3.9389` edge `-0.0004` maxDD `-0.5821`
- `market_context_high->unknown_4h` score `-0.5349` n `129` status `ready` deltaP `6.8384` edge `0.1217` maxDD `-6.2031`
- `market_context_high->commodity_1h` score `-0.7089` n `129` status `ready` deltaP `-3.2649` edge `-0.0119` maxDD `-1.5775`
- `market_context_high->index_1h` score `-0.7999` n `129` status `ready` deltaP `-5.1609` edge `-0.0073` maxDD `-1.868`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
