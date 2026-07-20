# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-20T15:52:27.997773+00:00`
- Price records: `672`
- Market context records: `7369`
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

- `risk_on_high->crypto_major_4h` score `6.6794` n `32` status `ready` deltaP `37.2713` edge `0.3274` maxDD `-0.8742`
- `risk_on_and_context->crypto_major_4h` score `6.6794` n `32` status `ready` deltaP `37.2713` edge `0.3274` maxDD `-0.8742`
- `risk_on_high->crypto_alt_4h` score `5.3766` n `32` status `ready` deltaP `30.1067` edge `0.2717` maxDD `-0.9492`
- `risk_on_and_context->crypto_alt_4h` score `5.3766` n `32` status `ready` deltaP `30.1067` edge `0.2717` maxDD `-0.9492`
- `risk_on_high->unknown_4h` score `5.1531` n `32` status `ready` deltaP `16.9207` edge `0.3596` maxDD `-0.4384`
- `risk_on_and_context->unknown_4h` score `5.1531` n `32` status `ready` deltaP `16.9207` edge `0.3596` maxDD `-0.4384`
- `risk_on_high->crypto_major_1h` score `1.223` n `32` status `ready` deltaP `20.2283` edge `0.0464` maxDD `-0.957`
- `risk_on_and_context->crypto_major_1h` score `1.223` n `32` status `ready` deltaP `20.2283` edge `0.0464` maxDD `-0.957`
- `risk_on_high->commodity_1h` score `0.31` n `32` status `ready` deltaP `4.7485` edge `0.0221` maxDD `-0.2339`
- `risk_on_and_context->commodity_1h` score `0.31` n `32` status `ready` deltaP `4.7485` edge `0.0221` maxDD `-0.2339`
- `risk_on_high->equity_1h` score `0.2061` n `32` status `ready` deltaP `4.2042` edge `0.0361` maxDD `-1.3497`
- `risk_on_and_context->equity_1h` score `0.2061` n `32` status `ready` deltaP `4.2042` edge `0.0361` maxDD `-1.3497`
- `risk_on_high->crypto_alt_1h` score `0.1304` n `32` status `ready` deltaP `0.8982` edge `0.0478` maxDD `-0.9651`
- `risk_on_and_context->crypto_alt_1h` score `0.1304` n `32` status `ready` deltaP `0.8982` edge `0.0478` maxDD `-0.9651`
- `market_context_high->fx_1h` score `-0.1613` n `129` status `ready` deltaP `4.2392` edge `0.0` maxDD `-0.5821`
- `risk_on_high->metal_4h` score `-0.1876` n `32` status `ready` deltaP `-0.7622` edge `0.0718` maxDD `-0.5882`
- `risk_on_and_context->metal_4h` score `-0.1876` n `32` status `ready` deltaP `-0.7622` edge `0.0718` maxDD `-0.5882`
- `market_context_high->commodity_1h` score `-0.6745` n `129` status `ready` deltaP `-2.6643` edge `-0.0115` maxDD `-1.5775`
- `market_context_high->unknown_4h` score `-0.6934` n `129` status `ready` deltaP `4.8567` edge `0.1146` maxDD `-6.2031`
- `market_context_high->index_1h` score `-0.8117` n `129` status `ready` deltaP `-5.4612` edge `-0.0068` maxDD `-1.868`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
