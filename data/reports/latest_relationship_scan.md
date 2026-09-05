# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-05T20:07:27.767762+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `10591`

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

- `risk_on_high->unknown_4h` score `20.9858` n `138` status `ready` deltaP `-1.3985` edge `1.9587` maxDD `-7.7112`
- `risk_on_and_context->unknown_4h` score `20.9858` n `138` status `ready` deltaP `-1.3985` edge `1.9587` maxDD `-7.7112`
- `market_context_high->unknown_4h` score `8.123` n `228` status `ready` deltaP `1.8052` edge `0.9117` maxDD `-9.4124`
- `news_risk_high->crypto_alt_24h` score `6.8363` n `37` status `ready` deltaP `25.1783` edge `0.4288` maxDD `-0.8236`
- `news_risk_high->commodity_24h` score `3.8191` n `37` status `ready` deltaP `20.1389` edge `0.184` maxDD `0.0`
- `news_risk_high->crypto_major_4h` score `3.2759` n `37` status `ready` deltaP `16.5706` edge `0.2038` maxDD `-0.9693`
- `news_risk_high->metal_4h` score `2.3759` n `37` status `ready` deltaP `24.1513` edge `0.0591` maxDD `-0.7692`
- `news_risk_high->commodity_4h` score `1.6853` n `37` status `ready` deltaP `8.9898` edge `0.1006` maxDD `-0.2737`
- `news_risk_high->equity_1h` score `1.6051` n `37` status `ready` deltaP `13.2344` edge `0.0846` maxDD `-0.7924`
- `news_risk_high->metal_1h` score `1.3077` n `37` status `ready` deltaP `15.6134` edge `0.0242` maxDD `-0.2118`
- `news_risk_high->index_1h` score `1.1131` n `37` status `ready` deltaP `13.9748` edge `0.013` maxDD `-0.0724`
- `news_risk_high->crypto_major_1h` score `1.0983` n `37` status `ready` deltaP `5.717` edge `0.0717` maxDD `-0.4628`
- `news_risk_high->crypto_alt_1h` score `0.8878` n `37` status `ready` deltaP `8.5775` edge `0.0433` maxDD `-0.7867`
- `news_risk_high->fx_24h` score `0.7832` n `37` status `ready` deltaP `18.3934` edge `0.0442` maxDD `-3.1244`
- `market_context_high->equity_24h` score `0.6736` n `168` status `ready` deltaP `12.4504` edge `0.4077` maxDD `-20.7654`
- `news_risk_high->crypto_major_24h` score `0.6084` n `37` status `ready` deltaP `16.5776` edge `0.2451` maxDD `-18.2098`
- `news_risk_high->crypto_alt_4h` score `0.3697` n `37` status `ready` deltaP `4.7215` edge `0.0322` maxDD `-1.296`
- `risk_on_high->index_1h` score `0.0565` n `145` status `ready` deltaP `7.7865` edge `-0.0025` maxDD `-0.5764`
- `risk_on_and_context->index_1h` score `0.0565` n `145` status `ready` deltaP `7.7865` edge `-0.0025` maxDD `-0.5764`
- `news_risk_high->commodity_1h` score `-0.0589` n `37` status `ready` deltaP `5.1263` edge `0.0029` maxDD `-0.9036`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
