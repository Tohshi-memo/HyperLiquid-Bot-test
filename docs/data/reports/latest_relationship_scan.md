# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-05T20:22:23.429839+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `10597`

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

- `risk_on_high->unknown_4h` score `21.1108` n `138` status `ready` deltaP `-0.8263` edge `1.9653` maxDD `-7.7112`
- `risk_on_and_context->unknown_4h` score `21.1108` n `138` status `ready` deltaP `-0.8263` edge `1.9653` maxDD `-7.7112`
- `market_context_high->unknown_4h` score `8.1866` n `228` status `ready` deltaP `2.0913` edge `0.9151` maxDD `-9.4124`
- `news_risk_high->crypto_alt_24h` score `6.8075` n `37` status `ready` deltaP `25.1783` edge `0.4264` maxDD `-0.8236`
- `news_risk_high->commodity_24h` score `3.8263` n `37` status `ready` deltaP `20.1389` edge `0.1846` maxDD `0.0`
- `news_risk_high->crypto_major_4h` score `3.2687` n `37` status `ready` deltaP `16.5706` edge `0.2032` maxDD `-0.9693`
- `news_risk_high->metal_4h` score `2.3759` n `37` status `ready` deltaP `24.1513` edge `0.0591` maxDD `-0.7692`
- `news_risk_high->commodity_4h` score `1.6719` n `37` status `ready` deltaP `8.8374` edge `0.1005` maxDD `-0.2737`
- `news_risk_high->equity_1h` score `1.6051` n `37` status `ready` deltaP `13.2344` edge `0.0846` maxDD `-0.7924`
- `news_risk_high->metal_1h` score `1.3197` n `37` status `ready` deltaP `15.7631` edge `0.0242` maxDD `-0.2118`
- `news_risk_high->index_1h` score `1.1251` n `37` status `ready` deltaP `14.1245` edge `0.013` maxDD `-0.0724`
- `news_risk_high->crypto_major_1h` score `1.1019` n `37` status `ready` deltaP `5.717` edge `0.072` maxDD `-0.4628`
- `news_risk_high->crypto_alt_1h` score `0.8878` n `37` status `ready` deltaP `8.5775` edge `0.0433` maxDD `-0.7867`
- `news_risk_high->fx_24h` score `0.7983` n `37` status `ready` deltaP `18.567` edge `0.0443` maxDD `-3.1244`
- `market_context_high->equity_24h` score `0.7028` n `167` status `ready` deltaP `12.29` edge `0.4112` maxDD `-20.7654`
- `news_risk_high->crypto_major_24h` score `0.5857` n `37` status `ready` deltaP `16.5776` edge `0.2422` maxDD `-18.2098`
- `news_risk_high->crypto_alt_4h` score `0.3625` n `37` status `ready` deltaP `4.7215` edge `0.0316` maxDD `-1.296`
- `risk_on_high->index_1h` score `0.0133` n `145` status `ready` deltaP `7.2466` edge `-0.0025` maxDD `-0.5764`
- `risk_on_and_context->index_1h` score `0.0133` n `145` status `ready` deltaP `7.2466` edge `-0.0025` maxDD `-0.5764`
- `news_risk_high->commodity_1h` score `-0.0511` n `37` status `ready` deltaP `5.276` edge `0.0029` maxDD `-0.9036`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
