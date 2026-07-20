# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-20T04:22:24.041373+00:00`
- Price records: `672`
- Market context records: `7318`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `14831`

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

- `risk_on_high->crypto_major_4h` score `7.1394` n `32` status `ready` deltaP `39.0317` edge `0.354` maxDD `-0.8742`
- `risk_on_and_context->crypto_major_4h` score `7.1394` n `32` status `ready` deltaP `39.0317` edge `0.354` maxDD `-0.8742`
- `risk_on_high->crypto_alt_4h` score `5.758` n `32` status `ready` deltaP `31.9945` edge `0.2909` maxDD `-0.9492`
- `risk_on_and_context->crypto_alt_4h` score `5.758` n `32` status `ready` deltaP `31.9945` edge `0.2909` maxDD `-0.9492`
- `risk_on_high->unknown_4h` score `5.2604` n `32` status `ready` deltaP `17.7068` edge `0.3633` maxDD `-0.4384`
- `risk_on_and_context->unknown_4h` score `5.2604` n `32` status `ready` deltaP `17.7068` edge `0.3633` maxDD `-0.4384`
- `risk_on_high->crypto_major_1h` score `1.2488` n `32` status `ready` deltaP `19.9289` edge `0.0517` maxDD `-0.957`
- `risk_on_and_context->crypto_major_1h` score `1.2488` n `32` status `ready` deltaP `19.9289` edge `0.0517` maxDD `-0.957`
- `risk_on_high->equity_1h` score `0.1983` n `32` status `ready` deltaP `4.0541` edge `0.0361` maxDD `-1.3497`
- `risk_on_and_context->equity_1h` score `0.1983` n `32` status `ready` deltaP `4.0541` edge `0.0361` maxDD `-1.3497`
- `risk_on_high->commodity_1h` score `0.1875` n `32` status `ready` deltaP `3.6974` edge `0.0189` maxDD `-0.2339`
- `risk_on_and_context->commodity_1h` score `0.1875` n `32` status `ready` deltaP `3.6974` edge `0.0189` maxDD `-0.2339`
- `risk_on_high->crypto_alt_1h` score `0.0845` n `32` status `ready` deltaP `0.0` edge `0.0479` maxDD `-0.9651`
- `risk_on_and_context->crypto_alt_1h` score `0.0845` n `32` status `ready` deltaP `0.0` edge `0.0479` maxDD `-0.9651`
- `risk_on_high->metal_4h` score `-0.0808` n `32` status `ready` deltaP `0.0474` edge `0.0753` maxDD `-0.5882`
- `risk_on_and_context->metal_4h` score `-0.0808` n `32` status `ready` deltaP `0.0474` edge `0.0753` maxDD `-0.5882`
- `market_context_high->fx_1h` score `-0.1847` n `129` status `ready` deltaP `3.7887` edge `0.0` maxDD `-0.5821`
- `market_context_high->unknown_4h` score `-0.5885` n `128` status `ready` deltaP `5.988` edge `0.1205` maxDD `-6.2031`
- `market_context_high->commodity_1h` score `-0.7542` n `129` status `ready` deltaP `-3.7154` edge `-0.0147` maxDD `-1.5775`
- `market_context_high->index_1h` score `-0.7547` n `129` status `ready` deltaP `-4.4102` edge `-0.0065` maxDD `-1.868`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
