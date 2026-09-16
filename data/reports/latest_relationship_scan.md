# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-16T11:07:31.351593+00:00`
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

- `news_risk_high->unknown_4h` score `366.6174` n `83` status `ready` deltaP `-21.358` edge `30.7833` maxDD `-4.1571`
- `news_risk_high->crypto_alt_24h` score `23.9739` n `78` status `ready` deltaP `47.7698` edge `1.7184` maxDD `-1.4564`
- `news_risk_high->crypto_major_24h` score `21.0541` n `78` status `ready` deltaP `39.7303` edge `1.6367` maxDD `-9.098`
- `news_risk_high->equity_24h` score `15.141` n `78` status `ready` deltaP `47.7697` edge `1.1207` maxDD `-6.5262`
- `news_risk_high->index_24h` score `7.82` n `78` status `ready` deltaP `54.821` edge `0.3038` maxDD `-0.075`
- `news_risk_high->metal_24h` score `6.6956` n `78` status `ready` deltaP `38.4882` edge `0.3468` maxDD `-0.6334`
- `risk_on_high->commodity_24h` score `5.4075` n `52` status `ready` deltaP `34.5486` edge `0.2203` maxDD `0.0`
- `risk_on_and_context->commodity_24h` score `5.4075` n `52` status `ready` deltaP `34.5486` edge `0.2203` maxDD `0.0`
- `market_context_high->commodity_24h` score `4.1083` n `149` status `ready` deltaP `27.8372` edge `0.2093` maxDD `-0.8682`
- `risk_on_high->fx_24h` score `2.3633` n `52` status `ready` deltaP `31.9311` edge `-0.0117` maxDD `-0.0054`
- `risk_on_and_context->fx_24h` score `2.3633` n `52` status `ready` deltaP `31.9311` edge `-0.0117` maxDD `-0.0054`
- `market_context_high->fx_24h` score `2.2284` n `149` status `ready` deltaP `29.1562` edge `0.0129` maxDD `-0.0593`
- `risk_on_high->commodity_4h` score `2.0735` n `52` status `ready` deltaP `27.2045` edge `0.0264` maxDD `-0.1313`
- `risk_on_and_context->commodity_4h` score `2.0735` n `52` status `ready` deltaP `27.2045` edge `0.0264` maxDD `-0.1313`
- `market_context_high->commodity_4h` score `1.9732` n `149` status `ready` deltaP `23.7068` edge `0.0482` maxDD `-0.345`
- `market_context_high->commodity_1h` score `0.8665` n `149` status `ready` deltaP `13.9654` edge `0.0168` maxDD `-0.3491`
- `risk_on_high->crypto_alt_4h` score `0.5771` n `52` status `ready` deltaP `10.917` edge `0.1627` maxDD `-6.2526`
- `risk_on_and_context->crypto_alt_4h` score `0.5771` n `52` status `ready` deltaP `10.917` edge `0.1627` maxDD `-6.2526`
- `news_risk_high->index_4h` score `0.5393` n `83` status `ready` deltaP `14.9372` edge `0.0324` maxDD `-0.6935`
- `risk_on_high->commodity_1h` score `0.2432` n `52` status `ready` deltaP `7.0475` edge `0.0085` maxDD `-0.1507`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
