# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-01T10:52:26.514769+00:00`
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

- `risk_on_high->unknown_4h` score `7.2387` n `107` status `ready` deltaP `20.3727` edge `0.5292` maxDD `-2.2768`
- `risk_on_and_context->unknown_4h` score `7.2387` n `107` status `ready` deltaP `20.3727` edge `0.5292` maxDD `-2.2768`
- `market_context_high->unknown_4h` score `5.7853` n `151` status `ready` deltaP `16.6653` edge `0.4405` maxDD `-2.5597`
- `risk_on_high->unknown_1h` score `2.1491` n `107` status `ready` deltaP `4.4197` edge `0.2073` maxDD `-1.9475`
- `risk_on_and_context->unknown_1h` score `2.1491` n `107` status `ready` deltaP `4.4197` edge `0.2073` maxDD `-1.9475`
- `market_context_high->unknown_1h` score `2.0183` n `151` status `ready` deltaP `3.7822` edge `0.206` maxDD `-2.042`
- `news_risk_high->unknown_1h` score `1.4211` n `60` status `ready` deltaP `2.535` edge `0.1362` maxDD `-1.1072`
- `risk_on_high->commodity_24h` score `0.5332` n `107` status `ready` deltaP `8.7796` edge `0.0847` maxDD `-0.5706`
- `risk_on_and_context->commodity_24h` score `0.5332` n `107` status `ready` deltaP `8.7796` edge `0.0847` maxDD `-0.5706`
- `news_risk_high->fx_4h` score `0.1635` n `60` status `ready` deltaP `10.7927` edge `0.001` maxDD `-0.7461`
- `risk_on_high->index_1h` score `0.0784` n `107` status `ready` deltaP `7.7942` edge `0.0026` maxDD `-0.5605`
- `risk_on_and_context->index_1h` score `0.0784` n `107` status `ready` deltaP `7.7942` edge `0.0026` maxDD `-0.5605`
- `market_context_high->commodity_1h` score `-0.0134` n `151` status `ready` deltaP `7.8241` edge `0.0117` maxDD `-1.5315`
- `news_risk_high->commodity_24h` score `-0.0351` n `58` status `ready` deltaP `3.4782` edge `-0.0041` maxDD `-0.4274`
- `risk_on_high->metal_1h` score `-0.0388` n `107` status `ready` deltaP `9.9992` edge `-0.0004` maxDD `-1.699`
- `risk_on_and_context->metal_1h` score `-0.0388` n `107` status `ready` deltaP `9.9992` edge `-0.0004` maxDD `-1.699`
- `market_context_high->commodity_24h` score `-0.0629` n `151` status `ready` deltaP `8.1482` edge `0.06` maxDD `-1.2314`
- `news_risk_high->commodity_4h` score `-0.0651` n `60` status `ready` deltaP `2.5305` edge `0.0107` maxDD `-0.8733`
- `risk_on_high->commodity_1h` score `-0.082` n `107` status `ready` deltaP `4.7233` edge `0.0102` maxDD `-0.8428`
- `risk_on_and_context->commodity_1h` score `-0.082` n `107` status `ready` deltaP `4.7233` edge `0.0102` maxDD `-0.8428`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
