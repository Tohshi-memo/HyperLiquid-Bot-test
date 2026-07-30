# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-30T10:07:30.214048+00:00`
- Price records: `672`
- Market context records: `8399`
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

- `news_risk_high->unknown_24h` score `6252.5781` n `52` status `ready` deltaP `37.7938` edge `520.8383` maxDD `-2.0332`
- `news_risk_high->equity_4h` score `7.3706` n `52` status `ready` deltaP `26.372` edge `0.4981` maxDD `-3.4427`
- `news_risk_high->equity_1h` score `2.9136` n `52` status `ready` deltaP `21.1308` edge `0.1328` maxDD `-1.1366`
- `news_risk_high->index_4h` score `2.641` n `52` status `ready` deltaP `21.9512` edge `0.0928` maxDD `-0.191`
- `news_risk_high->crypto_major_4h` score `1.9009` n `52` status `ready` deltaP `8.6069` edge `0.2557` maxDD `-2.8833`
- `news_risk_high->crypto_alt_1h` score `1.6771` n `52` status `ready` deltaP `12.9088` edge `0.0971` maxDD `-1.1388`
- `news_risk_high->crypto_major_1h` score `1.599` n `52` status `ready` deltaP `11.2621` edge `0.0979` maxDD `-1.1783`
- `news_risk_high->crypto_alt_4h` score `1.4119` n `52` status `ready` deltaP `16.8739` edge `0.2077` maxDD `-5.8012`
- `news_risk_high->metal_4h` score `0.6344` n `52` status `ready` deltaP `6.4142` edge `0.0569` maxDD `-0.7433`
- `news_risk_high->index_1h` score `0.26` n `52` status `ready` deltaP `4.7444` edge `0.0189` maxDD `-0.3089`
- `news_risk_high->fx_1h` score `0.0876` n `52` status `ready` deltaP `5.4929` edge `0.0027` maxDD `-0.2475`
- `news_risk_high->metal_1h` score `-0.236` n `52` status `ready` deltaP `2.1995` edge `0.006` maxDD `-0.5599`
- `news_risk_high->fx_4h` score `-0.4841` n `52` status `ready` deltaP `4.1979` edge `0.0057` maxDD `-0.6604`
- `news_risk_high->commodity_1h` score `-2.0507` n `52` status `ready` deltaP `-7.5196` edge `-0.0422` maxDD `-2.9516`
- `news_risk_high->fx_24h` score `-5.7493` n `52` status `ready` deltaP `-27.7244` edge `-0.0621` maxDD `-5.2413`
- `news_risk_high->metal_24h` score `-7.937` n `52` status `ready` deltaP `-30.7158` edge `-0.1796` maxDD `-10.8302`
- `news_risk_high->commodity_4h` score `-8.6708` n `52` status `ready` deltaP `-28.037` edge `-0.2049` maxDD `-13.1269`
- `news_risk_high->commodity_24h` score `-12.2097` n `52` status `ready` deltaP `-10.3499` edge `-0.3545` maxDD `-33.8515`
- `news_risk_high->index_24h` score `-12.3227` n `52` status `ready` deltaP `-25.2938` edge `-0.308` maxDD `-28.0214`
- `news_risk_high->equity_24h` score `-34.6307` n `52` status `ready` deltaP `-23.2105` edge `-0.9436` maxDD `-127.0042`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
