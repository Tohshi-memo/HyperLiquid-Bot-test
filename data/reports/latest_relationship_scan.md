# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-01T08:52:26.464098+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11438`

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

- `risk_on_high->unknown_4h` score `7.2437` n `107` status `ready` deltaP `20.5252` edge `0.5286` maxDD `-2.2768`
- `risk_on_and_context->unknown_4h` score `7.2437` n `107` status `ready` deltaP `20.5252` edge `0.5286` maxDD `-2.2768`
- `market_context_high->unknown_4h` score `5.7903` n `151` status `ready` deltaP `16.8178` edge `0.4399` maxDD `-2.5597`
- `risk_on_high->unknown_1h` score `2.1526` n `107` status `ready` deltaP `4.5694` edge `0.2066` maxDD `-1.9475`
- `risk_on_and_context->unknown_1h` score `2.1526` n `107` status `ready` deltaP `4.5694` edge `0.2066` maxDD `-1.9475`
- `market_context_high->unknown_1h` score `2.0219` n `151` status `ready` deltaP `3.9319` edge `0.2053` maxDD `-2.042`
- `news_risk_high->unknown_1h` score `1.4247` n `60` status `ready` deltaP `2.6847` edge `0.1355` maxDD `-1.1072`
- `risk_on_high->commodity_24h` score `0.7775` n `107` status `ready` deltaP `10.1685` edge `0.0958` maxDD `-0.5706`
- `risk_on_and_context->commodity_24h` score `0.7775` n `107` status `ready` deltaP `10.1685` edge `0.0958` maxDD `-0.5706`
- `news_risk_high->fx_4h` score `0.2317` n `60` status `ready` deltaP `11.5549` edge `0.0016` maxDD `-0.7461`
- `market_context_high->commodity_24h` score `0.1815` n `151` status `ready` deltaP `9.5371` edge `0.0711` maxDD `-1.2314`
- `news_risk_high->commodity_24h` score `0.1286` n `57` status `ready` deltaP `4.4134` edge `0.0033` maxDD `-0.4274`
- `news_risk_high->commodity_4h` score `0.0397` n `60` status `ready` deltaP `3.75` edge `0.016` maxDD `-0.8733`
- `risk_on_high->index_1h` score `0.0379` n `107` status `ready` deltaP `7.1954` edge `0.0014` maxDD `-0.5605`
- `risk_on_and_context->index_1h` score `0.0379` n `107` status `ready` deltaP `7.1954` edge `0.0014` maxDD `-0.5605`
- `market_context_high->commodity_1h` score `-0.0193` n `151` status `ready` deltaP `7.5247` edge `0.0132` maxDD `-1.5315`
- `risk_on_high->metal_1h` score `-0.0544` n `107` status `ready` deltaP `9.8495` edge `-0.0014` maxDD `-1.699`
- `risk_on_and_context->metal_1h` score `-0.0544` n `107` status `ready` deltaP `9.8495` edge `-0.0014` maxDD `-1.699`
- `risk_on_high->commodity_1h` score `-0.0859` n `107` status `ready` deltaP `4.4239` edge `0.0117` maxDD `-0.8428`
- `risk_on_and_context->commodity_1h` score `-0.0859` n `107` status `ready` deltaP `4.4239` edge `0.0117` maxDD `-0.8428`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
