# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-17T01:22:29.249213+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `10533`

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

- `news_risk_high->unknown_4h` score `377.184` n `83` status `ready` deltaP `-20.9007` edge `31.6608` maxDD `-4.1571`
- `news_risk_high->crypto_alt_24h` score `17.1908` n `83` status `ready` deltaP `39.5666` edge `1.3067` maxDD `-9.3661`
- `news_risk_high->crypto_major_24h` score `15.7247` n `83` status `ready` deltaP `31.6328` edge `1.299` maxDD `-13.2931`
- `news_risk_high->equity_24h` score `11.8875` n `83` status `ready` deltaP `40.8656` edge `0.8956` maxDD `-6.5262`
- `risk_on_high->commodity_24h` score `7.3859` n `52` status `ready` deltaP `42.0139` edge `0.3354` maxDD `0.0`
- `risk_on_and_context->commodity_24h` score `7.3859` n `52` status `ready` deltaP `42.0139` edge `0.3354` maxDD `0.0`
- `news_risk_high->index_24h` score `6.6508` n `83` status `ready` deltaP `46.2956` edge `0.2632` maxDD `-0.075`
- `market_context_high->commodity_24h` score `6.0868` n `149` status `ready` deltaP `35.3025` edge `0.3244` maxDD `-0.8682`
- `news_risk_high->metal_24h` score `4.8764` n `83` status `ready` deltaP `32.3377` edge `0.2362` maxDD `-0.6334`
- `risk_on_high->fx_24h` score `2.5011` n `52` status `ready` deltaP `32.7991` edge `-0.006` maxDD `-0.0054`
- `risk_on_and_context->fx_24h` score `2.5011` n `52` status `ready` deltaP `32.7991` edge `-0.006` maxDD `-0.0054`
- `market_context_high->fx_24h` score `2.3662` n `149` status `ready` deltaP `30.0242` edge `0.0186` maxDD `-0.0593`
- `risk_on_high->commodity_4h` score `2.3304` n `52` status `ready` deltaP `29.1862` edge `0.0346` maxDD `-0.1313`
- `risk_on_and_context->commodity_4h` score `2.3304` n `52` status `ready` deltaP `29.1862` edge `0.0346` maxDD `-0.1313`
- `market_context_high->commodity_4h` score `2.2301` n `149` status `ready` deltaP `25.6885` edge `0.0564` maxDD `-0.345`
- `market_context_high->commodity_1h` score `0.9935` n `149` status `ready` deltaP `15.163` edge `0.0194` maxDD `-0.3491`
- `risk_on_high->commodity_1h` score `0.3702` n `52` status `ready` deltaP `8.2451` edge `0.0111` maxDD `-0.1507`
- `risk_on_and_context->commodity_1h` score `0.3702` n `52` status `ready` deltaP `8.2451` edge `0.0111` maxDD `-0.1507`
- `news_risk_high->index_4h` score `0.3651` n `83` status `ready` deltaP `11.736` edge `0.0314` maxDD `-0.6935`
- `risk_on_high->metal_1h` score `0.1544` n `52` status `ready` deltaP `6.4141` edge `0.0076` maxDD `-0.1115`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
