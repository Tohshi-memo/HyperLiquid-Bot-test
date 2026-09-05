# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-05T22:52:25.089572+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `10807`

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

- `risk_on_high->unknown_4h` score `21.6456` n `133` status `ready` deltaP `-2.7061` edge `2.0224` maxDD `-7.7112`
- `risk_on_and_context->unknown_4h` score `21.6456` n `133` status `ready` deltaP `-2.7061` edge `2.0224` maxDD `-7.7112`
- `market_context_high->unknown_4h` score `8.6378` n `228` status `ready` deltaP `1.8052` edge `0.9546` maxDD `-9.4124`
- `news_risk_high->crypto_alt_24h` score `6.3191` n `37` status `ready` deltaP `25.1783` edge `0.3857` maxDD `-0.8236`
- `news_risk_high->commodity_24h` score `3.8911` n `37` status `ready` deltaP `20.1389` edge `0.19` maxDD `0.0`
- `news_risk_high->crypto_major_4h` score `3.2817` n `37` status `ready` deltaP `16.4181` edge `0.2053` maxDD `-0.9693`
- `news_risk_high->metal_4h` score `2.3625` n `37` status `ready` deltaP `23.9989` edge `0.059` maxDD `-0.7692`
- `market_context_high->equity_24h` score `1.6869` n `157` status `ready` deltaP `13.817` edge `0.4565` maxDD `-19.9766`
- `news_risk_high->equity_1h` score `1.6027` n `37` status `ready` deltaP `13.2344` edge `0.0844` maxDD `-0.7924`
- `news_risk_high->commodity_4h` score `1.5624` n `37` status `ready` deltaP `7.6179` edge `0.0995` maxDD `-0.2737`
- `news_risk_high->metal_1h` score `1.2957` n `37` status `ready` deltaP `15.4637` edge `0.0242` maxDD `-0.2118`
- `news_risk_high->crypto_major_1h` score `1.1535` n `37` status `ready` deltaP `6.1661` edge `0.0733` maxDD `-0.4628`
- `news_risk_high->index_1h` score `1.1503` n `37` status `ready` deltaP `14.4239` edge `0.0131` maxDD `-0.0724`
- `news_risk_high->fx_24h` score `0.9516` n `37` status `ready` deltaP `20.3031` edge `0.0455` maxDD `-3.1244`
- `news_risk_high->crypto_alt_1h` score `0.847` n `37` status `ready` deltaP `8.4278` edge `0.0409` maxDD `-0.7867`
- `news_risk_high->crypto_alt_4h` score `0.174` n `37` status `ready` deltaP `3.6544` edge `0.023` maxDD `-1.296`
- `news_risk_high->crypto_major_24h` score `0.1697` n `37` status `ready` deltaP `15.5359` edge `0.1958` maxDD `-18.2098`
- `risk_on_high->index_1h` score `-0.0491` n `145` status `ready` deltaP `6.1666` edge `-0.0027` maxDD `-0.5764`
- `risk_on_and_context->index_1h` score `-0.0491` n `145` status `ready` deltaP `6.1666` edge `-0.0027` maxDD `-0.5764`
- `news_risk_high->commodity_1h` score `-0.0605` n `37` status `ready` deltaP `5.1263` edge `0.0027` maxDD `-0.9036`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
