# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-14T12:07:30.099136+00:00`
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

- `news_risk_high->unknown_4h` score `862.1409` n `82` status `ready` deltaP `-20.5793` edge `72.0716` maxDD `-4.1464`
- `news_risk_high->unknown_1h` score `442.7226` n `82` status `ready` deltaP `-6.7475` edge `36.9807` maxDD `-1.7068`
- `news_risk_high->crypto_alt_24h` score `20.4233` n `82` status `ready` deltaP `41.781` edge `1.4722` maxDD `-2.2369`
- `news_risk_high->crypto_major_24h` score `16.8024` n `82` status `ready` deltaP `33.2487` edge `1.3256` maxDD `-9.098`
- `news_risk_high->equity_24h` score `12.219` n `82` status `ready` deltaP `35.4844` edge `0.9597` maxDD `-6.5742`
- `news_risk_high->index_24h` score `8.2692` n `82` status `ready` deltaP `59.3199` edge `0.3113` maxDD `-0.0797`
- `market_context_high->commodity_24h` score `7.1407` n `95` status `ready` deltaP `40.1042` edge `0.3277` maxDD `0.0`
- `risk_on_high->commodity_24h` score `6.1903` n `41` status `ready` deltaP `40.1042` edge `0.2485` maxDD `0.0`
- `risk_on_and_context->commodity_24h` score `6.1903` n `41` status `ready` deltaP `40.1042` edge `0.2485` maxDD `0.0`
- `news_risk_high->metal_24h` score `6.0264` n `82` status `ready` deltaP `36.3779` edge `0.3051` maxDD `-0.6334`
- `risk_on_high->fx_24h` score `4.9823` n `41` status `ready` deltaP `55.8943` edge `0.0468` maxDD `-0.0054`
- `risk_on_and_context->fx_24h` score `4.9823` n `41` status `ready` deltaP `55.8943` edge `0.0468` maxDD `-0.0054`
- `market_context_high->fx_24h` score `4.5301` n `95` status `ready` deltaP `52.0175` edge `0.0523` maxDD `-0.0593`
- `risk_on_high->commodity_4h` score `2.0019` n `52` status `ready` deltaP `26.5947` edge `0.0245` maxDD `-0.1313`
- `risk_on_and_context->commodity_4h` score `2.0019` n `52` status `ready` deltaP `26.5947` edge `0.0245` maxDD `-0.1313`
- `market_context_high->commodity_4h` score `1.8022` n `137` status `ready` deltaP `22.0046` edge `0.0453` maxDD `-0.345`
- `market_context_high->commodity_1h` score `0.7502` n `137` status `ready` deltaP `12.6623` edge `0.0158` maxDD `-0.3491`
- `news_risk_high->index_4h` score `0.6867` n `82` status `ready` deltaP `16.6158` edge `0.0401` maxDD `-0.6935`
- `market_context_high->fx_4h` score `0.3341` n `137` status `ready` deltaP `12.1406` edge `0.0095` maxDD `-0.1412`
- `risk_on_high->commodity_1h` score `0.2348` n `52` status `ready` deltaP `7.0475` edge `0.0078` maxDD `-0.1507`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
