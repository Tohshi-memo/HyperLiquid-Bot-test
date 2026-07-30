# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-30T11:37:25.092947+00:00`
- Price records: `672`
- Market context records: `8405`
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

- `news_risk_high->unknown_24h` score `6252.6999` n `52` status `ready` deltaP `38.8355` edge `520.8415` maxDD `-2.0332`
- `news_risk_high->equity_4h` score `7.0514` n `52` status `ready` deltaP `25.4573` edge `0.4776` maxDD `-3.4427`
- `news_risk_high->equity_1h` score `2.7877` n `52` status `ready` deltaP `20.532` edge `0.1263` maxDD `-1.1366`
- `news_risk_high->index_4h` score `2.5139` n `52` status `ready` deltaP `21.0366` edge `0.0883` maxDD `-0.191`
- `news_risk_high->crypto_major_4h` score `1.7449` n `52` status `ready` deltaP `7.6923` edge `0.2418` maxDD `-2.8833`
- `news_risk_high->crypto_alt_1h` score `1.6879` n `52` status `ready` deltaP `12.9088` edge `0.098` maxDD `-1.1388`
- `news_risk_high->crypto_major_1h` score `1.6194` n `52` status `ready` deltaP `11.4118` edge `0.0986` maxDD `-1.1783`
- `news_risk_high->crypto_alt_4h` score `1.3443` n `52` status `ready` deltaP `16.2641` edge `0.2031` maxDD `-5.8012`
- `news_risk_high->metal_4h` score `0.4785` n `52` status `ready` deltaP `5.4995` edge `0.05` maxDD `-0.7433`
- `news_risk_high->index_1h` score `0.2109` n `52` status `ready` deltaP `4.2953` edge `0.0178` maxDD `-0.3089`
- `news_risk_high->fx_1h` score `0.0977` n `52` status `ready` deltaP `5.6426` edge `0.003` maxDD `-0.2475`
- `news_risk_high->metal_1h` score `-0.2935` n `52` status `ready` deltaP `1.6007` edge `0.0052` maxDD `-0.5599`
- `news_risk_high->fx_4h` score `-0.4834` n `52` status `ready` deltaP `4.1979` edge `0.0058` maxDD `-0.6604`
- `news_risk_high->commodity_1h` score `-1.9716` n `52` status `ready` deltaP `-6.7711` edge `-0.0406` maxDD `-2.9516`
- `news_risk_high->fx_24h` score `-5.7589` n `52` status `ready` deltaP `-27.7244` edge `-0.0629` maxDD `-5.2413`
- `news_risk_high->metal_24h` score `-8.1187` n `52` status `ready` deltaP `-31.7575` edge `-0.1878` maxDD `-10.8302`
- `news_risk_high->commodity_4h` score `-8.5328` n `52` status `ready` deltaP `-27.1224` edge `-0.1995` maxDD `-13.1269`
- `news_risk_high->index_24h` score `-12.3335` n `52` status `ready` deltaP `-25.2938` edge `-0.3089` maxDD `-28.0214`
- `news_risk_high->commodity_24h` score `-12.3602` n `52` status `ready` deltaP `-11.3915` edge `-0.3601` maxDD `-33.8515`
- `news_risk_high->equity_24h` score `-34.5551` n `52` status `ready` deltaP `-23.2105` edge `-0.9373` maxDD `-127.0042`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
