# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-25T13:58:06.869081+00:00`
- Price records: `672`
- Market context records: `7884`
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

- `market_context_high->equity_24h` score `13.9191` n `110` status `ready` deltaP `29.5667` edge `1.097` maxDD `-6.0681`
- `market_context_high->equity_4h` score `4.7653` n `110` status `ready` deltaP `14.4483` edge `0.3984` maxDD `-5.1426`
- `market_context_high->metal_24h` score `4.2557` n `110` status `ready` deltaP `21.5665` edge `0.3049` maxDD `-0.8563`
- `market_context_high->crypto_alt_4h` score `1.7488` n `110` status `ready` deltaP `14.9176` edge `0.158` maxDD `-3.9374`
- `market_context_high->commodity_24h` score `1.6134` n `110` status `ready` deltaP `21.5094` edge `0.1494` maxDD `-7.0012`
- `market_context_high->crypto_major_4h` score `1.6093` n `110` status `ready` deltaP `16.4273` edge `0.1964` maxDD `-6.7444`
- `market_context_high->crypto_major_1h` score `1.2131` n `113` status `ready` deltaP `13.4174` edge `0.0525` maxDD `-1.6021`
- `market_context_high->fx_24h` score `1.1769` n `110` status `ready` deltaP `31.6717` edge `0.0485` maxDD `-3.0343`
- `market_context_high->equity_1h` score `0.9187` n `113` status `ready` deltaP `12.9501` edge `0.1132` maxDD `-4.2072`
- `market_context_high->index_4h` score `0.7024` n `110` status `ready` deltaP `14.9063` edge `0.0594` maxDD `-1.0191`
- `market_context_high->commodity_4h` score `0.6559` n `110` status `ready` deltaP `10.0069` edge `0.0473` maxDD `-1.0817`
- `market_context_high->crypto_alt_1h` score `0.4917` n `113` status `ready` deltaP `6.0649` edge `0.0438` maxDD `-1.4603`
- `market_context_high->index_1h` score `0.4589` n `113` status `ready` deltaP `9.4582` edge `0.0182` maxDD `-0.7743`
- `market_context_high->metal_4h` score `0.4546` n `110` status `ready` deltaP `9.0231` edge `0.0983` maxDD `-0.979`
- `market_context_high->commodity_1h` score `-0.079` n `113` status `ready` deltaP `4.353` edge `0.0103` maxDD `-0.6722`
- `market_context_high->index_24h` score `-0.1781` n `110` status `ready` deltaP `0.3971` edge `0.1187` maxDD `-1.562`
- `market_context_high->metal_1h` score `-0.3731` n `113` status `ready` deltaP `1.8163` edge `0.0238` maxDD `-0.6936`
- `market_context_high->fx_1h` score `-0.3781` n `113` status `ready` deltaP `1.075` edge `-0.0002` maxDD `-0.4112`
- `market_context_high->fx_4h` score `-0.7371` n `110` status `ready` deltaP `1.1937` edge `0.0003` maxDD `-1.5544`
- `market_context_high->crypto_alt_24h` score `-1.6294` n `110` status `ready` deltaP `12.5889` edge `0.2367` maxDD `-28.3623`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
