# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-10T01:22:24.741106+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `88`

- Symbol pattern count: `10906`

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

- `market_context_high->commodity_4h` score `1.4073` n `156` status `ready` deltaP `15.881` edge `0.0787` maxDD `-2.7169`
- `market_context_high->commodity_1h` score `0.8425` n `168` status `ready` deltaP `10.9959` edge `0.0312` maxDD `-0.7439`
- `market_context_high->fx_24h` score `0.4367` n `135` status `ready` deltaP `18.3217` edge `0.0205` maxDD `-1.9329`
- `market_context_high->fx_1h` score `-0.2376` n `168` status `ready` deltaP `3.1188` edge `-0.0017` maxDD `-0.9639`
- `market_context_high->fx_4h` score `-0.3503` n `156` status `ready` deltaP `4.4872` edge `0.0005` maxDD `-1.6928`
- `market_context_high->index_24h` score `-0.5768` n `135` status `ready` deltaP `1.8866` edge `0.0925` maxDD `-5.9181`
- `market_context_high->index_1h` score `-0.5867` n `168` status `ready` deltaP `-3.3005` edge `-0.0055` maxDD `-0.8168`
- `market_context_high->metal_24h` score `-0.6252` n `135` status `ready` deltaP `-1.6551` edge `0.0457` maxDD `-2.2743`
- `market_context_high->equity_24h` score `-0.7636` n `135` status `ready` deltaP `0.5324` edge `0.2388` maxDD `-21.1456`
- `market_context_high->metal_1h` score `-0.8106` n `168` status `ready` deltaP `-4.794` edge `-0.0109` maxDD `-1.8847`
- `market_context_high->equity_1h` score `-0.8212` n `168` status `ready` deltaP `-2.1528` edge `-0.0039` maxDD `-4.6286`
- `market_context_high->index_4h` score `-0.8752` n `156` status `ready` deltaP `-4.0533` edge `-0.0112` maxDD `-1.2518`
- `market_context_high->metal_4h` score `-1.49` n `156` status `ready` deltaP `-5.3588` edge `-0.0298` maxDD `-4.7066`
- `market_context_high->crypto_alt_1h` score `-1.5805` n `168` status `ready` deltaP `-9.121` edge `-0.0397` maxDD `-5.5029`
- `market_context_high->crypto_major_1h` score `-2.3976` n `168` status `ready` deltaP `-10.5753` edge `-0.0635` maxDD `-10.5372`
- `market_context_high->equity_4h` score `-3.1978` n `156` status `ready` deltaP `-5.0226` edge `-0.0826` maxDD `-7.6983`
- `market_context_high->crypto_alt_24h` score `-4.5123` n `135` status `ready` deltaP `-11.7477` edge `-0.1534` maxDD `-4.5445`
- `market_context_high->crypto_major_24h` score `-4.6367` n `135` status `ready` deltaP `-1.0301` edge `-0.1301` maxDD `-14.2873`
- `market_context_high->crypto_alt_4h` score `-5.4551` n `156` status `ready` deltaP `-11.4682` edge `-0.1505` maxDD `-11.5444`
- `market_context_high->unknown_1h` score `-7.5798` n `168` status `ready` deltaP `-4.9116` edge `-0.5532` maxDD `-1.323`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
