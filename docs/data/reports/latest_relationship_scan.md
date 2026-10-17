# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-17T22:37:30.290928+00:00`
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

- `risk_on_high->commodity_24h` score `7.0724` n `54` status `ready` deltaP `39.0244` edge `0.3292` maxDD `0.0`
- `risk_on_and_context->commodity_24h` score `7.0724` n `54` status `ready` deltaP `39.0244` edge `0.3292` maxDD `0.0`
- `market_context_high->crypto_major_4h` score `1.1175` n `174` status `ready` deltaP `12.5368` edge `0.3389` maxDD `-14.6817`
- `risk_on_high->crypto_major_4h` score `0.5202` n `90` status `ready` deltaP `15.6402` edge `0.1994` maxDD `-10.6246`
- `risk_on_and_context->crypto_major_4h` score `0.5202` n `90` status `ready` deltaP `15.6402` edge `0.1994` maxDD `-10.6246`
- `market_context_high->crypto_major_1h` score `0.5132` n `175` status `ready` deltaP `5.0342` edge `0.0981` maxDD `-3.7781`
- `market_context_high->crypto_alt_1h` score `0.1614` n `175` status `ready` deltaP `7.8511` edge `0.1111` maxDD `-7.3329`
- `risk_on_high->index_1h` score `0.0524` n `91` status `ready` deltaP `5.4565` edge `0.0064` maxDD `-0.7394`
- `risk_on_and_context->index_1h` score `0.0524` n `91` status `ready` deltaP `5.4565` edge `0.0064` maxDD `-0.7394`
- `market_context_high->index_1h` score `-0.1815` n `175` status `ready` deltaP `6.8631` edge `0.0058` maxDD `-1.3195`
- `market_context_high->metal_1h` score `-0.2658` n `175` status `ready` deltaP `6.6407` edge `0.0086` maxDD `-0.9556`
- `risk_on_high->fx_1h` score `-0.2726` n `91` status `ready` deltaP `0.8976` edge `-0.0029` maxDD `-0.376`
- `risk_on_and_context->fx_1h` score `-0.2726` n `91` status `ready` deltaP `0.8976` edge `-0.0029` maxDD `-0.376`
- `market_context_high->equity_1h` score `-0.3048` n `175` status `ready` deltaP `10.6169` edge `0.0441` maxDD `-7.3168`
- `risk_on_high->equity_1h` score `-0.3323` n `91` status `ready` deltaP `10.3093` edge `0.0332` maxDD `-5.3696`
- `risk_on_and_context->equity_1h` score `-0.3323` n `91` status `ready` deltaP `10.3093` edge `0.0332` maxDD `-5.3696`
- `risk_on_high->metal_1h` score `-0.4369` n `91` status `ready` deltaP `1.8934` edge `0.0045` maxDD `-0.8513`
- `risk_on_and_context->metal_1h` score `-0.4369` n `91` status `ready` deltaP `1.8934` edge `0.0045` maxDD `-0.8513`
- `market_context_high->metal_4h` score `-0.5171` n `174` status `ready` deltaP `6.802` edge `0.0411` maxDD `-1.6961`
- `risk_on_high->crypto_major_1h` score `-0.6583` n `91` status `ready` deltaP `0.199` edge `0.0062` maxDD `-4.6876`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
