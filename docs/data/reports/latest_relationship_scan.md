# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-01T15:22:33.561987+00:00`
- Price records: `672`
- Market context records: `8635`
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

- `news_risk_high->unknown_24h` score `5191.1046` n `60` status `ready` deltaP `34.2345` edge `432.4059` maxDD `-2.0332`
- `market_context_high->crypto_alt_24h` score `17.3174` n `52` status `ready` deltaP `54.3528` edge `1.1205` maxDD `-2.1786`
- `news_risk_high->equity_4h` score `6.35` n `60` status `ready` deltaP `22.5406` edge `0.4386` maxDD `-3.4427`
- `news_risk_high->index_4h` score `2.5948` n `60` status `ready` deltaP `22.6931` edge `0.084` maxDD `-0.191`
- `news_risk_high->equity_1h` score `1.7275` n `60` status `ready` deltaP `15.3793` edge `0.0891` maxDD `-2.4803`
- `news_risk_high->crypto_major_4h` score `1.268` n `60` status `ready` deltaP `7.7439` edge `0.1885` maxDD `-3.5385`
- `market_context_high->commodity_24h` score `1.1639` n `52` status `ready` deltaP `25.3666` edge `0.1954` maxDD `-11.5569`
- `market_context_high->crypto_alt_4h` score `0.7195` n `56` status `ready` deltaP `10.1481` edge `0.1203` maxDD `-5.323`
- `news_risk_high->crypto_alt_4h` score `0.4837` n `60` status `ready` deltaP `11.2195` edge `0.1264` maxDD `-5.8012`
- `news_risk_high->crypto_alt_1h` score `0.4615` n `60` status `ready` deltaP `8.483` edge `0.0553` maxDD `-1.8813`
- `news_risk_high->crypto_major_1h` score `0.352` n `60` status `ready` deltaP `6.3673` edge `0.0539` maxDD `-2.0972`
- `news_risk_high->fx_4h` score `0.3168` n `60` status `ready` deltaP `14.6037` edge `0.0248` maxDD `-0.6604`
- `news_risk_high->metal_4h` score `0.1448` n `60` status `ready` deltaP `4.6748` edge `0.035` maxDD `-0.8085`
- `market_context_high->commodity_1h` score `0.1235` n `56` status `ready` deltaP `7.0038` edge `0.0177` maxDD `-1.3282`
- `news_risk_high->fx_1h` score `0.118` n `60` status `ready` deltaP `5.7485` edge `0.0049` maxDD `-0.2475`
- `news_risk_high->metal_1h` score `0.105` n `60` status `ready` deltaP `6.0878` edge `0.0085` maxDD `-0.5599`
- `market_context_high->fx_4h` score `0.0899` n `56` status `ready` deltaP `11.3894` edge `0.0152` maxDD `-1.3685`
- `market_context_high->fx_24h` score `0.0862` n `52` status `ready` deltaP `9.3954` edge `0.0428` maxDD `-2.2172`
- `news_risk_high->index_1h` score `-0.0069` n `60` status `ready` deltaP `3.2236` edge `0.0093` maxDD `-0.5338`
- `market_context_high->fx_1h` score `-0.2515` n `56` status `ready` deltaP `4.3199` edge `0.0005` maxDD `-0.6874`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
