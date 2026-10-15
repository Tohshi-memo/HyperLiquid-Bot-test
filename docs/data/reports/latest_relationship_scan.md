# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-15T21:22:44.014123+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8970`

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

- `risk_on_high->commodity_24h` score `7.9796` n `54` status `ready` deltaP `42.1603` edge `0.3839` maxDD `0.0`
- `risk_on_and_context->commodity_24h` score `7.9796` n `54` status `ready` deltaP `42.1603` edge `0.3839` maxDD `0.0`
- `market_context_high->crypto_alt_4h` score `6.7903` n `122` status `ready` deltaP `16.8908` edge `0.5447` maxDD `-4.9825`
- `market_context_high->crypto_major_4h` score `5.4489` n `122` status `ready` deltaP `19.0999` edge `0.4589` maxDD `-5.906`
- `risk_on_high->crypto_alt_4h` score `4.5966` n `54` status `ready` deltaP `19.6534` edge `0.2967` maxDD `-1.907`
- `risk_on_and_context->crypto_alt_4h` score `4.5966` n `54` status `ready` deltaP `19.6534` edge `0.2967` maxDD `-1.907`
- `risk_on_high->crypto_major_4h` score `3.752` n `54` status `ready` deltaP `32.5486` edge `0.3493` maxDD `-4.1548`
- `risk_on_and_context->crypto_major_4h` score `3.752` n `54` status `ready` deltaP `32.5486` edge `0.3493` maxDD `-4.1548`
- `market_context_high->crypto_alt_1h` score `1.3206` n `122` status `ready` deltaP `12.808` edge `0.1311` maxDD `-5.8485`
- `market_context_high->crypto_major_1h` score `0.8324` n `122` status `ready` deltaP `5.6592` edge `0.1122` maxDD `-3.7781`
- `market_context_high->metal_4h` score `0.0327` n `122` status `ready` deltaP `10.3134` edge `0.0385` maxDD `-1.6961`
- `market_context_high->commodity_24h` score `-0.2372` n `115` status `ready` deltaP `14.3342` edge `0.1522` maxDD `-11.5869`
- `market_context_high->fx_1h` score `-0.3219` n `122` status `ready` deltaP `-0.1625` edge `-0.0018` maxDD `-0.4047`
- `risk_on_high->metal_1h` score `-0.5193` n `54` status `ready` deltaP `0.9537` edge `0.0002` maxDD `-0.8513`
- `risk_on_and_context->metal_1h` score `-0.5193` n `54` status `ready` deltaP `0.9537` edge `0.0002` maxDD `-0.8513`
- `market_context_high->metal_1h` score `-0.545` n `122` status `ready` deltaP `5.6592` edge `0.0038` maxDD `-0.9556`
- `market_context_high->index_1h` score `-0.5451` n `122` status `ready` deltaP `1.0634` edge `-0.0022` maxDD `-1.3154`
- `risk_on_high->crypto_major_1h` score `-0.552` n `54` status `ready` deltaP `0.9537` edge `-0.0049` maxDD `-3.7781`
- `risk_on_and_context->crypto_major_1h` score `-0.552` n `54` status `ready` deltaP `0.9537` edge `-0.0049` maxDD `-3.7781`
- `risk_on_high->index_1h` score `-0.5754` n `54` status `ready` deltaP `-4.7047` edge `-0.004` maxDD `-0.7394`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
