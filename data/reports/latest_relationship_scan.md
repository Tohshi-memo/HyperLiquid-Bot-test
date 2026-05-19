# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-19T00:22:15.367424+00:00`
- Price records: `672`
- Market context records: `1169`
- Flow alert records: `5268`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8750`

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

- `market_context_high->crypto_major_24h` score `20.9138` n `138` status `ready` deltaP `45.8861` edge `1.5501` maxDD `-8.0553`
- `market_context_high->crypto_alt_24h` score `10.1005` n `138` status `ready` deltaP `22.1317` edge `0.8958` maxDD `-15.1306`
- `market_context_high->equity_24h` score `7.681` n `138` status `ready` deltaP `21.958` edge `0.5867` maxDD `-6.4404`
- `market_context_high->index_24h` score `5.7317` n `138` status `ready` deltaP `20.5692` edge `0.3963` maxDD `-3.4627`
- `market_context_high->metal_24h` score `5.4939` n `138` status `ready` deltaP `-3.744` edge `0.6495` maxDD `-6.3373`
- `market_context_high->equity_4h` score `2.5073` n `153` status `ready` deltaP `12.8657` edge `0.1895` maxDD `-3.6396`
- `market_context_high->index_4h` score `1.1746` n `153` status `ready` deltaP `9.3575` edge `0.1038` maxDD `-2.1308`
- `market_context_high->unknown_24h` score `1.0296` n `138` status `ready` deltaP `2.6495` edge `0.3411` maxDD `-10.1706`
- `market_context_high->index_1h` score `0.5499` n `153` status `ready` deltaP `8.1777` edge `0.023` maxDD `-0.5353`
- `market_context_high->equity_1h` score `0.3039` n `153` status `ready` deltaP `3.0586` edge `0.0427` maxDD `-1.3546`
- `market_context_high->fx_1h` score `0.151` n `153` status `ready` deltaP `8.6484` edge `0.0005` maxDD `-0.3124`
- `market_context_high->crypto_major_4h` score `0.0963` n `153` status `ready` deltaP `8.1699` edge `0.15` maxDD `-8.3693`
- `market_context_high->crypto_major_1h` score `-0.0373` n `153` status `ready` deltaP `6.5232` edge `0.0283` maxDD `-4.1256`
- `market_context_high->unknown_4h` score `-0.1322` n `153` status `ready` deltaP `6.0358` edge `0.0704` maxDD `-6.7322`
- `market_context_high->crypto_alt_1h` score `-0.4727` n `153` status `ready` deltaP `1.9774` edge `0.0317` maxDD `-3.4088`
- `market_context_high->metal_1h` score `-0.5005` n `153` status `ready` deltaP `5.3149` edge `-0.0161` maxDD `-2.2164`
- `market_context_high->commodity_1h` score `-0.821` n `153` status `ready` deltaP `-3.1457` edge `-0.0035` maxDD `-3.7959`
- `market_context_high->fx_4h` score `-1.0165` n `153` status `ready` deltaP `-3.8976` edge `-0.0047` maxDD `-1.6381`
- `market_context_high->crypto_alt_4h` score `-1.3267` n `153` status `ready` deltaP `3.795` edge `0.1011` maxDD `-16.7194`
- `market_context_high->metal_4h` score `-1.9373` n `153` status `ready` deltaP `4.5802` edge `-0.0835` maxDD `-9.2991`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
