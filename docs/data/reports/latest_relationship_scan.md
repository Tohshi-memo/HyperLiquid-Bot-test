# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-26T00:37:36.644315+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `3887`

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

- `market_context_high->unknown_1h` score `32144.6126` n `45` status `ready` deltaP `1.5668` edge `2678.7167` maxDD `-0.4209`
- `market_context_high->unknown_4h` score `21793.0246` n `45` status `ready` deltaP `1.958` edge `1816.0862` maxDD `-0.7765`
- `news_risk_high->unknown_1h` score `909.6576` n `31` status `ready` deltaP `1.7819` edge `75.8105` maxDD `-0.7395`
- `news_risk_high->unknown_4h` score `540.0771` n `31` status `ready` deltaP `3.1766` edge `44.9909` maxDD `-0.1191`
- `news_risk_high->unknown_24h` score `177.5725` n `31` status `ready` deltaP `6.0764` edge `14.7572` maxDD `0.0`
- `news_risk_high->equity_24h` score `45.1763` n `31` status `ready` deltaP `51.3889` edge `3.4221` maxDD `0.0`
- `news_risk_high->crypto_major_24h` score `41.7238` n `31` status `ready` deltaP `52.2569` edge `3.1286` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `36.9054` n `31` status `ready` deltaP `51.5625` edge `2.7317` maxDD `0.0`
- `news_risk_high->metal_24h` score `11.296` n `31` status `ready` deltaP `37.9369` edge `0.7159` maxDD `-0.1986`
- `news_risk_high->crypto_alt_4h` score `10.9183` n `31` status `ready` deltaP `26.6079` edge `0.8195` maxDD `-5.2957`
- `news_risk_high->equity_4h` score `10.3591` n `31` status `ready` deltaP `37.682` edge `0.6601` maxDD `-2.178`
- `news_risk_high->index_24h` score `7.3734` n `31` status `ready` deltaP `52.7778` edge `0.2626` maxDD `0.0`
- `news_risk_high->crypto_major_4h` score `6.7008` n `31` status `ready` deltaP `17.2354` edge `0.8859` maxDD `-7.6714`
- `news_risk_high->fx_24h` score `5.2587` n `31` status `ready` deltaP `44.6629` edge `0.1533` maxDD `-0.0262`
- `news_risk_high->equity_1h` score `3.6223` n `31` status `ready` deltaP `19.8377` edge `0.1883` maxDD `-0.1621`
- `news_risk_high->index_4h` score `3.3464` n `31` status `ready` deltaP `36.4625` edge `0.0618` maxDD `-0.4146`
- `news_risk_high->index_1h` score `2.6578` n `31` status `ready` deltaP `31.5434` edge `0.0197` maxDD `-0.0136`
- `news_risk_high->crypto_major_1h` score `2.4407` n `31` status `ready` deltaP `10.1603` edge `0.2913` maxDD `-1.6897`
- `market_context_high->fx_4h` score `2.3559` n `45` status `ready` deltaP `29.1734` edge `0.0303` maxDD `-0.2774`
- `news_risk_high->crypto_alt_1h` score `2.2409` n `31` status `ready` deltaP `12.8549` edge `0.2373` maxDD `-1.5232`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
