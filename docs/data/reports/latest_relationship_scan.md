# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-16T06:52:26.540416+00:00`
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

- `news_risk_high->unknown_4h` score `365.5994` n `83` status `ready` deltaP `-21.6629` edge `30.7005` maxDD `-4.1571`
- `news_risk_high->crypto_alt_24h` score `24.4443` n `78` status `ready` deltaP `47.7698` edge `1.7576` maxDD `-1.4564`
- `news_risk_high->crypto_major_24h` score `21.1285` n `78` status `ready` deltaP `39.7303` edge `1.6429` maxDD `-9.098`
- `news_risk_high->equity_24h` score `15.7541` n `78` status `ready` deltaP `49.8531` edge `1.1579` maxDD `-6.5262`
- `news_risk_high->index_24h` score `8.1485` n `78` status `ready` deltaP `57.7724` edge `0.3115` maxDD `-0.075`
- `news_risk_high->metal_24h` score `6.8468` n `78` status `ready` deltaP `38.4882` edge `0.3594` maxDD `-0.6334`
- `risk_on_high->commodity_24h` score `5.5709` n `52` status `ready` deltaP `36.1111` edge `0.2235` maxDD `0.0`
- `risk_on_and_context->commodity_24h` score `5.5709` n `52` status `ready` deltaP `36.1111` edge `0.2235` maxDD `0.0`
- `market_context_high->commodity_24h` score `4.2717` n `149` status `ready` deltaP `29.3997` edge `0.2125` maxDD `-0.8682`
- `risk_on_high->fx_24h` score `2.3705` n `52` status `ready` deltaP `31.9311` edge `-0.0111` maxDD `-0.0054`
- `risk_on_and_context->fx_24h` score `2.3705` n `52` status `ready` deltaP `31.9311` edge `-0.0111` maxDD `-0.0054`
- `market_context_high->fx_24h` score `2.2356` n `149` status `ready` deltaP `29.1562` edge `0.0135` maxDD `-0.0593`
- `risk_on_high->commodity_4h` score `1.9301` n `52` status `ready` deltaP `25.8325` edge `0.0236` maxDD `-0.1313`
- `risk_on_and_context->commodity_4h` score `1.9301` n `52` status `ready` deltaP `25.8325` edge `0.0236` maxDD `-0.1313`
- `market_context_high->commodity_4h` score `1.8298` n `149` status `ready` deltaP `22.3348` edge `0.0454` maxDD `-0.345`
- `market_context_high->commodity_1h` score `0.7563` n `149` status `ready` deltaP `12.7678` edge `0.0156` maxDD `-0.3491`
- `news_risk_high->index_4h` score `0.6854` n `83` status `ready` deltaP `17.0713` edge `0.0369` maxDD `-0.6935`
- `risk_on_high->crypto_alt_4h` score `0.5684` n `52` status `ready` deltaP `10.7646` edge `0.1626` maxDD `-6.2526`
- `risk_on_and_context->crypto_alt_4h` score `0.5684` n `52` status `ready` deltaP `10.7646` edge `0.1626` maxDD `-6.2526`
- `risk_on_high->metal_1h` score `0.138` n `52` status `ready` deltaP `6.5638` edge `0.0045` maxDD `-0.1115`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
