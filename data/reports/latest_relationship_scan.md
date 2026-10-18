# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-18T02:22:24.326251+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9622`

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

- `risk_on_high->commodity_24h` score `7.0774` n `54` status `ready` deltaP `39.3728` edge `0.3273` maxDD `0.0`
- `risk_on_and_context->commodity_24h` score `7.0774` n `54` status `ready` deltaP `39.3728` edge `0.3273` maxDD `0.0`
- `market_context_high->crypto_major_4h` score `1.3172` n `167` status `ready` deltaP `14.3119` edge `0.3548` maxDD `-15.2359`
- `market_context_high->crypto_major_1h` score `0.314` n `167` status `ready` deltaP `3.2934` edge `0.0931` maxDD `-3.7781`
- `risk_on_high->crypto_major_4h` score `0.299` n `91` status `ready` deltaP `14.3712` edge `0.1906` maxDD `-11.1788`
- `risk_on_and_context->crypto_major_4h` score `0.299` n `91` status `ready` deltaP `14.3712` edge `0.1906` maxDD `-11.1788`
- `market_context_high->commodity_24h` score `0.1386` n `118` status `ready` deltaP `13.9491` edge `0.1297` maxDD `-8.8918`
- `risk_on_high->index_1h` score `0.0116` n `91` status `ready` deltaP `5.0061` edge `0.006` maxDD `-0.7394`
- `risk_on_and_context->index_1h` score `0.0116` n `91` status `ready` deltaP `5.0061` edge `0.006` maxDD `-0.7394`
- `market_context_high->crypto_alt_1h` score `-0.0178` n `167` status `ready` deltaP `6.8862` edge `0.1026` maxDD `-7.3329`
- `market_context_high->index_1h` score `-0.2083` n `167` status `ready` deltaP `6.4538` edge `0.0051` maxDD `-1.3195`
- `risk_on_high->fx_1h` score `-0.2726` n `91` status `ready` deltaP `0.8976` edge `-0.0029` maxDD `-0.376`
- `risk_on_and_context->fx_1h` score `-0.2726` n `91` status `ready` deltaP `0.8976` edge `-0.0029` maxDD `-0.376`
- `market_context_high->metal_1h` score `-0.3791` n `167` status `ready` deltaP `4.491` edge `0.0084` maxDD `-0.9556`
- `market_context_high->metal_4h` score `-0.3848` n `167` status `ready` deltaP `8.9008` edge `0.0423` maxDD `-1.6961`
- `risk_on_high->equity_1h` score `-0.4031` n `91` status `ready` deltaP `9.7087` edge `0.0313` maxDD `-5.3696`
- `risk_on_and_context->equity_1h` score `-0.4031` n `91` status `ready` deltaP `9.7087` edge `0.0313` maxDD `-5.3696`
- `risk_on_high->metal_1h` score `-0.4619` n `91` status `ready` deltaP `1.4443` edge `0.0043` maxDD `-0.8513`
- `risk_on_and_context->metal_1h` score `-0.4619` n `91` status `ready` deltaP `1.4443` edge `0.0043` maxDD `-0.8513`
- `market_context_high->fx_1h` score `-0.5375` n `167` status `ready` deltaP `-2.2478` edge `-0.0018` maxDD `-0.503`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
