# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-17T13:37:26.562950+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9348`

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

- `risk_on_high->commodity_24h` score `7.0161` n `54` status `ready` deltaP `38.5017` edge `0.328` maxDD `0.0`
- `risk_on_and_context->commodity_24h` score `7.0161` n `54` status `ready` deltaP `38.5017` edge `0.328` maxDD `0.0`
- `market_context_high->crypto_major_4h` score `4.8878` n `154` status `ready` deltaP `19.0113` edge `0.4169` maxDD `-5.906`
- `risk_on_high->crypto_major_4h` score `3.3521` n `80` status `ready` deltaP `22.2256` edge `0.263` maxDD `-5.5463`
- `risk_on_and_context->crypto_major_4h` score `3.3521` n `80` status `ready` deltaP `22.2256` edge `0.263` maxDD `-5.5463`
- `market_context_high->crypto_alt_4h` score `3.0923` n `154` status `ready` deltaP `11.2647` edge `0.4786` maxDD `-15.0141`
- `market_context_high->crypto_major_1h` score `0.398` n `166` status `ready` deltaP `4.6587` edge `0.091` maxDD `-3.7781`
- `market_context_high->metal_4h` score `0.2177` n `154` status `ready` deltaP `11.4567` edge `0.0463` maxDD `-1.6961`
- `risk_on_high->index_1h` score `0.0231` n `90` status `ready` deltaP `5.2553` edge `0.0053` maxDD `-0.7394`
- `risk_on_and_context->index_1h` score `0.0231` n `90` status `ready` deltaP `5.2553` edge `0.0053` maxDD `-0.7394`
- `market_context_high->crypto_alt_1h` score `-0.1173` n `166` status `ready` deltaP `6.163` edge `0.0989` maxDD `-7.3143`
- `market_context_high->metal_1h` score `-0.263` n `166` status `ready` deltaP `6.7545` edge `0.0082` maxDD `-0.9556`
- `risk_on_high->fx_1h` score `-0.2912` n `90` status `ready` deltaP `0.5705` edge `-0.0031` maxDD `-0.376`
- `risk_on_and_context->fx_1h` score `-0.2912` n `90` status `ready` deltaP `0.5705` edge `-0.0031` maxDD `-0.376`
- `market_context_high->index_1h` score `-0.3259` n `166` status `ready` deltaP `6.4601` edge `0.0046` maxDD `-1.3195`
- `market_context_high->equity_4h` score `-0.4173` n `154` status `ready` deltaP `13.1856` edge `0.2012` maxDD `-17.4086`
- `market_context_high->equity_1h` score `-0.4286` n `166` status `ready` deltaP `9.0108` edge `0.0364` maxDD `-7.1141`
- `market_context_high->fx_1h` score `-0.4423` n `166` status `ready` deltaP `-0.4469` edge `-0.0016` maxDD `-0.503`
- `risk_on_high->equity_1h` score `-0.4843` n `90` status `ready` deltaP `9.5195` edge `0.0258` maxDD `-5.3696`
- `risk_on_and_context->equity_1h` score `-0.4843` n `90` status `ready` deltaP `9.5195` edge `0.0258` maxDD `-5.3696`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
