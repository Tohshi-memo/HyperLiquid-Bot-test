# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-01T15:00:03.318288+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11475`

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

- `risk_on_high->unknown_4h` score `7.3437` n `107` status `ready` deltaP `20.83` edge `0.5349` maxDD `-2.2768`
- `risk_on_and_context->unknown_4h` score `7.3437` n `107` status `ready` deltaP `20.83` edge `0.5349` maxDD `-2.2768`
- `market_context_high->unknown_4h` score `5.8903` n `151` status `ready` deltaP `17.1226` edge `0.4462` maxDD `-2.5597`
- `risk_on_high->unknown_1h` score `2.0903` n `107` status `ready` deltaP `4.27` edge `0.2034` maxDD `-1.9475`
- `risk_on_and_context->unknown_1h` score `2.0903` n `107` status `ready` deltaP `4.27` edge `0.2034` maxDD `-1.9475`
- `market_context_high->unknown_1h` score `1.9595` n `151` status `ready` deltaP `3.6325` edge `0.2021` maxDD `-2.042`
- `news_risk_high->unknown_1h` score `1.38` n `59` status `ready` deltaP `1.7355` edge `0.1381` maxDD `-1.1072`
- `risk_on_high->commodity_24h` score `0.2134` n `107` status `ready` deltaP `6.5226` edge `0.0731` maxDD `-0.5706`
- `risk_on_and_context->commodity_24h` score `0.2134` n `107` status `ready` deltaP `6.5226` edge `0.0731` maxDD `-0.5706`
- `news_risk_high->fx_4h` score `0.1355` n `59` status `ready` deltaP `10.4873` edge `0.0007` maxDD `-0.7461`
- `risk_on_high->index_1h` score `0.0496` n `107` status `ready` deltaP `7.3451` edge `0.0019` maxDD `-0.5605`
- `risk_on_and_context->index_1h` score `0.0496` n `107` status `ready` deltaP `7.3451` edge `0.0019` maxDD `-0.5605`
- `market_context_high->commodity_1h` score `0.0142` n `151` status `ready` deltaP `8.1235` edge `0.012` maxDD `-1.5315`
- `news_risk_high->commodity_4h` score `-0.008` n `59` status `ready` deltaP `3.2244` edge `0.0134` maxDD `-0.8733`
- `risk_on_high->metal_1h` score `-0.0209` n `107` status `ready` deltaP `10.2986` edge `-0.0001` maxDD `-1.699`
- `risk_on_and_context->metal_1h` score `-0.0209` n `107` status `ready` deltaP `10.2986` edge `-0.0001` maxDD `-1.699`
- `news_risk_high->commodity_24h` score `-0.0348` n `59` status `ready` deltaP `3.3545` edge `-0.006` maxDD `-0.2074`
- `risk_on_high->commodity_1h` score `-0.0641` n `107` status `ready` deltaP `5.0227` edge `0.0105` maxDD `-0.8428`
- `risk_on_and_context->commodity_1h` score `-0.0641` n `107` status `ready` deltaP `5.0227` edge `0.0105` maxDD `-0.8428`
- `risk_on_high->index_4h` score `-0.1232` n `107` status `ready` deltaP `17.1245` edge `0.0031` maxDD `-3.6448`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
