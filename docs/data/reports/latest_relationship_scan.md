# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-30T09:37:29.855094+00:00`
- Price records: `672`
- Market context records: `8396`
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

- `news_risk_high->unknown_24h` score `6252.5431` n `52` status `ready` deltaP `37.4466` edge `520.8377` maxDD `-2.0332`
- `news_risk_high->equity_4h` score `7.4705` n `52` status `ready` deltaP `26.6768` edge `0.5044` maxDD `-3.4427`
- `news_risk_high->equity_1h` score `2.9579` n `52` status `ready` deltaP `21.4302` edge `0.1345` maxDD `-1.1366`
- `news_risk_high->index_4h` score `2.6774` n `52` status `ready` deltaP `22.2561` edge `0.0938` maxDD `-0.191`
- `news_risk_high->crypto_major_4h` score `1.9503` n `52` status `ready` deltaP `8.9118` edge `0.26` maxDD `-2.8833`
- `news_risk_high->crypto_alt_1h` score `1.6939` n `52` status `ready` deltaP `13.0585` edge `0.0975` maxDD `-1.1388`
- `news_risk_high->crypto_major_1h` score `1.635` n `52` status `ready` deltaP `11.5615` edge `0.0989` maxDD `-1.1783`
- `news_risk_high->crypto_alt_4h` score `1.448` n `52` status `ready` deltaP `17.1787` edge `0.2103` maxDD `-5.8012`
- `news_risk_high->metal_4h` score `0.69` n `52` status `ready` deltaP `6.7191` edge `0.0595` maxDD `-0.7433`
- `news_risk_high->index_1h` score `0.2864` n `52` status `ready` deltaP `5.0438` edge `0.0191` maxDD `-0.3089`
- `news_risk_high->fx_1h` score `0.0953` n `52` status `ready` deltaP `5.6426` edge `0.0027` maxDD `-0.2475`
- `news_risk_high->metal_1h` score `-0.2049` n `52` status `ready` deltaP `2.4989` edge `0.0066` maxDD `-0.5599`
- `news_risk_high->fx_4h` score `-0.4683` n `52` status `ready` deltaP `4.5028` edge `0.0057` maxDD `-0.6604`
- `news_risk_high->commodity_1h` score `-2.0771` n `52` status `ready` deltaP `-7.819` edge `-0.0424` maxDD `-2.9516`
- `news_risk_high->fx_24h` score `-5.7144` n `52` status `ready` deltaP `-27.3771` edge `-0.0615` maxDD `-5.2413`
- `news_risk_high->metal_24h` score `-7.878` n `52` status `ready` deltaP `-30.3686` edge `-0.177` maxDD `-10.8302`
- `news_risk_high->commodity_4h` score `-8.7084` n `52` status `ready` deltaP `-28.3419` edge `-0.206` maxDD `-13.1269`
- `news_risk_high->commodity_24h` score `-12.1447` n `52` status `ready` deltaP `-10.0027` edge `-0.3514` maxDD `-33.8515`
- `news_risk_high->index_24h` score `-12.3239` n `52` status `ready` deltaP `-25.2938` edge `-0.3081` maxDD `-28.0214`
- `news_risk_high->equity_24h` score `-34.6871` n `52` status `ready` deltaP `-23.2105` edge `-0.9483` maxDD `-127.0042`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
