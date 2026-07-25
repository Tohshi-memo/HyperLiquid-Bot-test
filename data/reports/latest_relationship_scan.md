# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-25T12:52:27.038265+00:00`
- Price records: `672`
- Market context records: `7879`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `14671`

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

- `market_context_high->equity_24h` score `13.4789` n `113` status `ready` deltaP `29.4045` edge `1.0614` maxDD `-6.0681`
- `market_context_high->equity_4h` score `4.5164` n `113` status `ready` deltaP `13.273` edge `0.3855` maxDD `-5.1426`
- `market_context_high->metal_24h` score `3.7862` n `113` status `ready` deltaP `19.7646` edge `0.2936` maxDD `-1.1213`
- `market_context_high->crypto_major_4h` score `1.5887` n `113` status `ready` deltaP `16.5151` edge `0.1941` maxDD `-6.7444`
- `market_context_high->crypto_alt_4h` score `1.5868` n `113` status `ready` deltaP `13.6125` edge `0.1532` maxDD `-3.9374`
- `market_context_high->commodity_24h` score `1.5131` n `113` status `ready` deltaP `21.3954` edge `0.1418` maxDD `-7.0012`
- `market_context_high->crypto_major_1h` score `1.1976` n `115` status `ready` deltaP `13.4036` edge `0.0513` maxDD `-1.6021`
- `market_context_high->fx_24h` score `1.1074` n `113` status `ready` deltaP `30.3201` edge `0.0486` maxDD `-3.0343`
- `market_context_high->equity_1h` score `0.8393` n `115` status `ready` deltaP `11.9041` edge `0.11` maxDD `-4.2072`
- `market_context_high->commodity_4h` score `0.4549` n `113` status `ready` deltaP `8.02` edge `0.0438` maxDD `-1.0817`
- `market_context_high->index_4h` score `0.4001` n `113` status `ready` deltaP `13.4256` edge `0.0575` maxDD `-1.093`
- `market_context_high->crypto_alt_1h` score `0.3504` n `115` status `ready` deltaP `4.7625` edge `0.0407` maxDD `-1.4603`
- `market_context_high->index_1h` score `0.3403` n `115` status `ready` deltaP `8.0959` edge `0.0174` maxDD `-0.7743`
- `market_context_high->metal_4h` score `0.141` n `113` status `ready` deltaP `7.807` edge `0.0945` maxDD `-1.1168`
- `market_context_high->commodity_1h` score `0.0046` n `115` status `ready` deltaP `5.0075` edge `0.0129` maxDD `-0.6722`
- `market_context_high->fx_1h` score `-0.3825` n `115` status `ready` deltaP `1.0195` edge `-0.0002` maxDD `-0.4112`
- `market_context_high->index_24h` score `-0.4875` n `113` status `ready` deltaP `-0.7131` edge `0.1145` maxDD `-1.6964`
- `market_context_high->metal_1h` score `-0.6393` n `115` status `ready` deltaP `0.4692` edge `0.0231` maxDD `-0.6936`
- `market_context_high->fx_4h` score `-0.9019` n `113` status `ready` deltaP `0.0352` edge `0.0001` maxDD `-1.6107`
- `market_context_high->crypto_alt_24h` score `-1.6153` n `113` status `ready` deltaP `12.7859` edge `0.2372` maxDD `-28.3623`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
