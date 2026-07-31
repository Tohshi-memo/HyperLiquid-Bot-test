# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-31T11:37:26.241784+00:00`
- Price records: `672`
- Market context records: `8511`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `5882`

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

- `news_risk_high->unknown_24h` score `6276.4221` n `52` status `ready` deltaP `44.7383` edge `522.779` maxDD `-2.0332`
- `news_risk_high->equity_4h` score `5.7274` n `64` status `ready` deltaP `21.4177` edge `0.3942` maxDD `-3.4427`
- `news_risk_high->index_4h` score `1.9915` n `64` status `ready` deltaP `16.5015` edge `0.075` maxDD `-0.191`
- `news_risk_high->equity_1h` score `1.7134` n `64` status `ready` deltaP `15.8028` edge `0.0851` maxDD `-2.4803`
- `news_risk_high->crypto_major_4h` score `0.8869` n `64` status `ready` deltaP `5.8308` edge `0.1524` maxDD `-3.5385`
- `news_risk_high->crypto_alt_4h` score `0.8077` n `64` status `ready` deltaP `14.3293` edge `0.1472` maxDD `-5.8012`
- `news_risk_high->crypto_alt_1h` score `0.5692` n `64` status `ready` deltaP `9.3095` edge `0.0636` maxDD `-1.8813`
- `news_risk_high->crypto_major_1h` score `0.3392` n `64` status `ready` deltaP `6.6149` edge `0.0506` maxDD `-2.0972`
- `market_context_high->equity_1h` score `0.307` n `39` status `ready` deltaP `1.3397` edge `0.0458` maxDD `-0.9985`
- `market_context_high->index_1h` score `0.1091` n `39` status `ready` deltaP `5.3816` edge `-0.0022` maxDD `-0.2417`
- `news_risk_high->fx_1h` score `0.101` n `64` status `ready` deltaP `5.5857` edge `0.0038` maxDD `-0.2475`
- `news_risk_high->index_1h` score `0.0395` n `64` status `ready` deltaP `4.2197` edge `0.0086` maxDD `-0.5338`
- `news_risk_high->fx_4h` score `-0.0014` n `64` status `ready` deltaP `11.1662` edge `0.0212` maxDD `-0.6604`
- `market_context_high->commodity_1h` score `-0.0362` n `39` status `ready` deltaP `8.2067` edge `0.0032` maxDD `-2.0038`
- `news_risk_high->metal_4h` score `-0.0674` n `64` status `ready` deltaP `1.1052` edge `0.0316` maxDD `-0.8085`
- `market_context_high->crypto_major_1h` score `-0.138` n `39` status `ready` deltaP `5.2127` edge `-0.0027` maxDD `-1.9791`
- `news_risk_high->metal_1h` score `-0.1407` n `64` status `ready` deltaP `3.1063` edge `0.0079` maxDD `-0.5599`
- `market_context_high->metal_1h` score `-0.1811` n `39` status `ready` deltaP `3.2666` edge `-0.0082` maxDD `-0.6101`
- `market_context_high->fx_1h` score `-0.6308` n `39` status `ready` deltaP `-5.5121` edge `0.0024` maxDD `-0.3888`
- `market_context_high->crypto_alt_1h` score `-0.6958` n `39` status `ready` deltaP `-7.4774` edge `0.0108` maxDD `-2.012`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
