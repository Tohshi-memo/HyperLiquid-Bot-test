# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-17T01:37:30.649865+00:00`
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

- `news_risk_high->unknown_4h` score `377.322` n `83` status `ready` deltaP `-20.9007` edge `31.6723` maxDD `-4.1571`
- `news_risk_high->crypto_alt_24h` score `17.0809` n `83` status `ready` deltaP `39.393` edge `1.2987` maxDD `-9.3661`
- `news_risk_high->crypto_major_24h` score `15.6196` n `83` status `ready` deltaP `31.4592` edge `1.2914` maxDD `-13.2931`
- `news_risk_high->equity_24h` score `11.7944` n `83` status `ready` deltaP `40.692` edge `0.889` maxDD `-6.5262`
- `risk_on_high->commodity_24h` score `7.4322` n `52` status `ready` deltaP `42.1875` edge `0.3381` maxDD `0.0`
- `risk_on_and_context->commodity_24h` score `7.4322` n `52` status `ready` deltaP `42.1875` edge `0.3381` maxDD `0.0`
- `news_risk_high->index_24h` score `6.6273` n `83` status `ready` deltaP `46.122` edge `0.2624` maxDD `-0.075`
- `market_context_high->commodity_24h` score `6.1331` n `149` status `ready` deltaP `35.4761` edge `0.3271` maxDD `-0.8682`
- `news_risk_high->metal_24h` score `4.8337` n `83` status `ready` deltaP `32.1641` edge `0.2338` maxDD `-0.6334`
- `risk_on_high->fx_24h` score `2.5186` n `52` status `ready` deltaP `32.9727` edge `-0.0057` maxDD `-0.0054`
- `risk_on_and_context->fx_24h` score `2.5186` n `52` status `ready` deltaP `32.9727` edge `-0.0057` maxDD `-0.0054`
- `market_context_high->fx_24h` score `2.3837` n `149` status `ready` deltaP `30.1978` edge `0.0189` maxDD `-0.0593`
- `risk_on_high->commodity_4h` score `2.3158` n `52` status `ready` deltaP `29.0338` edge `0.0344` maxDD `-0.1313`
- `risk_on_and_context->commodity_4h` score `2.3158` n `52` status `ready` deltaP `29.0338` edge `0.0344` maxDD `-0.1313`
- `market_context_high->commodity_4h` score `2.2155` n `149` status `ready` deltaP `25.5361` edge `0.0562` maxDD `-0.345`
- `market_context_high->commodity_1h` score `0.9911` n `149` status `ready` deltaP `15.163` edge `0.0192` maxDD `-0.3491`
- `risk_on_high->commodity_1h` score `0.3678` n `52` status `ready` deltaP `8.2451` edge `0.0109` maxDD `-0.1507`
- `risk_on_and_context->commodity_1h` score `0.3678` n `52` status `ready` deltaP `8.2451` edge `0.0109` maxDD `-0.1507`
- `news_risk_high->index_4h` score `0.3635` n `83` status `ready` deltaP `11.736` edge `0.0312` maxDD `-0.6935`
- `risk_on_high->metal_1h` score `0.1435` n `52` status `ready` deltaP `6.2644` edge `0.0072` maxDD `-0.1115`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
