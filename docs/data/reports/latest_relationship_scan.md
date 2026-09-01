# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-01T10:22:25.251940+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11486`

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

- `risk_on_high->unknown_4h` score `7.2557` n `107` status `ready` deltaP `20.5252` edge `0.5296` maxDD `-2.2768`
- `risk_on_and_context->unknown_4h` score `7.2557` n `107` status `ready` deltaP `20.5252` edge `0.5296` maxDD `-2.2768`
- `market_context_high->unknown_4h` score `5.8023` n `151` status `ready` deltaP `16.8178` edge `0.4409` maxDD `-2.5597`
- `risk_on_high->unknown_1h` score `2.1706` n `107` status `ready` deltaP `4.5694` edge `0.2081` maxDD `-1.9475`
- `risk_on_and_context->unknown_1h` score `2.1706` n `107` status `ready` deltaP `4.5694` edge `0.2081` maxDD `-1.9475`
- `market_context_high->unknown_1h` score `2.0399` n `151` status `ready` deltaP `3.9319` edge `0.2068` maxDD `-2.042`
- `news_risk_high->unknown_1h` score `1.4427` n `60` status `ready` deltaP `2.6847` edge `0.137` maxDD `-1.1072`
- `risk_on_high->commodity_24h` score `0.5826` n `107` status `ready` deltaP `9.1268` edge `0.0865` maxDD `-0.5706`
- `risk_on_and_context->commodity_24h` score `0.5826` n `107` status `ready` deltaP `9.1268` edge `0.0865` maxDD `-0.5706`
- `news_risk_high->fx_4h` score `0.1635` n `60` status `ready` deltaP `10.7927` edge `0.001` maxDD `-0.7461`
- `risk_on_high->index_1h` score `0.0792` n `107` status `ready` deltaP `7.7942` edge `0.0027` maxDD `-0.5605`
- `risk_on_and_context->index_1h` score `0.0792` n `107` status `ready` deltaP `7.7942` edge `0.0027` maxDD `-0.5605`
- `news_risk_high->commodity_24h` score `0.0143` n `58` status `ready` deltaP `3.8254` edge `-0.0023` maxDD `-0.4274`
- `market_context_high->commodity_24h` score `-0.0135` n `151` status `ready` deltaP `8.4954` edge `0.0618` maxDD `-1.2314`
- `risk_on_high->metal_1h` score `-0.0209` n `107` status `ready` deltaP `10.2986` edge `-0.0001` maxDD `-1.699`
- `risk_on_and_context->metal_1h` score `-0.0209` n `107` status `ready` deltaP `10.2986` edge `-0.0001` maxDD `-1.699`
- `market_context_high->commodity_1h` score `-0.0409` n `151` status `ready` deltaP `7.5247` edge `0.0114` maxDD `-1.5315`
- `news_risk_high->commodity_4h` score `-0.043` n `60` status `ready` deltaP `2.8354` edge `0.0115` maxDD `-0.8733`
- `risk_on_high->commodity_1h` score `-0.0999` n `107` status `ready` deltaP `4.4239` edge `0.0099` maxDD `-0.8428`
- `risk_on_and_context->commodity_1h` score `-0.0999` n `107` status `ready` deltaP `4.4239` edge `0.0099` maxDD `-0.8428`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
