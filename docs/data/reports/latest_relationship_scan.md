# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-11T18:52:27.366675+00:00`
- Price records: `672`
- Market context records: `6419`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `5871`

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

- `news_risk_high->crypto_alt_24h` score `12.6635` n `32` status `ready` deltaP `32.4653` edge `0.8536` maxDD `-0.5131`
- `news_risk_high->fx_24h` score `6.637` n `32` status `ready` deltaP `55.9028` edge `0.1804` maxDD `0.0`
- `market_context_high->unknown_24h` score `6.1354` n `146` status `ready` deltaP `16.2172` edge `0.7332` maxDD `-15.0689`
- `news_risk_high->fx_4h` score `4.2277` n `32` status `ready` deltaP `44.1311` edge `0.0627` maxDD `-0.0345`
- `news_risk_high->commodity_24h` score `4.1276` n `32` status `ready` deltaP `35.4167` edge `0.1284` maxDD `-0.3101`
- `news_risk_high->crypto_major_24h` score `3.7361` n `32` status `ready` deltaP `14.0625` edge `0.4632` maxDD `-4.2368`
- `news_risk_high->fx_1h` score `2.4721` n `32` status `ready` deltaP `29.7904` edge `0.0213` maxDD `-0.1113`
- `news_risk_high->crypto_major_1h` score `1.4983` n `32` status `ready` deltaP `14.2777` edge `0.1436` maxDD `-2.0691`
- `news_risk_high->crypto_alt_1h` score `0.8653` n `32` status `ready` deltaP `10.2732` edge `0.0886` maxDD `-1.6923`
- `market_context_high->unknown_1h` score `0.6513` n `204` status `ready` deltaP `-6.6162` edge `0.1992` maxDD `-3.7317`
- `market_context_high->metal_4h` score `0.369` n `200` status `ready` deltaP `10.9756` edge `0.0414` maxDD `-2.7056`
- `market_context_high->index_4h` score `0.2119` n `200` status `ready` deltaP `9.3293` edge `0.0231` maxDD `-0.4108`
- `news_risk_high->unknown_1h` score `-0.2417` n `32` status `ready` deltaP `6.6804` edge `-0.0302` maxDD `-0.7581`
- `market_context_high->metal_24h` score `-0.2867` n `146` status `ready` deltaP `18.5978` edge `0.0961` maxDD `-11.8809`
- `market_context_high->metal_1h` score `-0.5462` n `204` status `ready` deltaP `0.8307` edge `0.0022` maxDD `-1.8877`
- `market_context_high->equity_4h` score `-0.5462` n `200` status `ready` deltaP `7.689` edge `0.0486` maxDD `-8.2573`
- `news_risk_high->metal_1h` score `-0.5885` n `32` status `ready` deltaP `-0.1497` edge `-0.0247` maxDD `-1.6464`
- `market_context_high->commodity_1h` score `-0.6854` n `204` status `ready` deltaP `-2.5596` edge `-0.0025` maxDD `-2.1314`
- `market_context_high->fx_1h` score `-0.7093` n `204` status `ready` deltaP `-0.6018` edge `-0.0019` maxDD `-0.9225`
- `market_context_high->index_1h` score `-0.72` n `204` status `ready` deltaP `-3.4578` edge `0.0027` maxDD `-0.7564`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
