# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-18T00:52:25.632936+00:00`
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

- `risk_on_high->commodity_24h` score `7.1038` n `54` status `ready` deltaP `39.3728` edge `0.3295` maxDD `0.0`
- `risk_on_and_context->commodity_24h` score `7.1038` n `54` status `ready` deltaP `39.3728` edge `0.3295` maxDD `0.0`
- `market_context_high->crypto_major_4h` score `1.0803` n `173` status `ready` deltaP `12.8656` edge `0.3447` maxDD `-15.2359`
- `market_context_high->crypto_major_1h` score `0.3818` n `173` status `ready` deltaP `3.8862` edge `0.0948` maxDD `-3.7781`
- `risk_on_high->crypto_major_4h` score `0.3791` n `91` status `ready` deltaP `14.9809` edge `0.1968` maxDD `-11.1788`
- `risk_on_and_context->crypto_major_4h` score `0.3791` n `91` status `ready` deltaP `14.9809` edge `0.1968` maxDD `-11.1788`
- `market_context_high->crypto_alt_1h` score `0.0496` n `173` status `ready` deltaP `7.1588` edge `0.1064` maxDD `-7.3329`
- `risk_on_high->index_1h` score `0.014` n `91` status `ready` deltaP `5.0061` edge `0.0062` maxDD `-0.7394`
- `risk_on_and_context->index_1h` score `0.014` n `91` status `ready` deltaP `5.0061` edge `0.0062` maxDD `-0.7394`
- `market_context_high->index_1h` score `-0.1759` n `173` status `ready` deltaP `7.0007` edge `0.0056` maxDD `-1.3195`
- `risk_on_high->fx_1h` score `-0.2968` n `91` status `ready` deltaP `0.4472` edge `-0.003` maxDD `-0.376`
- `risk_on_and_context->fx_1h` score `-0.2968` n `91` status `ready` deltaP `0.4472` edge `-0.003` maxDD `-0.376`
- `market_context_high->metal_1h` score `-0.3273` n `173` status `ready` deltaP `5.487` edge `0.0084` maxDD `-0.9556`
- `risk_on_high->equity_1h` score `-0.408` n `91` status `ready` deltaP `9.5585` edge `0.0319` maxDD `-5.3696`
- `risk_on_and_context->equity_1h` score `-0.408` n `91` status `ready` deltaP `9.5585` edge `0.0319` maxDD `-5.3696`
- `risk_on_high->metal_1h` score `-0.4696` n `91` status `ready` deltaP `1.2946` edge `0.0043` maxDD `-0.8513`
- `risk_on_and_context->metal_1h` score `-0.4696` n `91` status `ready` deltaP `1.2946` edge `0.0043` maxDD `-0.8513`
- `market_context_high->metal_4h` score `-0.4948` n `173` status `ready` deltaP `7.5999` edge `0.0418` maxDD `-1.6961`
- `market_context_high->equity_1h` score `-0.5474` n `173` status `ready` deltaP `9.8761` edge `0.0425` maxDD `-7.3168`
- `risk_on_high->crypto_major_1h` score `-0.7463` n `91` status `ready` deltaP `-0.9986` edge `0.0029` maxDD `-4.6876`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
