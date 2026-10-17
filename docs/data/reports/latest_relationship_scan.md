# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-17T04:07:26.819818+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `7252`

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

- `market_context_high->crypto_alt_4h` score `8.3371` n `127` status `ready` deltaP `22.1108` edge `0.6388` maxDD `-4.9825`
- `risk_on_high->commodity_24h` score `7.1849` n `54` status `ready` deltaP `38.676` edge `0.3409` maxDD `0.0`
- `risk_on_and_context->commodity_24h` score `7.1849` n `54` status `ready` deltaP `38.676` edge `0.3409` maxDD `0.0`
- `market_context_high->crypto_major_4h` score `6.38` n `127` status `ready` deltaP `24.1693` edge `0.5027` maxDD `-5.906`
- `risk_on_high->crypto_alt_4h` score `6.3561` n `54` status `ready` deltaP `24.5314` edge `0.4108` maxDD `-1.907`
- `risk_on_and_context->crypto_alt_4h` score `6.3561` n `54` status `ready` deltaP `24.5314` edge `0.4108` maxDD `-1.907`
- `risk_on_high->crypto_major_4h` score `4.3986` n `54` status `ready` deltaP `36.3595` edge `0.4068` maxDD `-4.1548`
- `risk_on_and_context->crypto_major_4h` score `4.3986` n `54` status `ready` deltaP `36.3595` edge `0.4068` maxDD `-4.1548`
- `market_context_high->crypto_alt_1h` score `1.8326` n `128` status `ready` deltaP `14.8438` edge `0.1602` maxDD `-5.8485`
- `market_context_high->crypto_major_1h` score `1.0896` n `128` status `ready` deltaP `6.9985` edge `0.1247` maxDD `-3.7781`
- `market_context_high->metal_4h` score `0.6083` n `127` status `ready` deltaP `15.3039` edge `0.0532` maxDD `-1.6961`
- `market_context_high->metal_1h` score `-0.072` n `128` status `ready` deltaP `10.6568` edge `0.0099` maxDD `-0.9556`
- `risk_on_high->metal_1h` score `-0.292` n `54` status `ready` deltaP `4.6962` edge `0.0044` maxDD `-0.8513`
- `risk_on_and_context->metal_1h` score `-0.292` n `54` status `ready` deltaP `4.6962` edge `0.0044` maxDD `-0.8513`
- `market_context_high->index_1h` score `-0.2925` n `128` status `ready` deltaP `5.1943` edge `0.0027` maxDD `-1.3195`
- `risk_on_high->index_1h` score `-0.3256` n `54` status `ready` deltaP `-0.6506` edge `0.001` maxDD `-0.7394`
- `risk_on_and_context->index_1h` score `-0.3256` n `54` status `ready` deltaP `-0.6506` edge `0.001` maxDD `-0.7394`
- `risk_on_high->crypto_major_1h` score `-0.3611` n `54` status `ready` deltaP `2.6004` edge `0.0086` maxDD `-3.7781`
- `risk_on_and_context->crypto_major_1h` score `-0.3611` n `54` status `ready` deltaP `2.6004` edge `0.0086` maxDD `-3.7781`
- `risk_on_high->crypto_alt_1h` score `-0.4012` n `54` status `ready` deltaP `5.5556` edge `0.0138` maxDD `-5.8485`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
