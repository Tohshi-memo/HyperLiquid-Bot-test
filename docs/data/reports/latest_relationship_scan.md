# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-01T14:02:45.320897+00:00`
- Price records: `672`
- Market context records: `8628`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `5898`

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

- `news_risk_high->unknown_24h` score `5191.5234` n `60` status `ready` deltaP `34.2345` edge `432.4408` maxDD `-2.0332`
- `market_context_high->crypto_alt_24h` score `17.1176` n `47` status `ready` deltaP `53.5345` edge `1.1093` maxDD `-2.1786`
- `news_risk_high->equity_4h` score `6.2603` n `60` status `ready` deltaP `21.7784` edge `0.4362` maxDD `-3.4427`
- `news_risk_high->index_4h` score `2.5266` n `60` status `ready` deltaP `21.9309` edge `0.0834` maxDD `-0.191`
- `news_risk_high->equity_1h` score `1.6999` n `60` status `ready` deltaP `15.0799` edge `0.0888` maxDD `-2.4803`
- `news_risk_high->crypto_major_4h` score `1.2103` n `60` status `ready` deltaP `7.7439` edge `0.1811` maxDD `-3.5385`
- `market_context_high->commodity_24h` score `0.8783` n `47` status `ready` deltaP `22.7553` edge `0.1762` maxDD `-11.5569`
- `market_context_high->crypto_alt_4h` score `0.6868` n `56` status `ready` deltaP `10.1481` edge `0.1161` maxDD `-5.323`
- `news_risk_high->crypto_alt_4h` score `0.451` n `60` status `ready` deltaP `11.2195` edge `0.1222` maxDD `-5.8012`
- `news_risk_high->crypto_alt_1h` score `0.442` n `60` status `ready` deltaP `8.3333` edge `0.0538` maxDD `-1.8813`
- `news_risk_high->crypto_major_1h` score `0.3279` n `60` status `ready` deltaP `6.2176` edge `0.0518` maxDD `-2.0972`
- `news_risk_high->fx_4h` score `0.3278` n `60` status `ready` deltaP `14.7561` edge `0.0247` maxDD `-0.6604`
- `market_context_high->fx_24h` score `0.3014` n `47` status `ready` deltaP `13.2343` edge `0.0442` maxDD `-2.1692`
- `news_risk_high->metal_4h` score `0.1289` n `60` status `ready` deltaP `4.3699` edge `0.035` maxDD `-0.8085`
- `market_context_high->commodity_1h` score `0.1091` n `56` status `ready` deltaP `6.8541` edge `0.0175` maxDD `-1.3282`
- `market_context_high->fx_4h` score `0.097` n `56` status `ready` deltaP `11.5418` edge `0.0151` maxDD `-1.3685`
- `news_risk_high->fx_1h` score `0.0947` n `60` status `ready` deltaP `5.2994` edge `0.0049` maxDD `-0.2475`
- `news_risk_high->metal_1h` score `0.0679` n `60` status `ready` deltaP `5.6387` edge `0.0084` maxDD `-0.5599`
- `news_risk_high->index_1h` score `0.0173` n `60` status `ready` deltaP `3.6727` edge `0.0094` maxDD `-0.5338`
- `market_context_high->fx_1h` score `-0.2874` n `56` status `ready` deltaP `3.8708` edge `0.0005` maxDD `-0.6874`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
