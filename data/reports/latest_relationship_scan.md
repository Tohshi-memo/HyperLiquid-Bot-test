# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-16T04:22:29.359686+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `11569`

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

- `news_risk_high->unknown_4h` score `365.7866` n `83` status `ready` deltaP `-21.6629` edge `30.7161` maxDD `-4.1571`
- `news_risk_high->crypto_alt_24h` score `24.4479` n `78` status `ready` deltaP `47.7698` edge `1.7579` maxDD `-1.4564`
- `news_risk_high->crypto_major_24h` score `20.9305` n `78` status `ready` deltaP `39.7303` edge `1.6264` maxDD `-9.098`
- `news_risk_high->equity_24h` score `15.9113` n `78` status `ready` deltaP `49.8531` edge `1.171` maxDD `-6.5262`
- `news_risk_high->index_24h` score `8.3306` n `78` status `ready` deltaP `59.5085` edge `0.3151` maxDD `-0.075`
- `news_risk_high->metal_24h` score `6.8444` n `78` status `ready` deltaP `38.4882` edge `0.3592` maxDD `-0.6334`
- `risk_on_high->commodity_24h` score `5.6715` n `52` status `ready` deltaP `36.9792` edge `0.2261` maxDD `0.0`
- `risk_on_and_context->commodity_24h` score `5.6715` n `52` status `ready` deltaP `36.9792` edge `0.2261` maxDD `0.0`
- `market_context_high->commodity_24h` score `4.3724` n `149` status `ready` deltaP `30.2678` edge `0.2151` maxDD `-0.8682`
- `risk_on_high->fx_24h` score `2.4029` n `52` status `ready` deltaP `31.9311` edge `-0.0084` maxDD `-0.0054`
- `risk_on_and_context->fx_24h` score `2.4029` n `52` status `ready` deltaP `31.9311` edge `-0.0084` maxDD `-0.0054`
- `market_context_high->fx_24h` score `2.268` n `149` status `ready` deltaP `29.1562` edge `0.0162` maxDD `-0.0593`
- `risk_on_high->commodity_4h` score `1.7674` n `52` status `ready` deltaP `24.3082` edge `0.0202` maxDD `-0.1313`
- `risk_on_and_context->commodity_4h` score `1.7674` n `52` status `ready` deltaP `24.3082` edge `0.0202` maxDD `-0.1313`
- `market_context_high->commodity_4h` score `1.6671` n `149` status `ready` deltaP `20.8105` edge `0.042` maxDD `-0.345`
- `market_context_high->commodity_1h` score `0.779` n `149` status `ready` deltaP `13.0672` edge `0.0155` maxDD `-0.3491`
- `news_risk_high->index_4h` score `0.7534` n `83` status `ready` deltaP `18.1384` edge `0.0385` maxDD `-0.6935`
- `risk_on_high->crypto_alt_4h` score `0.4675` n `52` status `ready` deltaP `10.4597` edge `0.1517` maxDD `-6.2526`
- `risk_on_and_context->crypto_alt_4h` score `0.4675` n `52` status `ready` deltaP `10.4597` edge `0.1517` maxDD `-6.2526`
- `risk_on_high->commodity_1h` score `0.1557` n `52` status `ready` deltaP `6.1493` edge `0.0072` maxDD `-0.1507`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
