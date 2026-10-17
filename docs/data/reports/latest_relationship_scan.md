# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-17T05:37:27.500248+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8332`

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

- `market_context_high->crypto_alt_4h` score `8.2147` n `127` status `ready` deltaP `21.1962` edge `0.6347` maxDD `-4.9825`
- `risk_on_high->commodity_24h` score `7.1133` n `54` status `ready` deltaP `38.5017` edge `0.3361` maxDD `0.0`
- `risk_on_and_context->commodity_24h` score `7.1133` n `54` status `ready` deltaP `38.5017` edge `0.3361` maxDD `0.0`
- `market_context_high->crypto_major_4h` score `6.3922` n `127` status `ready` deltaP `24.3218` edge `0.5027` maxDD `-5.906`
- `risk_on_high->crypto_alt_4h` score `6.2337` n `54` status `ready` deltaP `23.6168` edge `0.4067` maxDD `-1.907`
- `risk_on_and_context->crypto_alt_4h` score `6.2337` n `54` status `ready` deltaP `23.6168` edge `0.4067` maxDD `-1.907`
- `risk_on_high->crypto_major_4h` score `4.4066` n `54` status `ready` deltaP `36.512` edge `0.4068` maxDD `-4.1548`
- `risk_on_and_context->crypto_major_4h` score `4.4066` n `54` status `ready` deltaP `36.512` edge `0.4068` maxDD `-4.1548`
- `market_context_high->crypto_alt_1h` score `1.8151` n `134` status `ready` deltaP `15.0751` edge `0.1572` maxDD `-5.8485`
- `market_context_high->crypto_major_1h` score `1.0599` n `134` status `ready` deltaP `7.018` edge `0.1221` maxDD `-3.7781`
- `market_context_high->metal_4h` score `0.5571` n `127` status `ready` deltaP `14.6941` edge `0.053` maxDD `-1.6961`
- `risk_on_high->index_1h` score `-0.1856` n `60` status `ready` deltaP `1.7568` edge `0.0029` maxDD `-0.7394`
- `risk_on_and_context->index_1h` score `-0.1856` n `60` status `ready` deltaP `1.7568` edge `0.0029` maxDD `-0.7394`
- `market_context_high->metal_1h` score `-0.1896` n `134` status `ready` deltaP `9.2613` edge `0.0094` maxDD `-0.9556`
- `market_context_high->index_1h` score `-0.2438` n `134` status `ready` deltaP `6.0105` edge `0.0035` maxDD `-1.3195`
- `risk_on_high->crypto_alt_1h` score `-0.2849` n `60` status `ready` deltaP `6.8164` edge `0.0203` maxDD `-5.8485`
- `risk_on_and_context->crypto_alt_1h` score `-0.2849` n `60` status `ready` deltaP `6.8164` edge `0.0203` maxDD `-5.8485`
- `risk_on_high->crypto_major_1h` score `-0.3224` n `60` status `ready` deltaP `2.7146` edge `0.0128` maxDD `-3.7781`
- `risk_on_and_context->crypto_major_1h` score `-0.3224` n `60` status `ready` deltaP `2.7146` edge `0.0128` maxDD `-3.7781`
- `risk_on_high->metal_1h` score `-0.4085` n `60` status `ready` deltaP `2.5449` edge `0.0038` maxDD `-0.8513`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
