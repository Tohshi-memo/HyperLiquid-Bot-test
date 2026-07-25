# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-25T13:22:30.387770+00:00`
- Price records: `672`
- Market context records: `7881`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `14677`

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

- `market_context_high->equity_24h` score `13.7534` n `111` status `ready` deltaP `29.4003` edge `1.0843` maxDD `-6.0681`
- `market_context_high->equity_4h` score `4.686` n `111` status `ready` deltaP `14.1476` edge `0.3938` maxDD `-5.1426`
- `market_context_high->metal_24h` score `4.0902` n `111` status `ready` deltaP `20.8376` edge `0.3012` maxDD `-0.9412`
- `market_context_high->crypto_alt_4h` score `1.6844` n `111` status `ready` deltaP `14.472` edge `0.1556` maxDD `-3.9374`
- `market_context_high->commodity_24h` score `1.5606` n `111` status `ready` deltaP `21.3593` edge `0.146` maxDD `-7.0012`
- `market_context_high->crypto_major_4h` score `1.5441` n `111` status `ready` deltaP `15.9571` edge `0.1941` maxDD `-6.7444`
- `market_context_high->fx_24h` score `1.1538` n `111` status `ready` deltaP `31.2131` edge `0.0486` maxDD `-3.0343`
- `market_context_high->crypto_major_1h` score `1.1327` n `113` status `ready` deltaP `12.7572` edge `0.0502` maxDD `-1.6021`
- `market_context_high->equity_1h` score `0.9211` n `113` status `ready` deltaP `13.0276` edge `0.113` maxDD `-4.2072`
- `market_context_high->index_4h` score `0.6058` n `111` status `ready` deltaP `14.453` edge `0.0588` maxDD `-1.0404`
- `market_context_high->commodity_4h` score `0.5747` n `111` status `ready` deltaP `9.2319` edge `0.0457` maxDD `-1.0817`
- `market_context_high->index_1h` score `0.4048` n `113` status `ready` deltaP `8.7965` edge `0.0181` maxDD `-0.7743`
- `market_context_high->crypto_alt_1h` score `0.4039` n `113` status `ready` deltaP `5.4023` edge `0.0409` maxDD `-1.4603`
- `market_context_high->metal_4h` score `0.3553` n `111` status `ready` deltaP `8.6594` edge `0.097` maxDD `-1.0098`
- `market_context_high->commodity_1h` score `0.0223` n `113` status `ready` deltaP `5.1691` edge `0.0133` maxDD `-0.6722`
- `market_context_high->index_24h` score `-0.2803` n `111` status `ready` deltaP `0.0203` edge `0.1174` maxDD `-1.605`
- `market_context_high->fx_1h` score `-0.4432` n `113` status `ready` deltaP `0.2614` edge `-0.0002` maxDD `-0.4112`
- `market_context_high->metal_1h` score `-0.4788` n `113` status `ready` deltaP `1.1508` edge `0.0236` maxDD `-0.6936`
- `market_context_high->fx_4h` score `-0.7959` n `111` status `ready` deltaP `0.8005` edge `0.0001` maxDD `-1.5981`
- `market_context_high->crypto_alt_24h` score `-1.6713` n `111` status `ready` deltaP `12.1139` edge `0.2345` maxDD `-28.3623`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
