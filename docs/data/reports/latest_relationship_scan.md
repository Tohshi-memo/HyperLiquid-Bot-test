# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-06T11:22:30.002696+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8702`

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

- `market_context_high->unknown_24h` score `95.8704` n `117` status `ready` deltaP `10.3974` edge `7.9579` maxDD `-1.3748`
- `news_risk_high->crypto_major_4h` score `9.5582` n `62` status `ready` deltaP `34.1611` edge `0.5891` maxDD `-0.6258`
- `news_risk_high->crypto_alt_4h` score `5.6351` n `62` status `ready` deltaP `20.1908` edge `0.4694` maxDD `-6.4195`
- `news_risk_high->equity_24h` score `3.499` n `62` status `ready` deltaP `10.7305` edge `0.23` maxDD `-0.1298`
- `news_risk_high->index_24h` score `3.2256` n `62` status `ready` deltaP `22.6804` edge `0.1176` maxDD `0.0`
- `market_context_high->crypto_major_4h` score `2.8134` n `117` status `ready` deltaP `14.0205` edge `0.2374` maxDD `-4.047`
- `news_risk_high->index_4h` score `2.5549` n `62` status `ready` deltaP `28.8012` edge `0.0471` maxDD `-0.4296`
- `news_risk_high->crypto_major_1h` score `1.9875` n `62` status `ready` deltaP `7.7796` edge `0.1493` maxDD `-1.5096`
- `news_risk_high->index_1h` score `1.7935` n `62` status `ready` deltaP `22.9284` edge `0.0116` maxDD `-0.1997`
- `news_risk_high->equity_4h` score `1.703` n `62` status `ready` deltaP `16.8618` edge `0.0893` maxDD `-2.7837`
- `market_context_high->commodity_4h` score `1.1885` n `117` status `ready` deltaP `16.2967` edge `0.0604` maxDD `-1.6002`
- `news_risk_high->metal_4h` score `1.1844` n `62` status `ready` deltaP `17.2846` edge `0.0782` maxDD `-0.993`
- `market_context_high->fx_4h` score `1.1161` n `117` status `ready` deltaP `21.9421` edge `0.0224` maxDD `-0.3868`
- `market_context_high->fx_1h` score `0.7935` n `117` status `ready` deltaP `13.2914` edge `0.0059` maxDD `-0.271`
- `market_context_high->commodity_1h` score `0.7346` n `117` status `ready` deltaP `11.9057` edge `0.0215` maxDD `-0.5059`
- `news_risk_high->commodity_24h` score `0.7343` n `62` status `ready` deltaP `27.0092` edge `0.0707` maxDD `-8.196`
- `news_risk_high->crypto_alt_1h` score `0.7148` n `62` status `ready` deltaP `2.4097` edge `0.0954` maxDD `-2.4854`
- `market_context_high->crypto_alt_4h` score `0.5103` n `117` status `ready` deltaP `-0.7218` edge `0.2197` maxDD `-7.1222`
- `news_risk_high->metal_1h` score `-0.0863` n `62` status `ready` deltaP `4.5055` edge `0.0046` maxDD `-1.0132`
- `market_context_high->crypto_major_1h` score `-0.1282` n `117` status `ready` deltaP `7.3661` edge `0.0291` maxDD `-3.7778`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
