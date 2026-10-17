# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-17T08:22:29.671038+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9372`

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

- `market_context_high->crypto_alt_4h` score `7.4909` n `133` status `ready` deltaP `17.9534` edge `0.596` maxDD `-4.9825`
- `risk_on_high->commodity_24h` score `7.0521` n `54` status `ready` deltaP `38.5017` edge `0.331` maxDD `0.0`
- `risk_on_and_context->commodity_24h` score `7.0521` n `54` status `ready` deltaP `38.5017` edge `0.331` maxDD `0.0`
- `risk_on_high->crypto_major_4h` score `6.5727` n `59` status `ready` deltaP `36.4045` edge `0.3903` maxDD `-4.1548`
- `risk_on_and_context->crypto_major_4h` score `6.5727` n `59` status `ready` deltaP `36.4045` edge `0.3903` maxDD `-4.1548`
- `market_context_high->crypto_major_4h` score `6.1937` n `133` status `ready` deltaP `24.0304` edge `0.4881` maxDD `-5.906`
- `risk_on_high->crypto_alt_4h` score `4.9985` n `59` status `ready` deltaP `16.5771` edge `0.3507` maxDD `-1.907`
- `risk_on_and_context->crypto_alt_4h` score `4.9985` n `59` status `ready` deltaP `16.5771` edge `0.3507` maxDD `-1.907`
- `market_context_high->crypto_alt_1h` score `1.2351` n `145` status `ready` deltaP `10.8394` edge `0.1371` maxDD `-5.8485`
- `market_context_high->crypto_major_1h` score `1.1593` n `145` status `ready` deltaP `8.9201` edge `0.1177` maxDD `-3.7781`
- `market_context_high->metal_4h` score `0.3765` n `133` status `ready` deltaP `12.7212` edge `0.0511` maxDD `-1.6961`
- `risk_on_high->crypto_major_1h` score `0.0274` n `71` status `ready` deltaP `8.0459` edge `0.0221` maxDD `-3.7781`
- `risk_on_and_context->crypto_major_1h` score `0.0274` n `71` status `ready` deltaP `8.0459` edge `0.0221` maxDD `-3.7781`
- `risk_on_high->index_1h` score `-0.0044` n `71` status `ready` deltaP `5.0015` edge `0.0047` maxDD `-0.7394`
- `risk_on_and_context->index_1h` score `-0.0044` n `71` status `ready` deltaP `5.0015` edge `0.0047` maxDD `-0.7394`
- `market_context_high->index_1h` score `-0.2012` n `145` status `ready` deltaP `6.7402` edge `0.0041` maxDD `-1.3195`
- `market_context_high->metal_1h` score `-0.2701` n `145` status `ready` deltaP `8.3161` edge `0.009` maxDD `-0.9556`
- `risk_on_high->metal_1h` score `-0.4865` n `71` status `ready` deltaP `1.031` edge `0.0039` maxDD `-0.8513`
- `risk_on_and_context->metal_1h` score `-0.4865` n `71` status `ready` deltaP `1.031` edge `0.0039` maxDD `-0.8513`
- `market_context_high->equity_1h` score `-0.4994` n `145` status `ready` deltaP `7.8523` edge `0.0346` maxDD `-7.0778`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
