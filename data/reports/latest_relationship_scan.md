# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-18T02:07:24.035553+00:00`
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

- `risk_on_high->commodity_24h` score `7.0834` n `54` status `ready` deltaP `39.3728` edge `0.3278` maxDD `0.0`
- `risk_on_and_context->commodity_24h` score `7.0834` n `54` status `ready` deltaP `39.3728` edge `0.3278` maxDD `0.0`
- `market_context_high->crypto_major_4h` score `1.2723` n `168` status `ready` deltaP `14.1115` edge `0.3524` maxDD `-15.2359`
- `risk_on_high->crypto_major_4h` score `0.3187` n `91` status `ready` deltaP `14.5236` edge `0.1921` maxDD `-11.1788`
- `risk_on_and_context->crypto_major_4h` score `0.3187` n `91` status `ready` deltaP `14.5236` edge `0.1921` maxDD `-11.1788`
- `market_context_high->crypto_major_1h` score `0.2931` n `168` status `ready` deltaP `3.1223` edge `0.0925` maxDD `-3.7781`
- `risk_on_high->index_1h` score `0.0116` n `91` status `ready` deltaP `5.0061` edge `0.006` maxDD `-0.7394`
- `risk_on_and_context->index_1h` score `0.0116` n `91` status `ready` deltaP `5.0061` edge `0.006` maxDD `-0.7394`
- `market_context_high->crypto_alt_1h` score `-0.0654` n `168` status `ready` deltaP `6.5619` edge `0.1008` maxDD `-7.3329`
- `market_context_high->commodity_24h` score `-0.0846` n `119` status `ready` deltaP `13.3224` edge `0.1242` maxDD `-9.2717`
- `market_context_high->index_1h` score `-0.224` n `168` status `ready` deltaP `6.1508` edge `0.0051` maxDD `-1.3195`
- `risk_on_high->fx_1h` score `-0.2726` n `91` status `ready` deltaP `0.8976` edge `-0.0029` maxDD `-0.376`
- `risk_on_and_context->fx_1h` score `-0.2726` n `91` status `ready` deltaP `0.8976` edge `-0.0029` maxDD `-0.376`
- `market_context_high->metal_1h` score `-0.3715` n `168` status `ready` deltaP `4.6371` edge `0.0084` maxDD `-0.9556`
- `market_context_high->metal_4h` score `-0.3988` n `168` status `ready` deltaP `8.7253` edge `0.0423` maxDD `-1.6961`
- `risk_on_high->equity_1h` score `-0.4031` n `91` status `ready` deltaP `9.7087` edge `0.0313` maxDD `-5.3696`
- `risk_on_and_context->equity_1h` score `-0.4031` n `91` status `ready` deltaP `9.7087` edge `0.0313` maxDD `-5.3696`
- `risk_on_high->metal_1h` score `-0.4696` n `91` status `ready` deltaP `1.2946` edge `0.0043` maxDD `-0.8513`
- `risk_on_and_context->metal_1h` score `-0.4696` n `91` status `ready` deltaP `1.2946` edge `0.0043` maxDD `-0.8513`
- `market_context_high->fx_1h` score `-0.5525` n `168` status `ready` deltaP `-2.5365` edge `-0.0018` maxDD `-0.503`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
