# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-06T08:37:32.063012+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8612`

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

- `news_risk_high->crypto_major_4h` score `9.51` n `62` status `ready` deltaP `34.0087` edge `0.5861` maxDD `-0.6258`
- `news_risk_high->crypto_alt_4h` score `5.5427` n `62` status `ready` deltaP `20.1908` edge `0.4617` maxDD `-6.4195`
- `news_risk_high->equity_24h` score `3.5458` n `62` status `ready` deltaP `10.7305` edge `0.2339` maxDD `-0.1298`
- `news_risk_high->index_24h` score `3.2544` n `62` status `ready` deltaP `22.6804` edge `0.12` maxDD `0.0`
- `market_context_high->crypto_major_4h` score `2.7652` n `117` status `ready` deltaP `13.8681` edge `0.2344` maxDD `-4.047`
- `news_risk_high->index_4h` score `2.5549` n `62` status `ready` deltaP `28.8012` edge `0.0471` maxDD `-0.4296`
- `news_risk_high->crypto_major_1h` score `2.0283` n `62` status `ready` deltaP `8.079` edge `0.1507` maxDD `-1.5096`
- `market_context_high->crypto_major_24h` score `1.8562` n `108` status `ready` deltaP `8.0565` edge `0.3174` maxDD `-13.3143`
- `news_risk_high->index_1h` score `1.8079` n `62` status `ready` deltaP `23.0781` edge `0.0118` maxDD `-0.1997`
- `news_risk_high->equity_4h` score `1.679` n `62` status `ready` deltaP `16.8618` edge `0.0873` maxDD `-2.7837`
- `market_context_high->fx_4h` score `1.2537` n `117` status `ready` deltaP `23.4665` edge `0.0237` maxDD `-0.3868`
- `news_risk_high->metal_4h` score `1.186` n `62` status `ready` deltaP `17.2846` edge `0.0784` maxDD `-0.993`
- `market_context_high->commodity_4h` score `1.1825` n `117` status `ready` deltaP `16.2967` edge `0.0599` maxDD `-1.6002`
- `market_context_high->fx_1h` score `0.8929` n `117` status `ready` deltaP `14.489` edge `0.0062` maxDD `-0.271`
- `market_context_high->commodity_1h` score `0.7346` n `117` status `ready` deltaP `11.9057` edge `0.0215` maxDD `-0.5059`
- `news_risk_high->commodity_24h` score `0.7273` n `62` status `ready` deltaP `27.0092` edge `0.0698` maxDD `-8.196`
- `news_risk_high->crypto_alt_1h` score `0.7052` n `62` status `ready` deltaP `2.4097` edge `0.0946` maxDD `-2.4854`
- `market_context_high->crypto_alt_4h` score `0.4179` n `117` status `ready` deltaP `-0.7218` edge `0.212` maxDD `-7.1222`
- `market_context_high->metal_24h` score `0.0376` n `108` status `ready` deltaP `13.7267` edge `0.0508` maxDD `-5.6663`
- `market_context_high->crypto_major_1h` score `-0.0874` n `117` status `ready` deltaP `7.6655` edge `0.0305` maxDD `-3.7778`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
