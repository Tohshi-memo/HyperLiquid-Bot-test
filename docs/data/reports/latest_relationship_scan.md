# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-16T06:25:31.951408+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `11471`

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

- `news_risk_high->unknown_4h` score `365.5802` n `83` status `ready` deltaP `-21.6629` edge `30.6989` maxDD `-4.1571`
- `news_risk_high->crypto_alt_24h` score `24.4419` n `78` status `ready` deltaP `47.7698` edge `1.7574` maxDD `-1.4564`
- `news_risk_high->crypto_major_24h` score `21.0889` n `78` status `ready` deltaP `39.7303` edge `1.6396` maxDD `-9.098`
- `news_risk_high->equity_24h` score `15.7841` n `78` status `ready` deltaP `49.8531` edge `1.1604` maxDD `-6.5262`
- `news_risk_high->index_24h` score `8.1847` n `78` status `ready` deltaP `58.1196` edge `0.3122` maxDD `-0.075`
- `news_risk_high->metal_24h` score `6.8492` n `78` status `ready` deltaP `38.4882` edge `0.3596` maxDD `-0.6334`
- `risk_on_high->commodity_24h` score `5.6035` n `52` status `ready` deltaP `36.4583` edge `0.2239` maxDD `0.0`
- `risk_on_and_context->commodity_24h` score `5.6035` n `52` status `ready` deltaP `36.4583` edge `0.2239` maxDD `0.0`
- `market_context_high->commodity_24h` score `4.3043` n `149` status `ready` deltaP `29.7469` edge `0.2129` maxDD `-0.8682`
- `risk_on_high->fx_24h` score `2.3741` n `52` status `ready` deltaP `31.9311` edge `-0.0108` maxDD `-0.0054`
- `risk_on_and_context->fx_24h` score `2.3741` n `52` status `ready` deltaP `31.9311` edge `-0.0108` maxDD `-0.0054`
- `market_context_high->fx_24h` score `2.2392` n `149` status `ready` deltaP `29.1562` edge `0.0138` maxDD `-0.0593`
- `risk_on_high->commodity_4h` score `1.8937` n `52` status `ready` deltaP `25.5277` edge `0.0226` maxDD `-0.1313`
- `risk_on_and_context->commodity_4h` score `1.8937` n `52` status `ready` deltaP `25.5277` edge `0.0226` maxDD `-0.1313`
- `market_context_high->commodity_4h` score `1.7935` n `149` status `ready` deltaP `22.03` edge `0.0444` maxDD `-0.345`
- `market_context_high->commodity_1h` score `0.7383` n `149` status `ready` deltaP `12.6181` edge `0.0151` maxDD `-0.3491`
- `news_risk_high->index_4h` score `0.7059` n `83` status `ready` deltaP `17.3762` edge `0.0375` maxDD `-0.6935`
- `risk_on_high->crypto_alt_4h` score `0.5409` n `52` status `ready` deltaP `10.4597` edge `0.1611` maxDD `-6.2526`
- `risk_on_and_context->crypto_alt_4h` score `0.5409` n `52` status `ready` deltaP `10.4597` edge `0.1611` maxDD `-6.2526`
- `risk_on_high->metal_1h` score `0.1201` n `52` status `ready` deltaP `6.2644` edge `0.0042` maxDD `-0.1115`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
