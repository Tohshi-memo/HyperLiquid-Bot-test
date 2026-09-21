# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-21T23:07:29.187017+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9868`

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

- `market_context_high->unknown_4h` score `25.3227` n `58` status `ready` deltaP `2.2971` edge `2.1099` maxDD `-0.5326`
- `news_risk_high->crypto_major_24h` score `12.1081` n `101` status `ready` deltaP `1.0262` edge `1.688` maxDD `-46.1999`
- `news_risk_high->crypto_alt_24h` score `7.3753` n `101` status `ready` deltaP `1.4112` edge `1.0933` maxDD `-32.7147`
- `news_risk_high->crypto_alt_4h` score `3.2828` n `101` status `ready` deltaP `15.8702` edge `0.2887` maxDD `-7.675`
- `market_context_high->crypto_major_24h` score `2.8039` n `50` status `ready` deltaP `2.7292` edge `1.0071` maxDD `-48.5989`
- `market_context_high->equity_24h` score `2.6799` n `50` status `ready` deltaP `-4.0417` edge `0.53` maxDD `-17.7117`
- `news_risk_high->crypto_alt_1h` score `2.4009` n `101` status `ready` deltaP `14.7344` edge `0.1484` maxDD `-2.058`
- `news_risk_high->commodity_24h` score `2.3927` n `101` status `ready` deltaP `30.1413` edge `0.2364` maxDD `-3.4467`
- `news_risk_high->crypto_major_4h` score `2.301` n `101` status `ready` deltaP `17.0898` edge `0.2036` maxDD `-8.0625`
- `news_risk_high->crypto_major_1h` score `1.6072` n `101` status `ready` deltaP `15.932` edge `0.08` maxDD `-2.8494`
- `market_context_high->index_24h` score `1.5707` n `50` status `ready` deltaP `-0.0486` edge `0.2101` maxDD `-1.644`
- `market_context_high->equity_1h` score `0.6006` n `58` status `ready` deltaP `4.2123` edge `0.0473` maxDD `-0.36`
- `market_context_high->index_1h` score `0.4944` n `58` status `ready` deltaP `8.1819` edge `0.0122` maxDD `-0.0435`
- `market_context_high->fx_1h` score `0.4696` n `58` status `ready` deltaP `10.2726` edge `0.0063` maxDD `-0.1854`
- `news_risk_high->metal_1h` score `0.4687` n `101` status `ready` deltaP `13.101` edge `0.0119` maxDD `-0.8144`
- `news_risk_high->fx_4h` score `0.44` n `101` status `ready` deltaP `11.0797` edge `0.0264` maxDD `-0.421`
- `market_context_high->metal_24h` score `0.2339` n `50` status `ready` deltaP `16.6319` edge `-0.068` maxDD `-0.2042`
- `news_risk_high->metal_4h` score `0.1931` n `101` status `ready` deltaP `13.4403` edge `0.0319` maxDD `-2.0994`
- `market_context_high->metal_1h` score `0.1908` n `58` status `ready` deltaP `4.6511` edge `0.0157` maxDD `-0.1314`
- `market_context_high->index_4h` score `0.0871` n `58` status `ready` deltaP `11.1228` edge `0.0007` maxDD `-1.0949`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
