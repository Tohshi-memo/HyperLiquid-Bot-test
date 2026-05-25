# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-25T01:36:04.264639+00:00`
- Price records: `672`
- Market context records: `1797`
- Flow alert records: `7069`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8872`

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

- `market_context_high->metal_24h` score `7.1005` n `188` status `ready` deltaP `28.487` edge `0.6444` maxDD `-12.7414`
- `news_risk_high->commodity_4h` score `6.463` n `30` status `ready` deltaP `29.2582` edge `0.409` maxDD `-3.5713`
- `market_context_high->crypto_alt_4h` score `5.7554` n `193` status `ready` deltaP `21.4109` edge `0.5135` maxDD `-9.1295`
- `market_context_high->crypto_major_4h` score `4.6147` n `193` status `ready` deltaP `23.5127` edge `0.4552` maxDD `-9.8583`
- `market_context_high->unknown_4h` score `4.0255` n `193` status `ready` deltaP `16.2289` edge `0.4429` maxDD `-10.2508`
- `news_risk_high->commodity_1h` score `3.2686` n `30` status `ready` deltaP `24.8703` edge `0.1383` maxDD `-1.2043`
- `market_context_high->equity_4h` score `2.9139` n `193` status `ready` deltaP `16.1965` edge `0.2443` maxDD `-5.0894`
- `market_context_high->index_24h` score `2.7671` n `188` status `ready` deltaP `13.8039` edge `0.2614` maxDD `-4.1604`
- `market_context_high->equity_24h` score `1.5911` n `188` status `ready` deltaP `15.455` edge `0.5194` maxDD `-33.1875`
- `market_context_high->unknown_24h` score `1.0749` n `188` status `ready` deltaP `12.4076` edge `0.5389` maxDD `-35.8966`
- `news_risk_high->fx_4h` score `0.8767` n `30` status `ready` deltaP `21.3313` edge `-0.0026` maxDD `-0.1774`
- `market_context_high->index_4h` score `0.8661` n `193` status `ready` deltaP `12.2962` edge `0.0991` maxDD `-3.7119`
- `news_risk_high->unknown_4h` score `0.4042` n `30` status `ready` deltaP `10.1321` edge `0.0566` maxDD `-2.7857`
- `market_context_high->crypto_alt_1h` score `0.3561` n `195` status `ready` deltaP `7.0697` edge `0.0937` maxDD `-4.8924`
- `market_context_high->crypto_major_1h` score `0.2797` n `195` status `ready` deltaP `5.4038` edge `0.0859` maxDD `-3.2225`
- `market_context_high->equity_1h` score `-0.1093` n `195` status `ready` deltaP `4.2669` edge `0.0433` maxDD `-2.8014`
- `market_context_high->index_1h` score `-0.3817` n `195` status `ready` deltaP `2.2601` edge `0.0163` maxDD `-1.7205`
- `market_context_high->fx_24h` score `-0.3862` n `188` status `ready` deltaP `9.109` edge `0.012` maxDD `-1.3925`
- `news_risk_high->unknown_1h` score `-0.399` n `30` status `ready` deltaP `17.1557` edge `-0.1183` maxDD `-2.1115`
- `market_context_high->metal_4h` score `-0.4402` n `193` status `ready` deltaP `11.9629` edge `0.133` maxDD `-12.5349`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
