# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-24T01:07:35.296522+00:00`
- Price records: `672`
- Market context records: `4572`
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

- `market_context_high->unknown_1h` score `69.8827` n `157` status `ready` deltaP `6.4353` edge `5.8307` maxDD `-2.3371`
- `market_context_high->unknown_4h` score `3.0497` n `157` status `ready` deltaP `7.3025` edge `0.3265` maxDD `-4.6834`
- `market_context_high->fx_4h` score `-0.5325` n `157` status `ready` deltaP `5.681` edge `0.0021` maxDD `-1.9927`
- `market_context_high->commodity_1h` score `-0.6188` n `157` status `ready` deltaP `1.2491` edge `0.0197` maxDD `-2.0345`
- `market_context_high->equity_4h` score `-0.7084` n `157` status `ready` deltaP `2.1147` edge `0.072` maxDD `-8.8203`
- `market_context_high->equity_1h` score `-0.712` n `157` status `ready` deltaP `-2.1883` edge `0.022` maxDD `-5.5624`
- `market_context_high->fx_1h` score `-0.737` n `157` status `ready` deltaP `-0.3976` edge `-0.0033` maxDD `-1.1038`
- `market_context_high->index_4h` score `-0.8088` n `157` status `ready` deltaP `2.6536` edge `-0.0091` maxDD `-5.9823`
- `market_context_high->commodity_4h` score `-1.1759` n `157` status `ready` deltaP `3.6614` edge `0.0356` maxDD `-9.1941`
- `market_context_high->index_1h` score `-1.6067` n `157` status `ready` deltaP `-3.1246` edge `-0.0122` maxDD `-2.7358`
- `market_context_high->metal_1h` score `-2.9486` n `157` status `ready` deltaP `-4.554` edge `-0.0825` maxDD `-17.8795`
- `market_context_high->unknown_24h` score `-3.0138` n `155` status `ready` deltaP `1.5278` edge `-0.169` maxDD `-4.7201`
- `market_context_high->fx_24h` score `-5.4326` n `155` status `ready` deltaP `-13.3782` edge `-0.0123` maxDD `-6.0982`
- `market_context_high->index_24h` score `-5.4579` n `155` status `ready` deltaP `-8.4073` edge `-0.1062` maxDD `-29.3321`
- `market_context_high->crypto_alt_1h` score `-5.4956` n `157` status `ready` deltaP `-2.6755` edge `-0.1114` maxDD `-22.2982`
- `market_context_high->commodity_24h` score `-5.8221` n `155` status `ready` deltaP `8.3815` edge `0.0434` maxDD `-34.0892`
- `market_context_high->crypto_major_1h` score `-6.7279` n `157` status `ready` deltaP `-6.0862` edge `-0.1448` maxDD `-27.356`
- `market_context_high->crypto_alt_4h` score `-9.0271` n `157` status `ready` deltaP `-3.6449` edge `-0.2673` maxDD `-63.9243`
- `market_context_high->metal_4h` score `-10.2659` n `157` status `ready` deltaP `-8.5822` edge `-0.3372` maxDD `-67.4051`
- `market_context_high->crypto_major_4h` score `-11.8153` n `157` status `ready` deltaP `-2.507` edge `-0.4037` maxDD `-82.2164`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
