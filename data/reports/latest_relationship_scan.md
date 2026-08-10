# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-10T22:07:29.154696+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11712`

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

- `market_context_high->fx_24h` score `1.0245` n `145` status `ready` deltaP `20.4064` edge `0.0301` maxDD `-1.4613`
- `market_context_high->commodity_4h` score `0.8906` n `176` status `ready` deltaP `12.0566` edge `0.0653` maxDD `-2.7169`
- `market_context_high->commodity_1h` score `0.6574` n `181` status `ready` deltaP `8.9523` edge `0.0294` maxDD `-0.7439`
- `market_context_high->fx_4h` score `-0.0466` n `176` status `ready` deltaP `7.3032` edge `0.0074` maxDD `-0.4647`
- `market_context_high->fx_1h` score `-0.1038` n `181` status `ready` deltaP `4.764` edge `0.0001` maxDD `-0.613`
- `market_context_high->index_1h` score `-0.6783` n `181` status `ready` deltaP `-5.3197` edge `-0.0036` maxDD `-0.832`
- `market_context_high->index_24h` score `-0.6889` n `145` status `ready` deltaP `-1.3625` edge `0.0739` maxDD `-5.9181`
- `market_context_high->index_4h` score `-0.9614` n `176` status `ready` deltaP `-4.5455` edge `-0.0132` maxDD `-1.3801`
- `market_context_high->metal_24h` score `-1.041` n `145` status `ready` deltaP `2.5482` edge `0.0287` maxDD `-2.9283`
- `market_context_high->equity_1h` score `-1.0799` n `181` status `ready` deltaP `-3.7797` edge `-0.0096` maxDD `-5.9591`
- `market_context_high->metal_1h` score `-1.246` n `181` status `ready` deltaP `-4.6994` edge `-0.0089` maxDD `-2.0884`
- `market_context_high->equity_24h` score `-2.3266` n `145` status `ready` deltaP `-1.2072` edge `0.1763` maxDD `-27.9895`
- `market_context_high->crypto_alt_1h` score `-2.7754` n `181` status `ready` deltaP `-10.431` edge `-0.042` maxDD `-6.5795`
- `market_context_high->metal_4h` score `-3.0732` n `176` status `ready` deltaP `-6.7212` edge `-0.0349` maxDD `-6.1111`
- `market_context_high->crypto_major_1h` score `-3.7367` n `181` status `ready` deltaP `-10.0605` edge `-0.0539` maxDD `-11.9002`
- `market_context_high->crypto_major_24h` score `-3.8023` n `145` status `ready` deltaP `-3.9479` edge `-0.1021` maxDD `-21.724`
- `market_context_high->equity_4h` score `-3.8296` n `176` status `ready` deltaP `-13.678` edge `-0.12` maxDD `-13.3831`
- `market_context_high->crypto_alt_4h` score `-6.6112` n `176` status `ready` deltaP `-13.7195` edge `-0.1479` maxDD `-18.2586`
- `market_context_high->commodity_24h` score `-6.6688` n `145` status `ready` deltaP `-1.0017` edge `-0.0932` maxDD `-45.4075`
- `market_context_high->crypto_alt_24h` score `-6.7085` n `145` status `ready` deltaP `-12.8226` edge `-0.1942` maxDD `-17.0155`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
