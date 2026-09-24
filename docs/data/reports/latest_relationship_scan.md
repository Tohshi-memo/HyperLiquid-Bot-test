# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-24T14:07:43.173587+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `10068`

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

- `market_context_high->unknown_1h` score `89.4151` n `47` status `ready` deltaP `10.116` edge `7.3909` maxDD `-0.2334`
- `market_context_high->crypto_major_24h` score `42.3176` n `47` status `ready` deltaP `29.9017` edge `3.3664` maxDD `-2.4756`
- `market_context_high->crypto_alt_24h` score `28.324` n `47` status `ready` deltaP `24.782` edge `2.2331` maxDD `-2.7051`
- `market_context_high->equity_24h` score `23.9102` n `47` status `ready` deltaP `27.2976` edge `1.8461` maxDD `-2.1786`
- `market_context_high->index_24h` score `7.8281` n `47` status `ready` deltaP `34.9364` edge `0.4324` maxDD `-0.3705`
- `news_risk_high->crypto_alt_24h` score `7.2369` n `100` status `ready` deltaP `0.9097` edge `1.2983` maxDD `-49.7699`
- `news_risk_high->crypto_major_24h` score `6.4829` n `100` status `ready` deltaP `3.2847` edge `1.7135` maxDD `-63.6743`
- `market_context_high->metal_24h` score `3.5291` n `47` status `ready` deltaP `30.5445` edge `0.1143` maxDD `-0.2401`
- `market_context_high->index_4h` score `3.0712` n `47` status `ready` deltaP `34.941` edge `0.0384` maxDD `-0.2323`
- `news_risk_high->crypto_alt_1h` score `2.6787` n `120` status `ready` deltaP `12.8344` edge `0.1867` maxDD `-1.5895`
- `market_context_high->equity_4h` score `2.6527` n `47` status `ready` deltaP `17.7542` edge `0.1445` maxDD `-1.3444`
- `news_risk_high->crypto_major_1h` score `2.1939` n `120` status `ready` deltaP `15.0799` edge `0.1258` maxDD `-1.8141`
- `news_risk_high->fx_4h` score `1.8516` n `111` status `ready` deltaP `26.534` edge `0.041` maxDD `-0.421`
- `news_risk_high->fx_24h` score `1.316` n `100` status `ready` deltaP `30.4097` edge `0.1291` maxDD `-1.7159`
- `news_risk_high->commodity_24h` score `1.1808` n `100` status `ready` deltaP `16.7986` edge `0.1043` maxDD `-2.431`
- `news_risk_high->metal_24h` score `1.0965` n `100` status `ready` deltaP `24.0764` edge `0.1249` maxDD `-7.2536`
- `market_context_high->index_1h` score `0.9763` n `47` status `ready` deltaP `14.7598` edge `0.0108` maxDD `-0.2275`
- `market_context_high->equity_1h` score `0.9163` n `47` status `ready` deltaP `11.0173` edge `0.0432` maxDD `-1.5564`
- `news_risk_high->metal_1h` score `0.4762` n `120` status `ready` deltaP `15.2595` edge `0.017` maxDD `-0.6142`
- `news_risk_high->crypto_major_4h` score `0.465` n `111` status `ready` deltaP `12.5797` edge `0.1889` maxDD `-13.719`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
