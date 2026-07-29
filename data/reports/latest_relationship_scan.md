# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-29T02:22:33.043095+00:00`
- Price records: `672`
- Market context records: `8258`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `5924`

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

- `news_risk_high->unknown_24h` score `7957.8638` n `43` status `ready` deltaP `39.0625` edge `662.8949` maxDD `0.0`
- `news_risk_high->equity_4h` score `7.1663` n `54` status `ready` deltaP `26.3832` edge `0.481` maxDD `-3.4427`
- `news_risk_high->equity_1h` score `3.1925` n `54` status `ready` deltaP `22.4274` edge `0.1474` maxDD `-1.1366`
- `news_risk_high->index_4h` score `2.7031` n `54` status `ready` deltaP `22.8771` edge `0.0918` maxDD `-0.191`
- `news_risk_high->crypto_major_4h` score `2.3015` n `54` status `ready` deltaP `11.241` edge `0.2895` maxDD `-2.8833`
- `news_risk_high->crypto_alt_1h` score `1.8711` n `54` status `ready` deltaP `14.8536` edge `0.1003` maxDD `-1.1388`
- `news_risk_high->crypto_major_1h` score `1.7396` n `54` status `ready` deltaP `11.5048` edge `0.108` maxDD `-1.1783`
- `news_risk_high->crypto_alt_4h` score `1.359` n `54` status `ready` deltaP `16.6215` edge `0.2026` maxDD `-5.8012`
- `news_risk_high->metal_4h` score `1.2128` n `54` status `ready` deltaP `10.9587` edge `0.0748` maxDD `-0.7433`
- `news_risk_high->index_1h` score `0.5238` n `54` status `ready` deltaP `7.5017` edge `0.0225` maxDD `-0.3089`
- `news_risk_high->fx_1h` score `0.1907` n `54` status `ready` deltaP `7.4462` edge `0.0029` maxDD `-0.2475`
- `news_risk_high->metal_1h` score `-0.0473` n `54` status `ready` deltaP `3.554` edge `0.0127` maxDD `-0.5599`
- `news_risk_high->fx_4h` score `-0.4318` n `54` status `ready` deltaP `5.07` edge `0.0066` maxDD `-0.6604`
- `news_risk_high->commodity_1h` score `-2.1624` n `54` status `ready` deltaP `-8.8102` edge `-0.0429` maxDD `-2.9516`
- `news_risk_high->fx_24h` score `-4.072` n `43` status `ready` deltaP `-18.6491` edge `-0.0434` maxDD `-4.0615`
- `news_risk_high->metal_24h` score `-5.5554` n `43` status `ready` deltaP `-19.2103` edge `-0.0834` maxDD `-10.1184`
- `news_risk_high->commodity_4h` score `-9.0877` n `54` status `ready` deltaP `-33.2487` edge `-0.2049` maxDD `-13.1269`
- `news_risk_high->index_24h` score `-11.6732` n `43` status `ready` deltaP `-24.3096` edge `-0.3529` maxDD `-24.2912`
- `news_risk_high->commodity_24h` score `-13.8833` n `43` status `ready` deltaP `-17.571` edge `-0.4567` maxDD `-32.9813`
- `news_risk_high->equity_24h` score `-33.9952` n `43` status `ready` deltaP `-23.4415` edge `-1.1977` maxDD `-105.9832`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
