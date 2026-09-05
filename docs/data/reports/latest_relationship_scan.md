# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-05T23:37:25.642787+00:00`
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

- `risk_on_high->unknown_4h` score `21.09` n `133` status `ready` deltaP `-2.7061` edge `1.9761` maxDD `-7.7112`
- `risk_on_and_context->unknown_4h` score `21.09` n `133` status `ready` deltaP `-2.7061` edge `1.9761` maxDD `-7.7112`
- `market_context_high->unknown_4h` score `8.3726` n `228` status `ready` deltaP `1.8052` edge `0.9325` maxDD `-9.4124`
- `news_risk_high->crypto_alt_24h` score `6.0928` n `37` status `ready` deltaP `25.0047` edge `0.368` maxDD `-0.8236`
- `news_risk_high->commodity_24h` score `3.8995` n `37` status `ready` deltaP `20.1389` edge `0.1907` maxDD `0.0`
- `news_risk_high->crypto_major_4h` score `3.3045` n `37` status `ready` deltaP `16.4181` edge `0.2072` maxDD `-0.9693`
- `market_context_high->equity_24h` score `2.4872` n `154` status `ready` deltaP `14.7727` edge `0.4797` maxDD `-18.0065`
- `news_risk_high->metal_4h` score `2.3503` n `37` status `ready` deltaP `23.8464` edge `0.059` maxDD `-0.7692`
- `news_risk_high->equity_1h` score `1.6015` n `37` status `ready` deltaP `13.2344` edge `0.0843` maxDD `-0.7924`
- `news_risk_high->commodity_4h` score `1.5356` n `37` status `ready` deltaP `7.313` edge `0.0993` maxDD `-0.2737`
- `news_risk_high->metal_1h` score `1.3077` n `37` status `ready` deltaP `15.6134` edge `0.0242` maxDD `-0.2118`
- `news_risk_high->crypto_major_1h` score `1.1942` n `37` status `ready` deltaP `6.4655` edge `0.0747` maxDD `-0.4628`
- `news_risk_high->index_1h` score `1.1742` n `37` status `ready` deltaP `14.7233` edge `0.0131` maxDD `-0.0724`
- `news_risk_high->fx_24h` score `0.9993` n `37` status `ready` deltaP `20.8239` edge `0.046` maxDD `-3.1244`
- `risk_on_high->crypto_major_24h` score `0.9645` n `79` status `ready` deltaP `11.2518` edge `0.8151` maxDD `-50.3164`
- `risk_on_and_context->crypto_major_24h` score `0.9645` n `79` status `ready` deltaP `11.2518` edge `0.8151` maxDD `-50.3164`
- `news_risk_high->crypto_alt_1h` score `0.8949` n `37` status `ready` deltaP `8.8769` edge `0.0419` maxDD `-0.7867`
- `news_risk_high->crypto_alt_4h` score `0.1474` n `37` status `ready` deltaP `3.502` edge `0.0218` maxDD `-1.296`
- `news_risk_high->crypto_major_24h` score `-0.0017` n `37` status `ready` deltaP `15.0151` edge `0.1773` maxDD `-18.2098`
- `news_risk_high->commodity_1h` score `-0.0519` n `37` status `ready` deltaP `5.276` edge `0.0028` maxDD `-0.9036`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
