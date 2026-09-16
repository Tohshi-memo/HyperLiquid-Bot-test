# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-16T15:22:32.086914+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `11441`

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

- `news_risk_high->unknown_4h` score `368.4274` n `83` status `ready` deltaP `-21.0531` edge `30.9321` maxDD `-4.1571`
- `news_risk_high->crypto_alt_24h` score `23.2827` n `78` status `ready` deltaP `47.7698` edge `1.6608` maxDD `-1.4564`
- `news_risk_high->crypto_major_24h` score `20.6689` n `78` status `ready` deltaP `39.7303` edge `1.6046` maxDD `-9.098`
- `news_risk_high->equity_24h` score `14.3235` n `78` status `ready` deltaP `45.86` edge `1.0653` maxDD `-6.5262`
- `news_risk_high->index_24h` score `7.4711` n `78` status `ready` deltaP `51.8696` edge `0.2944` maxDD `-0.075`
- `news_risk_high->metal_24h` score `6.1007` n `78` status `ready` deltaP `35.5368` edge `0.3169` maxDD `-0.6334`
- `risk_on_high->commodity_24h` score `5.5332` n `52` status `ready` deltaP `35.0694` edge `0.2273` maxDD `0.0`
- `risk_on_and_context->commodity_24h` score `5.5332` n `52` status `ready` deltaP `35.0694` edge `0.2273` maxDD `0.0`
- `market_context_high->commodity_24h` score `4.234` n `149` status `ready` deltaP `28.358` edge `0.2163` maxDD `-0.8682`
- `risk_on_high->fx_24h` score `2.3705` n `52` status `ready` deltaP `31.9311` edge `-0.0111` maxDD `-0.0054`
- `risk_on_and_context->fx_24h` score `2.3705` n `52` status `ready` deltaP `31.9311` edge `-0.0111` maxDD `-0.0054`
- `market_context_high->fx_24h` score `2.2356` n `149` status `ready` deltaP `29.1562` edge `0.0135` maxDD `-0.0593`
- `risk_on_high->commodity_4h` score `2.2132` n `52` status `ready` deltaP `28.5764` edge `0.0289` maxDD `-0.1313`
- `risk_on_and_context->commodity_4h` score `2.2132` n `52` status `ready` deltaP `28.5764` edge `0.0289` maxDD `-0.1313`
- `market_context_high->commodity_4h` score `2.1129` n `149` status `ready` deltaP `25.0787` edge `0.0507` maxDD `-0.345`
- `market_context_high->commodity_1h` score `0.9312` n `149` status `ready` deltaP `14.4145` edge `0.0192` maxDD `-0.3491`
- `news_risk_high->index_4h` score `0.4183` n `83` status `ready` deltaP `12.9555` edge `0.0301` maxDD `-0.6935`
- `risk_on_high->crypto_alt_4h` score `0.3756` n `52` status `ready` deltaP `9.6975` edge `0.145` maxDD `-6.2526`
- `risk_on_and_context->crypto_alt_4h` score `0.3756` n `52` status `ready` deltaP `9.6975` edge `0.145` maxDD `-6.2526`
- `risk_on_high->commodity_1h` score `0.3079` n `52` status `ready` deltaP `7.4966` edge `0.0109` maxDD `-0.1507`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
