# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-25T12:37:23.323105+00:00`
- Price records: `672`
- Market context records: `7878`
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

- `market_context_high->equity_24h` score `13.2796` n `114` status `ready` deltaP `29.3129` edge `1.0454` maxDD `-6.0681`
- `market_context_high->equity_4h` score `4.4442` n `114` status `ready` deltaP `12.9245` edge `0.3818` maxDD `-5.1426`
- `market_context_high->metal_24h` score `3.6088` n `114` status `ready` deltaP `18.9714` edge `0.2894` maxDD `-1.2117`
- `market_context_high->crypto_alt_4h` score `1.6212` n `114` status `ready` deltaP `13.9977` edge `0.1535` maxDD `-3.9374`
- `market_context_high->crypto_major_4h` score `1.6175` n `114` status `ready` deltaP `16.8592` edge `0.1942` maxDD `-6.7444`
- `market_context_high->commodity_24h` score `1.4725` n `114` status `ready` deltaP `21.3085` edge `0.139` maxDD `-7.0012`
- `market_context_high->fx_24h` score `1.1302` n `114` status `ready` deltaP `30.7292` edge `0.0488` maxDD `-3.0343`
- `market_context_high->crypto_major_1h` score `1.1256` n `115` status `ready` deltaP `12.7584` edge `0.0496` maxDD `-1.6021`
- `market_context_high->equity_1h` score `0.7979` n `115` status `ready` deltaP `11.2573` edge `0.109` maxDD `-4.2072`
- `market_context_high->commodity_4h` score `0.4464` n `114` status `ready` deltaP `8.0638` edge `0.0428` maxDD `-1.0817`
- `market_context_high->index_4h` score `0.3084` n `114` status `ready` deltaP `13.0774` edge `0.0568` maxDD `-1.1293`
- `market_context_high->crypto_alt_1h` score `0.269` n `115` status `ready` deltaP `4.12` edge `0.0382` maxDD `-1.4603`
- `market_context_high->index_1h` score `0.1871` n `115` status `ready` deltaP `7.454` edge `0.0173` maxDD `-0.7743`
- `market_context_high->metal_4h` score `0.025` n `114` status `ready` deltaP `7.2449` edge `0.0932` maxDD `-1.1535`
- `market_context_high->commodity_1h` score `0.0125` n `115` status `ready` deltaP `5.0763` edge `0.0131` maxDD `-0.6722`
- `market_context_high->fx_1h` score `-0.3295` n `115` status `ready` deltaP `1.6673` edge `-0.0001` maxDD `-0.4112`
- `market_context_high->index_24h` score `-0.6025` n `114` status `ready` deltaP `-1.1422` edge `0.1126` maxDD `-1.7485`
- `market_context_high->metal_1h` score `-0.6949` n `115` status `ready` deltaP `0.3996` edge `0.0231` maxDD `-0.6936`
- `market_context_high->fx_4h` score `-0.9575` n `114` status `ready` deltaP `-0.4023` edge `0.0001` maxDD `-1.6144`
- `market_context_high->crypto_alt_24h` score `-1.6097` n `114` status `ready` deltaP `12.9542` edge `0.2368` maxDD `-28.3623`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
