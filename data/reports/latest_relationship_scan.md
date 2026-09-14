# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-14T10:07:30.129428+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `11190`

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

- `news_risk_high->unknown_1h` score `442.8533` n `82` status `ready` deltaP `-6.1487` edge `36.9876` maxDD `-1.7068`
- `news_risk_high->crypto_alt_24h` score `20.3081` n `82` status `ready` deltaP `41.781` edge `1.4626` maxDD `-2.2369`
- `news_risk_high->crypto_major_24h` score `17.3035` n `82` status `ready` deltaP `34.6376` edge `1.3581` maxDD `-9.098`
- `news_risk_high->equity_24h` score `12.1002` n `82` status `ready` deltaP `35.4844` edge `0.9498` maxDD `-6.5742`
- `news_risk_high->index_24h` score `8.244` n `82` status `ready` deltaP `59.3199` edge `0.3092` maxDD `-0.0797`
- `market_context_high->commodity_24h` score `7.0639` n `87` status `ready` deltaP `40.1042` edge `0.3213` maxDD `0.0`
- `risk_on_high->commodity_24h` score `6.2179` n `41` status `ready` deltaP `40.1042` edge `0.2508` maxDD `0.0`
- `risk_on_and_context->commodity_24h` score `6.2179` n `41` status `ready` deltaP `40.1042` edge `0.2508` maxDD `0.0`
- `news_risk_high->metal_24h` score `5.8253` n `82` status `ready` deltaP `34.989` edge `0.2976` maxDD `-0.6334`
- `risk_on_high->fx_24h` score `5.1186` n `41` status `ready` deltaP `57.2832` edge `0.0489` maxDD `-0.0054`
- `risk_on_and_context->fx_24h` score `5.1186` n `41` status `ready` deltaP `57.2832` edge `0.0489` maxDD `-0.0054`
- `market_context_high->fx_24h` score `4.6044` n `87` status `ready` deltaP `52.8256` edge `0.0531` maxDD `-0.0593`
- `risk_on_high->commodity_4h` score `1.9499` n `52` status `ready` deltaP `26.2899` edge `0.0222` maxDD `-0.1313`
- `risk_on_and_context->commodity_4h` score `1.9499` n `52` status `ready` deltaP `26.2899` edge `0.0222` maxDD `-0.1313`
- `market_context_high->commodity_4h` score `1.7502` n `137` status `ready` deltaP `21.6998` edge `0.043` maxDD `-0.345`
- `market_context_high->commodity_1h` score `0.7083` n `137` status `ready` deltaP `12.3629` edge `0.0143` maxDD `-0.3491`
- `news_risk_high->index_4h` score `0.6654` n `82` status `ready` deltaP `16.311` edge `0.0394` maxDD `-0.6935`
- `market_context_high->fx_4h` score `0.3334` n `137` status `ready` deltaP `12.1406` edge `0.0094` maxDD `-0.1412`
- `market_context_high->fx_1h` score `0.195` n `137` status `ready` deltaP `5.9607` edge `0.0023` maxDD `-0.063`
- `risk_on_high->commodity_1h` score `0.1928` n `52` status `ready` deltaP `6.7481` edge `0.0063` maxDD `-0.1507`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
