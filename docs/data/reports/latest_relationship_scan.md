# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-16T11:22:30.590322+00:00`
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

- `news_risk_high->unknown_4h` score `366.9488` n `83` status `ready` deltaP `-21.2056` edge `30.8099` maxDD `-4.1571`
- `news_risk_high->crypto_alt_24h` score `23.9415` n `78` status `ready` deltaP `47.7698` edge `1.7157` maxDD `-1.4564`
- `news_risk_high->crypto_major_24h` score `21.0505` n `78` status `ready` deltaP `39.7303` edge `1.6364` maxDD `-9.098`
- `news_risk_high->equity_24h` score `15.1314` n `78` status `ready` deltaP `47.7697` edge `1.1199` maxDD `-6.5262`
- `news_risk_high->index_24h` score `7.8049` n `78` status `ready` deltaP `54.6474` edge `0.3037` maxDD `-0.075`
- `news_risk_high->metal_24h` score `6.671` n `78` status `ready` deltaP `38.3146` edge `0.3459` maxDD `-0.6334`
- `risk_on_high->commodity_24h` score `5.39` n `52` status `ready` deltaP `34.375` edge `0.22` maxDD `0.0`
- `risk_on_and_context->commodity_24h` score `5.39` n `52` status `ready` deltaP `34.375` edge `0.22` maxDD `0.0`
- `market_context_high->commodity_24h` score `4.0909` n `149` status `ready` deltaP `27.6636` edge `0.209` maxDD `-0.8682`
- `risk_on_high->fx_24h` score `2.3633` n `52` status `ready` deltaP `31.9311` edge `-0.0117` maxDD `-0.0054`
- `risk_on_and_context->fx_24h` score `2.3633` n `52` status `ready` deltaP `31.9311` edge `-0.0117` maxDD `-0.0054`
- `market_context_high->fx_24h` score `2.2284` n `149` status `ready` deltaP `29.1562` edge `0.0129` maxDD `-0.0593`
- `risk_on_high->commodity_4h` score `2.0869` n `52` status `ready` deltaP `27.3569` edge `0.0265` maxDD `-0.1313`
- `risk_on_and_context->commodity_4h` score `2.0869` n `52` status `ready` deltaP `27.3569` edge `0.0265` maxDD `-0.1313`
- `market_context_high->commodity_4h` score `1.9866` n `149` status `ready` deltaP `23.8592` edge `0.0483` maxDD `-0.345`
- `market_context_high->commodity_1h` score `0.8808` n `149` status `ready` deltaP `14.1151` edge `0.017` maxDD `-0.3491`
- `risk_on_high->crypto_alt_4h` score `0.5661` n `52` status `ready` deltaP `10.7646` edge `0.1623` maxDD `-6.2526`
- `risk_on_and_context->crypto_alt_4h` score `0.5661` n `52` status `ready` deltaP `10.7646` edge `0.1623` maxDD `-6.2526`
- `news_risk_high->index_4h` score `0.5393` n `83` status `ready` deltaP `14.9372` edge `0.0324` maxDD `-0.6935`
- `risk_on_high->commodity_1h` score `0.2576` n `52` status `ready` deltaP `7.1972` edge `0.0087` maxDD `-0.1507`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
