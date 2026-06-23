# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-23T21:37:30.909140+00:00`
- Price records: `672`
- Market context records: `4556`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `10045`

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

- `market_context_high->unknown_1h` score `62.3339` n `159` status `ready` deltaP `6.7262` edge `5.1997` maxDD `-2.3371`
- `market_context_high->unknown_4h` score `3.0173` n `159` status `ready` deltaP `7.9777` edge `0.3193` maxDD `-4.6834`
- `market_context_high->fx_4h` score `-0.5149` n `159` status `ready` deltaP `5.9739` edge `0.0024` maxDD `-1.9927`
- `market_context_high->equity_1h` score `-0.6892` n `159` status `ready` deltaP `-2.1702` edge `0.0248` maxDD `-5.5624`
- `market_context_high->fx_1h` score `-0.6921` n `159` status `ready` deltaP `0.1337` edge `-0.0031` maxDD `-1.1038`
- `market_context_high->equity_4h` score `-0.6971` n `159` status `ready` deltaP `1.8973` edge `0.0749` maxDD `-8.8203`
- `market_context_high->commodity_1h` score `-0.7105` n `159` status `ready` deltaP `0.2231` edge `0.0189` maxDD `-2.0345`
- `market_context_high->index_4h` score `-0.7141` n `159` status `ready` deltaP `4.0699` edge `-0.0064` maxDD `-5.9823`
- `market_context_high->commodity_4h` score `-1.2061` n `159` status `ready` deltaP `3.229` edge `0.0346` maxDD `-9.1941`
- `market_context_high->index_1h` score `-1.5004` n `159` status `ready` deltaP `-2.0506` edge `-0.0105` maxDD `-2.7358`
- `market_context_high->metal_1h` score `-2.9166` n `159` status `ready` deltaP `-3.9986` edge `-0.0821` maxDD `-17.8795`
- `market_context_high->unknown_24h` score `-3.0438` n `157` status `ready` deltaP `1.7826` edge `-0.1732` maxDD `-4.7201`
- `market_context_high->crypto_alt_1h` score `-5.4647` n `159` status `ready` deltaP `-2.6795` edge `-0.1088` maxDD `-22.2982`
- `market_context_high->fx_24h` score `-5.6279` n `157` status `ready` deltaP `-15.145` edge `-0.0168` maxDD `-6.0982`
- `market_context_high->index_24h` score `-5.7718` n `157` status `ready` deltaP `-10.2132` edge `-0.1344` maxDD `-29.3321`
- `market_context_high->commodity_24h` score `-6.1018` n `157` status `ready` deltaP `7.7815` edge `0.0469` maxDD `-35.9138`
- `market_context_high->crypto_major_1h` score `-6.5403` n `159` status `ready` deltaP `-4.9561` edge `-0.1367` maxDD `-27.356`
- `market_context_high->crypto_alt_4h` score `-8.762` n `159` status `ready` deltaP `-1.6672` edge `-0.2465` maxDD `-63.9243`
- `market_context_high->metal_4h` score `-10.2623` n `159` status `ready` deltaP `-8.8722` edge `-0.3348` maxDD `-67.4051`
- `market_context_high->crypto_major_4h` score `-11.4969` n `159` status `ready` deltaP `-0.0288` edge `-0.3794` maxDD `-82.2164`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
