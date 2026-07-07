# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-07T09:52:26.762643+00:00`
- Price records: `672`
- Market context records: `5969`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11220`

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

- `news_risk_high->fx_24h` score `7.1417` n `30` status `ready` deltaP `65.4514` edge `0.1588` maxDD `0.0`
- `news_risk_high->commodity_24h` score `5.0671` n `30` status `ready` deltaP `36.8403` edge `0.1972` maxDD `-0.3101`
- `news_risk_high->fx_4h` score `3.8832` n `30` status `ready` deltaP `40.3049` edge `0.0595` maxDD `-0.0345`
- `news_risk_high->fx_1h` score `2.1603` n `30` status `ready` deltaP `26.0279` edge `0.0204` maxDD `-0.1113`
- `market_context_high->equity_4h` score `1.4936` n `235` status `ready` deltaP `9.4662` edge `0.1708` maxDD `-4.0887`
- `news_risk_high->crypto_major_1h` score `0.8465` n `30` status `ready` deltaP `10.3393` edge `0.0863` maxDD `-2.0691`
- `news_risk_high->crypto_alt_1h` score `0.2138` n `30` status `ready` deltaP `5.4691` edge `0.0371` maxDD `-1.6923`
- `news_risk_high->index_24h` score `-0.0838` n `30` status `ready` deltaP `7.8472` edge `0.0241` maxDD `-2.3058`
- `news_risk_high->metal_1h` score `-0.3798` n `30` status `ready` deltaP `1.986` edge `-0.0253` maxDD `-1.2643`
- `market_context_high->equity_1h` score `-0.4299` n `244` status `ready` deltaP `3.6345` edge `0.0335` maxDD `-4.3608`
- `market_context_high->metal_1h` score `-0.4636` n `244` status `ready` deltaP `2.7511` edge `0.0021` maxDD `-2.0564`
- `market_context_high->commodity_1h` score `-0.5197` n `244` status `ready` deltaP `-1.7105` edge `0.0005` maxDD `-1.4578`
- `market_context_high->index_1h` score `-0.6802` n `244` status `ready` deltaP `-0.0393` edge `0.0044` maxDD `-1.3078`
- `market_context_high->fx_1h` score `-0.7025` n `244` status `ready` deltaP `-0.9939` edge `-0.0008` maxDD `-0.756`
- `market_context_high->equity_24h` score `-0.9525` n `215` status `ready` deltaP `20.927` edge `0.3054` maxDD `-31.2762`
- `market_context_high->index_4h` score `-1.0904` n `235` status `ready` deltaP `1.2351` edge `0.0207` maxDD `-3.165`
- `news_risk_high->index_1h` score `-1.1093` n `30` status `ready` deltaP `-10.4491` edge `-0.0211` maxDD `-1.1161`
- `market_context_high->crypto_major_1h` score `-1.1234` n `244` status `ready` deltaP `1.924` edge `0.0199` maxDD `-9.807`
- `market_context_high->crypto_alt_1h` score `-1.1576` n `244` status `ready` deltaP `1.6713` edge `0.0157` maxDD `-9.3536`
- `market_context_high->commodity_4h` score `-1.4111` n `235` status `ready` deltaP `-0.9555` edge `-0.0032` maxDD `-6.3734`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
