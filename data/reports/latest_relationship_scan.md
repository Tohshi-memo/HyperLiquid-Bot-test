# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-16T14:37:34.199816+00:00`
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

- `news_risk_high->unknown_4h` score `369.0322` n `83` status `ready` deltaP `-21.0531` edge `30.9825` maxDD `-4.1571`
- `news_risk_high->crypto_alt_24h` score `23.4375` n `78` status `ready` deltaP `47.7698` edge `1.6737` maxDD `-1.4564`
- `news_risk_high->crypto_major_24h` score `20.8165` n `78` status `ready` deltaP `39.7303` edge `1.6169` maxDD `-9.098`
- `news_risk_high->equity_24h` score `14.5883` n `78` status `ready` deltaP `46.3809` edge `1.0839` maxDD `-6.5262`
- `news_risk_high->index_24h` score `7.5548` n `78` status `ready` deltaP `52.3905` edge `0.2979` maxDD `-0.075`
- `news_risk_high->metal_24h` score `6.2384` n `78` status `ready` deltaP `36.0577` edge `0.3249` maxDD `-0.6334`
- `risk_on_high->commodity_24h` score `5.4375` n `52` status `ready` deltaP `34.5486` edge `0.2228` maxDD `0.0`
- `risk_on_and_context->commodity_24h` score `5.4375` n `52` status `ready` deltaP `34.5486` edge `0.2228` maxDD `0.0`
- `market_context_high->commodity_24h` score `4.1383` n `149` status `ready` deltaP `27.8372` edge `0.2118` maxDD `-0.8682`
- `risk_on_high->fx_24h` score `2.3681` n `52` status `ready` deltaP `31.9311` edge `-0.0113` maxDD `-0.0054`
- `risk_on_and_context->fx_24h` score `2.3681` n `52` status `ready` deltaP `31.9311` edge `-0.0113` maxDD `-0.0054`
- `market_context_high->fx_24h` score `2.2332` n `149` status `ready` deltaP `29.1562` edge `0.0133` maxDD `-0.0593`
- `risk_on_high->commodity_4h` score `2.1854` n `52` status `ready` deltaP `28.424` edge `0.0276` maxDD `-0.1313`
- `risk_on_and_context->commodity_4h` score `2.1854` n `52` status `ready` deltaP `28.424` edge `0.0276` maxDD `-0.1313`
- `market_context_high->commodity_4h` score `2.0852` n `149` status `ready` deltaP `24.9263` edge `0.0494` maxDD `-0.345`
- `market_context_high->commodity_1h` score `0.8749` n `149` status `ready` deltaP `13.9654` edge `0.0175` maxDD `-0.3491`
- `news_risk_high->index_4h` score `0.4491` n `83` status `ready` deltaP `13.4128` edge `0.031` maxDD `-0.6935`
- `risk_on_high->crypto_alt_4h` score `0.3639` n `52` status `ready` deltaP `9.6975` edge `0.1435` maxDD `-6.2526`
- `risk_on_and_context->crypto_alt_4h` score `0.3639` n `52` status `ready` deltaP `9.6975` edge `0.1435` maxDD `-6.2526`
- `risk_on_high->commodity_1h` score `0.2516` n `52` status `ready` deltaP `7.0475` edge `0.0092` maxDD `-0.1507`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
