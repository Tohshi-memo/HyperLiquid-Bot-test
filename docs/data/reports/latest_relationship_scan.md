# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-05T08:07:25.653842+00:00`
- Price records: `672`
- Market context records: `2951`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `72`

- Symbol pattern count: `6954`

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

- `market_context_high->crypto_alt_24h` score `17.0825` n `131` status `ready` deltaP `14.3726` edge `1.7194` maxDD `-22.6673`
- `market_context_high->equity_24h` score `8.1506` n `131` status `ready` deltaP `18.4186` edge `0.7568` maxDD `-12.6963`
- `market_context_high->unknown_24h` score `7.7925` n `131` status `ready` deltaP `16.6414` edge `0.5849` maxDD `-1.7175`
- `market_context_high->commodity_24h` score `4.3699` n `131` status `ready` deltaP `21.2322` edge `0.4321` maxDD `-8.0928`
- `market_context_high->index_24h` score `3.0991` n `131` status `ready` deltaP `14.2546` edge `0.2613` maxDD `-2.5127`
- `market_context_high->equity_4h` score `2.2951` n `132` status `ready` deltaP `12.6801` edge `0.1799` maxDD `-3.5206`
- `market_context_high->crypto_alt_4h` score `1.0652` n `132` status `ready` deltaP `18.9902` edge `0.4183` maxDD `-30.8239`
- `market_context_high->index_4h` score `0.735` n `132` status `ready` deltaP `14.5463` edge `0.0814` maxDD `-2.3986`
- `market_context_high->unknown_4h` score `0.5021` n `132` status `ready` deltaP `4.8411` edge `0.1149` maxDD `-3.7602`
- `market_context_high->index_1h` score `0.1117` n `132` status `ready` deltaP `6.2285` edge `0.0222` maxDD `-1.2855`
- `market_context_high->equity_1h` score `-0.0568` n `132` status `ready` deltaP `2.6266` edge `0.0532` maxDD `-2.0358`
- `market_context_high->fx_1h` score `-0.2747` n `132` status `ready` deltaP `0.6351` edge `0.0036` maxDD `-0.1244`
- `market_context_high->crypto_alt_1h` score `-0.3408` n `132` status `ready` deltaP `5.9109` edge `0.0929` maxDD `-10.747`
- `market_context_high->metal_1h` score `-0.5567` n `132` status `ready` deltaP `1.1794` edge `0.0095` maxDD `-3.4325`
- `market_context_high->crypto_major_1h` score `-0.625` n `132` status `ready` deltaP `5.117` edge `0.0727` maxDD `-9.622`
- `market_context_high->fx_4h` score `-0.7086` n `132` status `ready` deltaP `1.3535` edge `0.0098` maxDD `-0.5631`
- `market_context_high->commodity_1h` score `-0.7274` n `132` status `ready` deltaP `-1.7873` edge `-0.0104` maxDD `-4.0086`
- `market_context_high->unknown_1h` score `-0.8623` n `132` status `ready` deltaP `1.3836` edge `-0.008` maxDD `-3.1801`
- `market_context_high->commodity_4h` score `-0.9013` n `132` status `ready` deltaP `4.6517` edge `0.0324` maxDD `-8.9839`
- `market_context_high->crypto_major_4h` score `-1.1867` n `132` status `ready` deltaP `9.1509` edge `0.2994` maxDD `-33.6701`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
