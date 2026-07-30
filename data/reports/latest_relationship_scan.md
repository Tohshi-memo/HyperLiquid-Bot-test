# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-30T10:22:29.053739+00:00`
- Price records: `672`
- Market context records: `8400`
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

- `news_risk_high->unknown_24h` score `6252.5992` n `52` status `ready` deltaP `37.9674` edge `520.8389` maxDD `-2.0332`
- `news_risk_high->equity_4h` score `7.3236` n `52` status `ready` deltaP `26.2195` edge `0.4952` maxDD `-3.4427`
- `news_risk_high->equity_1h` score `2.9088` n `52` status `ready` deltaP `21.1308` edge `0.1324` maxDD `-1.1366`
- `news_risk_high->index_4h` score `2.6217` n `52` status `ready` deltaP `21.7988` edge `0.0922` maxDD `-0.191`
- `news_risk_high->crypto_major_4h` score `1.8735` n `52` status `ready` deltaP `8.4545` edge `0.2532` maxDD `-2.8833`
- `news_risk_high->crypto_alt_1h` score `1.6627` n `52` status `ready` deltaP `12.7591` edge `0.0969` maxDD `-1.1388`
- `news_risk_high->crypto_major_1h` score `1.5978` n `52` status `ready` deltaP `11.2621` edge `0.0978` maxDD `-1.1783`
- `news_risk_high->crypto_alt_4h` score `1.3938` n `52` status `ready` deltaP `16.7214` edge `0.2064` maxDD `-5.8012`
- `news_risk_high->metal_4h` score `0.609` n `52` status `ready` deltaP `6.2617` edge `0.0558` maxDD `-0.7433`
- `news_risk_high->index_1h` score `0.26` n `52` status `ready` deltaP `4.7444` edge `0.0189` maxDD `-0.3089`
- `news_risk_high->fx_1h` score `0.0883` n `52` status `ready` deltaP `5.4929` edge `0.0028` maxDD `-0.2475`
- `news_risk_high->metal_1h` score `-0.2504` n `52` status `ready` deltaP `2.0498` edge `0.0058` maxDD `-0.5599`
- `news_risk_high->fx_4h` score `-0.4849` n `52` status `ready` deltaP `4.1979` edge `0.0056` maxDD `-0.6604`
- `news_risk_high->commodity_1h` score `-2.0495` n `52` status `ready` deltaP `-7.5196` edge `-0.0421` maxDD `-2.9516`
- `news_risk_high->fx_24h` score `-5.7517` n `52` status `ready` deltaP `-27.7244` edge `-0.0623` maxDD `-5.2413`
- `news_risk_high->metal_24h` score `-7.9677` n `52` status `ready` deltaP `-30.8894` edge `-0.181` maxDD `-10.8302`
- `news_risk_high->commodity_4h` score `-8.6514` n `52` status `ready` deltaP `-27.8846` edge `-0.2043` maxDD `-13.1269`
- `news_risk_high->commodity_24h` score `-12.2404` n `52` status `ready` deltaP `-10.5235` edge `-0.3559` maxDD `-33.8515`
- `news_risk_high->index_24h` score `-12.3239` n `52` status `ready` deltaP `-25.2938` edge `-0.3081` maxDD `-28.0214`
- `news_risk_high->equity_24h` score `-34.6067` n `52` status `ready` deltaP `-23.2105` edge `-0.9416` maxDD `-127.0042`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
