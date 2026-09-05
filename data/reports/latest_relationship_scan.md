# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-05T05:08:00.442292+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `10740`

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

- `risk_on_high->unknown_4h` score `19.5542` n `133` status `ready` deltaP `7.6265` edge `1.6405` maxDD `-2.2797`
- `risk_on_and_context->unknown_4h` score `19.5542` n `133` status `ready` deltaP `7.6265` edge `1.6405` maxDD `-2.2797`
- `market_context_high->unknown_4h` score `9.0566` n `217` status `ready` deltaP `8.0631` edge `0.7705` maxDD `-2.563`
- `news_risk_high->crypto_alt_24h` score `7.4063` n `37` status `ready` deltaP `25.1783` edge `0.4763` maxDD `-0.8236`
- `news_risk_high->commodity_24h` score `4.3412` n `37` status `ready` deltaP `25.0` edge `0.1951` maxDD `0.0`
- `news_risk_high->crypto_major_4h` score `3.8376` n `37` status `ready` deltaP `17.6376` edge `0.2435` maxDD `-0.9693`
- `news_risk_high->metal_4h` score `2.1676` n `37` status `ready` deltaP `21.7123` edge `0.058` maxDD `-0.7692`
- `news_risk_high->commodity_4h` score `1.7875` n `37` status `ready` deltaP `10.0569` edge `0.102` maxDD `-0.2737`
- `news_risk_high->equity_1h` score `1.6554` n `37` status `ready` deltaP `13.8332` edge `0.0848` maxDD `-0.7924`
- `news_risk_high->crypto_major_1h` score `1.4112` n `37` status `ready` deltaP `7.8128` edge `0.0838` maxDD `-0.4628`
- `news_risk_high->index_1h` score `1.2736` n `37` status `ready` deltaP `15.9209` edge `0.0134` maxDD `-0.0724`
- `news_risk_high->metal_1h` score `1.2203` n `37` status `ready` deltaP `14.5655` edge `0.0239` maxDD `-0.2118`
- `news_risk_high->crypto_alt_1h` score `1.1072` n `37` status `ready` deltaP `9.7751` edge `0.0536` maxDD `-0.7867`
- `news_risk_high->crypto_alt_4h` score `1.0246` n `37` status `ready` deltaP `8.2276` edge `0.0634` maxDD `-1.296`
- `news_risk_high->fx_24h` score `0.1642` n `37` status `ready` deltaP `11.7961` edge `0.0366` maxDD `-3.1244`
- `risk_on_high->metal_1h` score `0.0621` n `137` status `ready` deltaP `11.7444` edge `0.0009` maxDD `-1.699`
- `risk_on_and_context->metal_1h` score `0.0621` n `137` status `ready` deltaP `11.7444` edge `0.0009` maxDD `-1.699`
- `news_risk_high->commodity_1h` score `-0.0324` n `37` status `ready` deltaP `5.5754` edge `0.0033` maxDD `-0.9036`
- `news_risk_high->crypto_major_24h` score `-0.0895` n `37` status `ready` deltaP `11.5428` edge `0.1892` maxDD `-18.2098`
- `risk_on_high->index_1h` score `-0.1777` n `137` status `ready` deltaP `3.8278` edge `-0.0036` maxDD `-0.5764`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
