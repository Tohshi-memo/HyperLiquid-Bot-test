# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-20T15:37:34.872895+00:00`
- Price records: `672`
- Market context records: `7368`
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

- `risk_on_high->crypto_major_4h` score `6.718` n `32` status `ready` deltaP `37.4238` edge `0.3296` maxDD `-0.8742`
- `risk_on_and_context->crypto_major_4h` score `6.718` n `32` status `ready` deltaP `37.4238` edge `0.3296` maxDD `-0.8742`
- `risk_on_high->crypto_alt_4h` score `5.4211` n `32` status `ready` deltaP `30.2591` edge `0.2744` maxDD `-0.9492`
- `risk_on_and_context->crypto_alt_4h` score `5.4211` n `32` status `ready` deltaP `30.2591` edge `0.2744` maxDD `-0.9492`
- `risk_on_high->unknown_4h` score `5.1543` n `32` status `ready` deltaP `16.9207` edge `0.3597` maxDD `-0.4384`
- `risk_on_and_context->unknown_4h` score `5.1543` n `32` status `ready` deltaP `16.9207` edge `0.3597` maxDD `-0.4384`
- `risk_on_high->crypto_major_1h` score `1.2495` n `32` status `ready` deltaP `20.378` edge `0.0488` maxDD `-0.957`
- `risk_on_and_context->crypto_major_1h` score `1.2495` n `32` status `ready` deltaP `20.378` edge `0.0488` maxDD `-0.957`
- `risk_on_high->commodity_1h` score `0.2932` n `32` status `ready` deltaP `4.5983` edge `0.0217` maxDD `-0.2339`
- `risk_on_and_context->commodity_1h` score `0.2932` n `32` status `ready` deltaP `4.5983` edge `0.0217` maxDD `-0.2339`
- `risk_on_high->equity_1h` score `0.2217` n `32` status `ready` deltaP `4.3544` edge `0.0371` maxDD `-1.3497`
- `risk_on_and_context->equity_1h` score `0.2217` n `32` status `ready` deltaP `4.3544` edge `0.0371` maxDD `-1.3497`
- `risk_on_high->crypto_alt_1h` score `0.1538` n `32` status `ready` deltaP `1.0479` edge `0.0498` maxDD `-0.9651`
- `risk_on_and_context->crypto_alt_1h` score `0.1538` n `32` status `ready` deltaP `1.0479` edge `0.0498` maxDD `-0.9651`
- `market_context_high->fx_1h` score `-0.1621` n `129` status `ready` deltaP `4.2392` edge `-0.0001` maxDD `-0.5821`
- `risk_on_high->metal_4h` score `-0.1864` n `32` status `ready` deltaP `-0.7622` edge `0.0719` maxDD `-0.5882`
- `risk_on_and_context->metal_4h` score `-0.1864` n `32` status `ready` deltaP `-0.7622` edge `0.0719` maxDD `-0.5882`
- `market_context_high->commodity_1h` score `-0.6855` n `129` status `ready` deltaP `-2.8145` edge `-0.0119` maxDD `-1.5775`
- `market_context_high->unknown_4h` score `-0.6926` n `129` status `ready` deltaP `4.8567` edge `0.1147` maxDD `-6.2031`
- `market_context_high->index_1h` score `-0.8023` n `129` status `ready` deltaP `-5.3111` edge `-0.0066` maxDD `-1.868`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
