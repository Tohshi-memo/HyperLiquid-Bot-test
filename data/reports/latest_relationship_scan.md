# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-15T22:37:56.765564+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8883`

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

- `risk_on_high->commodity_24h` score `7.9868` n `54` status `ready` deltaP `42.1603` edge `0.3845` maxDD `0.0`
- `risk_on_and_context->commodity_24h` score `7.9868` n `54` status `ready` deltaP `42.1603` edge `0.3845` maxDD `0.0`
- `market_context_high->crypto_alt_4h` score `6.7877` n `122` status `ready` deltaP `16.7383` edge `0.5455` maxDD `-4.9825`
- `market_context_high->crypto_major_4h` score `5.4077` n `122` status `ready` deltaP `18.795` edge `0.4575` maxDD `-5.906`
- `risk_on_high->crypto_alt_4h` score `4.594` n `54` status `ready` deltaP `19.5009` edge `0.2975` maxDD `-1.907`
- `risk_on_and_context->crypto_alt_4h` score `4.594` n `54` status `ready` deltaP `19.5009` edge `0.2975` maxDD `-1.907`
- `risk_on_high->crypto_major_4h` score `3.7252` n `54` status `ready` deltaP `32.2437` edge `0.3479` maxDD `-4.1548`
- `risk_on_and_context->crypto_major_4h` score `3.7252` n `54` status `ready` deltaP `32.2437` edge `0.3479` maxDD `-4.1548`
- `market_context_high->crypto_alt_1h` score `1.3625` n `122` status `ready` deltaP `13.2571` edge `0.1316` maxDD `-5.8485`
- `market_context_high->crypto_major_1h` score `0.8564` n `122` status `ready` deltaP `5.9586` edge `0.1122` maxDD `-3.7781`
- `market_context_high->metal_4h` score `0.0555` n `122` status `ready` deltaP `10.3134` edge `0.0404` maxDD `-1.6961`
- `market_context_high->commodity_24h` score `-0.2325` n `115` status `ready` deltaP `14.3342` edge `0.1528` maxDD `-11.5869`
- `market_context_high->fx_1h` score `-0.3219` n `122` status `ready` deltaP `-0.1625` edge `-0.0018` maxDD `-0.4047`
- `risk_on_high->metal_1h` score `-0.4859` n `54` status `ready` deltaP `1.5525` edge `0.0005` maxDD `-0.8513`
- `risk_on_and_context->metal_1h` score `-0.4859` n `54` status `ready` deltaP `1.5525` edge `0.0005` maxDD `-0.8513`
- `market_context_high->metal_1h` score `-0.4935` n `122` status `ready` deltaP `6.258` edge `0.0041` maxDD `-0.9556`
- `market_context_high->index_1h` score `-0.5279` n `122` status `ready` deltaP `1.3637` edge `-0.002` maxDD `-1.3154`
- `risk_on_high->crypto_major_1h` score `-0.5364` n `54` status `ready` deltaP `1.2531` edge `-0.0049` maxDD `-3.7781`
- `risk_on_and_context->crypto_major_1h` score `-0.5364` n `54` status `ready` deltaP `1.2531` edge `-0.0049` maxDD `-3.7781`
- `risk_on_high->index_1h` score `-0.5583` n `54` status `ready` deltaP `-4.4044` edge `-0.0038` maxDD `-0.7394`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
