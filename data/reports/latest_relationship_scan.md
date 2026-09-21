# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-21T17:22:30.464183+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `10204`

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

- `market_context_high->unknown_4h` score `28.2637` n `58` status `ready` deltaP `1.23` edge `2.3621` maxDD `-0.5326`
- `news_risk_high->crypto_major_24h` score `17.3488` n `101` status `ready` deltaP `5.0192` edge `2.0981` maxDD `-46.1999`
- `news_risk_high->crypto_alt_24h` score `11.4363` n `101` status `ready` deltaP `5.4043` edge `1.4051` maxDD `-32.7147`
- `news_risk_high->crypto_alt_4h` score `3.7349` n `101` status `ready` deltaP `17.5471` edge `0.3152` maxDD `-7.675`
- `news_risk_high->crypto_major_4h` score `3.2887` n `101` status `ready` deltaP `19.9861` edge `0.2666` maxDD `-8.0625`
- `news_risk_high->crypto_alt_1h` score `2.5759` n `101` status `ready` deltaP `15.7823` edge `0.156` maxDD `-2.058`
- `news_risk_high->crypto_major_1h` score `1.8865` n `101` status `ready` deltaP `17.2793` edge `0.0943` maxDD `-2.8494`
- `news_risk_high->commodity_24h` score `1.7186` n `101` status `ready` deltaP `26.1482` edge `0.1766` maxDD `-3.4467`
- `market_context_high->equity_1h` score `0.7744` n `58` status `ready` deltaP `5.5596` edge `0.0528` maxDD `-0.36`
- `news_risk_high->metal_1h` score `0.5718` n `101` status `ready` deltaP `14.1489` edge `0.0135` maxDD `-0.8144`
- `market_context_high->index_1h` score `0.5651` n `58` status `ready` deltaP `8.9304` edge `0.0131` maxDD `-0.0435`
- `market_context_high->fx_1h` score `0.4337` n `58` status `ready` deltaP `9.8235` edge `0.0063` maxDD `-0.1854`
- `news_risk_high->metal_4h` score `0.3221` n `101` status `ready` deltaP `14.8122` edge `0.0335` maxDD `-2.0994`
- `news_risk_high->fx_4h` score `0.3171` n `101` status `ready` deltaP `9.7078` edge `0.0253` maxDD `-0.421`
- `market_context_high->metal_1h` score `0.2938` n `58` status `ready` deltaP `5.699` edge `0.0173` maxDD `-0.1314`
- `market_context_high->index_4h` score `0.1772` n `58` status `ready` deltaP `12.4947` edge `0.0031` maxDD `-1.0949`
- `market_context_high->metal_24h` score `0.051` n `32` status `ready` deltaP `11.2847` edge `-0.0569` maxDD `-0.1267`
- `news_risk_high->fx_1h` score `-0.1154` n `101` status `ready` deltaP `4.1901` edge `0.0068` maxDD `-0.2147`
- `news_risk_high->equity_1h` score `-0.3005` n `101` status `ready` deltaP `1.1724` edge `0.0077` maxDD `-0.9112`
- `market_context_high->crypto_major_1h` score `-0.3984` n `58` status `ready` deltaP `-2.5397` edge `0.0556` maxDD `-2.7494`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
