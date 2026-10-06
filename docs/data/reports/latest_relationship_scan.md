# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-06T18:22:26.299276+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8730`

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

- `market_context_high->unknown_24h` score `1546.8778` n `117` status `ready` deltaP `11.0847` edge `128.8706` maxDD `-1.3748`
- `market_context_high->unknown_4h` score `28.7547` n `117` status `ready` deltaP `-0.3583` edge `2.4525` maxDD `-2.3109`
- `news_risk_high->crypto_major_4h` score `9.0005` n `62` status `ready` deltaP `32.4843` edge `0.5538` maxDD `-0.6258`
- `news_risk_high->crypto_alt_4h` score `5.1196` n `62` status `ready` deltaP `18.6664` edge `0.4366` maxDD `-6.4195`
- `news_risk_high->index_24h` score `3.0868` n `62` status `ready` deltaP `21.6495` edge `0.1129` maxDD `0.0`
- `news_risk_high->equity_24h` score `2.7181` n `62` status `ready` deltaP `7.8096` edge `0.1844` maxDD `-0.1298`
- `news_risk_high->index_4h` score `2.4759` n `62` status `ready` deltaP `28.039` edge `0.0456` maxDD `-0.4296`
- `market_context_high->crypto_major_4h` score `2.2556` n `117` status `ready` deltaP `12.3437` edge `0.2021` maxDD `-4.047`
- `news_risk_high->crypto_major_1h` score `1.8532` n `62` status `ready` deltaP `7.0311` edge `0.1431` maxDD `-1.5096`
- `news_risk_high->index_1h` score `1.7911` n `62` status `ready` deltaP `22.9284` edge `0.0114` maxDD `-0.1997`
- `news_risk_high->equity_4h` score `1.4015` n `62` status `ready` deltaP `14.7276` edge `0.0784` maxDD `-2.7837`
- `news_risk_high->metal_4h` score `1.1939` n `62` status `ready` deltaP `17.437` edge `0.0784` maxDD `-0.993`
- `news_risk_high->commodity_24h` score `0.9749` n `62` status `ready` deltaP `29.0711` edge `0.0878` maxDD `-8.196`
- `market_context_high->fx_4h` score `0.8678` n `117` status `ready` deltaP `19.1982` edge `0.02` maxDD `-0.3868`
- `market_context_high->commodity_4h` score `0.8204` n `117` status `ready` deltaP `13.7052` edge `0.047` maxDD `-1.6002`
- `market_context_high->fx_1h` score `0.6653` n `117` status `ready` deltaP `11.7944` edge `0.0052` maxDD `-0.271`
- `news_risk_high->crypto_alt_1h` score `0.6548` n `62` status `ready` deltaP `2.4097` edge `0.0904` maxDD `-2.4854`
- `market_context_high->commodity_1h` score `0.5452` n `117` status `ready` deltaP `10.259` edge `0.0167` maxDD `-0.5059`
- `market_context_high->crypto_alt_4h` score `-0.0052` n `117` status `ready` deltaP `-2.2462` edge `0.1869` maxDD `-7.1222`
- `news_risk_high->metal_1h` score `-0.1091` n `62` status `ready` deltaP `4.3558` edge `0.0037` maxDD `-1.0132`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
