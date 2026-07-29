# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-29T12:52:29.578946+00:00`
- Price records: `672`
- Market context records: `8304`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `5892`

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

- `news_risk_high->unknown_24h` score `5952.3074` n `54` status `ready` deltaP `35.4745` edge `495.8312` maxDD `-2.0332`
- `news_risk_high->equity_4h` score `6.8839` n `54` status `ready` deltaP `25.1637` edge `0.4656` maxDD `-3.4427`
- `news_risk_high->equity_1h` score `2.9155` n `54` status `ready` deltaP `21.0801` edge `0.1333` maxDD `-1.1366`
- `news_risk_high->index_4h` score `2.5889` n `54` status `ready` deltaP `21.81` edge `0.0894` maxDD `-0.191`
- `news_risk_high->crypto_major_4h` score `2.0666` n `54` status `ready` deltaP `10.1739` edge `0.2665` maxDD `-2.8833`
- `news_risk_high->crypto_alt_1h` score `1.8963` n `54` status `ready` deltaP `14.8536` edge `0.1024` maxDD `-1.1388`
- `news_risk_high->crypto_alt_4h` score `1.6553` n `54` status `ready` deltaP `18.4508` edge `0.2284` maxDD `-5.8012`
- `news_risk_high->crypto_major_1h` score `1.5646` n `54` status `ready` deltaP `10.6066` edge `0.0994` maxDD `-1.1783`
- `news_risk_high->metal_4h` score `1.2334` n `54` status `ready` deltaP `11.1111` edge `0.0755` maxDD `-0.7433`
- `news_risk_high->index_1h` score `0.3597` n `54` status `ready` deltaP `5.855` edge `0.0198` maxDD `-0.3089`
- `news_risk_high->fx_1h` score `0.1673` n `54` status `ready` deltaP `6.9971` edge `0.0029` maxDD `-0.2475`
- `news_risk_high->metal_1h` score `-0.0197` n `54` status `ready` deltaP `3.8534` edge `0.013` maxDD `-0.5599`
- `news_risk_high->fx_4h` score `-0.5221` n `54` status `ready` deltaP `3.3931` edge `0.0062` maxDD `-0.6604`
- `news_risk_high->commodity_1h` score `-2.1827` n `54` status `ready` deltaP `-9.1096` edge `-0.0426` maxDD `-2.9516`
- `news_risk_high->fx_24h` score `-5.0452` n `54` status `ready` deltaP `-20.544` edge `-0.0491` maxDD `-5.4165`
- `news_risk_high->metal_24h` score `-5.8681` n `54` status `ready` deltaP `-22.1644` edge `-0.0642` maxDD `-10.8302`
- `news_risk_high->commodity_4h` score `-8.868` n `54` status `ready` deltaP `-31.2669` edge `-0.1998` maxDD `-13.1269`
- `news_risk_high->commodity_24h` score `-10.823` n `54` status `ready` deltaP `-5.9606` edge `-0.2682` maxDD `-33.8515`
- `news_risk_high->index_24h` score `-11.8541` n `54` status `ready` deltaP `-22.5115` edge `-0.2875` maxDD `-28.0214`
- `news_risk_high->crypto_major_24h` score `-32.3033` n `54` status `ready` deltaP `-13.2523` edge `-1.1511` maxDD `-103.8662`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
