# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-20T18:22:29.736274+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9862`

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

- `news_risk_high->crypto_major_24h` score `23.4323` n `98` status `ready` deltaP `10.5336` edge `2.5683` maxDD `-46.1999`
- `news_risk_high->crypto_alt_24h` score `20.3403` n `98` status `ready` deltaP `15.0935` edge `2.0825` maxDD `-32.7147`
- `market_context_high->unknown_4h` score `16.765` n `43` status `ready` deltaP `-0.5743` edge `1.4159` maxDD `-0.5326`
- `news_risk_high->crypto_alt_4h` score `5.461` n `101` status `ready` deltaP `22.5776` edge `0.4255` maxDD `-7.675`
- `market_context_high->commodity_4h` score `4.4677` n `43` status `ready` deltaP `37.6099` edge `0.1349` maxDD `-0.0659`
- `news_risk_high->crypto_major_4h` score `4.2293` n `101` status `ready` deltaP `21.6629` edge `0.3338` maxDD `-8.0625`
- `market_context_high->commodity_24h` score `3.1794` n `32` status `ready` deltaP `18.0556` edge `0.1971` maxDD `-0.8682`
- `news_risk_high->crypto_alt_1h` score `2.9189` n `101` status `ready` deltaP `16.6805` edge `0.1786` maxDD `-2.058`
- `news_risk_high->crypto_major_1h` score `2.2115` n `101` status `ready` deltaP `18.7763` edge `0.1114` maxDD `-2.8494`
- `market_context_high->fx_4h` score `2.1453` n `43` status `ready` deltaP `27.9282` edge `0.0141` maxDD `-0.0543`
- `market_context_high->fx_24h` score `2.1204` n `32` status `ready` deltaP `21.1806` edge `0.0397` maxDD `-0.0027`
- `market_context_high->commodity_1h` score `1.3595` n `52` status `ready` deltaP `15.3616` edge `0.0384` maxDD `-0.2012`
- `news_risk_high->commodity_24h` score `1.0588` n `98` status `ready` deltaP `22.775` edge `0.1145` maxDD `-3.4467`
- `market_context_high->fx_1h` score `0.7436` n `52` status `ready` deltaP `10.8936` edge `0.0068` maxDD `-0.063`
- `news_risk_high->metal_1h` score `0.6425` n `101` status `ready` deltaP `14.7477` edge `0.0154` maxDD `-0.8144`
- `news_risk_high->metal_4h` score `0.6348` n `101` status `ready` deltaP `17.2512` edge `0.0433` maxDD `-2.0994`
- `news_risk_high->equity_24h` score `0.5614` n `98` status `ready` deltaP `16.3974` edge `0.0784` maxDD `-4.941`
- `news_risk_high->equity_1h` score `0.2472` n `101` status `ready` deltaP `5.5137` edge `0.0244` maxDD `-0.9112`
- `market_context_high->metal_1h` score `0.2469` n `52` status `ready` deltaP `7.0935` edge `0.0067` maxDD `-0.4538`
- `news_risk_high->metal_24h` score `0.1566` n `98` status `ready` deltaP `14.9837` edge `0.0046` maxDD `-2.4203`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
