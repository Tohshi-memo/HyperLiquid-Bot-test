# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-17T06:23:02.370674+00:00`
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

- `news_risk_high->unknown_4h` score `384.7438` n `83` status `ready` deltaP `-21.0531` edge `32.2918` maxDD `-4.1571`
- `news_risk_high->crypto_alt_24h` score `15.2474` n `83` status `ready` deltaP `36.0944` edge `1.1679` maxDD `-9.3661`
- `news_risk_high->crypto_major_24h` score `14.0141` n `83` status `ready` deltaP `28.1605` edge `1.1796` maxDD `-13.2931`
- `news_risk_high->equity_24h` score `10.3209` n `83` status `ready` deltaP `37.3934` edge `0.7882` maxDD `-6.5262`
- `risk_on_high->commodity_24h` score `8.3009` n `52` status `ready` deltaP `45.4861` edge `0.3885` maxDD `0.0`
- `risk_on_and_context->commodity_24h` score `8.3009` n `52` status `ready` deltaP `45.4861` edge `0.3885` maxDD `0.0`
- `market_context_high->commodity_24h` score `7.0017` n `149` status `ready` deltaP `38.7747` edge `0.3775` maxDD `-0.8682`
- `news_risk_high->index_24h` score `6.2038` n `83` status `ready` deltaP `42.8234` edge `0.2491` maxDD `-0.075`
- `news_risk_high->metal_24h` score `4.3914` n `83` status `ready` deltaP `31.9905` edge `0.1981` maxDD `-0.6334`
- `risk_on_high->fx_24h` score `2.6181` n `52` status `ready` deltaP `33.8408` edge `-0.0032` maxDD `-0.0054`
- `risk_on_and_context->fx_24h` score `2.6181` n `52` status `ready` deltaP `33.8408` edge `-0.0032` maxDD `-0.0054`
- `market_context_high->fx_24h` score `2.4832` n `149` status `ready` deltaP `31.0659` edge `0.0214` maxDD `-0.0593`
- `risk_on_high->commodity_4h` score `2.1992` n `52` status `ready` deltaP `27.9667` edge `0.0318` maxDD `-0.1313`
- `risk_on_and_context->commodity_4h` score `2.1992` n `52` status `ready` deltaP `27.9667` edge `0.0318` maxDD `-0.1313`
- `market_context_high->commodity_4h` score `2.099` n `149` status `ready` deltaP `24.469` edge `0.0536` maxDD `-0.345`
- `market_context_high->commodity_1h` score `0.9048` n `149` status `ready` deltaP `14.2648` edge `0.018` maxDD `-0.3491`
- `news_risk_high->index_4h` score `0.4102` n `83` status `ready` deltaP `12.4982` edge `0.0321` maxDD `-0.6935`
- `risk_on_high->commodity_1h` score `0.2815` n `52` status `ready` deltaP `7.3469` edge `0.0097` maxDD `-0.1507`
- `risk_on_and_context->commodity_1h` score `0.2815` n `52` status `ready` deltaP `7.3469` edge `0.0097` maxDD `-0.1507`
- `risk_on_high->metal_1h` score `0.1443` n `52` status `ready` deltaP `6.2644` edge `0.0073` maxDD `-0.1115`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
