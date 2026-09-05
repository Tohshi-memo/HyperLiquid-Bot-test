# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-05T16:22:27.733022+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `10537`

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

- `risk_on_high->unknown_4h` score `21.6307` n `140` status `ready` deltaP `2.0122` edge `1.9014` maxDD `-3.3137`
- `risk_on_and_context->unknown_4h` score `21.6307` n `140` status `ready` deltaP `2.0122` edge `1.9014` maxDD `-3.3137`
- `market_context_high->unknown_4h` score `9.8271` n `228` status `ready` deltaP `4.3806` edge `0.9197` maxDD `-3.7315`
- `news_risk_high->crypto_alt_24h` score `7.1363` n `37` status `ready` deltaP `25.1783` edge `0.4538` maxDD `-0.8236`
- `news_risk_high->commodity_24h` score `3.7769` n `37` status `ready` deltaP `19.7917` edge `0.1828` maxDD `0.0`
- `news_risk_high->crypto_major_4h` score `3.5682` n `37` status `ready` deltaP `17.1803` edge `0.2241` maxDD `-0.9693`
- `news_risk_high->metal_4h` score `2.3807` n `37` status `ready` deltaP `24.1513` edge `0.0595` maxDD `-0.7692`
- `news_risk_high->commodity_4h` score `1.8327` n `37` status `ready` deltaP `10.6666` edge `0.1017` maxDD `-0.2737`
- `news_risk_high->equity_1h` score `1.5835` n `37` status `ready` deltaP `13.0847` edge `0.0838` maxDD `-0.7924`
- `news_risk_high->metal_1h` score `1.2598` n `37` status `ready` deltaP `15.0146` edge `0.0242` maxDD `-0.2118`
- `news_risk_high->crypto_major_1h` score `1.199` n `37` status `ready` deltaP `6.3158` edge `0.0761` maxDD `-0.4628`
- `news_risk_high->index_1h` score `1.1622` n `37` status `ready` deltaP `14.5736` edge `0.0131` maxDD `-0.0724`
- `news_risk_high->crypto_alt_1h` score `1.0041` n `37` status `ready` deltaP `9.4757` edge `0.047` maxDD `-0.7867`
- `news_risk_high->crypto_major_24h` score `0.9055` n `37` status `ready` deltaP `16.5776` edge `0.2832` maxDD `-18.2098`
- `news_risk_high->fx_24h` score `0.5871` n `37` status `ready` deltaP `16.1364` edge `0.0429` maxDD `-3.1244`
- `news_risk_high->crypto_alt_4h` score `0.5801` n `37` status `ready` deltaP `5.941` edge `0.0416` maxDD `-1.296`
- `market_context_high->equity_24h` score `0.4843` n `181` status `ready` deltaP `14.3742` edge `0.3791` maxDD `-20.7654`
- `risk_on_high->index_1h` score `-0.032` n `148` status `ready` deltaP `6.4655` edge `-0.0025` maxDD `-0.5764`
- `risk_on_and_context->index_1h` score `-0.032` n `148` status `ready` deltaP `6.4655` edge `-0.0025` maxDD `-0.5764`
- `news_risk_high->commodity_1h` score `-0.041` n `37` status `ready` deltaP `5.4257` edge `0.0032` maxDD `-0.9036`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
