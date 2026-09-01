# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-01T16:22:29.036572+00:00`
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

- `risk_on_high->unknown_4h` score `7.2697` n `107` status `ready` deltaP `20.2203` edge `0.5328` maxDD `-2.2768`
- `risk_on_and_context->unknown_4h` score `7.2697` n `107` status `ready` deltaP `20.2203` edge `0.5328` maxDD `-2.2768`
- `market_context_high->unknown_4h` score `5.8163` n `151` status `ready` deltaP `16.5129` edge `0.4441` maxDD `-2.5597`
- `risk_on_high->unknown_1h` score `2.0975` n `107` status `ready` deltaP `4.4197` edge `0.203` maxDD `-1.9475`
- `risk_on_and_context->unknown_1h` score `2.0975` n `107` status `ready` deltaP `4.4197` edge `0.203` maxDD `-1.9475`
- `market_context_high->unknown_1h` score `1.9667` n `151` status `ready` deltaP `3.7822` edge `0.2017` maxDD `-2.042`
- `news_risk_high->unknown_1h` score `1.3871` n `59` status `ready` deltaP `1.8852` edge `0.1377` maxDD `-1.1072`
- `risk_on_high->commodity_24h` score `0.1966` n `107` status `ready` deltaP `6.5226` edge `0.0717` maxDD `-0.5706`
- `risk_on_and_context->commodity_24h` score `0.1966` n `107` status `ready` deltaP `6.5226` edge `0.0717` maxDD `-0.5706`
- `news_risk_high->fx_4h` score `0.1501` n `59` status `ready` deltaP `10.6397` edge `0.0009` maxDD `-0.7461`
- `risk_on_high->index_1h` score `0.0675` n `107` status `ready` deltaP `7.6445` edge `0.0022` maxDD `-0.5605`
- `risk_on_and_context->index_1h` score `0.0675` n `107` status `ready` deltaP `7.6445` edge `0.0022` maxDD `-0.5605`
- `risk_on_high->metal_1h` score `0.0079` n `107` status `ready` deltaP `10.7477` edge `0.0006` maxDD `-1.699`
- `risk_on_and_context->metal_1h` score `0.0079` n `107` status `ready` deltaP `10.7477` edge `0.0006` maxDD `-1.699`
- `news_risk_high->commodity_4h` score `-0.0134` n `59` status `ready` deltaP `3.2244` edge `0.0127` maxDD `-0.8733`
- `news_risk_high->commodity_24h` score `-0.0516` n `59` status `ready` deltaP `3.3545` edge `-0.0074` maxDD `-0.2074`
- `market_context_high->commodity_1h` score `-0.0517` n `151` status `ready` deltaP `7.5247` edge `0.0105` maxDD `-1.5315`
- `risk_on_high->commodity_1h` score `-0.1069` n `107` status `ready` deltaP `4.4239` edge `0.009` maxDD `-0.8428`
- `risk_on_and_context->commodity_1h` score `-0.1069` n `107` status `ready` deltaP `4.4239` edge `0.009` maxDD `-0.8428`
- `risk_on_high->index_4h` score `-0.1232` n `107` status `ready` deltaP `17.1245` edge `0.0031` maxDD `-3.6448`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
