# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-01T14:37:28.926234+00:00`
- Price records: `672`
- Market context records: `8631`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `5898`

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

- `news_risk_high->unknown_24h` score `5191.3482` n `60` status `ready` deltaP `34.2345` edge `432.4262` maxDD `-2.0332`
- `market_context_high->crypto_alt_24h` score `17.2078` n `49` status `ready` deltaP `53.8818` edge `1.1145` maxDD `-2.1786`
- `news_risk_high->equity_4h` score `6.2955` n `60` status `ready` deltaP `22.0833` edge `0.4371` maxDD `-3.4427`
- `news_risk_high->index_4h` score `2.5534` n `60` status `ready` deltaP `22.2357` edge `0.0836` maxDD `-0.191`
- `news_risk_high->equity_1h` score `1.7143` n `60` status `ready` deltaP `15.2296` edge `0.089` maxDD `-2.4803`
- `news_risk_high->crypto_major_4h` score `1.2352` n `60` status `ready` deltaP `7.7439` edge `0.1843` maxDD `-3.5385`
- `market_context_high->commodity_24h` score `1.0096` n `49` status `ready` deltaP `23.885` edge `0.1855` maxDD `-11.5569`
- `market_context_high->crypto_alt_4h` score `0.7` n `56` status `ready` deltaP `10.1481` edge `0.1178` maxDD `-5.323`
- `news_risk_high->crypto_alt_4h` score `0.4642` n `60` status `ready` deltaP `11.2195` edge `0.1239` maxDD `-5.8012`
- `news_risk_high->crypto_alt_1h` score `0.4343` n `60` status `ready` deltaP `8.1836` edge `0.0538` maxDD `-1.8813`
- `news_risk_high->crypto_major_1h` score `0.3318` n `60` status `ready` deltaP `6.2176` edge `0.0523` maxDD `-2.0972`
- `news_risk_high->fx_4h` score `0.329` n `60` status `ready` deltaP `14.7561` edge `0.0248` maxDD `-0.6604`
- `market_context_high->fx_24h` score `0.214` n `49` status `ready` deltaP `11.5835` edge `0.044` maxDD `-2.1692`
- `news_risk_high->metal_4h` score `0.1368` n `60` status `ready` deltaP `4.5223` edge `0.035` maxDD `-0.8085`
- `market_context_high->commodity_1h` score `0.1366` n `56` status `ready` deltaP `7.1535` edge `0.0178` maxDD `-1.3282`
- `news_risk_high->fx_1h` score `0.1102` n `60` status `ready` deltaP `5.5988` edge `0.0049` maxDD `-0.2475`
- `market_context_high->fx_4h` score `0.0978` n `56` status `ready` deltaP `11.5418` edge `0.0152` maxDD `-1.3685`
- `news_risk_high->metal_1h` score `0.0931` n `60` status `ready` deltaP `5.9381` edge `0.0085` maxDD `-0.5599`
- `news_risk_high->index_1h` score `0.0087` n `60` status `ready` deltaP `3.523` edge `0.0093` maxDD `-0.5338`
- `market_context_high->fx_1h` score `-0.2635` n `56` status `ready` deltaP `4.1702` edge `0.0005` maxDD `-0.6874`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
