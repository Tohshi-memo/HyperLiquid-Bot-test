# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-18T08:52:30.828668+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9930`

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

- `market_context_high->commodity_24h` score `2.7569` n `118` status `ready` deltaP `20.0083` edge `0.1815` maxDD `-1.8119`
- `risk_on_high->commodity_24h` score `2.3033` n `77` status `ready` deltaP `19.6231` edge `0.1409` maxDD `-1.7154`
- `risk_on_and_context->commodity_24h` score `2.3033` n `77` status `ready` deltaP `19.6231` edge `0.1409` maxDD `-1.7154`
- `market_context_high->crypto_major_4h` score `2.1494` n `143` status `ready` deltaP `17.8151` edge `0.4008` maxDD `-15.2359`
- `market_context_high->crypto_major_1h` score `0.7429` n `143` status `ready` deltaP `5.5955` edge `0.1135` maxDD `-3.7781`
- `risk_on_high->crypto_major_4h` score `0.2498` n `91` status `ready` deltaP `14.2187` edge `0.1853` maxDD `-11.1788`
- `risk_on_and_context->crypto_major_4h` score `0.2498` n `91` status `ready` deltaP `14.2187` edge `0.1853` maxDD `-11.1788`
- `market_context_high->crypto_alt_1h` score `0.2208` n `143` status `ready` deltaP `7.1396` edge `0.1208` maxDD `-7.3329`
- `risk_on_high->index_1h` score `-0.0521` n `91` status `ready` deltaP `4.2553` edge `0.0057` maxDD `-0.7394`
- `risk_on_and_context->index_1h` score `-0.0521` n `91` status `ready` deltaP `4.2553` edge `0.0057` maxDD `-0.7394`
- `risk_on_high->fx_1h` score `-0.2718` n `91` status `ready` deltaP `0.8976` edge `-0.0028` maxDD `-0.376`
- `risk_on_and_context->fx_1h` score `-0.2718` n `91` status `ready` deltaP `0.8976` edge `-0.0028` maxDD `-0.376`
- `market_context_high->metal_1h` score `-0.2954` n `143` status `ready` deltaP `6.0404` edge `0.0088` maxDD `-0.9556`
- `market_context_high->index_1h` score `-0.3804` n `143` status `ready` deltaP `5.8538` edge `0.0041` maxDD `-1.3195`
- `risk_on_high->equity_1h` score `-0.4572` n `91` status `ready` deltaP `9.2582` edge `0.0298` maxDD `-5.3696`
- `risk_on_and_context->equity_1h` score `-0.4572` n `91` status `ready` deltaP `9.2582` edge `0.0298` maxDD `-5.3696`
- `risk_on_high->metal_1h` score `-0.493` n `91` status `ready` deltaP `0.8455` edge `0.0043` maxDD `-0.8513`
- `risk_on_and_context->metal_1h` score `-0.493` n `91` status `ready` deltaP `0.8455` edge `0.0043` maxDD `-0.8513`
- `market_context_high->metal_4h` score `-0.5322` n `143` status `ready` deltaP `6.653` edge `0.045` maxDD `-1.6961`
- `market_context_high->fx_1h` score `-0.7363` n `143` status `ready` deltaP `-1.1005` edge `-0.0019` maxDD `-0.503`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
