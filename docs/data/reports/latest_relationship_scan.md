# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-31T02:07:27.791687+00:00`
- Price records: `672`
- Market context records: `8470`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `5828`

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

- `news_risk_high->unknown_24h` score `6265.6409` n `52` status `ready` deltaP `44.0438` edge `521.8852` maxDD `-2.0332`
- `news_risk_high->equity_4h` score `6.373` n `61` status `ready` deltaP `23.3531` edge `0.4351` maxDD `-3.4427`
- `news_risk_high->equity_1h` score `2.5639` n `62` status `ready` deltaP `19.07` edge `0.1174` maxDD `-1.1366`
- `news_risk_high->index_4h` score `2.2905` n `61` status `ready` deltaP `19.0848` edge `0.0827` maxDD `-0.191`
- `news_risk_high->crypto_alt_1h` score `1.4302` n `62` status `ready` deltaP `11.7732` edge `0.0841` maxDD `-1.1388`
- `news_risk_high->crypto_alt_4h` score `1.2223` n `61` status `ready` deltaP `16.1836` edge `0.188` maxDD `-5.8012`
- `news_risk_high->crypto_major_4h` score `1.1779` n `61` status `ready` deltaP `6.3874` edge `0.1778` maxDD `-2.8833`
- `news_risk_high->crypto_major_1h` score `1.0788` n `62` status `ready` deltaP `8.6295` edge `0.0721` maxDD `-1.1783`
- `news_risk_high->fx_1h` score `0.348` n `62` status `ready` deltaP `7.7989` edge `0.0051` maxDD `-0.2475`
- `news_risk_high->index_1h` score `0.3144` n `62` status `ready` deltaP `6.0846` edge `0.0145` maxDD `-0.3089`
- `news_risk_high->fx_4h` score `0.079` n `61` status `ready` deltaP `11.7953` edge `0.0237` maxDD `-0.6604`
- `news_risk_high->metal_1h` score `-0.1081` n `62` status `ready` deltaP `3.7232` edge `0.0065` maxDD `-0.5599`
- `news_risk_high->metal_4h` score `-0.4834` n `61` status `ready` deltaP `-2.0742` edge `0.0208` maxDD `-0.7801`
- `news_risk_high->commodity_1h` score `-1.5482` n `62` status `ready` deltaP `-2.8588` edge `-0.0314` maxDD `-2.9516`
- `news_risk_high->fx_24h` score `-5.5717` n `52` status `ready` deltaP `-27.7244` edge `-0.0473` maxDD `-5.2413`
- `news_risk_high->commodity_4h` score `-7.4478` n `61` status `ready` deltaP `-18.705` edge `-0.1652` maxDD `-13.1269`
- `news_risk_high->metal_24h` score `-9.2408` n `52` status `ready` deltaP `-36.6186` edge `-0.2489` maxDD `-10.8302`
- `news_risk_high->commodity_24h` score `-12.9078` n `52` status `ready` deltaP `-13.3013` edge `-0.393` maxDD `-33.8515`
- `news_risk_high->index_24h` score `-14.1632` n `52` status `ready` deltaP `-33.9744` edge `-0.4035` maxDD `-28.0214`
- `news_risk_high->crypto_major_24h` score `-40.1702` n `52` status `ready` deltaP `-29.3135` edge `-1.6996` maxDD `-103.8662`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
