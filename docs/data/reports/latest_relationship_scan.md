# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-20T10:07:31.920254+00:00`
- Price records: `672`
- Market context records: `7343`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `14623`

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

- `risk_on_high->crypto_major_4h` score `7.3899` n `32` status `ready` deltaP `40.1677` edge `0.3673` maxDD `-0.8742`
- `risk_on_and_context->crypto_major_4h` score `7.3899` n `32` status `ready` deltaP `40.1677` edge `0.3673` maxDD `-0.8742`
- `risk_on_high->crypto_alt_4h` score `6.0707` n `32` status `ready` deltaP `33.3079` edge `0.3082` maxDD `-0.9492`
- `risk_on_and_context->crypto_alt_4h` score `6.0707` n `32` status `ready` deltaP `33.3079` edge `0.3082` maxDD `-0.9492`
- `risk_on_high->unknown_4h` score `5.415` n `32` status `ready` deltaP `19.0549` edge `0.3672` maxDD `-0.4384`
- `risk_on_and_context->unknown_4h` score `5.415` n `32` status `ready` deltaP `19.0549` edge `0.3672` maxDD `-0.4384`
- `risk_on_high->crypto_major_1h` score `1.3103` n `32` status `ready` deltaP `20.6774` edge `0.0546` maxDD `-0.957`
- `risk_on_and_context->crypto_major_1h` score `1.3103` n `32` status `ready` deltaP `20.6774` edge `0.0546` maxDD `-0.957`
- `risk_on_high->equity_1h` score `0.2428` n `32` status `ready` deltaP `4.8048` edge `0.0368` maxDD `-1.3497`
- `risk_on_and_context->equity_1h` score `0.2428` n `32` status `ready` deltaP `4.8048` edge `0.0368` maxDD `-1.3497`
- `risk_on_high->commodity_1h` score `0.2259` n `32` status `ready` deltaP `3.9977` edge `0.0201` maxDD `-0.2339`
- `risk_on_and_context->commodity_1h` score `0.2259` n `32` status `ready` deltaP `3.9977` edge `0.0201` maxDD `-0.2339`
- `risk_on_high->crypto_alt_1h` score `0.1819` n `32` status `ready` deltaP `1.1976` edge `0.0524` maxDD `-0.9651`
- `risk_on_and_context->crypto_alt_1h` score `0.1819` n `32` status `ready` deltaP `1.1976` edge `0.0524` maxDD `-0.9651`
- `risk_on_high->metal_4h` score `0.0024` n `32` status `ready` deltaP `0.4573` edge `0.0795` maxDD `-0.5882`
- `risk_on_and_context->metal_4h` score `0.0024` n `32` status `ready` deltaP `0.4573` edge `0.0795` maxDD `-0.5882`
- `market_context_high->fx_1h` score `-0.1879` n `129` status `ready` deltaP `3.7887` edge `-0.0004` maxDD `-0.5821`
- `market_context_high->unknown_4h` score `-0.5231` n `129` status `ready` deltaP `6.9909` edge `0.1222` maxDD `-6.2031`
- `market_context_high->commodity_1h` score `-0.7292` n `129` status `ready` deltaP `-3.4151` edge `-0.0135` maxDD `-1.5775`
- `market_context_high->index_1h` score `-0.7711` n `129` status `ready` deltaP `-4.7105` edge `-0.0066` maxDD `-1.868`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
