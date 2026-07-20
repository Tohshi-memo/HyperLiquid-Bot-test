# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-20T11:22:29.121074+00:00`
- Price records: `672`
- Market context records: `7349`
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

- `risk_on_high->crypto_major_4h` score `7.1897` n `32` status `ready` deltaP `39.4055` edge `0.3557` maxDD `-0.8742`
- `risk_on_and_context->crypto_major_4h` score `7.1897` n `32` status `ready` deltaP `39.4055` edge `0.3557` maxDD `-0.8742`
- `risk_on_high->crypto_alt_4h` score `5.8885` n `32` status `ready` deltaP `32.5457` edge `0.2981` maxDD `-0.9492`
- `risk_on_and_context->crypto_alt_4h` score `5.8885` n `32` status `ready` deltaP `32.5457` edge `0.2981` maxDD `-0.9492`
- `risk_on_high->unknown_4h` score `5.4028` n `32` status `ready` deltaP `18.9024` edge `0.3672` maxDD `-0.4384`
- `risk_on_and_context->unknown_4h` score `5.4028` n `32` status `ready` deltaP `18.9024` edge `0.3672` maxDD `-0.4384`
- `risk_on_high->crypto_major_1h` score `1.2745` n `32` status `ready` deltaP `20.2283` edge `0.053` maxDD `-0.957`
- `risk_on_and_context->crypto_major_1h` score `1.2745` n `32` status `ready` deltaP `20.2283` edge `0.053` maxDD `-0.957`
- `risk_on_high->commodity_1h` score `0.2343` n `32` status `ready` deltaP `3.9977` edge `0.0208` maxDD `-0.2339`
- `risk_on_and_context->commodity_1h` score `0.2343` n `32` status `ready` deltaP `3.9977` edge `0.0208` maxDD `-0.2339`
- `risk_on_high->equity_1h` score `0.2069` n `32` status `ready` deltaP `4.3544` edge `0.0352` maxDD `-1.3497`
- `risk_on_and_context->equity_1h` score `0.2069` n `32` status `ready` deltaP `4.3544` edge `0.0352` maxDD `-1.3497`
- `risk_on_high->crypto_alt_1h` score `0.171` n `32` status `ready` deltaP `1.0479` edge `0.052` maxDD `-0.9651`
- `risk_on_and_context->crypto_alt_1h` score `0.171` n `32` status `ready` deltaP `1.0479` edge `0.052` maxDD `-0.9651`
- `risk_on_high->metal_4h` score `-0.0886` n `32` status `ready` deltaP `-0.3049` edge `0.077` maxDD `-0.5882`
- `risk_on_and_context->metal_4h` score `-0.0886` n `32` status `ready` deltaP `-0.3049` edge `0.077` maxDD `-0.5882`
- `market_context_high->fx_1h` score `-0.1964` n `129` status `ready` deltaP `3.6386` edge `-0.0005` maxDD `-0.5821`
- `market_context_high->unknown_4h` score `-0.531` n `129` status `ready` deltaP `6.8384` edge `0.1222` maxDD `-6.2031`
- `market_context_high->commodity_1h` score `-0.7237` n `129` status `ready` deltaP `-3.4151` edge `-0.0128` maxDD `-1.5775`
- `market_context_high->index_1h` score `-0.7984` n `129` status `ready` deltaP `-5.1609` edge `-0.0071` maxDD `-1.868`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
