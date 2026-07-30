# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-30T02:22:33.987212+00:00`
- Price records: `672`
- Market context records: `8365`
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

- `news_risk_high->unknown_24h` score `6252.1046` n `52` status `ready` deltaP `35.1896` edge `520.8162` maxDD `-2.0332`
- `news_risk_high->equity_4h` score `7.2216` n `52` status `ready` deltaP `25.3049` edge `0.4928` maxDD `-3.4427`
- `news_risk_high->equity_1h` score `2.7637` n `52` status `ready` deltaP `20.2326` edge `0.1263` maxDD `-1.1366`
- `news_risk_high->index_4h` score `2.6424` n `52` status `ready` deltaP `22.1037` edge `0.0919` maxDD `-0.191`
- `news_risk_high->crypto_major_4h` score `1.9721` n `52` status `ready` deltaP `8.9118` edge `0.2628` maxDD `-2.8833`
- `news_risk_high->crypto_alt_1h` score `1.6555` n `52` status `ready` deltaP `12.7591` edge `0.0963` maxDD `-1.1388`
- `news_risk_high->crypto_major_1h` score `1.6122` n `52` status `ready` deltaP `11.2621` edge `0.099` maxDD `-1.1783`
- `news_risk_high->crypto_alt_4h` score `1.4466` n `52` status `ready` deltaP `16.4165` edge `0.2152` maxDD `-5.8012`
- `news_risk_high->metal_4h` score `0.8062` n `52` status `ready` deltaP `7.4813` edge `0.0641` maxDD `-0.7433`
- `news_risk_high->index_1h` score `0.1809` n `52` status `ready` deltaP `3.9959` edge `0.0173` maxDD `-0.3089`
- `news_risk_high->fx_1h` score `0.0362` n `52` status `ready` deltaP `4.5947` edge `0.0021` maxDD `-0.2475`
- `news_risk_high->metal_1h` score `-0.1905` n `52` status `ready` deltaP `2.4989` edge `0.0078` maxDD `-0.5599`
- `news_risk_high->fx_4h` score `-0.5885` n `52` status `ready` deltaP `2.5211` edge `0.0035` maxDD `-0.6604`
- `news_risk_high->commodity_1h` score `-2.1621` n `52` status `ready` deltaP `-8.7172` edge `-0.0435` maxDD `-2.9516`
- `news_risk_high->fx_24h` score `-5.3713` n `52` status `ready` deltaP `-24.0785` edge `-0.0549` maxDD `-5.2413`
- `news_risk_high->metal_24h` score `-7.111` n `52` status `ready` deltaP `-27.5908` edge `-0.1316` maxDD `-10.8302`
- `news_risk_high->commodity_4h` score `-8.8905` n `52` status `ready` deltaP `-30.0187` edge `-0.21` maxDD `-13.1269`
- `news_risk_high->commodity_24h` score `-11.8816` n `52` status `ready` deltaP `-9.3082` edge `-0.3341` maxDD `-33.8515`
- `news_risk_high->index_24h` score `-12.0865` n `52` status `ready` deltaP `-24.4258` edge `-0.2941` maxDD `-28.0214`
- `news_risk_high->equity_24h` score `-35.0435` n `52` status `ready` deltaP `-23.2105` edge `-0.978` maxDD `-127.0042`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
