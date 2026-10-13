# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-13T15:37:31.577059+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9582`

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

- `market_context_high->crypto_alt_4h` score `8.1334` n `117` status `ready` deltaP `20.5754` edge `0.6855` maxDD `-9.2574`
- `market_context_high->crypto_major_4h` score `7.0865` n `117` status `ready` deltaP `24.3212` edge `0.5843` maxDD `-7.4722`
- `risk_on_high->crypto_alt_4h` score `6.7223` n `54` status `ready` deltaP `22.8546` edge `0.4526` maxDD `-1.9151`
- `risk_on_and_context->crypto_alt_4h` score `6.7223` n `54` status `ready` deltaP `22.8546` edge `0.4526` maxDD `-1.9151`
- `risk_on_high->commodity_24h` score `6.1993` n `48` status `ready` deltaP `32.0557` edge `0.3029` maxDD `0.0`
- `risk_on_and_context->commodity_24h` score `6.1993` n `48` status `ready` deltaP `32.0557` edge `0.3029` maxDD `0.0`
- `risk_on_high->crypto_major_4h` score `5.146` n `54` status `ready` deltaP `37.4266` edge `0.4955` maxDD `-4.1548`
- `risk_on_and_context->crypto_major_4h` score `5.146` n `54` status `ready` deltaP `37.4266` edge `0.4955` maxDD `-4.1548`
- `market_context_high->unknown_4h` score `4.0878` n `117` status `ready` deltaP `-3.467` edge `0.4284` maxDD `-1.8373`
- `market_context_high->crypto_alt_1h` score `2.1572` n `117` status `ready` deltaP `15.2132` edge `0.1851` maxDD `-5.8734`
- `market_context_high->crypto_major_1h` score `1.6122` n `117` status `ready` deltaP `8.2067` edge `0.1602` maxDD `-3.7781`
- `market_context_high->metal_4h` score `0.2304` n `117` status `ready` deltaP `13.4603` edge `0.034` maxDD `-1.6961`
- `risk_on_high->crypto_major_1h` score `-0.1085` n `54` status `ready` deltaP `3.6483` edge `0.034` maxDD `-3.7781`
- `risk_on_and_context->crypto_major_1h` score `-0.1085` n `54` status `ready` deltaP `3.6483` edge `0.034` maxDD `-3.7781`
- `market_context_high->fx_1h` score `-0.3299` n `117` status `ready` deltaP `1.2474` edge `0.0022` maxDD `-0.3742`
- `risk_on_high->crypto_alt_1h` score `-0.331` n `54` status `ready` deltaP `4.9568` edge `0.0271` maxDD `-5.8734`
- `risk_on_and_context->crypto_alt_1h` score `-0.331` n `54` status `ready` deltaP `4.9568` edge `0.0271` maxDD `-5.8734`
- `market_context_high->metal_1h` score `-0.3817` n `117` status `ready` deltaP `7.265` edge `0.0067` maxDD `-0.9556`
- `risk_on_high->metal_1h` score `-0.4625` n `54` status `ready` deltaP `1.8519` edge `0.0015` maxDD `-0.8513`
- `risk_on_and_context->metal_1h` score `-0.4625` n `54` status `ready` deltaP `1.8519` edge `0.0015` maxDD `-0.8513`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
