# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-01T13:37:37.705984+00:00`
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

- `risk_on_high->unknown_4h` score `7.3171` n `107` status `ready` deltaP `20.6776` edge `0.5337` maxDD `-2.2768`
- `risk_on_and_context->unknown_4h` score `7.3171` n `107` status `ready` deltaP `20.6776` edge `0.5337` maxDD `-2.2768`
- `market_context_high->unknown_4h` score `5.8637` n `151` status `ready` deltaP `16.9702` edge `0.445` maxDD `-2.5597`
- `risk_on_high->unknown_1h` score `2.1371` n `107` status `ready` deltaP `4.4197` edge `0.2063` maxDD `-1.9475`
- `risk_on_and_context->unknown_1h` score `2.1371` n `107` status `ready` deltaP `4.4197` edge `0.2063` maxDD `-1.9475`
- `market_context_high->unknown_1h` score `2.0063` n `151` status `ready` deltaP `3.7822` edge `0.205` maxDD `-2.042`
- `news_risk_high->unknown_1h` score `1.4267` n `59` status `ready` deltaP `1.8852` edge `0.141` maxDD `-1.1072`
- `risk_on_high->commodity_24h` score `0.2736` n `107` status `ready` deltaP `6.8699` edge `0.0758` maxDD `-0.5706`
- `risk_on_and_context->commodity_24h` score `0.2736` n `107` status `ready` deltaP `6.8699` edge `0.0758` maxDD `-0.5706`
- `news_risk_high->fx_4h` score `0.1233` n `59` status `ready` deltaP `10.3349` edge `0.0007` maxDD `-0.7461`
- `risk_on_high->index_1h` score `0.0963` n `107` status `ready` deltaP `8.0936` edge `0.0029` maxDD `-0.5605`
- `risk_on_and_context->index_1h` score `0.0963` n `107` status `ready` deltaP `8.0936` edge `0.0029` maxDD `-0.5605`
- `news_risk_high->commodity_24h` score `0.0254` n `59` status `ready` deltaP `3.7018` edge `-0.0033` maxDD `-0.2074`
- `risk_on_high->metal_1h` score `-0.031` n `107` status `ready` deltaP `10.1489` edge `-0.0004` maxDD `-1.699`
- `risk_on_and_context->metal_1h` score `-0.031` n `107` status `ready` deltaP `10.1489` edge `-0.0004` maxDD `-1.699`
- `market_context_high->commodity_1h` score `-0.0433` n `151` status `ready` deltaP `7.5247` edge `0.0112` maxDD `-1.5315`
- `news_risk_high->commodity_4h` score `-0.0696` n `59` status `ready` deltaP `2.3098` edge `0.0116` maxDD `-0.8733`
- `risk_on_high->commodity_1h` score `-0.1015` n `107` status `ready` deltaP `4.4239` edge `0.0097` maxDD `-0.8428`
- `risk_on_and_context->commodity_1h` score `-0.1015` n `107` status `ready` deltaP `4.4239` edge `0.0097` maxDD `-0.8428`
- `risk_on_high->index_4h` score `-0.1035` n `107` status `ready` deltaP `17.4294` edge `0.0036` maxDD `-3.6448`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
