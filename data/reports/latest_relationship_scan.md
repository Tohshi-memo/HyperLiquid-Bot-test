# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-01T20:07:25.387458+00:00`
- Price records: `672`
- Market context records: `2593`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9200`

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

- `market_context_high->unknown_24h` score `7.6437` n `132` status `ready` deltaP `18.1345` edge `0.5489` maxDD `-1.626`
- `market_context_high->crypto_alt_4h` score `5.6477` n `146` status `ready` deltaP `25.8061` edge `0.5665` maxDD `-15.4319`
- `market_context_high->crypto_major_4h` score `3.9302` n `146` status `ready` deltaP `16.5929` edge `0.3979` maxDD `-10.1468`
- `market_context_high->crypto_alt_24h` score `1.6779` n `132` status `ready` deltaP `3.1882` edge `0.7564` maxDD `-39.0265`
- `market_context_high->crypto_alt_1h` score `1.4324` n `146` status `ready` deltaP `11.73` edge `0.1599` maxDD `-6.1656`
- `market_context_high->unknown_4h` score `0.9491` n `146` status `ready` deltaP `7.9895` edge `0.1308` maxDD `-3.7312`
- `market_context_high->index_24h` score `0.9111` n `132` status `ready` deltaP `8.7752` edge `0.1155` maxDD `-2.5127`
- `market_context_high->crypto_major_1h` score `0.836` n `146` status `ready` deltaP `9.4619` edge `0.126` maxDD `-4.2199`
- `market_context_high->index_4h` score `0.2474` n `146` status `ready` deltaP `9.28` edge `0.0429` maxDD `-2.3986`
- `market_context_high->equity_24h` score `0.2276` n `132` status `ready` deltaP `16.8876` edge `-0.0266` maxDD `-2.3615`
- `market_context_high->index_1h` score `-0.1467` n `146` status `ready` deltaP `3.9414` edge `0.0109` maxDD `-1.2855`
- `market_context_high->unknown_1h` score `-0.3756` n `146` status `ready` deltaP `2.0999` edge `0.021` maxDD `-2.6375`
- `market_context_high->commodity_1h` score `-0.4374` n `146` status `ready` deltaP `5.2026` edge `0.0167` maxDD `-4.3601`
- `market_context_high->metal_1h` score `-0.6284` n `146` status `ready` deltaP `1.1115` edge `0.015` maxDD `-2.9823`
- `market_context_high->metal_4h` score `-0.6292` n `146` status `ready` deltaP `4.5021` edge `0.0563` maxDD `-4.7664`
- `market_context_high->fx_1h` score `-0.676` n `146` status `ready` deltaP `-0.9843` edge `0.0037` maxDD `-0.278`
- `market_context_high->crypto_major_24h` score `-0.7451` n `132` status `ready` deltaP `5.2557` edge `0.4252` maxDD `-30.1198`
- `market_context_high->equity_1h` score `-0.8073` n `146` status `ready` deltaP `-0.2276` edge `0.0181` maxDD `-2.7085`
- `market_context_high->fx_4h` score `-0.9144` n `146` status `ready` deltaP `-0.378` edge `0.0121` maxDD `-0.8621`
- `market_context_high->fx_24h` score `-0.9777` n `132` status `ready` deltaP `2.6831` edge `0.0` maxDD `-1.6157`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
