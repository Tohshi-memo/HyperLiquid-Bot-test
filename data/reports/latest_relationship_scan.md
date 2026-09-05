# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-05T03:22:25.031444+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `10466`

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

- `risk_on_high->unknown_4h` score `19.5746` n `133` status `ready` deltaP `7.6265` edge `1.6422` maxDD `-2.2797`
- `risk_on_and_context->unknown_4h` score `19.5746` n `133` status `ready` deltaP `7.6265` edge `1.6422` maxDD `-2.2797`
- `market_context_high->unknown_4h` score `9.077` n `217` status `ready` deltaP `8.0631` edge `0.7722` maxDD `-2.563`
- `news_risk_high->crypto_alt_24h` score `7.3047` n `37` status `ready` deltaP `24.6575` edge `0.4713` maxDD `-0.8236`
- `news_risk_high->commodity_24h` score `4.3889` n `37` status `ready` deltaP `25.5208` edge `0.1956` maxDD `0.0`
- `news_risk_high->crypto_major_4h` score `3.858` n `37` status `ready` deltaP `17.6376` edge `0.2452` maxDD `-0.9693`
- `news_risk_high->metal_4h` score `2.1932` n `37` status `ready` deltaP `22.0172` edge `0.0581` maxDD `-0.7692`
- `news_risk_high->commodity_4h` score `1.8655` n `37` status `ready` deltaP `10.9715` edge `0.1024` maxDD `-0.2737`
- `news_risk_high->equity_1h` score `1.6183` n `37` status `ready` deltaP `13.3841` edge `0.0847` maxDD `-0.7924`
- `news_risk_high->crypto_major_1h` score `1.3717` n `37` status `ready` deltaP `7.5134` edge `0.0825` maxDD `-0.4628`
- `news_risk_high->index_1h` score `1.2353` n `37` status `ready` deltaP `15.4718` edge `0.0132` maxDD `-0.0724`
- `news_risk_high->crypto_alt_4h` score `1.2288` n `37` status `ready` deltaP `9.2947` edge `0.0733` maxDD `-1.296`
- `news_risk_high->metal_1h` score `1.1963` n `37` status `ready` deltaP `14.2661` edge `0.0239` maxDD `-0.2118`
- `news_risk_high->crypto_alt_1h` score `1.0665` n `37` status `ready` deltaP `9.4757` edge `0.0522` maxDD `-0.7867`
- `risk_on_high->metal_1h` score `0.1451` n `133` status `ready` deltaP `13.311` edge `0.0011` maxDD `-1.699`
- `risk_on_and_context->metal_1h` score `0.1451` n `133` status `ready` deltaP `13.311` edge `0.0011` maxDD `-1.699`
- `news_risk_high->fx_24h` score `0.145` n `37` status `ready` deltaP `11.7961` edge `0.035` maxDD `-3.1244`
- `news_risk_high->commodity_1h` score `0.0088` n `37` status `ready` deltaP `6.3239` edge `0.0036` maxDD `-0.9036`
- `risk_on_high->index_1h` score `-0.1886` n `133` status `ready` deltaP `3.5433` edge `-0.0033` maxDD `-0.5605`
- `risk_on_and_context->index_1h` score `-0.1886` n `133` status `ready` deltaP `3.5433` edge `-0.0033` maxDD `-0.5605`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
