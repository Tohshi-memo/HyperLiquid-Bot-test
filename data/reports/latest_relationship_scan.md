# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-06T05:07:26.731024+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9496`

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

- `news_risk_high->crypto_major_4h` score `9.4176` n `65` status `ready` deltaP `32.704` edge `0.5871` maxDD `-0.6258`
- `news_risk_high->crypto_alt_4h` score `5.9778` n `65` status `ready` deltaP `20.2439` edge `0.4976` maxDD `-6.4195`
- `market_context_high->crypto_major_24h` score `5.8142` n `94` status `ready` deltaP `16.0342` edge `0.4932` maxDD `-5.2462`
- `news_risk_high->equity_24h` score `3.68` n `65` status `ready` deltaP `11.0283` edge `0.2431` maxDD `-0.1298`
- `news_risk_high->index_24h` score `3.2508` n `65` status `ready` deltaP `22.6804` edge `0.1197` maxDD `0.0`
- `news_risk_high->index_4h` score `2.6083` n `65` status `ready` deltaP `29.1698` edge `0.0491` maxDD `-0.4296`
- `news_risk_high->crypto_major_1h` score `2.4533` n `65` status `ready` deltaP `9.4173` edge `0.1772` maxDD `-1.5096`
- `market_context_high->crypto_major_4h` score `2.3082` n `117` status `ready` deltaP `12.1912` edge `0.2075` maxDD `-4.047`
- `news_risk_high->equity_4h` score `1.9795` n `65` status `ready` deltaP `17.5281` edge `0.1079` maxDD `-2.7837`
- `news_risk_high->index_1h` score `1.9704` n `65` status `ready` deltaP `24.5693` edge `0.0154` maxDD `-0.1997`
- `news_risk_high->metal_4h` score `1.8` n `65` status `ready` deltaP `17.0967` edge `0.0776` maxDD `-0.993`
- `market_context_high->fx_4h` score `1.3133` n `117` status `ready` deltaP `24.0763` edge `0.0246` maxDD `-0.3868`
- `market_context_high->commodity_4h` score `1.2659` n `117` status `ready` deltaP `16.754` edge `0.0638` maxDD `-1.6002`
- `news_risk_high->crypto_alt_1h` score `1.2212` n `65` status `ready` deltaP `4.1202` edge `0.1262` maxDD `-2.4854`
- `market_context_high->fx_1h` score `0.9312` n `117` status `ready` deltaP `14.9381` edge `0.0064` maxDD `-0.271`
- `market_context_high->commodity_1h` score `0.7369` n `117` status `ready` deltaP `12.0554` edge `0.0207` maxDD `-0.5059`
- `market_context_high->metal_24h` score `0.4783` n `94` status `ready` deltaP `20.147` edge `0.0645` maxDD `-5.6663`
- `news_risk_high->metal_1h` score `0.1069` n `65` status `ready` deltaP `6.216` edge `0.0093` maxDD `-1.0132`
- `news_risk_high->commodity_24h` score `-0.0028` n `65` status `ready` deltaP `24.0259` edge `0.0426` maxDD `-10.9169`
- `market_context_high->crypto_alt_4h` score `-0.1196` n `117` status `ready` deltaP `-1.6364` edge `0.1733` maxDD `-7.1222`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
