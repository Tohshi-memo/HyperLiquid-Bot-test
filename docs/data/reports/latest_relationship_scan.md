# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-30T10:52:29.046364+00:00`
- Price records: `672`
- Market context records: `8402`
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

- `news_risk_high->unknown_24h` score `6252.639` n `52` status `ready` deltaP `38.3146` edge `520.8399` maxDD `-2.0332`
- `news_risk_high->equity_4h` score `7.232` n `52` status `ready` deltaP `25.9146` edge `0.4896` maxDD `-3.4427`
- `news_risk_high->equity_1h` score `2.8812` n `52` status `ready` deltaP `20.9811` edge `0.1311` maxDD `-1.1366`
- `news_risk_high->index_4h` score `2.5829` n `52` status `ready` deltaP `21.4939` edge `0.091` maxDD `-0.191`
- `news_risk_high->crypto_major_4h` score `1.8178` n `52` status `ready` deltaP `8.1496` edge `0.2481` maxDD `-2.8833`
- `news_risk_high->crypto_alt_1h` score `1.6651` n `52` status `ready` deltaP `12.7591` edge `0.0971` maxDD `-1.1388`
- `news_risk_high->crypto_major_1h` score `1.6002` n `52` status `ready` deltaP `11.2621` edge `0.098` maxDD `-1.1783`
- `news_risk_high->crypto_alt_4h` score `1.3624` n `52` status `ready` deltaP `16.4165` edge `0.2044` maxDD `-5.8012`
- `news_risk_high->metal_4h` score `0.5547` n `52` status `ready` deltaP `5.9569` edge `0.0533` maxDD `-0.7433`
- `news_risk_high->index_1h` score `0.2576` n `52` status `ready` deltaP `4.7444` edge `0.0187` maxDD `-0.3089`
- `news_risk_high->fx_1h` score `0.0891` n `52` status `ready` deltaP `5.4929` edge `0.0029` maxDD `-0.2475`
- `news_risk_high->metal_1h` score `-0.2648` n `52` status `ready` deltaP `1.9001` edge `0.0056` maxDD `-0.5599`
- `news_risk_high->fx_4h` score `-0.4841` n `52` status `ready` deltaP `4.1979` edge `0.0057` maxDD `-0.6604`
- `news_risk_high->commodity_1h` score `-2.0184` n `52` status `ready` deltaP `-7.2202` edge `-0.0415` maxDD `-2.9516`
- `news_risk_high->fx_24h` score `-5.7553` n `52` status `ready` deltaP `-27.7244` edge `-0.0626` maxDD `-5.2413`
- `news_risk_high->metal_24h` score `-8.0279` n `52` status `ready` deltaP `-31.2366` edge `-0.1837` maxDD `-10.8302`
- `news_risk_high->commodity_4h` score `-8.603` n `52` status `ready` deltaP `-27.5797` edge `-0.2023` maxDD `-13.1269`
- `news_risk_high->commodity_24h` score `-12.291` n `52` status `ready` deltaP `-10.8707` edge `-0.3578` maxDD `-33.8515`
- `news_risk_high->index_24h` score `-12.3275` n `52` status `ready` deltaP `-25.2938` edge `-0.3084` maxDD `-28.0214`
- `news_risk_high->equity_24h` score `-34.5731` n `52` status `ready` deltaP `-23.2105` edge `-0.9388` maxDD `-127.0042`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
