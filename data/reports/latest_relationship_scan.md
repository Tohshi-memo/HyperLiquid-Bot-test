# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-28T12:22:29.443128+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `64`

- Symbol pattern count: `5558`

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

- `news_risk_high->unknown_1h` score `3395.9748` n `31` status `ready` deltaP `2.0813` edge `283.0016` maxDD `-0.7395`
- `news_risk_high->unknown_4h` score `3260.0098` n `31` status `ready` deltaP `3.7864` edge `271.6479` maxDD `-0.1191`
- `news_risk_high->crypto_major_24h` score `23.4942` n `31` status `ready` deltaP `35.182` edge `1.7233` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `17.2054` n `31` status `ready` deltaP `33.1023` edge `1.2131` maxDD `0.0`
- `news_risk_high->equity_24h` score `12.7437` n `31` status `ready` deltaP `28.0763` edge `0.8748` maxDD `0.0`
- `news_risk_high->crypto_alt_4h` score `9.0288` n `31` status `ready` deltaP `23.2543` edge `0.6844` maxDD `-5.2957`
- `news_risk_high->crypto_major_4h` score `5.7463` n `31` status `ready` deltaP `17.5403` edge `0.7615` maxDD `-7.6714`
- `news_risk_high->equity_4h` score `5.6443` n `31` status `ready` deltaP `31.1271` edge `0.3109` maxDD `-2.178`
- `news_risk_high->fx_24h` score `5.0304` n `31` status `ready` deltaP `41.4491` edge `0.1557` maxDD `-0.0262`
- `news_risk_high->metal_24h` score `3.9662` n `31` status `ready` deltaP `17.0403` edge `0.2444` maxDD `-0.1986`
- `news_risk_high->index_4h` score `2.5366` n `31` status `ready` deltaP `30.9747` edge `0.0309` maxDD `-0.4146`
- `news_risk_high->index_24h` score `2.4032` n `31` status `ready` deltaP `26.1698` edge `0.0258` maxDD `0.0`
- `news_risk_high->index_1h` score `2.3379` n `31` status `ready` deltaP `28.6991` edge `0.012` maxDD `-0.0136`
- `news_risk_high->equity_1h` score `2.1568` n `31` status `ready` deltaP `14.2988` edge `0.1031` maxDD `-0.1621`
- `news_risk_high->crypto_major_1h` score `2.0066` n `31` status `ready` deltaP `7.0166` edge `0.2566` maxDD `-1.6897`
- `news_risk_high->crypto_alt_1h` score `1.8083` n `31` status `ready` deltaP `9.7112` edge `0.2028` maxDD `-1.5232`
- `news_risk_high->metal_1h` score `1.1169` n `31` status `ready` deltaP `24.3432` edge `0.0088` maxDD `-0.2315`
- `market_context_high->metal_4h` score `1.0381` n `42` status `ready` deltaP `14.4381` edge `0.0314` maxDD `-0.2914`
- `news_risk_high->commodity_4h` score `0.4568` n `31` status `ready` deltaP `10.656` edge `0.0273` maxDD `-0.5151`
- `market_context_high->fx_1h` score `0.4201` n `54` status `ready` deltaP `10.9614` edge `0.0022` maxDD `-0.0471`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
