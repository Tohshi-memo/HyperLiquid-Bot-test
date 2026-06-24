# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-24T06:22:33.463147+00:00`
- Price records: `672`
- Market context records: `4595`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9905`

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

- `market_context_high->unknown_1h` score `68.4635` n `148` status `ready` deltaP `6.0285` edge `5.711` maxDD `-2.0052`
- `market_context_high->unknown_4h` score `4.0458` n `148` status `ready` deltaP `7.9185` edge `0.4054` maxDD `-4.6834`
- `market_context_high->fx_1h` score `-0.5493` n `148` status `ready` deltaP `-1.6589` edge `-0.0039` maxDD `-1.1038`
- `market_context_high->commodity_1h` score `-0.5901` n `148` status `ready` deltaP `0.9629` edge `0.024` maxDD `-2.0345`
- `market_context_high->fx_4h` score `-0.7265` n `148` status `ready` deltaP `2.2206` edge `0.0003` maxDD `-1.9927`
- `market_context_high->index_4h` score `-0.9162` n `148` status `ready` deltaP `1.2031` edge `-0.0132` maxDD `-5.9823`
- `market_context_high->equity_1h` score `-0.9895` n `148` status `ready` deltaP `-3.6697` edge `-0.0037` maxDD `-5.5624`
- `market_context_high->commodity_4h` score `-1.2343` n `148` status `ready` deltaP `3.1971` edge `0.0312` maxDD `-9.1941`
- `market_context_high->equity_4h` score `-1.6659` n `148` status `ready` deltaP `-0.5191` edge `-0.0332` maxDD `-8.8203`
- `market_context_high->index_1h` score `-1.744` n `148` status `ready` deltaP `-4.6448` edge `-0.0135` maxDD `-2.7358`
- `market_context_high->unknown_24h` score `-2.745` n `146` status `ready` deltaP `1.8574` edge `-0.1488` maxDD `-4.7201`
- `market_context_high->metal_1h` score `-3.0064` n `148` status `ready` deltaP `-4.661` edge `-0.0892` maxDD `-17.8795`
- `market_context_high->commodity_24h` score `-4.5476` n `146` status `ready` deltaP `11.2847` edge `0.0707` maxDD `-29.3255`
- `market_context_high->fx_24h` score `-5.4841` n `146` status `ready` deltaP `-14.0672` edge `-0.012` maxDD `-6.0982`
- `market_context_high->crypto_alt_1h` score `-5.6003` n `148` status `ready` deltaP `-2.6946` edge `-0.12` maxDD `-22.2982`
- `market_context_high->crypto_major_1h` score `-6.9202` n `148` status `ready` deltaP `-6.8255` edge `-0.1559` maxDD `-27.356`
- `market_context_high->index_24h` score `-8.5552` n `146` status `ready` deltaP `-7.9576` edge `-0.1224` maxDD `-29.3321`
- `market_context_high->crypto_alt_4h` score `-9.1011` n `148` status `ready` deltaP `-3.2672` edge `-0.2793` maxDD `-63.9243`
- `market_context_high->metal_4h` score `-10.2659` n `148` status `ready` deltaP `-5.9328` edge `-0.3552` maxDD `-67.3775`
- `market_context_high->crypto_major_4h` score `-12.238` n `148` status `ready` deltaP `-4.8163` edge `-0.4425` maxDD `-82.2164`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
