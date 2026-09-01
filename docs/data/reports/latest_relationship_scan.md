# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-01T17:37:29.466945+00:00`
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

- `risk_on_high->unknown_4h` score `7.2805` n `107` status `ready` deltaP `20.2203` edge `0.5337` maxDD `-2.2768`
- `risk_on_and_context->unknown_4h` score `7.2805` n `107` status `ready` deltaP `20.2203` edge `0.5337` maxDD `-2.2768`
- `market_context_high->unknown_4h` score `5.8271` n `151` status `ready` deltaP `16.5129` edge `0.445` maxDD `-2.5597`
- `risk_on_high->unknown_1h` score `2.0687` n `107` status `ready` deltaP `4.27` edge `0.2016` maxDD `-1.9475`
- `risk_on_and_context->unknown_1h` score `2.0687` n `107` status `ready` deltaP `4.27` edge `0.2016` maxDD `-1.9475`
- `market_context_high->unknown_1h` score `1.9379` n `151` status `ready` deltaP `3.6325` edge `0.2003` maxDD `-2.042`
- `news_risk_high->unknown_1h` score `1.3584` n `59` status `ready` deltaP `1.7355` edge `0.1363` maxDD `-1.1072`
- `news_risk_high->fx_4h` score `0.1769` n `59` status `ready` deltaP `10.9446` edge `0.0011` maxDD `-0.7461`
- `risk_on_high->commodity_24h` score `0.175` n `107` status `ready` deltaP `6.5226` edge `0.0699` maxDD `-0.5706`
- `risk_on_and_context->commodity_24h` score `0.175` n `107` status `ready` deltaP `6.5226` edge `0.0699` maxDD `-0.5706`
- `risk_on_high->index_1h` score `0.08` n `107` status `ready` deltaP `7.7942` edge `0.0028` maxDD `-0.5605`
- `risk_on_and_context->index_1h` score `0.08` n `107` status `ready` deltaP `7.7942` edge `0.0028` maxDD `-0.5605`
- `risk_on_high->metal_1h` score `0.0289` n `107` status `ready` deltaP `11.0471` edge `0.0013` maxDD `-1.699`
- `risk_on_and_context->metal_1h` score `0.0289` n `107` status `ready` deltaP `11.0471` edge `0.0013` maxDD `-1.699`
- `market_context_high->commodity_1h` score `-0.0637` n `151` status `ready` deltaP `7.5247` edge `0.0095` maxDD `-1.5315`
- `news_risk_high->commodity_4h` score `-0.0676` n `59` status `ready` deltaP `2.7671` edge `0.0088` maxDD `-0.8733`
- `news_risk_high->commodity_24h` score `-0.0732` n `59` status `ready` deltaP `3.3545` edge `-0.0092` maxDD `-0.2074`
- `risk_on_high->index_4h` score `-0.0884` n `107` status `ready` deltaP `17.7342` edge `0.0035` maxDD `-3.6448`
- `risk_on_and_context->index_4h` score `-0.0884` n `107` status `ready` deltaP `17.7342` edge `0.0035` maxDD `-3.6448`
- `risk_on_high->commodity_1h` score `-0.1147` n `107` status `ready` deltaP `4.4239` edge `0.008` maxDD `-0.8428`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
