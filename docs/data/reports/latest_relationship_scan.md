# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-16T14:22:40.693995+00:00`
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

- `news_risk_high->unknown_4h` score `368.9506` n `83` status `ready` deltaP `-21.0531` edge `30.9757` maxDD `-4.1571`
- `news_risk_high->crypto_alt_24h` score `23.4819` n `78` status `ready` deltaP `47.7698` edge `1.6774` maxDD `-1.4564`
- `news_risk_high->crypto_major_24h` score `20.8609` n `78` status `ready` deltaP `39.7303` edge `1.6206` maxDD `-9.098`
- `news_risk_high->equity_24h` score `14.667` n `78` status `ready` deltaP `46.5545` edge `1.0893` maxDD `-6.5262`
- `news_risk_high->index_24h` score `7.5807` n `78` status `ready` deltaP `52.5641` edge `0.2989` maxDD `-0.075`
- `news_risk_high->metal_24h` score `6.2835` n `78` status `ready` deltaP `36.2313` edge `0.3275` maxDD `-0.6334`
- `risk_on_high->commodity_24h` score `5.4104` n `52` status `ready` deltaP `34.375` edge `0.2217` maxDD `0.0`
- `risk_on_and_context->commodity_24h` score `5.4104` n `52` status `ready` deltaP `34.375` edge `0.2217` maxDD `0.0`
- `market_context_high->commodity_24h` score `4.1113` n `149` status `ready` deltaP `27.6636` edge `0.2107` maxDD `-0.8682`
- `risk_on_high->fx_24h` score `2.3669` n `52` status `ready` deltaP `31.9311` edge `-0.0114` maxDD `-0.0054`
- `risk_on_and_context->fx_24h` score `2.3669` n `52` status `ready` deltaP `31.9311` edge `-0.0114` maxDD `-0.0054`
- `market_context_high->fx_24h` score `2.232` n `149` status `ready` deltaP `29.1562` edge `0.0132` maxDD `-0.0593`
- `risk_on_high->commodity_4h` score `2.183` n `52` status `ready` deltaP `28.424` edge `0.0274` maxDD `-0.1313`
- `risk_on_and_context->commodity_4h` score `2.183` n `52` status `ready` deltaP `28.424` edge `0.0274` maxDD `-0.1313`
- `market_context_high->commodity_4h` score `2.0828` n `149` status `ready` deltaP `24.9263` edge `0.0492` maxDD `-0.345`
- `market_context_high->commodity_1h` score `0.8593` n `149` status `ready` deltaP `13.8157` edge `0.0172` maxDD `-0.3491`
- `news_risk_high->index_4h` score `0.4579` n `83` status `ready` deltaP `13.5652` edge `0.0311` maxDD `-0.6935`
- `risk_on_high->crypto_alt_4h` score `0.36` n `52` status `ready` deltaP `9.6975` edge `0.143` maxDD `-6.2526`
- `risk_on_and_context->crypto_alt_4h` score `0.36` n `52` status `ready` deltaP `9.6975` edge `0.143` maxDD `-6.2526`
- `risk_on_high->commodity_1h` score `0.236` n `52` status `ready` deltaP `6.8978` edge `0.0089` maxDD `-0.1507`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
