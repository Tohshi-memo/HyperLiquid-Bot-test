# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-28T12:07:24.947472+00:00`
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

- `news_risk_high->unknown_1h` score `3393.306` n `31` status `ready` deltaP `2.0813` edge `282.7792` maxDD `-0.7395`
- `news_risk_high->unknown_4h` score `3263.413` n `31` status `ready` deltaP `3.7864` edge `271.9315` maxDD `-0.1191`
- `news_risk_high->crypto_major_24h` score `23.3459` n `31` status `ready` deltaP `35.0087` edge `1.7121` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `17.0607` n `31` status `ready` deltaP `32.9289` edge `1.2022` maxDD `0.0`
- `news_risk_high->equity_24h` score `12.7065` n `31` status `ready` deltaP `28.0763` edge `0.8717` maxDD `0.0`
- `news_risk_high->crypto_alt_4h` score `8.9758` n `31` status `ready` deltaP `23.1018` edge `0.681` maxDD `-5.2957`
- `news_risk_high->crypto_major_4h` score `5.7095` n `31` status `ready` deltaP `17.3879` edge `0.7578` maxDD `-7.6714`
- `news_risk_high->equity_4h` score `5.6141` n `31` status `ready` deltaP `30.9747` edge `0.3094` maxDD `-2.178`
- `news_risk_high->fx_24h` score `5.0292` n `31` status `ready` deltaP `41.4491` edge `0.1556` maxDD `-0.0262`
- `news_risk_high->metal_24h` score `3.9464` n `31` status `ready` deltaP `16.867` edge `0.2439` maxDD `-0.1986`
- `news_risk_high->index_4h` score `2.522` n `31` status `ready` deltaP `30.8222` edge `0.0307` maxDD `-0.4146`
- `news_risk_high->index_24h` score `2.3984` n `31` status `ready` deltaP `26.1698` edge `0.0254` maxDD `0.0`
- `news_risk_high->index_1h` score `2.3379` n `31` status `ready` deltaP `28.6991` edge `0.012` maxDD `-0.0136`
- `news_risk_high->equity_1h` score `2.152` n `31` status `ready` deltaP `14.2988` edge `0.1027` maxDD `-0.1621`
- `news_risk_high->crypto_major_1h` score `1.9949` n `31` status `ready` deltaP `7.0166` edge `0.2551` maxDD `-1.6897`
- `news_risk_high->crypto_alt_1h` score `1.7982` n `31` status `ready` deltaP `9.7112` edge `0.2015` maxDD `-1.5232`
- `news_risk_high->metal_1h` score `1.1161` n `31` status `ready` deltaP `24.3432` edge `0.0087` maxDD `-0.2315`
- `market_context_high->metal_4h` score `0.9733` n `41` status `ready` deltaP `13.567` edge `0.0318` maxDD `-0.2914`
- `news_risk_high->commodity_4h` score `0.4489` n `31` status `ready` deltaP `10.5035` edge `0.0273` maxDD `-0.5151`
- `market_context_high->fx_1h` score `0.3905` n `53` status `ready` deltaP `10.3774` edge `0.0023` maxDD `-0.0471`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
