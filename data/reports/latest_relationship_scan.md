# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-16T01:07:32.917925+00:00`
- Price records: `672`
- Market context records: `4044`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `10624`

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

- `risk_on_high->unknown_4h` score `144.9243` n `40` status `ready` deltaP `-7.8963` edge `12.3113` maxDD `-10.864`
- `risk_on_and_context->unknown_4h` score `144.9243` n `40` status `ready` deltaP `-7.8963` edge `12.3113` maxDD `-10.864`
- `market_context_high->unknown_24h` score `46.4208` n `134` status `ready` deltaP `-8.1055` edge `4.3253` maxDD `-24.2289`
- `market_context_high->unknown_4h` score `22.2103` n `156` status `ready` deltaP `1.9114` edge `2.3804` maxDD `-35.7161`
- `risk_on_high->equity_24h` score `4.354` n `40` status `ready` deltaP `34.8354` edge `0.1306` maxDD `0.0`
- `risk_on_and_context->equity_24h` score `4.354` n `40` status `ready` deltaP `34.8354` edge `0.1306` maxDD `0.0`
- `risk_on_high->equity_4h` score `3.4276` n `40` status `ready` deltaP `37.1341` edge `0.0428` maxDD `-0.0446`
- `risk_on_and_context->equity_4h` score `3.4276` n `40` status `ready` deltaP `37.1341` edge `0.0428` maxDD `-0.0446`
- `market_context_high->index_24h` score `2.4267` n `134` status `ready` deltaP `21.784` edge `0.0782` maxDD `-1.3629`
- `market_context_high->equity_4h` score `1.7078` n `156` status `ready` deltaP `15.9162` edge `0.1643` maxDD `-6.9137`
- `market_context_high->metal_24h` score `1.2333` n `134` status `ready` deltaP `10.6612` edge `0.1304` maxDD `-4.8962`
- `risk_on_high->crypto_major_4h` score `0.9379` n `40` status `ready` deltaP `18.8415` edge `0.0191` maxDD `-2.6576`
- `risk_on_and_context->crypto_major_4h` score `0.9379` n `40` status `ready` deltaP `18.8415` edge `0.0191` maxDD `-2.6576`
- `market_context_high->equity_1h` score `0.8578` n `164` status `ready` deltaP `6.3678` edge `0.085` maxDD `-2.144`
- `risk_on_high->equity_1h` score `0.4124` n `40` status `ready` deltaP `11.0629` edge `-0.0003` maxDD `-0.7937`
- `risk_on_and_context->equity_1h` score `0.4124` n `40` status `ready` deltaP `11.0629` edge `-0.0003` maxDD `-0.7937`
- `risk_on_high->commodity_24h` score `0.2974` n `40` status `ready` deltaP `1.4298` edge `0.2434` maxDD `-12.9187`
- `risk_on_and_context->commodity_24h` score `0.2974` n `40` status `ready` deltaP `1.4298` edge `0.2434` maxDD `-12.9187`
- `market_context_high->crypto_major_1h` score `0.2388` n `164` status `ready` deltaP `7.2112` edge `0.044` maxDD `-3.7739`
- `market_context_high->metal_1h` score `0.2301` n `164` status `ready` deltaP `8.9638` edge `0.0418` maxDD `-3.7651`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
