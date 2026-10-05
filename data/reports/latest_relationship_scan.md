# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-05T13:07:27.954746+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `80`

- Symbol pattern count: `8444`

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

- `market_context_high->crypto_major_24h` score `10.9544` n `82` status `ready` deltaP `29.8484` edge `0.7275` maxDD `-0.423`
- `news_risk_high->crypto_major_4h` score `9.3864` n `65` status `ready` deltaP `32.704` edge `0.5845` maxDD `-0.6258`
- `market_context_high->crypto_alt_24h` score `6.153` n `82` status `ready` deltaP `25.487` edge `0.4048` maxDD `-2.9571`
- `news_risk_high->crypto_alt_4h` score `5.7442` n `65` status `ready` deltaP `19.6341` edge `0.4822` maxDD `-6.4195`
- `news_risk_high->index_24h` score `3.4585` n `65` status `ready` deltaP `24.8264` edge `0.1227` maxDD `0.0`
- `market_context_high->crypto_major_4h` score `3.0646` n `114` status `ready` deltaP `14.0805` edge `0.2496` maxDD `-4.047`
- `news_risk_high->equity_24h` score `3.007` n `65` status `ready` deltaP `9.6448` edge `0.1963` maxDD `-0.1344`
- `news_risk_high->index_4h` score `2.9256` n `65` status `ready` deltaP `32.371` edge `0.0542` maxDD `-0.4296`
- `news_risk_high->crypto_major_1h` score `2.5432` n `65` status `ready` deltaP `10.0161` edge `0.1807` maxDD `-1.5096`
- `news_risk_high->equity_4h` score `2.4428` n `65` status `ready` deltaP `20.5769` edge `0.1274` maxDD `-2.881`
- `news_risk_high->index_1h` score `2.0734` n `65` status `ready` deltaP `25.6172` edge `0.017` maxDD `-0.1997`
- `news_risk_high->metal_4h` score `1.7672` n `65` status `ready` deltaP `16.7918` edge `0.0769` maxDD `-0.993`
- `market_context_high->fx_4h` score `1.6768` n `114` status `ready` deltaP `28.1397` edge `0.0278` maxDD `-0.3868`
- `news_risk_high->crypto_alt_1h` score `1.2045` n `65` status `ready` deltaP `3.6711` edge `0.1278` maxDD `-2.4854`
- `market_context_high->commodity_4h` score `1.0503` n `114` status `ready` deltaP `14.8347` edge `0.0557` maxDD `-1.3656`
- `market_context_high->equity_24h` score `1.0401` n `82` status `ready` deltaP `13.3596` edge `0.0037` maxDD `-0.1536`
- `market_context_high->metal_24h` score `0.9403` n `82` status `ready` deltaP `27.3374` edge `0.0774` maxDD `-5.7943`
- `market_context_high->fx_1h` score `0.8982` n `121` status `ready` deltaP `14.6001` edge `0.0059` maxDD `-0.271`
- `market_context_high->crypto_alt_4h` score `0.7501` n `114` status `ready` deltaP `1.9148` edge `0.2221` maxDD `-7.1222`
- `news_risk_high->commodity_24h` score `0.4505` n `65` status `ready` deltaP `24.9119` edge `0.0948` maxDD `-10.9169`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
