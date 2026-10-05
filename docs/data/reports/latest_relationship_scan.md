# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-05T13:22:39.220595+00:00`
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

- `market_context_high->crypto_major_24h` score `10.9532` n `82` status `ready` deltaP `29.8484` edge `0.7274` maxDD `-0.423`
- `news_risk_high->crypto_major_4h` score `9.3792` n `65` status `ready` deltaP `32.704` edge `0.5839` maxDD `-0.6258`
- `market_context_high->crypto_alt_24h` score `6.1602` n `82` status `ready` deltaP `25.487` edge `0.4054` maxDD `-2.9571`
- `news_risk_high->crypto_alt_4h` score `5.7226` n `65` status `ready` deltaP `19.6341` edge `0.4804` maxDD `-6.4195`
- `news_risk_high->index_24h` score `3.4585` n `65` status `ready` deltaP `24.8264` edge `0.1227` maxDD `0.0`
- `news_risk_high->equity_24h` score `2.9895` n `65` status `ready` deltaP `9.4712` edge `0.196` maxDD `-0.1344`
- `market_context_high->crypto_major_4h` score `2.9117` n `115` status `ready` deltaP `13.4398` edge `0.2453` maxDD `-4.047`
- `news_risk_high->index_4h` score `2.911` n `65` status `ready` deltaP `32.2186` edge `0.054` maxDD `-0.4296`
- `news_risk_high->crypto_major_1h` score `2.5396` n `65` status `ready` deltaP `10.0161` edge `0.1804` maxDD `-1.5096`
- `news_risk_high->equity_4h` score `2.4296` n `65` status `ready` deltaP `20.5769` edge `0.1263` maxDD `-2.881`
- `news_risk_high->index_1h` score `2.0722` n `65` status `ready` deltaP `25.6172` edge `0.0169` maxDD `-0.1997`
- `news_risk_high->metal_4h` score `1.7672` n `65` status `ready` deltaP `16.7918` edge `0.0769` maxDD `-0.993`
- `market_context_high->fx_4h` score `1.6395` n `115` status `ready` deltaP `27.6896` edge `0.0277` maxDD `-0.3868`
- `news_risk_high->crypto_alt_1h` score `1.1973` n `65` status `ready` deltaP `3.6711` edge `0.1272` maxDD `-2.4854`
- `market_context_high->equity_24h` score `1.0226` n `82` status `ready` deltaP `13.186` edge `0.0034` maxDD `-0.1536`
- `market_context_high->commodity_4h` score `0.9776` n `115` status `ready` deltaP `14.2855` edge `0.0533` maxDD `-1.3656`
- `market_context_high->metal_24h` score `0.9258` n `82` status `ready` deltaP `27.1638` edge `0.0767` maxDD `-5.7943`
- `market_context_high->fx_1h` score `0.8982` n `121` status `ready` deltaP `14.6001` edge `0.0059` maxDD `-0.271`
- `market_context_high->crypto_alt_4h` score `0.6419` n `115` status `ready` deltaP `1.3732` edge `0.2167` maxDD `-7.1222`
- `news_risk_high->commodity_24h` score `0.4466` n `65` status `ready` deltaP `24.9119` edge `0.0943` maxDD `-10.9169`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
