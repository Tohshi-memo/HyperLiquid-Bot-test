# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-25T10:07:32.606004+00:00`
- Price records: `672`
- Market context records: `7867`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `14661`

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

- `market_context_high->equity_24h` score `12.1536` n `122` status `ready` deltaP `29.0976` edge `0.953` maxDD `-6.0681`
- `market_context_high->metal_24h` score `2.1899` n `123` status `ready` deltaP `13.2589` edge `0.2569` maxDD `-2.0241`
- `market_context_high->equity_4h` score `2.0869` n `123` status `ready` deltaP `8.3277` edge `0.3489` maxDD `-5.9491`
- `market_context_high->crypto_major_4h` score `1.4898` n `123` status `ready` deltaP `16.4634` edge `0.1862` maxDD `-6.7444`
- `market_context_high->commodity_24h` score `1.3683` n `122` status `ready` deltaP `21.3714` edge `0.1299` maxDD `-7.0012`
- `market_context_high->crypto_major_1h` score `1.2661` n `123` status `ready` deltaP `14.0779` edge `0.0516` maxDD `-1.5286`
- `market_context_high->crypto_alt_4h` score `1.2279` n `123` status `ready` deltaP `11.3313` edge `0.1385` maxDD `-3.9374`
- `market_context_high->fx_24h` score `0.9884` n `122` status `ready` deltaP `28.0627` edge `0.0484` maxDD `-3.0343`
- `market_context_high->equity_1h` score `0.6818` n `123` status `ready` deltaP `10.0747` edge `0.102` maxDD `-4.2072`
- `market_context_high->crypto_alt_1h` score `0.4529` n `123` status `ready` deltaP `5.8188` edge `0.0422` maxDD `-1.4603`
- `market_context_high->commodity_4h` score `0.3638` n `123` status `ready` deltaP `7.5409` edge `0.0394` maxDD `-1.0817`
- `market_context_high->index_1h` score `0.1962` n `123` status `ready` deltaP `7.7493` edge `0.0165` maxDD `-0.7743`
- `market_context_high->commodity_1h` score `0.035` n `123` status `ready` deltaP `5.2076` edge `0.0141` maxDD `-0.6722`
- `market_context_high->index_4h` score `-0.2074` n `123` status `ready` deltaP `10.0582` edge `0.0519` maxDD `-1.3101`
- `market_context_high->fx_1h` score `-0.3007` n `123` status `ready` deltaP `0.0696` edge `-0.0003` maxDD `-0.4304`
- `market_context_high->metal_1h` score `-0.5846` n `123` status `ready` deltaP `0.5976` edge `0.0214` maxDD `-0.6936`
- `market_context_high->metal_4h` score `-0.8165` n `123` status `ready` deltaP `4.1158` edge `0.0844` maxDD `-1.3906`
- `market_context_high->fx_4h` score `-1.38` n `123` status `ready` deltaP `-2.8716` edge `0.0004` maxDD `-1.6539`
- `market_context_high->index_24h` score `-1.3965` n `122` status `ready` deltaP `-3.8603` edge `0.1014` maxDD `-2.0299`
- `market_context_high->crypto_alt_24h` score `-1.5076` n `123` status `ready` deltaP `14.7962` edge `0.2376` maxDD `-28.3623`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
