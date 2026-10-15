# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-15T07:22:28.016933+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9729`

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

- `risk_on_high->commodity_24h` score `7.9243` n `54` status `ready` deltaP `41.2892` edge `0.3851` maxDD `0.0`
- `risk_on_and_context->commodity_24h` score `7.9243` n `54` status `ready` deltaP `41.2892` edge `0.3851` maxDD `0.0`
- `market_context_high->crypto_alt_4h` score `7.8233` n `120` status `ready` deltaP `19.2378` edge `0.6681` maxDD `-9.2196`
- `risk_on_high->crypto_alt_4h` score `6.9185` n `54` status `ready` deltaP `23.3119` edge `0.4658` maxDD `-1.907`
- `risk_on_and_context->crypto_alt_4h` score `6.9185` n `54` status `ready` deltaP `23.3119` edge `0.4658` maxDD `-1.907`
- `market_context_high->crypto_major_4h` score `6.339` n `120` status `ready` deltaP `20.7826` edge `0.5456` maxDD `-7.4722`
- `risk_on_high->crypto_major_4h` score `4.8816` n `54` status `ready` deltaP `35.5974` edge `0.4738` maxDD `-4.1548`
- `risk_on_and_context->crypto_major_4h` score `4.8816` n `54` status `ready` deltaP `35.5974` edge `0.4738` maxDD `-4.1548`
- `market_context_high->crypto_alt_1h` score `1.859` n `123` status `ready` deltaP `13.6288` edge `0.1705` maxDD `-5.8485`
- `market_context_high->crypto_major_1h` score `1.1796` n `123` status `ready` deltaP `5.6485` edge `0.1412` maxDD `-3.7781`
- `market_context_high->metal_4h` score `0.1886` n `120` status `ready` deltaP `12.0528` edge `0.0399` maxDD `-1.6961`
- `risk_on_high->crypto_major_1h` score `-0.2767` n `54` status `ready` deltaP `1.4028` edge `0.0274` maxDD `-3.7781`
- `risk_on_and_context->crypto_major_1h` score `-0.2767` n `54` status `ready` deltaP `1.4028` edge `0.0274` maxDD `-3.7781`
- `risk_on_high->crypto_alt_1h` score `-0.3122` n `54` status `ready` deltaP `4.9568` edge `0.0292` maxDD `-5.8485`
- `risk_on_and_context->crypto_alt_1h` score `-0.3122` n `54` status `ready` deltaP `4.9568` edge `0.0292` maxDD `-5.8485`
- `market_context_high->fx_1h` score `-0.3483` n `123` status `ready` deltaP `-0.6702` edge `-0.0018` maxDD `-0.4047`
- `market_context_high->metal_1h` score `-0.3981` n `123` status `ready` deltaP `7.0603` edge `0.0067` maxDD `-0.9556`
- `market_context_high->commodity_24h` score `-0.439` n `116` status `ready` deltaP `12.8409` edge `0.1466` maxDD `-12.0788`
- `risk_on_high->metal_1h` score `-0.4422` n `54` status `ready` deltaP `2.0016` edge `0.0031` maxDD `-0.8513`
- `risk_on_and_context->metal_1h` score `-0.4422` n `54` status `ready` deltaP `2.0016` edge `0.0031` maxDD `-0.8513`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
