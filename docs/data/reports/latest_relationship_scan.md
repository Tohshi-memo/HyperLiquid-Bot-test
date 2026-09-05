# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-05T05:22:24.068189+00:00`
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

- `risk_on_high->unknown_4h` score `19.5602` n `133` status `ready` deltaP `7.6265` edge `1.641` maxDD `-2.2797`
- `risk_on_and_context->unknown_4h` score `19.5602` n `133` status `ready` deltaP `7.6265` edge `1.641` maxDD `-2.2797`
- `market_context_high->unknown_4h` score `8.8216` n `218` status `ready` deltaP `7.7058` edge `0.7533` maxDD `-2.563`
- `news_risk_high->crypto_alt_24h` score `7.4075` n `37` status `ready` deltaP `25.1783` edge `0.4764` maxDD `-0.8236`
- `news_risk_high->commodity_24h` score `4.3388` n `37` status `ready` deltaP `25.0` edge `0.1949` maxDD `0.0`
- `news_risk_high->crypto_major_4h` score `3.8316` n `37` status `ready` deltaP `17.6376` edge `0.243` maxDD `-0.9693`
- `news_risk_high->metal_4h` score `2.1676` n `37` status `ready` deltaP `21.7123` edge `0.058` maxDD `-0.7692`
- `news_risk_high->commodity_4h` score `1.7875` n `37` status `ready` deltaP `10.0569` edge `0.102` maxDD `-0.2737`
- `news_risk_high->equity_1h` score `1.641` n `37` status `ready` deltaP `13.6835` edge `0.0846` maxDD `-0.7924`
- `news_risk_high->crypto_major_1h` score `1.4016` n `37` status `ready` deltaP `7.8128` edge `0.083` maxDD `-0.4628`
- `news_risk_high->index_1h` score `1.2604` n `37` status `ready` deltaP `15.7712` edge `0.0133` maxDD `-0.0724`
- `news_risk_high->metal_1h` score `1.2083` n `37` status `ready` deltaP `14.4158` edge `0.0239` maxDD `-0.2118`
- `news_risk_high->crypto_alt_1h` score `1.0832` n `37` status `ready` deltaP `9.6254` edge `0.0526` maxDD `-0.7867`
- `news_risk_high->crypto_alt_4h` score `0.992` n `37` status `ready` deltaP `8.0752` edge `0.0617` maxDD `-1.296`
- `news_risk_high->fx_24h` score `0.1666` n `37` status `ready` deltaP `11.7961` edge `0.0368` maxDD `-3.1244`
- `risk_on_high->metal_1h` score `0.0694` n `138` status `ready` deltaP `11.8697` edge `0.001` maxDD `-1.699`
- `risk_on_and_context->metal_1h` score `0.0694` n `138` status `ready` deltaP `11.8697` edge `0.001` maxDD `-1.699`
- `news_risk_high->commodity_1h` score `-0.0324` n `37` status `ready` deltaP `5.5754` edge `0.0033` maxDD `-0.9036`
- `news_risk_high->crypto_major_24h` score `-0.0446` n `37` status `ready` deltaP `11.7164` edge `0.1938` maxDD `-18.2098`
- `risk_on_high->index_1h` score `-0.1672` n `138` status `ready` deltaP `4.0007` edge `-0.0034` maxDD `-0.5764`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
