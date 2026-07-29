# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-29T03:22:39.995875+00:00`
- Price records: `672`
- Market context records: `8262`
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

- `news_risk_high->unknown_24h` score `7519.6622` n `45` status `ready` deltaP `39.0625` edge `626.3781` maxDD `0.0`
- `news_risk_high->equity_4h` score `7.0991` n `54` status `ready` deltaP `26.3832` edge `0.4754` maxDD `-3.4427`
- `news_risk_high->equity_1h` score `3.1901` n `54` status `ready` deltaP `22.4274` edge `0.1472` maxDD `-1.1366`
- `news_risk_high->index_4h` score `2.7055` n `54` status `ready` deltaP `22.8771` edge `0.092` maxDD `-0.191`
- `news_risk_high->crypto_major_4h` score `2.1988` n `54` status `ready` deltaP `10.6313` edge `0.2804` maxDD `-2.8833`
- `news_risk_high->crypto_alt_1h` score `1.8794` n `54` status `ready` deltaP `15.0033` edge `0.1` maxDD `-1.1388`
- `news_risk_high->crypto_major_1h` score `1.6629` n `54` status `ready` deltaP `10.906` edge `0.1056` maxDD `-1.1783`
- `news_risk_high->crypto_alt_4h` score `1.3403` n `54` status `ready` deltaP `16.6215` edge `0.2002` maxDD `-5.8012`
- `news_risk_high->metal_4h` score `1.1496` n `54` status `ready` deltaP `10.3489` edge `0.0736` maxDD `-0.7433`
- `news_risk_high->index_1h` score `0.5322` n `54` status `ready` deltaP `7.5017` edge `0.0232` maxDD `-0.3089`
- `news_risk_high->fx_1h` score `0.2156` n `54` status `ready` deltaP `7.8953` edge `0.0031` maxDD `-0.2475`
- `news_risk_high->metal_1h` score `-0.0473` n `54` status `ready` deltaP `3.554` edge `0.0127` maxDD `-0.5599`
- `news_risk_high->fx_4h` score `-0.4151` n `54` status `ready` deltaP `5.3748` edge `0.0067` maxDD `-0.6604`
- `news_risk_high->commodity_1h` score `-2.1707` n `54` status `ready` deltaP `-8.9599` edge `-0.0426` maxDD `-2.9516`
- `news_risk_high->fx_24h` score `-4.2471` n `45` status `ready` deltaP `-19.0625` edge `-0.0442` maxDD `-4.2782`
- `news_risk_high->metal_24h` score `-5.7033` n `45` status `ready` deltaP `-20.3473` edge `-0.0778` maxDD `-10.2796`
- `news_risk_high->commodity_4h` score `-9.0609` n `54` status `ready` deltaP `-32.9438` edge `-0.2047` maxDD `-13.1269`
- `news_risk_high->index_24h` score `-11.8459` n `45` status `ready` deltaP `-24.8264` edge `-0.3451` maxDD `-25.1241`
- `news_risk_high->commodity_24h` score `-13.228` n `45` status `ready` deltaP `-15.0347` edge `-0.419` maxDD `-32.9813`
- `news_risk_high->equity_24h` score `-34.5525` n `45` status `ready` deltaP `-23.9583` edge `-1.1787` maxDD `-110.2762`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
