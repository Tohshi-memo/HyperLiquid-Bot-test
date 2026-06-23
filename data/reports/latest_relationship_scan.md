# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-23T21:52:32.542921+00:00`
- Price records: `672`
- Market context records: `4557`
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

- `market_context_high->unknown_1h` score `62.8528` n `158` status `ready` deltaP `6.5073` edge `5.2444` maxDD `-2.3371`
- `market_context_high->unknown_4h` score `3.1757` n `158` status `ready` deltaP `8.2471` edge `0.3307` maxDD `-4.6834`
- `market_context_high->fx_4h` score `-0.5319` n `158` status `ready` deltaP `5.6634` edge `0.0023` maxDD `-1.9927`
- `market_context_high->commodity_1h` score `-0.6852` n `158` status `ready` deltaP `0.5097` edge `0.0191` maxDD `-2.0345`
- `market_context_high->equity_4h` score `-0.7025` n `158` status `ready` deltaP `1.7791` edge `0.075` maxDD `-8.8203`
- `market_context_high->index_4h` score `-0.7035` n `158` status `ready` deltaP `4.2876` edge `-0.0065` maxDD `-5.9823`
- `market_context_high->fx_1h` score `-0.706` n `158` status `ready` deltaP `-0.055` edge `-0.003` maxDD `-1.1038`
- `market_context_high->equity_1h` score `-0.7075` n `158` status `ready` deltaP `-2.4767` edge `0.0245` maxDD `-5.5624`
- `market_context_high->commodity_4h` score `-1.1887` n `158` status `ready` deltaP `3.5196` edge `0.0349` maxDD `-9.1941`
- `market_context_high->index_1h` score `-1.5301` n `158` status `ready` deltaP `-2.3611` edge `-0.0109` maxDD `-2.7358`
- `market_context_high->metal_1h` score `-2.941` n `158` status `ready` deltaP `-4.3489` edge `-0.0829` maxDD `-17.8795`
- `market_context_high->unknown_24h` score `-3.1235` n `156` status `ready` deltaP `1.656` edge `-0.179` maxDD `-4.7201`
- `market_context_high->crypto_alt_1h` score `-5.4608` n `158` status `ready` deltaP `-2.5108` edge `-0.1096` maxDD `-22.2982`
- `market_context_high->fx_24h` score `-5.6105` n `156` status `ready` deltaP `-14.9572` edge `-0.0166` maxDD `-6.0982`
- `market_context_high->index_24h` score `-5.7898` n `156` status `ready` deltaP `-10.3498` edge `-0.1358` maxDD `-29.3321`
- `market_context_high->commodity_24h` score `-5.908` n `156` status `ready` deltaP `8.0796` edge `0.0503` maxDD `-35.0534`
- `market_context_high->crypto_major_1h` score `-6.5914` n `158` status `ready` deltaP `-5.2945` edge `-0.1387` maxDD `-27.356`
- `market_context_high->crypto_alt_4h` score `-8.8041` n `158` status `ready` deltaP `-1.9817` edge `-0.2498` maxDD `-63.9243`
- `market_context_high->metal_4h` score `-10.2924` n `158` status `ready` deltaP `-9.1058` edge `-0.3371` maxDD `-67.4051`
- `market_context_high->crypto_major_4h` score `-11.5425` n `158` status `ready` deltaP `-0.3512` edge `-0.3831` maxDD `-82.2164`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
