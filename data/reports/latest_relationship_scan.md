# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-16T12:22:32.463256+00:00`
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

- `news_risk_high->unknown_4h` score `367.8178` n `83` status `ready` deltaP `-21.0531` edge `30.8813` maxDD `-4.1571`
- `news_risk_high->crypto_alt_24h` score `23.8047` n `78` status `ready` deltaP `47.7698` edge `1.7043` maxDD `-1.4564`
- `news_risk_high->crypto_major_24h` score `21.0109` n `78` status `ready` deltaP `39.7303` edge `1.6331` maxDD `-9.098`
- `news_risk_high->equity_24h` score `15.0178` n `78` status `ready` deltaP `47.2489` edge `1.1139` maxDD `-6.5262`
- `news_risk_high->index_24h` score `7.7398` n `78` status `ready` deltaP `53.953` edge `0.3029` maxDD `-0.075`
- `news_risk_high->metal_24h` score `6.547` n `78` status `ready` deltaP `37.6202` edge `0.3402` maxDD `-0.6334`
- `risk_on_high->commodity_24h` score `5.3291` n `52` status `ready` deltaP `33.8542` edge `0.2184` maxDD `0.0`
- `risk_on_and_context->commodity_24h` score `5.3291` n `52` status `ready` deltaP `33.8542` edge `0.2184` maxDD `0.0`
- `market_context_high->commodity_24h` score `4.03` n `149` status `ready` deltaP `27.1428` edge `0.2074` maxDD `-0.8682`
- `risk_on_high->fx_24h` score `2.3657` n `52` status `ready` deltaP `31.9311` edge `-0.0115` maxDD `-0.0054`
- `risk_on_and_context->fx_24h` score `2.3657` n `52` status `ready` deltaP `31.9311` edge `-0.0115` maxDD `-0.0054`
- `market_context_high->fx_24h` score `2.2308` n `149` status `ready` deltaP `29.1562` edge `0.0131` maxDD `-0.0593`
- `risk_on_high->commodity_4h` score `2.1294` n `52` status `ready` deltaP `27.8143` edge `0.027` maxDD `-0.1313`
- `risk_on_and_context->commodity_4h` score `2.1294` n `52` status `ready` deltaP `27.8143` edge `0.027` maxDD `-0.1313`
- `market_context_high->commodity_4h` score `2.0292` n `149` status `ready` deltaP `24.3166` edge `0.0488` maxDD `-0.345`
- `market_context_high->commodity_1h` score `0.882` n `149` status `ready` deltaP `14.1151` edge `0.0171` maxDD `-0.3491`
- `news_risk_high->index_4h` score `0.5291` n `83` status `ready` deltaP `14.7847` edge `0.0321` maxDD `-0.6935`
- `risk_on_high->crypto_alt_4h` score `0.5081` n `52` status `ready` deltaP `10.4597` edge `0.1569` maxDD `-6.2526`
- `risk_on_and_context->crypto_alt_4h` score `0.5081` n `52` status `ready` deltaP `10.4597` edge `0.1569` maxDD `-6.2526`
- `risk_on_high->commodity_1h` score `0.2588` n `52` status `ready` deltaP `7.1972` edge `0.0088` maxDD `-0.1507`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
