# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-17T08:37:28.693797+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8658`

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

- `news_risk_high->unknown_4h` score `384.6434` n `83` status `ready` deltaP `-21.6629` edge `32.2875` maxDD `-4.1571`
- `news_risk_high->crypto_alt_24h` score `14.2488` n `83` status `ready` deltaP `34.5319` edge `1.0951` maxDD `-9.3661`
- `news_risk_high->crypto_major_24h` score `13.2591` n `83` status `ready` deltaP `26.598` edge `1.1271` maxDD `-13.2931`
- `news_risk_high->equity_24h` score `9.6835` n `83` status `ready` deltaP `35.8309` edge `0.7455` maxDD `-6.5262`
- `risk_on_high->commodity_24h` score `8.6839` n `52` status `ready` deltaP `47.0486` edge `0.41` maxDD `0.0`
- `risk_on_and_context->commodity_24h` score `8.6839` n `52` status `ready` deltaP `47.0486` edge `0.41` maxDD `0.0`
- `market_context_high->commodity_24h` score `7.3847` n `149` status `ready` deltaP `40.3372` edge `0.399` maxDD `-0.8682`
- `news_risk_high->index_24h` score `6.0128` n `83` status `ready` deltaP `41.2609` edge `0.2436` maxDD `-0.075`
- `news_risk_high->metal_24h` score `4.1674` n `83` status `ready` deltaP `31.4696` edge `0.1829` maxDD `-0.6334`
- `risk_on_high->fx_24h` score `2.6169` n `52` status `ready` deltaP `33.8408` edge `-0.0033` maxDD `-0.0054`
- `risk_on_and_context->fx_24h` score `2.6169` n `52` status `ready` deltaP `33.8408` edge `-0.0033` maxDD `-0.0054`
- `market_context_high->fx_24h` score `2.482` n `149` status `ready` deltaP `31.0659` edge `0.0213` maxDD `-0.0593`
- `risk_on_high->commodity_4h` score `2.3762` n `52` status `ready` deltaP `29.3386` edge `0.0374` maxDD `-0.1313`
- `risk_on_and_context->commodity_4h` score `2.3762` n `52` status `ready` deltaP `29.3386` edge `0.0374` maxDD `-0.1313`
- `market_context_high->commodity_4h` score `2.2759` n `149` status `ready` deltaP `25.8409` edge `0.0592` maxDD `-0.345`
- `market_context_high->commodity_1h` score `0.9515` n `149` status `ready` deltaP `14.7139` edge `0.0189` maxDD `-0.3491`
- `news_risk_high->index_4h` score `0.3335` n `83` status `ready` deltaP `11.2786` edge `0.0304` maxDD `-0.6935`
- `risk_on_high->commodity_1h` score `0.3283` n `52` status `ready` deltaP `7.796` edge `0.0106` maxDD `-0.1507`
- `risk_on_and_context->commodity_1h` score `0.3283` n `52` status `ready` deltaP `7.796` edge `0.0106` maxDD `-0.1507`
- `risk_on_high->metal_1h` score `0.0742` n `52` status `ready` deltaP `5.2165` edge `0.0053` maxDD `-0.1115`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
