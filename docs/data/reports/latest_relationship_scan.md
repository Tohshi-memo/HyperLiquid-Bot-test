# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-20T06:37:25.580551+00:00`
- Price records: `672`
- Market context records: `7328`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `14722`

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

- `risk_on_high->crypto_major_4h` score `7.3321` n `32` status `ready` deltaP `40.0152` edge `0.3635` maxDD `-0.8742`
- `risk_on_and_context->crypto_major_4h` score `7.3321` n `32` status `ready` deltaP `40.0152` edge `0.3635` maxDD `-0.8742`
- `risk_on_high->crypto_alt_4h` score `6.0525` n `32` status `ready` deltaP `33.1555` edge `0.3077` maxDD `-0.9492`
- `risk_on_and_context->crypto_alt_4h` score `6.0525` n `32` status `ready` deltaP `33.1555` edge `0.3077` maxDD `-0.9492`
- `risk_on_high->unknown_4h` score `5.3556` n `32` status `ready` deltaP `18.5976` edge `0.3653` maxDD `-0.4384`
- `risk_on_and_context->unknown_4h` score `5.3556` n `32` status `ready` deltaP `18.5976` edge `0.3653` maxDD `-0.4384`
- `risk_on_high->crypto_major_1h` score `1.315` n `32` status `ready` deltaP `20.5277` edge `0.0562` maxDD `-0.957`
- `risk_on_and_context->crypto_major_1h` score `1.315` n `32` status `ready` deltaP `20.5277` edge `0.0562` maxDD `-0.957`
- `risk_on_high->equity_1h` score `0.2147` n `32` status `ready` deltaP `4.2042` edge `0.0372` maxDD `-1.3497`
- `risk_on_and_context->equity_1h` score `0.2147` n `32` status `ready` deltaP `4.2042` edge `0.0372` maxDD `-1.3497`
- `risk_on_high->crypto_alt_1h` score `0.2092` n `32` status `ready` deltaP `1.1976` edge `0.0559` maxDD `-0.9651`
- `risk_on_and_context->crypto_alt_1h` score `0.2092` n `32` status `ready` deltaP `1.1976` edge `0.0559` maxDD `-0.9651`
- `risk_on_high->commodity_1h` score `0.1983` n `32` status `ready` deltaP `3.8476` edge `0.0188` maxDD `-0.2339`
- `risk_on_and_context->commodity_1h` score `0.1983` n `32` status `ready` deltaP `3.8476` edge `0.0188` maxDD `-0.2339`
- `risk_on_high->metal_4h` score `0.0195` n `32` status `ready` deltaP `0.7622` edge `0.0789` maxDD `-0.5882`
- `risk_on_and_context->metal_4h` score `0.0195` n `32` status `ready` deltaP `0.7622` edge `0.0789` maxDD `-0.5882`
- `market_context_high->fx_1h` score `-0.152` n `129` status `ready` deltaP `4.3893` edge `0.0002` maxDD `-0.5821`
- `market_context_high->unknown_4h` score `-0.5617` n `129` status `ready` deltaP `6.5336` edge `0.1203` maxDD `-6.2031`
- `market_context_high->commodity_1h` score `-0.7471` n `129` status `ready` deltaP `-3.5652` edge `-0.0148` maxDD `-1.5775`
- `market_context_high->crypto_major_1h` score `-0.774` n `129` status `ready` deltaP `3.6915` edge `0.0172` maxDD `-7.6171`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
