# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-30T11:52:23.660606+00:00`
- Price records: `672`
- Market context records: `8406`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `5742`

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

- `news_risk_high->unknown_24h` score `6252.7221` n `52` status `ready` deltaP `39.0091` edge `520.8422` maxDD `-2.0332`
- `news_risk_high->equity_4h` score `6.9696` n `52` status `ready` deltaP `25.3049` edge `0.4718` maxDD `-3.4427`
- `news_risk_high->equity_1h` score `2.7553` n `52` status `ready` deltaP `20.3823` edge `0.1246` maxDD `-1.1366`
- `news_risk_high->index_4h` score `2.4885` n `52` status `ready` deltaP `20.8841` edge `0.0872` maxDD `-0.191`
- `news_risk_high->crypto_major_4h` score `1.712` n `52` status `ready` deltaP `7.5399` edge `0.2386` maxDD `-2.8833`
- `news_risk_high->crypto_alt_1h` score `1.6855` n `52` status `ready` deltaP `12.9088` edge `0.0978` maxDD `-1.1388`
- `news_risk_high->crypto_major_1h` score `1.6026` n `52` status `ready` deltaP `11.2621` edge `0.0982` maxDD `-1.1783`
- `news_risk_high->crypto_alt_4h` score `1.3255` n `52` status `ready` deltaP `16.1117` edge `0.2017` maxDD `-5.8012`
- `news_risk_high->metal_4h` score `0.4531` n `52` status `ready` deltaP `5.3471` edge `0.0489` maxDD `-0.7433`
- `news_risk_high->index_1h` score `0.1965` n `52` status `ready` deltaP `4.1456` edge `0.0176` maxDD `-0.3089`
- `news_risk_high->fx_1h` score `0.1062` n `52` status `ready` deltaP `5.7923` edge `0.0031` maxDD `-0.2475`
- `news_risk_high->metal_1h` score `-0.3067` n `52` status `ready` deltaP `1.451` edge `0.0051` maxDD `-0.5599`
- `news_risk_high->fx_4h` score `-0.4834` n `52` status `ready` deltaP `4.1979` edge `0.0058` maxDD `-0.6604`
- `news_risk_high->commodity_1h` score `-1.9716` n `52` status `ready` deltaP `-6.7711` edge `-0.0406` maxDD `-2.9516`
- `news_risk_high->fx_24h` score `-5.7613` n `52` status `ready` deltaP `-27.7244` edge `-0.0631` maxDD `-5.2413`
- `news_risk_high->metal_24h` score `-8.147` n `52` status `ready` deltaP `-31.9311` edge `-0.189` maxDD `-10.8302`
- `news_risk_high->commodity_4h` score `-8.511` n `52` status `ready` deltaP `-26.97` edge `-0.1987` maxDD `-13.1269`
- `news_risk_high->index_24h` score `-12.3371` n `52` status `ready` deltaP `-25.2938` edge `-0.3092` maxDD `-28.0214`
- `news_risk_high->commodity_24h` score `-12.3861` n `52` status `ready` deltaP `-11.5652` edge `-0.3611` maxDD `-33.8515`
- `news_risk_high->equity_24h` score `-34.5527` n `52` status `ready` deltaP `-23.2105` edge `-0.9371` maxDD `-127.0042`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
