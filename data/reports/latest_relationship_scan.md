# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-02T10:37:25.558814+00:00`
- Price records: `672`
- Market context records: `5446`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11438`

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

- `market_context_high->equity_24h` score `4.1595` n `185` status `ready` deltaP `11.8694` edge `0.6211` maxDD `-21.6219`
- `market_context_high->crypto_major_4h` score `3.3029` n `196` status `ready` deltaP `16.003` edge `0.3978` maxDD `-14.0065`
- `market_context_high->crypto_major_24h` score `3.2214` n `185` status `ready` deltaP `17.5911` edge `0.6052` maxDD `-29.6555`
- `market_context_high->equity_4h` score `2.7588` n `196` status `ready` deltaP `13.1191` edge `0.3063` maxDD `-7.4425`
- `market_context_high->crypto_alt_4h` score `2.5235` n `196` status `ready` deltaP `11.0659` edge `0.3006` maxDD `-9.46`
- `market_context_high->equity_1h` score `0.5459` n `199` status `ready` deltaP `8.4622` edge `0.0856` maxDD `-5.0555`
- `market_context_high->fx_24h` score `0.3014` n `185` status `ready` deltaP `11.692` edge `0.0367` maxDD `-0.8294`
- `market_context_high->index_1h` score `0.1702` n `199` status `ready` deltaP `6.9336` edge `0.0173` maxDD `-0.9472`
- `market_context_high->crypto_alt_1h` score `-0.2734` n `199` status `ready` deltaP `1.406` edge `0.064` maxDD `-5.0257`
- `market_context_high->metal_1h` score `-0.3312` n `199` status `ready` deltaP `3.3626` edge `0.0175` maxDD `-2.0682`
- `market_context_high->crypto_major_1h` score `-0.3679` n `199` status `ready` deltaP `2.4433` edge `0.0776` maxDD `-6.9639`
- `market_context_high->fx_1h` score `-0.5656` n `199` status `ready` deltaP `0.2618` edge `0.0` maxDD `-0.577`
- `market_context_high->index_4h` score `-0.7625` n `196` status `ready` deltaP `7.9921` edge `0.0441` maxDD `-2.874`
- `market_context_high->index_24h` score `-1.1286` n `185` status `ready` deltaP `16.1627` edge `0.0968` maxDD `-12.5551`
- `market_context_high->fx_4h` score `-1.1418` n `196` status `ready` deltaP `0.5942` edge `0.0034` maxDD `-1.5345`
- `market_context_high->commodity_1h` score `-1.4427` n `199` status `ready` deltaP `-2.8706` edge `-0.0063` maxDD `-3.5831`
- `market_context_high->metal_4h` score `-2.6632` n `196` status `ready` deltaP `-8.4277` edge `-0.0328` maxDD `-12.8631`
- `market_context_high->commodity_4h` score `-4.2733` n `196` status `ready` deltaP `-6.8224` edge `-0.0468` maxDD `-14.1062`
- `market_context_high->crypto_alt_24h` score `-7.4563` n `185` status `ready` deltaP `8.3033` edge `0.193` maxDD `-54.2437`
- `market_context_high->metal_24h` score `-7.4908` n `185` status `ready` deltaP `-5.7742` edge `-0.1841` maxDD `-33.021`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
