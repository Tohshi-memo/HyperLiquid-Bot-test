# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-30T02:52:30.234933+00:00`
- Price records: `672`
- Market context records: `8367`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `5886`

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

- `news_risk_high->unknown_24h` score `6252.1154` n `52` status `ready` deltaP `35.1896` edge `520.8171` maxDD `-2.0332`
- `news_risk_high->equity_4h` score `7.1708` n `52` status `ready` deltaP `25.0` edge `0.4906` maxDD `-3.4427`
- `news_risk_high->equity_1h` score `2.7877` n `52` status `ready` deltaP `20.2326` edge `0.1283` maxDD `-1.1366`
- `news_risk_high->index_4h` score `2.6109` n `52` status `ready` deltaP `21.7988` edge `0.0913` maxDD `-0.191`
- `news_risk_high->crypto_major_4h` score `1.9391` n `52` status `ready` deltaP `8.6069` edge `0.2606` maxDD `-2.8833`
- `news_risk_high->crypto_alt_1h` score `1.6375` n `52` status `ready` deltaP `12.6094` edge `0.0958` maxDD `-1.1388`
- `news_risk_high->crypto_major_1h` score `1.6098` n `52` status `ready` deltaP `11.2621` edge `0.0988` maxDD `-1.1783`
- `news_risk_high->crypto_alt_4h` score `1.4081` n `52` status `ready` deltaP `16.1117` edge `0.2123` maxDD `-5.8012`
- `news_risk_high->metal_4h` score `0.822` n `52` status `ready` deltaP `7.6337` edge `0.0644` maxDD `-0.7433`
- `news_risk_high->index_1h` score `0.1857` n `52` status `ready` deltaP `3.9959` edge `0.0177` maxDD `-0.3089`
- `news_risk_high->fx_1h` score `0.0533` n `52` status `ready` deltaP `4.8941` edge `0.0023` maxDD `-0.2475`
- `news_risk_high->metal_1h` score `-0.1593` n `52` status `ready` deltaP `2.7983` edge `0.0084` maxDD `-0.5599`
- `news_risk_high->fx_4h` score `-0.5711` n `52` status `ready` deltaP `2.826` edge `0.0037` maxDD `-0.6604`
- `news_risk_high->commodity_1h` score `-2.1346` n `52` status `ready` deltaP `-8.4178` edge `-0.0432` maxDD `-2.9516`
- `news_risk_high->fx_24h` score `-5.4039` n `52` status `ready` deltaP `-24.4258` edge `-0.0553` maxDD `-5.2413`
- `news_risk_high->metal_24h` score `-7.182` n `52` status `ready` deltaP `-27.938` edge `-0.1352` maxDD `-10.8302`
- `news_risk_high->commodity_4h` score `-8.8577` n `52` status `ready` deltaP `-29.7139` edge `-0.2093` maxDD `-13.1269`
- `news_risk_high->commodity_24h` score `-11.8792` n `52` status `ready` deltaP `-9.3082` edge `-0.3339` maxDD `-33.8515`
- `news_risk_high->index_24h` score `-12.1045` n `52` status `ready` deltaP `-24.4258` edge `-0.2956` maxDD `-28.0214`
- `news_risk_high->equity_24h` score `-35.0339` n `52` status `ready` deltaP `-23.2105` edge `-0.9772` maxDD `-127.0042`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
