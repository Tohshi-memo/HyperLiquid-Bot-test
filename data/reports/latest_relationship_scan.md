# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-24T08:22:26.908985+00:00`
- Price records: `672`
- Market context records: `4603`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9849`

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

- `market_context_high->unknown_1h` score `68.5654` n `148` status `ready` deltaP `6.777` edge `5.7145` maxDD `-2.0052`
- `market_context_high->unknown_4h` score `4.1983` n `148` status `ready` deltaP `8.9856` edge `0.411` maxDD `-4.6834`
- `market_context_high->commodity_1h` score `-0.5135` n `148` status `ready` deltaP `1.7114` edge `0.0254` maxDD `-2.0345`
- `market_context_high->fx_1h` score `-0.5501` n `148` status `ready` deltaP `-1.6589` edge `-0.004` maxDD `-1.1038`
- `market_context_high->fx_4h` score `-0.7399` n `148` status `ready` deltaP `2.0682` edge `-0.0004` maxDD `-1.9927`
- `market_context_high->index_4h` score `-0.924` n `148` status `ready` deltaP `1.2031` edge `-0.0142` maxDD `-5.9823`
- `market_context_high->equity_1h` score `-0.935` n `148` status `ready` deltaP `-2.9212` edge `-0.0017` maxDD `-5.5624`
- `market_context_high->commodity_4h` score `-1.1692` n `148` status `ready` deltaP `3.6544` edge `0.0365` maxDD `-9.1941`
- `market_context_high->index_1h` score `-1.7284` n `148` status `ready` deltaP `-4.4951` edge `-0.0132` maxDD `-2.7358`
- `market_context_high->equity_4h` score `-1.7695` n `148` status `ready` deltaP `-1.2813` edge `-0.0414` maxDD `-8.8203`
- `market_context_high->unknown_24h` score `-2.4111` n `146` status `ready` deltaP `2.5518` edge `-0.1256` maxDD `-4.7201`
- `market_context_high->metal_1h` score `-3.0033` n `148` status `ready` deltaP `-4.661` edge `-0.0888` maxDD `-17.8795`
- `market_context_high->commodity_24h` score `-4.6616` n `146` status `ready` deltaP `11.2847` edge `0.0612` maxDD `-29.3255`
- `market_context_high->fx_24h` score `-5.355` n `146` status `ready` deltaP `-12.6783` edge `-0.0105` maxDD `-6.0982`
- `market_context_high->crypto_alt_1h` score `-5.5344` n `148` status `ready` deltaP `-2.0958` edge `-0.1185` maxDD `-22.2982`
- `market_context_high->crypto_major_1h` score `-6.8148` n `148` status `ready` deltaP `-6.077` edge `-0.1521` maxDD `-27.356`
- `market_context_high->index_24h` score `-8.4064` n `146` status `ready` deltaP `-7.9576` edge `-0.11` maxDD `-29.3321`
- `market_context_high->crypto_alt_4h` score `-9.2123` n `148` status `ready` deltaP `-3.8769` edge `-0.2895` maxDD `-63.9243`
- `market_context_high->metal_4h` score `-10.3636` n `148` status `ready` deltaP `-7.1523` edge `-0.3596` maxDD `-67.3775`
- `market_context_high->crypto_major_4h` score `-12.3567` n `148` status `ready` deltaP `-5.8834` edge `-0.4506` maxDD `-82.2164`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
