# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-29T03:37:36.231789+00:00`
- Price records: `672`
- Market context records: `5106`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `10340`

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

- `market_context_high->unknown_24h` score `19.4299` n `78` status `ready` deltaP `28.1117` edge `1.466` maxDD `-1.4072`
- `market_context_high->unknown_4h` score `8.2217` n `112` status `ready` deltaP `22.9747` edge `0.6342` maxDD `-5.5109`
- `market_context_high->unknown_1h` score `6.3877` n `124` status `ready` deltaP `4.689` edge `0.5652` maxDD `-2.7986`
- `market_context_high->crypto_alt_4h` score `3.1886` n `112` status `ready` deltaP `14.8519` edge `0.4697` maxDD `-9.46`
- `market_context_high->crypto_major_4h` score `2.4568` n `112` status `ready` deltaP `13.2186` edge `0.4561` maxDD `-14.0065`
- `market_context_high->crypto_alt_1h` score `1.199` n `124` status `ready` deltaP `8.6054` edge `0.1387` maxDD `-5.0257`
- `market_context_high->crypto_major_1h` score `0.6571` n `124` status `ready` deltaP `9.4794` edge `0.1456` maxDD `-6.9639`
- `market_context_high->equity_1h` score `0.5298` n `124` status `ready` deltaP `9.4698` edge `0.0641` maxDD `-2.745`
- `market_context_high->metal_1h` score `0.4203` n `124` status `ready` deltaP `10.5515` edge `0.0332` maxDD `-1.3057`
- `market_context_high->equity_4h` score `0.4071` n `112` status `ready` deltaP `7.622` edge `0.1519` maxDD `-7.0418`
- `market_context_high->index_1h` score `-0.0414` n `124` status `ready` deltaP `4.9884` edge `0.0118` maxDD `-1.0296`
- `market_context_high->index_4h` score `-0.329` n `112` status `ready` deltaP `4.29` edge `0.026` maxDD `-2.7427`
- `market_context_high->metal_4h` score `-0.3825` n `112` status `ready` deltaP `3.8981` edge `0.066` maxDD `-4.6157`
- `market_context_high->fx_1h` score `-0.7684` n `124` status `ready` deltaP `-5.0126` edge `-0.001` maxDD `-0.7944`
- `market_context_high->commodity_1h` score `-0.8922` n `124` status `ready` deltaP `0.1835` edge `0.0002` maxDD `-2.062`
- `market_context_high->fx_4h` score `-1.1311` n `112` status `ready` deltaP `-5.3571` edge `-0.002` maxDD `-1.9169`
- `market_context_high->commodity_24h` score `-1.5113` n `78` status `ready` deltaP `8.3333` edge `0.0352` maxDD `-14.428`
- `market_context_high->fx_24h` score `-1.614` n `78` status `ready` deltaP `-3.8061` edge `-0.0085` maxDD `-1.7166`
- `market_context_high->commodity_4h` score `-2.1522` n `112` status `ready` deltaP `1.9817` edge `-0.0216` maxDD `-7.3435`
- `market_context_high->metal_24h` score `-4.4181` n `78` status `ready` deltaP `-6.3836` edge `0.0079` maxDD `-32.2084`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
