# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-02T14:22:27.868427+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11512`

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

- `risk_on_high->unknown_4h` score `7.1248` n `107` status `ready` deltaP `17.0191` edge `0.5421` maxDD `-2.2797`
- `risk_on_and_context->unknown_4h` score `7.1248` n `107` status `ready` deltaP `17.0191` edge `0.5421` maxDD `-2.2797`
- `risk_on_high->equity_24h` score `5.3762` n `107` status `ready` deltaP `25.2645` edge `0.6941` maxDD `-19.828`
- `risk_on_and_context->equity_24h` score `5.3762` n `107` status `ready` deltaP `25.2645` edge `0.6941` maxDD `-19.828`
- `market_context_high->unknown_4h` score `5.2054` n `147` status `ready` deltaP `12.7531` edge `0.4183` maxDD `-2.563`
- `news_risk_high->equity_24h` score `2.3763` n `59` status `ready` deltaP `11.2141` edge `0.37` maxDD `-15.4056`
- `market_context_high->equity_24h` score `1.8399` n `147` status `ready` deltaP `21.2337` edge `0.5752` maxDD `-24.4698`
- `risk_on_high->unknown_1h` score `1.7013` n `107` status `ready` deltaP `2.773` edge `0.181` maxDD `-1.95`
- `risk_on_and_context->unknown_1h` score `1.7013` n `107` status `ready` deltaP `2.773` edge `0.181` maxDD `-1.95`
- `news_risk_high->unknown_1h` score `0.9904` n `65` status `ready` deltaP `2.2985` edge `0.1019` maxDD `-1.1086`
- `market_context_high->unknown_1h` score `0.3714` n `147` status `ready` deltaP `1.1264` edge `0.0865` maxDD `-2.0446`
- `news_risk_high->fx_4h` score `0.3148` n `59` status `ready` deltaP `11.8593` edge `0.0065` maxDD `-0.7461`
- `risk_on_high->crypto_alt_24h` score `0.1914` n `107` status `ready` deltaP `15.1804` edge `0.6137` maxDD `-42.8959`
- `risk_on_and_context->crypto_alt_24h` score `0.1914` n `107` status `ready` deltaP `15.1804` edge `0.6137` maxDD `-42.8959`
- `news_risk_high->crypto_alt_24h` score `0.1624` n `59` status `ready` deltaP `15.1012` edge `0.2136` maxDD `-19.4761`
- `risk_on_high->index_4h` score `0.1351` n `107` status `ready` deltaP `21.0879` edge `0.0098` maxDD `-3.6448`
- `risk_on_and_context->index_4h` score `0.1351` n `107` status `ready` deltaP `21.0879` edge `0.0098` maxDD `-3.6448`
- `risk_on_high->index_1h` score `0.0932` n `107` status `ready` deltaP `7.9439` edge `0.0035` maxDD `-0.5605`
- `risk_on_and_context->index_1h` score `0.0932` n `107` status `ready` deltaP `7.9439` edge `0.0035` maxDD `-0.5605`
- `risk_on_high->metal_1h` score `-0.0419` n `107` status `ready` deltaP `9.9992` edge `-0.0008` maxDD `-1.699`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
