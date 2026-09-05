# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-05T22:37:29.613934+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `10805`

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

- `risk_on_high->unknown_4h` score `21.7548` n `133` status `ready` deltaP `-2.7061` edge `2.0315` maxDD `-7.7112`
- `risk_on_and_context->unknown_4h` score `21.7548` n `133` status `ready` deltaP `-2.7061` edge `2.0315` maxDD `-7.7112`
- `market_context_high->unknown_4h` score `8.6906` n `228` status `ready` deltaP `1.8052` edge `0.959` maxDD `-9.4124`
- `news_risk_high->crypto_alt_24h` score `6.3827` n `37` status `ready` deltaP `25.1783` edge `0.391` maxDD `-0.8236`
- `news_risk_high->commodity_24h` score `3.8887` n `37` status `ready` deltaP `20.1389` edge `0.1898` maxDD `0.0`
- `news_risk_high->crypto_major_4h` score `3.2587` n `37` status `ready` deltaP `16.2657` edge `0.2044` maxDD `-0.9693`
- `news_risk_high->metal_4h` score `2.3503` n `37` status `ready` deltaP `23.8464` edge `0.059` maxDD `-0.7692`
- `news_risk_high->equity_1h` score `1.6039` n `37` status `ready` deltaP `13.2344` edge `0.0845` maxDD `-0.7924`
- `news_risk_high->commodity_4h` score `1.5758` n `37` status `ready` deltaP `7.7703` edge `0.0996` maxDD `-0.2737`
- `market_context_high->equity_24h` score `1.5044` n `158` status `ready` deltaP `13.5109` edge `0.4509` maxDD `-20.2483`
- `news_risk_high->metal_1h` score `1.2957` n `37` status `ready` deltaP `15.4637` edge `0.0242` maxDD `-0.2118`
- `news_risk_high->index_1h` score `1.1503` n `37` status `ready` deltaP `14.4239` edge `0.0131` maxDD `-0.0724`
- `news_risk_high->crypto_major_1h` score `1.1343` n `37` status `ready` deltaP `6.0164` edge `0.0727` maxDD `-0.4628`
- `news_risk_high->fx_24h` score `0.9353` n `37` status `ready` deltaP `20.1295` edge `0.0453` maxDD `-3.1244`
- `news_risk_high->crypto_alt_1h` score `0.8314` n `37` status `ready` deltaP `8.2781` edge `0.0406` maxDD `-0.7867`
- `news_risk_high->crypto_major_24h` score `0.2224` n `37` status `ready` deltaP `15.7095` edge `0.2014` maxDD `-18.2098`
- `news_risk_high->crypto_alt_4h` score `0.1812` n `37` status `ready` deltaP `3.6544` edge `0.0236` maxDD `-1.296`
- `risk_on_high->index_1h` score `-0.0499` n `145` status `ready` deltaP `6.1666` edge `-0.0028` maxDD `-0.5764`
- `risk_on_and_context->index_1h` score `-0.0499` n `145` status `ready` deltaP `6.1666` edge `-0.0028` maxDD `-0.5764`
- `news_risk_high->commodity_1h` score `-0.0605` n `37` status `ready` deltaP `5.1263` edge `0.0027` maxDD `-0.9036`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
