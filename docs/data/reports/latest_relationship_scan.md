# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-26T04:07:28.801072+00:00`
- Price records: `672`
- Market context records: `4791`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `72`

- Symbol pattern count: `7548`

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

- `market_context_high->unknown_4h` score `7.6733` n `122` status `ready` deltaP `18.5676` edge `0.6367` maxDD `-4.6834`
- `market_context_high->unknown_1h` score `7.5565` n `122` status `ready` deltaP `12.7295` edge `0.5866` maxDD `-1.674`
- `market_context_high->unknown_24h` score `2.048` n `108` status `ready` deltaP `11.8055` edge `0.1843` maxDD `-4.7201`
- `market_context_high->commodity_1h` score `0.1597` n `122` status `ready` deltaP `5.8309` edge `0.0332` maxDD `-2.0345`
- `market_context_high->commodity_4h` score `0.0667` n `122` status `ready` deltaP `11.8153` edge `0.047` maxDD `-4.377`
- `market_context_high->equity_4h` score `-0.1607` n `122` status `ready` deltaP `8.0818` edge `0.0941` maxDD `-8.8203`
- `market_context_high->index_4h` score `-0.3812` n `122` status `ready` deltaP `6.8423` edge `0.0124` maxDD `-5.5505`
- `market_context_high->fx_4h` score `-0.4606` n `122` status `ready` deltaP `2.5165` edge `0.0018` maxDD `-1.5439`
- `market_context_high->equity_1h` score `-0.7247` n `122` status `ready` deltaP `1.4185` edge `0.0069` maxDD `-4.1397`
- `market_context_high->fx_1h` score `-0.9364` n `122` status `ready` deltaP `-1.4823` edge `-0.0032` maxDD `-0.8626`
- `market_context_high->index_1h` score `-1.3776` n `122` status `ready` deltaP `-1.3473` edge `-0.0054` maxDD `-2.6999`
- `market_context_high->metal_1h` score `-2.2556` n `122` status `ready` deltaP `-0.7976` edge `-0.0663` maxDD `-14.0715`
- `market_context_high->commodity_24h` score `-2.2669` n `108` status `ready` deltaP `18.9236` edge `0.0941` maxDD `-27.5371`
- `market_context_high->crypto_alt_1h` score `-3.1376` n `122` status `ready` deltaP `0.8982` edge `-0.0435` maxDD `-15.2495`
- `market_context_high->fx_24h` score `-3.4143` n `108` status `ready` deltaP `-16.0301` edge `-0.0227` maxDD `-3.3968`
- `market_context_high->crypto_major_1h` score `-4.4647` n `122` status `ready` deltaP `0.6847` edge `-0.0676` maxDD `-22.0555`
- `market_context_high->crypto_alt_4h` score `-4.7931` n `122` status `ready` deltaP `4.7456` edge `-0.0037` maxDD `-46.0617`
- `market_context_high->index_24h` score `-5.7871` n `108` status `ready` deltaP `-5.6135` edge `-0.1059` maxDD `-19.1149`
- `market_context_high->crypto_major_4h` score `-8.0849` n `122` status `ready` deltaP `3.5061` edge `-0.1368` maxDD `-68.5143`
- `market_context_high->metal_4h` score `-8.3534` n `122` status `ready` deltaP `6.23` edge `-0.2884` maxDD `-61.2596`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
