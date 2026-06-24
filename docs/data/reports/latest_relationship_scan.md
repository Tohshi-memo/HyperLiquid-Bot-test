# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-24T08:07:28.887637+00:00`
- Price records: `672`
- Market context records: `4602`
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

- `market_context_high->unknown_1h` score `68.551` n `148` status `ready` deltaP `6.6273` edge `5.7143` maxDD `-2.0052`
- `market_context_high->unknown_4h` score `4.1935` n `148` status `ready` deltaP `8.9856` edge `0.4106` maxDD `-4.6834`
- `market_context_high->commodity_1h` score `-0.529` n `148` status `ready` deltaP `1.5617` edge `0.0251` maxDD `-2.0345`
- `market_context_high->fx_1h` score `-0.5579` n `148` status `ready` deltaP `-1.8086` edge `-0.004` maxDD `-1.1038`
- `market_context_high->fx_4h` score `-0.7312` n `148` status `ready` deltaP `2.2206` edge `-0.0003` maxDD `-1.9927`
- `market_context_high->index_4h` score `-0.9209` n `148` status `ready` deltaP `1.2031` edge `-0.0138` maxDD `-5.9823`
- `market_context_high->equity_1h` score `-0.9342` n `148` status `ready` deltaP `-2.9212` edge `-0.0016` maxDD `-5.5624`
- `market_context_high->commodity_4h` score `-1.1849` n `148` status `ready` deltaP `3.502` edge `0.0355` maxDD `-9.1941`
- `market_context_high->index_1h` score `-1.7284` n `148` status `ready` deltaP `-4.4951` edge `-0.0132` maxDD `-2.7358`
- `market_context_high->equity_4h` score `-1.7444` n `148` status `ready` deltaP `-1.1288` edge `-0.0392` maxDD `-8.8203`
- `market_context_high->unknown_24h` score `-2.4586` n `146` status `ready` deltaP `2.3782` edge `-0.1284` maxDD `-4.7201`
- `market_context_high->metal_1h` score `-3.004` n `148` status `ready` deltaP `-4.661` edge `-0.0889` maxDD `-17.8795`
- `market_context_high->commodity_24h` score `-4.652` n `146` status `ready` deltaP `11.2847` edge `0.062` maxDD `-29.3255`
- `market_context_high->fx_24h` score `-5.3701` n `146` status `ready` deltaP `-12.8519` edge `-0.0106` maxDD `-6.0982`
- `market_context_high->crypto_alt_1h` score `-5.5308` n `148` status `ready` deltaP `-2.0958` edge `-0.1182` maxDD `-22.2982`
- `market_context_high->crypto_major_1h` score `-6.8148` n `148` status `ready` deltaP `-6.077` edge `-0.1521` maxDD `-27.356`
- `market_context_high->index_24h` score `-8.422` n `146` status `ready` deltaP `-7.9576` edge `-0.1113` maxDD `-29.3321`
- `market_context_high->crypto_alt_4h` score `-9.1794` n `148` status `ready` deltaP `-3.7245` edge `-0.2863` maxDD `-63.9243`
- `market_context_high->metal_4h` score `-10.351` n `148` status `ready` deltaP `-6.9998` edge `-0.359` maxDD `-67.3775`
- `market_context_high->crypto_major_4h` score `-12.3285` n `148` status `ready` deltaP `-5.7309` edge `-0.448` maxDD `-82.2164`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
