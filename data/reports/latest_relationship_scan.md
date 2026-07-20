# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-20T06:52:25.627251+00:00`
- Price records: `672`
- Market context records: `7329`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `14728`

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

- `risk_on_high->crypto_major_4h` score `7.3683` n `32` status `ready` deltaP `40.1677` edge `0.3655` maxDD `-0.8742`
- `risk_on_and_context->crypto_major_4h` score `7.3683` n `32` status `ready` deltaP `40.1677` edge `0.3655` maxDD `-0.8742`
- `risk_on_high->crypto_alt_4h` score `6.0875` n `32` status `ready` deltaP `33.3079` edge `0.3096` maxDD `-0.9492`
- `risk_on_and_context->crypto_alt_4h` score `6.0875` n `32` status `ready` deltaP `33.3079` edge `0.3096` maxDD `-0.9492`
- `risk_on_high->unknown_4h` score `5.3762` n `32` status `ready` deltaP `18.75` edge `0.366` maxDD `-0.4384`
- `risk_on_and_context->unknown_4h` score `5.3762` n `32` status `ready` deltaP `18.75` edge `0.366` maxDD `-0.4384`
- `risk_on_high->crypto_major_1h` score `1.3173` n `32` status `ready` deltaP `20.5277` edge `0.0565` maxDD `-0.957`
- `risk_on_and_context->crypto_major_1h` score `1.3173` n `32` status `ready` deltaP `20.5277` edge `0.0565` maxDD `-0.957`
- `risk_on_high->equity_1h` score `0.2116` n `32` status `ready` deltaP `4.2042` edge `0.0368` maxDD `-1.3497`
- `risk_on_and_context->equity_1h` score `0.2116` n `32` status `ready` deltaP `4.2042` edge `0.0368` maxDD `-1.3497`
- `risk_on_high->crypto_alt_1h` score `0.2092` n `32` status `ready` deltaP `1.1976` edge `0.0559` maxDD `-0.9651`
- `risk_on_and_context->crypto_alt_1h` score `0.2092` n `32` status `ready` deltaP `1.1976` edge `0.0559` maxDD `-0.9651`
- `risk_on_high->commodity_1h` score `0.1959` n `32` status `ready` deltaP `3.8476` edge `0.0186` maxDD `-0.2339`
- `risk_on_and_context->commodity_1h` score `0.1959` n `32` status `ready` deltaP `3.8476` edge `0.0186` maxDD `-0.2339`
- `risk_on_high->metal_4h` score `0.0389` n `32` status `ready` deltaP `0.9146` edge `0.0795` maxDD `-0.5882`
- `risk_on_and_context->metal_4h` score `0.0389` n `32` status `ready` deltaP `0.9146` edge `0.0795` maxDD `-0.5882`
- `market_context_high->fx_1h` score `-0.152` n `129` status `ready` deltaP `4.3893` edge `0.0002` maxDD `-0.5821`
- `market_context_high->unknown_4h` score `-0.5483` n `129` status `ready` deltaP `6.686` edge `0.121` maxDD `-6.2031`
- `market_context_high->commodity_1h` score `-0.7487` n `129` status `ready` deltaP `-3.5652` edge `-0.015` maxDD `-1.5775`
- `market_context_high->crypto_major_1h` score `-0.7717` n `129` status `ready` deltaP `3.6915` edge `0.0175` maxDD `-7.6171`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
