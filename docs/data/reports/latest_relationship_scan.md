# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-17T01:52:31.382702+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `7056`

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

- `market_context_high->crypto_alt_4h` score `8.2523` n `127` status `ready` deltaP `21.5011` edge `0.6358` maxDD `-4.9825`
- `risk_on_high->commodity_24h` score `7.2845` n `54` status `ready` deltaP `38.676` edge `0.3492` maxDD `0.0`
- `risk_on_and_context->commodity_24h` score `7.2845` n `54` status `ready` deltaP `38.676` edge `0.3492` maxDD `0.0`
- `risk_on_high->crypto_alt_4h` score `6.2713` n `54` status `ready` deltaP `23.9217` edge `0.4078` maxDD `-1.907`
- `risk_on_and_context->crypto_alt_4h` score `6.2713` n `54` status `ready` deltaP `23.9217` edge `0.4078` maxDD `-1.907`
- `market_context_high->crypto_major_4h` score `6.2151` n `127` status `ready` deltaP `22.7974` edge `0.4981` maxDD `-5.906`
- `risk_on_high->crypto_major_4h` score `4.2914` n `54` status `ready` deltaP `34.9876` edge `0.4022` maxDD `-4.1548`
- `risk_on_and_context->crypto_major_4h` score `4.2914` n `54` status `ready` deltaP `34.9876` edge `0.4022` maxDD `-4.1548`
- `market_context_high->crypto_alt_1h` score `1.8249` n `127` status `ready` deltaP `14.7166` edge `0.1604` maxDD `-5.8485`
- `market_context_high->crypto_major_1h` score `1.1099` n `127` status `ready` deltaP `7.1031` edge `0.1257` maxDD `-3.7781`
- `market_context_high->metal_4h` score `0.6705` n `127` status `ready` deltaP `16.0661` edge `0.0533` maxDD `-1.6961`
- `market_context_high->metal_1h` score `-0.0746` n `127` status `ready` deltaP `10.624` edge `0.0099` maxDD `-0.9556`
- `risk_on_high->metal_1h` score `-0.2756` n `54` status `ready` deltaP `4.9956` edge `0.0045` maxDD `-0.8513`
- `risk_on_and_context->metal_1h` score `-0.2756` n `54` status `ready` deltaP `4.9956` edge `0.0045` maxDD `-0.8513`
- `market_context_high->index_1h` score `-0.2988` n `127` status `ready` deltaP `5.0886` edge `0.0026` maxDD `-1.3195`
- `risk_on_high->index_1h` score `-0.3092` n `54` status `ready` deltaP `-0.3503` edge `0.0011` maxDD `-0.7394`
- `risk_on_and_context->index_1h` score `-0.3092` n `54` status `ready` deltaP `-0.3503` edge `0.0011` maxDD `-0.7394`
- `risk_on_high->crypto_major_1h` score `-0.3252` n `54` status `ready` deltaP `3.0495` edge `0.0102` maxDD `-3.7781`
- `risk_on_and_context->crypto_major_1h` score `-0.3252` n `54` status `ready` deltaP `3.0495` edge `0.0102` maxDD `-3.7781`
- `risk_on_high->crypto_alt_1h` score `-0.3817` n `54` status `ready` deltaP `5.7053` edge `0.0153` maxDD `-5.8485`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
