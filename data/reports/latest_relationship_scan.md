# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-16T03:52:28.685196+00:00`
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

- `news_risk_high->unknown_4h` score `365.7662` n `83` status `ready` deltaP `-21.6629` edge `30.7144` maxDD `-4.1571`
- `news_risk_high->crypto_alt_24h` score `24.4227` n `78` status `ready` deltaP `47.7698` edge `1.7558` maxDD `-1.4564`
- `news_risk_high->crypto_major_24h` score `20.8633` n `78` status `ready` deltaP `39.7303` edge `1.6208` maxDD `-9.098`
- `news_risk_high->equity_24h` score `15.9425` n `78` status `ready` deltaP `49.8531` edge `1.1736` maxDD `-6.5262`
- `news_risk_high->index_24h` score `8.3529` n `78` status `ready` deltaP `59.6821` edge `0.3158` maxDD `-0.075`
- `news_risk_high->metal_24h` score `6.8432` n `78` status `ready` deltaP `38.4882` edge `0.3591` maxDD `-0.6334`
- `risk_on_high->commodity_24h` score `5.7101` n `52` status `ready` deltaP `37.3264` edge `0.227` maxDD `0.0`
- `risk_on_and_context->commodity_24h` score `5.7101` n `52` status `ready` deltaP `37.3264` edge `0.227` maxDD `0.0`
- `market_context_high->commodity_24h` score `4.411` n `149` status `ready` deltaP `30.615` edge `0.216` maxDD `-0.8682`
- `risk_on_high->fx_24h` score `2.4113` n `52` status `ready` deltaP `31.9311` edge `-0.0077` maxDD `-0.0054`
- `risk_on_and_context->fx_24h` score `2.4113` n `52` status `ready` deltaP `31.9311` edge `-0.0077` maxDD `-0.0054`
- `market_context_high->fx_24h` score `2.2764` n `149` status `ready` deltaP `29.1562` edge `0.0169` maxDD `-0.0593`
- `risk_on_high->commodity_4h` score `1.7516` n `52` status `ready` deltaP `24.1557` edge `0.0199` maxDD `-0.1313`
- `risk_on_and_context->commodity_4h` score `1.7516` n `52` status `ready` deltaP `24.1557` edge `0.0199` maxDD `-0.1313`
- `market_context_high->commodity_4h` score `1.6513` n `149` status `ready` deltaP `20.658` edge `0.0417` maxDD `-0.345`
- `market_context_high->commodity_1h` score `0.7946` n `149` status `ready` deltaP `13.2169` edge `0.0158` maxDD `-0.3491`
- `news_risk_high->index_4h` score `0.7636` n `83` status `ready` deltaP `18.2908` edge `0.0388` maxDD `-0.6935`
- `risk_on_high->crypto_alt_4h` score `0.4237` n `52` status `ready` deltaP `10.3072` edge `0.1471` maxDD `-6.2526`
- `risk_on_and_context->crypto_alt_4h` score `0.4237` n `52` status `ready` deltaP `10.3072` edge `0.1471` maxDD `-6.2526`
- `risk_on_high->commodity_1h` score `0.1713` n `52` status `ready` deltaP `6.299` edge `0.0075` maxDD `-0.1507`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
