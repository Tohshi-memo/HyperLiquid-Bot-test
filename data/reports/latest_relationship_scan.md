# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-03T19:52:28.683779+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `5930`

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

- `market_context_high->unknown_24h` score `45.6442` n `39` status `ready` deltaP `28.9931` edge `3.6104` maxDD `0.0`
- `market_context_high->unknown_4h` score `17.3388` n `52` status `ready` deltaP `13.6609` edge `1.3913` maxDD `-0.9977`
- `market_context_high->crypto_alt_24h` score `11.1377` n `39` status `ready` deltaP `49.4258` edge `0.616` maxDD `-0.3889`
- `market_context_high->commodity_24h` score `11.1094` n `39` status `ready` deltaP `53.4722` edge `0.5693` maxDD `0.0`
- `news_risk_high->fx_24h` score `0.9809` n `31` status `ready` deltaP `12.192` edge `0.0657` maxDD `-1.5526`
- `news_risk_high->commodity_1h` score `0.8688` n `31` status `ready` deltaP `18.7898` edge `0.0073` maxDD `-0.6947`
- `news_risk_high->equity_4h` score `0.6302` n `31` status `ready` deltaP `-7.735` edge `0.1725` maxDD `-2.8064`
- `market_context_high->commodity_4h` score `0.5159` n `52` status `ready` deltaP `8.6655` edge `0.093` maxDD `-2.7703`
- `market_context_high->commodity_1h` score `0.3957` n `64` status `ready` deltaP `8.8604` edge `0.0291` maxDD `-1.3282`
- `news_risk_high->fx_4h` score `0.0964` n `31` status `ready` deltaP `4.1306` edge `0.0351` maxDD `-0.356`
- `news_risk_high->index_4h` score `0.0724` n `31` status `ready` deltaP `-0.8261` edge `0.0496` maxDD `-0.3783`
- `market_context_high->fx_1h` score `0.0458` n `64` status `ready` deltaP `6.5494` edge `-0.005` maxDD `-0.7878`
- `news_risk_high->commodity_4h` score `-0.0037` n `31` status `ready` deltaP `10.9608` edge `-0.0233` maxDD `-1.6728`
- `news_risk_high->index_1h` score `-0.0649` n `31` status `ready` deltaP `2.5932` edge `-0.0058` maxDD `-0.5845`
- `market_context_high->fx_4h` score `-0.0985` n `52` status `ready` deltaP `12.1951` edge `-0.0037` maxDD `-1.8648`
- `news_risk_high->crypto_alt_1h` score `-0.1244` n `31` status `ready` deltaP `9.943` edge `-0.0182` maxDD `-3.1233`
- `market_context_high->crypto_alt_1h` score `-0.231` n `64` status `ready` deltaP `3.3402` edge `0.015` maxDD `-3.0178`
- `news_risk_high->fx_1h` score `-0.2926` n `31` status `ready` deltaP `-1.3135` edge `0.0024` maxDD `-0.1588`
- `market_context_high->crypto_alt_4h` score `-0.3759` n `52` status `ready` deltaP `3.2951` edge `0.0204` maxDD `-4.9116`
- `market_context_high->index_1h` score `-0.4987` n `64` status `ready` deltaP `0.8795` edge `-0.0164` maxDD `-1.6054`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
