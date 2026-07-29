# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-29T12:37:36.152738+00:00`
- Price records: `672`
- Market context records: `8303`
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

- `news_risk_high->unknown_24h` score `5952.0962` n `54` status `ready` deltaP `35.4745` edge `495.8136` maxDD `-2.0332`
- `news_risk_high->equity_4h` score `6.8587` n `54` status `ready` deltaP `25.1637` edge `0.4635` maxDD `-3.4427`
- `news_risk_high->equity_1h` score `2.9011` n `54` status `ready` deltaP `20.9304` edge `0.1331` maxDD `-1.1366`
- `news_risk_high->index_4h` score `2.5708` n `54` status `ready` deltaP `21.6576` edge `0.0889` maxDD `-0.191`
- `news_risk_high->crypto_major_4h` score `2.0478` n `54` status `ready` deltaP `10.0215` edge `0.2651` maxDD `-2.8833`
- `news_risk_high->crypto_alt_1h` score `1.8927` n `54` status `ready` deltaP `14.8536` edge `0.1021` maxDD `-1.1388`
- `news_risk_high->crypto_alt_4h` score `1.6365` n `54` status `ready` deltaP `18.2984` edge `0.227` maxDD `-5.8012`
- `news_risk_high->crypto_major_1h` score `1.561` n `54` status `ready` deltaP `10.6066` edge `0.0991` maxDD `-1.1783`
- `news_risk_high->metal_4h` score `1.2152` n `54` status `ready` deltaP `10.9587` edge `0.075` maxDD `-0.7433`
- `news_risk_high->index_1h` score `0.3465` n `54` status `ready` deltaP `5.7053` edge `0.0197` maxDD `-0.3089`
- `news_risk_high->fx_1h` score `0.1673` n `54` status `ready` deltaP `6.9971` edge `0.0029` maxDD `-0.2475`
- `news_risk_high->metal_1h` score `-0.0209` n `54` status `ready` deltaP `3.8534` edge `0.0129` maxDD `-0.5599`
- `news_risk_high->fx_4h` score `-0.5221` n `54` status `ready` deltaP `3.3931` edge `0.0062` maxDD `-0.6604`
- `news_risk_high->commodity_1h` score `-2.1623` n `54` status `ready` deltaP `-8.9599` edge `-0.0419` maxDD `-2.9516`
- `news_risk_high->fx_24h` score `-5.0452` n `54` status `ready` deltaP `-20.544` edge `-0.0491` maxDD `-5.4165`
- `news_risk_high->metal_24h` score `-5.8621` n `54` status `ready` deltaP `-22.1644` edge `-0.0637` maxDD `-10.8302`
- `news_risk_high->commodity_4h` score `-8.8426` n `54` status `ready` deltaP `-31.1145` edge `-0.1987` maxDD `-13.1269`
- `news_risk_high->commodity_24h` score `-10.8266` n `54` status `ready` deltaP `-5.9606` edge `-0.2685` maxDD `-33.8515`
- `news_risk_high->index_24h` score `-11.874` n `54` status `ready` deltaP `-22.6851` edge `-0.288` maxDD `-28.0214`
- `news_risk_high->crypto_major_24h` score `-32.2877` n `54` status `ready` deltaP `-13.2523` edge `-1.1498` maxDD `-103.8662`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
