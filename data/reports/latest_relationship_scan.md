# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-24T04:52:27.558827+00:00`
- Price records: `672`
- Market context records: `4588`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9937`

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

- `market_context_high->unknown_1h` score `72.4` n `153` status `ready` deltaP `6.4176` edge `6.0406` maxDD `-2.3371`
- `market_context_high->unknown_4h` score `3.7999` n `153` status `ready` deltaP `8.1301` edge `0.3835` maxDD `-4.6834`
- `market_context_high->commodity_1h` score `-0.5516` n `153` status `ready` deltaP `1.5498` edge `0.0233` maxDD `-2.0345`
- `market_context_high->fx_4h` score `-0.6602` n `153` status `ready` deltaP `3.3756` edge `0.0011` maxDD `-1.9927`
- `market_context_high->index_4h` score `-0.8419` n `153` status `ready` deltaP `2.1809` edge `-0.0102` maxDD `-5.9823`
- `market_context_high->fx_1h` score `-0.8506` n `153` status `ready` deltaP `-1.7583` edge `-0.0037` maxDD `-1.1038`
- `market_context_high->equity_1h` score `-0.9129` n `153` status `ready` deltaP `-2.8717` edge `0.0008` maxDD `-5.5624`
- `market_context_high->commodity_4h` score `-1.1418` n `153` status `ready` deltaP `4.3759` edge `0.0352` maxDD `-9.1941`
- `market_context_high->equity_4h` score `-1.3554` n `153` status `ready` deltaP `0.9824` edge `-0.0034` maxDD `-8.8203`
- `market_context_high->index_1h` score `-1.6284` n `153` status `ready` deltaP `-3.4705` edge `-0.0117` maxDD `-2.7358`
- `market_context_high->unknown_24h` score `-2.5686` n `151` status `ready` deltaP `1.6924` edge `-0.133` maxDD `-4.7201`
- `market_context_high->metal_1h` score `-2.8901` n `153` status `ready` deltaP `-3.3101` edge `-0.0833` maxDD `-17.8795`
- `market_context_high->commodity_24h` score `-5.0882` n `151` status `ready` deltaP `9.6291` edge `0.0507` maxDD `-30.4463`
- `market_context_high->fx_24h` score `-5.3517` n `151` status `ready` deltaP `-12.6368` edge `-0.0105` maxDD `-6.0982`
- `market_context_high->crypto_alt_1h` score `-5.3815` n `153` status `ready` deltaP `-1.4148` edge `-0.1103` maxDD `-22.2982`
- `market_context_high->crypto_major_1h` score `-6.7366` n `153` status `ready` deltaP `-5.8951` edge `-0.1468` maxDD `-27.356`
- `market_context_high->index_24h` score `-8.1748` n `151` status `ready` deltaP `-7.1019` edge `-0.0964` maxDD `-29.3321`
- `market_context_high->crypto_alt_4h` score `-9.0774` n `153` status `ready` deltaP `-3.8767` edge `-0.2722` maxDD `-63.9243`
- `market_context_high->metal_4h` score `-10.2121` n `153` status `ready` deltaP `-6.9086` edge `-0.3418` maxDD `-67.3775`
- `market_context_high->crypto_major_4h` score `-12.0542` n `153` status `ready` deltaP `-4.1607` edge `-0.4233` maxDD `-82.2164`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
