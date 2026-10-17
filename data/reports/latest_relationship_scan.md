# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-17T05:52:31.225908+00:00`
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

- `market_context_high->crypto_alt_4h` score `8.1893` n `127` status `ready` deltaP `21.0437` edge `0.6336` maxDD `-4.9825`
- `risk_on_high->commodity_24h` score `7.1037` n `54` status `ready` deltaP `38.5017` edge `0.3353` maxDD `0.0`
- `risk_on_and_context->commodity_24h` score `7.1037` n `54` status `ready` deltaP `38.5017` edge `0.3353` maxDD `0.0`
- `market_context_high->crypto_major_4h` score `6.3752` n `127` status `ready` deltaP `24.1693` edge `0.5023` maxDD `-5.906`
- `risk_on_high->crypto_alt_4h` score `6.2083` n `54` status `ready` deltaP `23.4643` edge `0.4056` maxDD `-1.907`
- `risk_on_and_context->crypto_alt_4h` score `6.2083` n `54` status `ready` deltaP `23.4643` edge `0.4056` maxDD `-1.907`
- `risk_on_high->crypto_major_4h` score `4.3955` n `54` status `ready` deltaP `36.3595` edge `0.4064` maxDD `-4.1548`
- `risk_on_and_context->crypto_major_4h` score `4.3955` n `54` status `ready` deltaP `36.3595` edge `0.4064` maxDD `-4.1548`
- `market_context_high->crypto_alt_1h` score `1.7503` n `135` status `ready` deltaP `14.5941` edge `0.155` maxDD `-5.8485`
- `market_context_high->crypto_major_1h` score `1.0668` n `135` status `ready` deltaP `7.1945` edge `0.1215` maxDD `-3.7781`
- `market_context_high->metal_4h` score `0.5571` n `127` status `ready` deltaP `14.6941` edge `0.053` maxDD `-1.6961`
- `risk_on_high->index_1h` score `-0.1426` n `61` status `ready` deltaP `2.5082` edge `0.0034` maxDD `-0.7394`
- `risk_on_and_context->index_1h` score `-0.1426` n `61` status `ready` deltaP `2.5082` edge `0.0034` maxDD `-0.7394`
- `market_context_high->metal_1h` score `-0.2125` n `135` status `ready` deltaP `8.9909` edge `0.0093` maxDD `-0.9556`
- `market_context_high->index_1h` score `-0.2313` n `135` status `ready` deltaP `6.2362` edge `0.0036` maxDD `-1.3195`
- `risk_on_high->crypto_major_1h` score `-0.2819` n `61` status `ready` deltaP `3.3572` edge `0.0137` maxDD `-3.7781`
- `risk_on_and_context->crypto_major_1h` score `-0.2819` n `61` status `ready` deltaP `3.3572` edge `0.0137` maxDD `-3.7781`
- `risk_on_high->crypto_alt_1h` score `-0.3527` n `61` status `ready` deltaP `5.8874` edge `0.0178` maxDD `-5.8485`
- `risk_on_and_context->crypto_alt_1h` score `-0.3527` n `61` status `ready` deltaP `5.8874` edge `0.0178` maxDD `-5.8485`
- `risk_on_high->metal_1h` score `-0.4449` n `61` status `ready` deltaP `1.8749` edge `0.0036` maxDD `-0.8513`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
