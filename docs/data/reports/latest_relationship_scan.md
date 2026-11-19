# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-19T20:37:28.551768+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `24`

- Symbol pattern count: `2662`

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

- `market_context_high->unknown_1h` score `11999.3925` n `108` status `ready` deltaP `0.8373` edge `999.9636` maxDD `-0.9181`
- `market_context_high->unknown_4h` score `7537.9708` n `107` status `ready` deltaP `-0.0071` edge `628.1927` maxDD `-0.6072`
- `market_context_high->crypto_major_24h` score `24.1565` n `88` status `ready` deltaP `42.8503` edge `1.7867` maxDD `-2.746`
- `market_context_high->crypto_alt_24h` score `11.9175` n `88` status `ready` deltaP `25.2683` edge `1.4987` maxDD `-7.4749`
- `market_context_high->crypto_major_4h` score `1.7258` n `107` status `ready` deltaP `3.781` edge `0.4005` maxDD `-16.2179`
- `market_context_high->crypto_alt_4h` score `1.0697` n `107` status `ready` deltaP `4.8481` edge `0.2644` maxDD `-12.9396`
- `market_context_high->metal_24h` score `0.5144` n `88` status `ready` deltaP `19.0656` edge `0.2246` maxDD `-14.7068`
- `market_context_high->metal_4h` score `0.3172` n `107` status `ready` deltaP `16.9905` edge `0.0424` maxDD `-6.0054`
- `market_context_high->crypto_major_1h` score `-0.2749` n `108` status `ready` deltaP `4.3968` edge `0.0751` maxDD `-6.5061`
- `market_context_high->index_1h` score `-0.3122` n `108` status `ready` deltaP `2.5172` edge `0.0044` maxDD `-1.2295`
- `market_context_high->metal_1h` score `-0.3244` n `108` status `ready` deltaP `3.8922` edge `0.0135` maxDD `-2.6517`
- `market_context_high->crypto_alt_1h` score `-0.7839` n `108` status `ready` deltaP `-2.5338` edge `0.0386` maxDD `-5.4428`
- `market_context_high->equity_1h` score `-1.3941` n `108` status `ready` deltaP `5.5944` edge `0.0244` maxDD `-10.8962`
- `market_context_high->fx_1h` score `-1.6564` n `108` status `ready` deltaP `-11.9982` edge `-0.0021` maxDD `-0.4757`
- `market_context_high->index_4h` score `-2.0419` n `107` status `ready` deltaP `-4.113` edge `-0.0084` maxDD `-4.7471`
- `market_context_high->commodity_1h` score `-2.4007` n `108` status `ready` deltaP `-9.6696` edge `-0.0274` maxDD `-3.9892`
- `market_context_high->fx_4h` score `-2.4049` n `107` status `ready` deltaP `-15.335` edge `-0.0045` maxDD `-1.794`
- `market_context_high->fx_24h` score `-7.262` n `88` status `ready` deltaP `-24.9842` edge `-0.0113` maxDD `-5.5179`
- `market_context_high->commodity_4h` score `-8.1107` n `107` status `ready` deltaP `-29.1615` edge `-0.1122` maxDD `-15.5426`
- `market_context_high->equity_4h` score `-9.9499` n `107` status `ready` deltaP `-8.5608` edge `-0.1044` maxDD `-43.0813`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
