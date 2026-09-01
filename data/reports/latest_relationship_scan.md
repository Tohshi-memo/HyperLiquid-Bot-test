# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-01T11:22:26.306230+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11487`

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

- `risk_on_high->unknown_4h` score `7.2375` n `107` status `ready` deltaP `20.3727` edge `0.5291` maxDD `-2.2768`
- `risk_on_and_context->unknown_4h` score `7.2375` n `107` status `ready` deltaP `20.3727` edge `0.5291` maxDD `-2.2768`
- `market_context_high->unknown_4h` score `5.7841` n `151` status `ready` deltaP `16.6653` edge `0.4404` maxDD `-2.5597`
- `risk_on_high->unknown_1h` score `2.1622` n `107` status `ready` deltaP `4.5694` edge `0.2074` maxDD `-1.9475`
- `risk_on_and_context->unknown_1h` score `2.1622` n `107` status `ready` deltaP `4.5694` edge `0.2074` maxDD `-1.9475`
- `market_context_high->unknown_1h` score `2.0315` n `151` status `ready` deltaP `3.9319` edge `0.2061` maxDD `-2.042`
- `news_risk_high->unknown_1h` score `1.4343` n `60` status `ready` deltaP `2.6847` edge `0.1363` maxDD `-1.1072`
- `risk_on_high->commodity_24h` score `0.4814` n `107` status `ready` deltaP `8.4324` edge `0.0827` maxDD `-0.5706`
- `risk_on_and_context->commodity_24h` score `0.4814` n `107` status `ready` deltaP `8.4324` edge `0.0827` maxDD `-0.5706`
- `news_risk_high->fx_4h` score `0.1635` n `60` status `ready` deltaP `10.7927` edge `0.001` maxDD `-0.7461`
- `risk_on_high->index_1h` score `0.0784` n `107` status `ready` deltaP `7.7942` edge `0.0026` maxDD `-0.5605`
- `risk_on_and_context->index_1h` score `0.0784` n `107` status `ready` deltaP `7.7942` edge `0.0026` maxDD `-0.5605`
- `news_risk_high->commodity_24h` score `0.0061` n `60` status `ready` deltaP `3.9931` edge `-0.0041` maxDD `-0.4274`
- `market_context_high->commodity_1h` score `-0.011` n `151` status `ready` deltaP `7.8241` edge `0.0119` maxDD `-1.5315`
- `risk_on_high->metal_1h` score `-0.038` n `107` status `ready` deltaP `9.9992` edge `-0.0003` maxDD `-1.699`
- `risk_on_and_context->metal_1h` score `-0.038` n `107` status `ready` deltaP `9.9992` edge `-0.0003` maxDD `-1.699`
- `news_risk_high->commodity_4h` score `-0.0762` n `60` status `ready` deltaP `2.378` edge `0.0103` maxDD `-0.8733`
- `risk_on_high->commodity_1h` score `-0.0804` n `107` status `ready` deltaP `4.7233` edge `0.0104` maxDD `-0.8428`
- `risk_on_and_context->commodity_1h` score `-0.0804` n `107` status `ready` deltaP `4.7233` edge `0.0104` maxDD `-0.8428`
- `risk_on_high->index_4h` score `-0.112` n `107` status `ready` deltaP `17.4294` edge `0.0025` maxDD `-3.6448`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
