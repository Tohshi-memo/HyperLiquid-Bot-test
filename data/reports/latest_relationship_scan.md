# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-20T18:07:30.093247+00:00`
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

- `news_risk_high->crypto_major_24h` score `23.3584` n `98` status `ready` deltaP `10.36` edge `2.5633` maxDD `-46.1999`
- `news_risk_high->crypto_alt_24h` score `20.3415` n `98` status `ready` deltaP `15.0935` edge `2.0826` maxDD `-32.7147`
- `market_context_high->unknown_4h` score `16.7284` n `44` status `ready` deltaP `-0.4158` edge `1.4118` maxDD `-0.5326`
- `news_risk_high->crypto_alt_4h` score `5.5608` n `101` status `ready` deltaP `22.73` edge `0.4328` maxDD `-7.675`
- `market_context_high->commodity_4h` score `4.5391` n `44` status `ready` deltaP `37.7218` edge `0.1401` maxDD `-0.0659`
- `news_risk_high->crypto_major_4h` score `4.2943` n `101` status `ready` deltaP `21.8154` edge `0.3382` maxDD `-8.0625`
- `market_context_high->commodity_24h` score `3.2936` n `33` status `ready` deltaP `19.0026` edge `0.2003` maxDD `-0.8682`
- `news_risk_high->crypto_alt_1h` score `2.9381` n `101` status `ready` deltaP `16.8302` edge `0.1792` maxDD `-2.058`
- `news_risk_high->crypto_major_1h` score `2.2283` n `101` status `ready` deltaP `18.926` edge `0.1118` maxDD `-2.8494`
- `market_context_high->fx_4h` score `2.1785` n `44` status `ready` deltaP `28.2982` edge `0.0144` maxDD `-0.0543`
- `market_context_high->fx_24h` score `2.0925` n `33` status `ready` deltaP `21.1016` edge `0.0379` maxDD `-0.0027`
- `market_context_high->commodity_1h` score `1.5158` n `52` status `ready` deltaP `17.135` edge `0.0396` maxDD `-0.2012`
- `news_risk_high->commodity_24h` score `1.0596` n `98` status `ready` deltaP `22.775` edge `0.1146` maxDD `-3.4467`
- `market_context_high->fx_1h` score `0.8891` n `52` status `ready` deltaP `12.667` edge `0.0071` maxDD `-0.063`
- `news_risk_high->metal_1h` score `0.6413` n `101` status `ready` deltaP `14.7477` edge `0.0153` maxDD `-0.8144`
- `news_risk_high->metal_4h` score `0.6372` n `101` status `ready` deltaP `17.2512` edge `0.0435` maxDD `-2.0994`
- `news_risk_high->equity_24h` score `0.565` n `98` status `ready` deltaP `16.3974` edge `0.0787` maxDD `-4.941`
- `news_risk_high->equity_1h` score `0.2472` n `101` status `ready` deltaP `5.5137` edge `0.0244` maxDD `-0.9112`
- `market_context_high->metal_1h` score `0.2466` n `52` status `ready` deltaP `7.0935` edge `0.0067` maxDD `-0.4568`
- `news_risk_high->metal_24h` score `0.1605` n `98` status `ready` deltaP `14.9837` edge `0.0051` maxDD `-2.4203`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
