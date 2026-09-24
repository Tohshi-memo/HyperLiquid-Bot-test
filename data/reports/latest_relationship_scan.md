# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-24T17:22:37.313166+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `10041`

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

- `market_context_high->unknown_1h` score `87.1951` n `47` status `ready` deltaP `10.116` edge `7.2059` maxDD `-0.2334`
- `market_context_high->crypto_major_24h` score `43.8221` n `47` status `ready` deltaP `30.4226` edge `3.4883` maxDD `-2.4756`
- `market_context_high->crypto_alt_24h` score `29.326` n `47` status `ready` deltaP `24.782` edge `2.3166` maxDD `-2.7051`
- `market_context_high->equity_24h` score `24.4729` n `47` status `ready` deltaP `29.3809` edge `1.8791` maxDD `-2.1786`
- `market_context_high->index_24h` score `7.8274` n `47` status `ready` deltaP `34.7628` edge `0.4335` maxDD `-0.3705`
- `news_risk_high->crypto_major_24h` score `5.243` n `92` status `ready` deltaP `0.936` edge `1.5702` maxDD `-63.6743`
- `market_context_high->metal_24h` score `3.7321` n `47` status `ready` deltaP `32.107` edge `0.1208` maxDD `-0.2401`
- `news_risk_high->crypto_alt_24h` score `3.1497` n `92` status `ready` deltaP `-1.3512` edge `1.1141` maxDD `-49.7699`
- `market_context_high->index_4h` score `3.0592` n `47` status `ready` deltaP `34.941` edge `0.0374` maxDD `-0.2323`
- `news_risk_high->crypto_alt_1h` score `2.9539` n `116` status `ready` deltaP `14.2939` edge `0.1999` maxDD `-1.5895`
- `news_risk_high->crypto_major_1h` score `2.5752` n `116` status `ready` deltaP `17.2517` edge `0.1431` maxDD `-1.8141`
- `market_context_high->equity_4h` score `2.5433` n `47` status `ready` deltaP `17.6018` edge `0.1364` maxDD `-1.3444`
- `news_risk_high->crypto_major_4h` score `2.3313` n `113` status `ready` deltaP `16.3838` edge `0.2982` maxDD `-13.719`
- `news_risk_high->crypto_alt_4h` score `2.2401` n `113` status `ready` deltaP `8.9102` edge `0.3724` maxDD `-15.9436`
- `news_risk_high->fx_4h` score `1.6045` n `113` status `ready` deltaP `23.566` edge `0.0402` maxDD `-0.421`
- `news_risk_high->metal_24h` score `1.1546` n `92` status `ready` deltaP `25.0302` edge `0.126` maxDD `-7.2536`
- `news_risk_high->fx_24h` score `1.1195` n `92` status `ready` deltaP `27.8004` edge `0.1213` maxDD `-1.7159`
- `market_context_high->index_1h` score `0.9954` n `47` status `ready` deltaP `15.0592` edge `0.0104` maxDD `-0.2275`
- `news_risk_high->commodity_24h` score `0.8803` n `92` status `ready` deltaP `15.1042` edge `0.0834` maxDD `-2.1924`
- `market_context_high->equity_1h` score `0.8743` n `47` status `ready` deltaP `11.0173` edge `0.0397` maxDD `-1.5564`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
