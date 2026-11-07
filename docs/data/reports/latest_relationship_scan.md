# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-07T13:52:28.709545+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `4099`

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

- `market_context_high->unknown_4h` score `244.036` n `31` status `ready` deltaP `5.2862` edge `20.313` maxDD `-0.2857`
- `market_context_high->fx_4h` score `3.4511` n `31` status `ready` deltaP `36.5362` edge `0.053` maxDD `-0.0521`
- `market_context_high->equity_1h` score `3.0628` n `37` status `ready` deltaP `8.4116` edge `0.2451` maxDD `-2.3425`
- `market_context_high->index_4h` score `1.7605` n `31` status `ready` deltaP `22.9987` edge `0.0404` maxDD `-2.4279`
- `news_risk_high->equity_4h` score `1.1565` n `59` status `ready` deltaP `10.2547` edge `0.1538` maxDD `-4.2454`
- `news_risk_high->index_4h` score `0.7548` n `59` status `ready` deltaP `13.3759` edge `0.0215` maxDD `-0.4888`
- `market_context_high->crypto_major_1h` score `0.7207` n `37` status `ready` deltaP `9.4514` edge `0.0556` maxDD `-3.0172`
- `news_risk_high->fx_24h` score `0.5133` n `59` status `ready` deltaP `-0.1678` edge `0.0746` maxDD `-0.1235`
- `market_context_high->fx_1h` score `0.4817` n `37` status `ready` deltaP `7.8209` edge `0.0151` maxDD `-0.1681`
- `market_context_high->crypto_alt_1h` score `0.3688` n `37` status `ready` deltaP `10.3496` edge `0.0598` maxDD `-3.1881`
- `news_risk_high->index_24h` score `0.337` n `59` status `ready` deltaP `9.6781` edge `0.1455` maxDD `-6.6786`
- `market_context_high->index_1h` score `0.2853` n `37` status `ready` deltaP `1.8005` edge `0.0388` maxDD `-0.1621`
- `news_risk_high->index_1h` score `0.1849` n `59` status `ready` deltaP `9.7711` edge `0.0039` maxDD `-0.2931`
- `market_context_high->commodity_1h` score `0.1779` n `37` status `ready` deltaP `10.0664` edge `0.0103` maxDD `-1.7019`
- `news_risk_high->equity_1h` score `0.0399` n `59` status `ready` deltaP `1.4945` edge `0.0501` maxDD `-1.396`
- `news_risk_high->fx_4h` score `-0.0978` n `59` status `ready` deltaP `4.0047` edge `0.005` maxDD `-0.2052`
- `market_context_high->metal_1h` score `-0.0988` n `37` status `ready` deltaP `0.6029` edge `0.0161` maxDD `-0.6226`
- `news_risk_high->fx_1h` score `-0.1094` n `59` status `ready` deltaP `3.2858` edge `0.0026` maxDD `-0.0826`
- `market_context_high->commodity_4h` score `-0.2898` n `31` status `ready` deltaP `-1.4605` edge `0.018` maxDD `-1.633`
- `news_risk_high->metal_1h` score `-0.5918` n `59` status `ready` deltaP `-4.9858` edge `-0.0069` maxDD `-0.5256`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
