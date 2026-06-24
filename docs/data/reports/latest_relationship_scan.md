# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-24T01:22:53.943574+00:00`
- Price records: `672`
- Market context records: `4573`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9991`

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

- `market_context_high->unknown_1h` score `69.9186` n `157` status `ready` deltaP `6.585` edge `5.8327` maxDD `-2.3371`
- `market_context_high->unknown_4h` score `3.1123` n `157` status `ready` deltaP `7.4549` edge `0.3307` maxDD `-4.6834`
- `market_context_high->fx_4h` score `-0.5404` n `157` status `ready` deltaP `5.5286` edge `0.0021` maxDD `-1.9927`
- `market_context_high->commodity_1h` score `-0.6188` n `157` status `ready` deltaP `1.2491` edge `0.0197` maxDD `-2.0345`
- `market_context_high->equity_4h` score `-0.7108` n `157` status `ready` deltaP `2.1147` edge `0.0717` maxDD `-8.8203`
- `market_context_high->equity_1h` score `-0.7112` n `157` status `ready` deltaP `-2.1883` edge `0.0221` maxDD `-5.5624`
- `market_context_high->fx_1h` score `-0.737` n `157` status `ready` deltaP `-0.3976` edge `-0.0033` maxDD `-1.1038`
- `market_context_high->index_4h` score `-0.8095` n `157` status `ready` deltaP `2.6536` edge `-0.0092` maxDD `-5.9823`
- `market_context_high->commodity_4h` score `-1.1774` n `157` status `ready` deltaP `3.6614` edge `0.0354` maxDD `-9.1941`
- `market_context_high->index_1h` score `-1.5924` n `157` status `ready` deltaP `-2.9749` edge `-0.012` maxDD `-2.7358`
- `market_context_high->metal_1h` score `-2.9392` n `157` status `ready` deltaP `-4.4043` edge `-0.0823` maxDD `-17.8795`
- `market_context_high->unknown_24h` score `-2.9502` n `155` status `ready` deltaP `1.5278` edge `-0.1637` maxDD `-4.7201`
- `market_context_high->fx_24h` score `-5.4151` n `155` status `ready` deltaP `-13.2045` edge `-0.012` maxDD `-6.0982`
- `market_context_high->index_24h` score `-5.4278` n `155` status `ready` deltaP `-8.2337` edge `-0.1035` maxDD `-29.3321`
- `market_context_high->crypto_alt_1h` score `-5.4968` n `157` status `ready` deltaP `-2.6755` edge `-0.1115` maxDD `-22.2982`
- `market_context_high->commodity_24h` score `-5.8329` n `155` status `ready` deltaP `8.3815` edge `0.0425` maxDD `-34.0892`
- `market_context_high->crypto_major_1h` score `-6.7303` n `157` status `ready` deltaP `-6.0862` edge `-0.145` maxDD `-27.356`
- `market_context_high->crypto_alt_4h` score `-9.0318` n `157` status `ready` deltaP `-3.6449` edge `-0.2679` maxDD `-63.9243`
- `market_context_high->metal_4h` score `-10.2549` n `157` status `ready` deltaP `-8.4297` edge `-0.3368` maxDD `-67.4051`
- `market_context_high->crypto_major_4h` score `-11.8334` n `157` status `ready` deltaP `-2.6595` edge `-0.405` maxDD `-82.2164`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
