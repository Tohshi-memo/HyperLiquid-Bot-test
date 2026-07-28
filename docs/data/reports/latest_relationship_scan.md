# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-28T02:07:33.527621+00:00`
- Price records: `672`
- Market context records: `8152`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11842`

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

- `market_context_high->equity_24h` score `22.7847` n `78` status `ready` deltaP `44.2575` edge `1.6947` maxDD `-4.9489`
- `market_context_high->equity_4h` score `10.0883` n `79` status `ready` deltaP `37.2685` edge `0.6157` maxDD `-0.5442`
- `market_context_high->metal_24h` score `8.8692` n `78` status `ready` deltaP `38.7153` edge `0.481` maxDD `0.0`
- `news_risk_high->equity_4h` score `8.3076` n `43` status `ready` deltaP `31.9697` edge `0.4997` maxDD `-0.6428`
- `news_risk_high->crypto_major_4h` score `5.0492` n `43` status `ready` deltaP `18.6614` edge `0.3569` maxDD `-2.1767`
- `market_context_high->index_4h` score `3.9493` n `79` status `ready` deltaP `35.6379` edge `0.0958` maxDD `-0.0092`
- `market_context_high->index_24h` score `3.9113` n `78` status `ready` deltaP `24.7596` edge `0.2279` maxDD `-1.3621`
- `news_risk_high->equity_1h` score `3.8003` n `43` status `ready` deltaP `29.3796` edge `0.1517` maxDD `-1.1366`
- `market_context_high->equity_1h` score `3.6207` n `79` status `ready` deltaP `19.0764` edge `0.1955` maxDD `-0.676`
- `news_risk_high->index_4h` score `2.6347` n `43` status `ready` deltaP `22.0965` edge `0.0913` maxDD `-0.191`
- `market_context_high->metal_4h` score `2.6039` n `79` status `ready` deltaP `24.259` edge `0.1175` maxDD `-0.979`
- `market_context_high->crypto_alt_4h` score `2.5195` n `79` status `ready` deltaP `11.2766` edge `0.2465` maxDD `-3.9374`
- `market_context_high->crypto_major_4h` score `2.2979` n `79` status `ready` deltaP `13.2448` edge `0.275` maxDD `-6.7444`
- `market_context_high->fx_24h` score `2.1524` n `78` status `ready` deltaP `29.0732` edge `0.0559` maxDD `-0.6283`
- `market_context_high->commodity_24h` score `1.7899` n `78` status `ready` deltaP `32.7324` edge `0.2998` maxDD `-15.7497`
- `market_context_high->index_1h` score `1.6186` n `79` status `ready` deltaP `19.0215` edge `0.0277` maxDD `-0.2368`
- `news_risk_high->metal_4h` score `1.4521` n `43` status `ready` deltaP `14.2796` edge `0.0726` maxDD `-0.7433`
- `market_context_high->crypto_major_1h` score `1.4046` n `79` status `ready` deltaP `13.3044` edge `0.0694` maxDD `-1.6171`
- `news_risk_high->crypto_major_1h` score `1.3103` n `43` status `ready` deltaP `6.0333` edge `0.1087` maxDD `-1.1783`
- `market_context_high->metal_1h` score `1.151` n `79` status `ready` deltaP `14.8431` edge `0.0348` maxDD `-0.6936`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
