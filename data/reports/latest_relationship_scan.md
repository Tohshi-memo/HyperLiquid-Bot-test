# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-15T20:22:27.652328+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8920`

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

- `risk_on_high->commodity_24h` score `7.9652` n `54` status `ready` deltaP `42.1603` edge `0.3827` maxDD `0.0`
- `risk_on_and_context->commodity_24h` score `7.9652` n `54` status `ready` deltaP `42.1603` edge `0.3827` maxDD `0.0`
- `market_context_high->crypto_alt_4h` score `6.8593` n `122` status `ready` deltaP `17.3481` edge `0.5474` maxDD `-4.9825`
- `market_context_high->crypto_major_4h` score `5.4523` n `122` status `ready` deltaP `18.9474` edge `0.4602` maxDD `-5.906`
- `risk_on_high->crypto_alt_4h` score `4.6656` n `54` status `ready` deltaP `20.1107` edge `0.2994` maxDD `-1.907`
- `risk_on_and_context->crypto_alt_4h` score `4.6656` n `54` status `ready` deltaP `20.1107` edge `0.2994` maxDD `-1.907`
- `risk_on_high->crypto_major_4h` score `3.7542` n `54` status `ready` deltaP `32.3961` edge `0.3506` maxDD `-4.1548`
- `risk_on_and_context->crypto_major_4h` score `3.7542` n `54` status `ready` deltaP `32.3961` edge `0.3506` maxDD `-4.1548`
- `market_context_high->crypto_alt_1h` score `1.3002` n `122` status `ready` deltaP `12.6583` edge `0.1304` maxDD `-5.8485`
- `market_context_high->crypto_major_1h` score `0.7797` n `122` status `ready` deltaP `5.2101` edge `0.1108` maxDD `-3.7781`
- `market_context_high->metal_4h` score `0.0339` n `122` status `ready` deltaP `10.3134` edge `0.0386` maxDD `-1.6961`
- `market_context_high->commodity_24h` score `-0.2465` n `115` status `ready` deltaP `14.3342` edge `0.151` maxDD `-11.5869`
- `market_context_high->fx_1h` score `-0.3305` n `122` status `ready` deltaP `-0.3127` edge `-0.0019` maxDD `-0.4047`
- `risk_on_high->metal_1h` score `-0.5264` n `54` status `ready` deltaP `0.804` edge `0.0003` maxDD `-0.8513`
- `risk_on_and_context->metal_1h` score `-0.5264` n `54` status `ready` deltaP `0.804` edge `0.0003` maxDD `-0.8513`
- `market_context_high->index_1h` score `-0.5467` n `122` status `ready` deltaP `1.0634` edge `-0.0024` maxDD `-1.3154`
- `market_context_high->metal_1h` score `-0.5558` n `122` status `ready` deltaP `5.5095` edge `0.0039` maxDD `-0.9556`
- `risk_on_high->index_1h` score `-0.577` n `54` status `ready` deltaP `-4.7047` edge `-0.0042` maxDD `-0.7394`
- `risk_on_and_context->index_1h` score `-0.577` n `54` status `ready` deltaP `-4.7047` edge `-0.0042` maxDD `-0.7394`
- `risk_on_high->crypto_major_1h` score `-0.5863` n `54` status `ready` deltaP `0.5046` edge `-0.0063` maxDD `-3.7781`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
