# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-20T16:22:31.408301+00:00`
- Price records: `672`
- Market context records: `7371`
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

- `risk_on_high->crypto_major_4h` score `6.5818` n `32` status `ready` deltaP `36.9665` edge `0.3213` maxDD `-0.8742`
- `risk_on_and_context->crypto_major_4h` score `6.5818` n `32` status `ready` deltaP `36.9665` edge `0.3213` maxDD `-0.8742`
- `risk_on_high->crypto_alt_4h` score `5.2754` n `32` status `ready` deltaP `29.8018` edge `0.2653` maxDD `-0.9492`
- `risk_on_and_context->crypto_alt_4h` score `5.2754` n `32` status `ready` deltaP `29.8018` edge `0.2653` maxDD `-0.9492`
- `risk_on_high->unknown_4h` score `5.1531` n `32` status `ready` deltaP `16.9207` edge `0.3596` maxDD `-0.4384`
- `risk_on_and_context->unknown_4h` score `5.1531` n `32` status `ready` deltaP `16.9207` edge `0.3596` maxDD `-0.4384`
- `risk_on_high->crypto_major_1h` score `1.1739` n `32` status `ready` deltaP `19.9289` edge `0.0421` maxDD `-0.957`
- `risk_on_and_context->crypto_major_1h` score `1.1739` n `32` status `ready` deltaP `19.9289` edge `0.0421` maxDD `-0.957`
- `risk_on_high->commodity_1h` score `0.34` n `32` status `ready` deltaP `5.0488` edge `0.0226` maxDD `-0.2339`
- `risk_on_and_context->commodity_1h` score `0.34` n `32` status `ready` deltaP `5.0488` edge `0.0226` maxDD `-0.2339`
- `risk_on_high->equity_1h` score `0.1593` n `32` status `ready` deltaP `3.9039` edge `0.0321` maxDD `-1.3497`
- `risk_on_and_context->equity_1h` score `0.1593` n `32` status `ready` deltaP `3.9039` edge `0.0321` maxDD `-1.3497`
- `risk_on_high->crypto_alt_1h` score `0.0876` n `32` status `ready` deltaP `0.5988` edge `0.0443` maxDD `-0.9651`
- `risk_on_and_context->crypto_alt_1h` score `0.0876` n `32` status `ready` deltaP `0.5988` edge `0.0443` maxDD `-0.9651`
- `market_context_high->fx_1h` score `-0.1691` n `129` status `ready` deltaP `4.089` edge `0.0` maxDD `-0.5821`
- `risk_on_high->metal_4h` score `-0.2252` n `32` status `ready` deltaP `-1.0671` edge `0.0707` maxDD `-0.5882`
- `risk_on_and_context->metal_4h` score `-0.2252` n `32` status `ready` deltaP `-1.0671` edge `0.0707` maxDD `-0.5882`
- `market_context_high->commodity_1h` score `-0.655` n `129` status `ready` deltaP `-2.364` edge `-0.011` maxDD `-1.5775`
- `market_context_high->unknown_4h` score `-0.6934` n `129` status `ready` deltaP `4.8567` edge `0.1146` maxDD `-6.2031`
- `market_context_high->commodity_4h` score `-0.8009` n `129` status `ready` deltaP `-0.9352` edge `0.0004` maxDD `-2.4139`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
