# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-24T08:37:35.017165+00:00`
- Price records: `672`
- Market context records: `4604`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9851`

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

- `market_context_high->unknown_1h` score `68.5522` n `148` status `ready` deltaP `6.6273` edge `5.7144` maxDD `-2.0052`
- `market_context_high->unknown_4h` score `4.1959` n `148` status `ready` deltaP `8.9856` edge `0.4108` maxDD `-4.6834`
- `market_context_high->commodity_1h` score `-0.4991` n `148` status `ready` deltaP `1.8611` edge `0.0256` maxDD `-2.0345`
- `market_context_high->fx_1h` score `-0.5423` n `148` status `ready` deltaP `-1.5092` edge `-0.004` maxDD `-1.1038`
- `market_context_high->fx_4h` score `-0.7399` n `148` status `ready` deltaP `2.0682` edge `-0.0004` maxDD `-1.9927`
- `market_context_high->index_4h` score `-0.9335` n `148` status `ready` deltaP `1.0506` edge `-0.0144` maxDD `-5.9823`
- `market_context_high->equity_1h` score `-0.9358` n `148` status `ready` deltaP `-2.9212` edge `-0.0018` maxDD `-5.5624`
- `market_context_high->commodity_4h` score `-1.1566` n `148` status `ready` deltaP `3.8069` edge `0.0371` maxDD `-9.1941`
- `market_context_high->index_1h` score `-1.7284` n `148` status `ready` deltaP `-4.4951` edge `-0.0132` maxDD `-2.7358`
- `market_context_high->equity_4h` score `-1.7899` n `148` status `ready` deltaP `-1.4337` edge `-0.043` maxDD `-8.8203`
- `market_context_high->unknown_24h` score `-2.3835` n `146` status `ready` deltaP `2.5518` edge `-0.1233` maxDD `-4.7201`
- `market_context_high->metal_1h` score `-3.0033` n `148` status `ready` deltaP `-4.661` edge `-0.0888` maxDD `-17.8795`
- `market_context_high->commodity_24h` score `-4.6712` n `146` status `ready` deltaP `11.2847` edge `0.0604` maxDD `-29.3255`
- `market_context_high->fx_24h` score `-5.3387` n `146` status `ready` deltaP `-12.5047` edge `-0.0103` maxDD `-6.0982`
- `market_context_high->crypto_alt_1h` score `-5.55` n `148` status `ready` deltaP `-2.2455` edge `-0.1188` maxDD `-22.2982`
- `market_context_high->crypto_major_1h` score `-6.8172` n `148` status `ready` deltaP `-6.077` edge `-0.1523` maxDD `-27.356`
- `market_context_high->index_24h` score `-8.3896` n `146` status `ready` deltaP `-7.9576` edge `-0.1086` maxDD `-29.3321`
- `market_context_high->crypto_alt_4h` score `-9.2429` n `148` status `ready` deltaP `-4.0294` edge `-0.2924` maxDD `-63.9243`
- `market_context_high->metal_4h` score `-10.3747` n `148` status `ready` deltaP `-7.3047` edge `-0.36` maxDD `-67.3775`
- `market_context_high->crypto_major_4h` score `-12.3841` n `148` status `ready` deltaP `-6.0358` edge `-0.4531` maxDD `-82.2164`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
