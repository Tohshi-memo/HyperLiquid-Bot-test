# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-24T14:37:24.837955+00:00`
- Price records: `672`
- Market context records: `7783`
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

- `market_context_high->equity_24h` score `7.3744` n `132` status `ready` deltaP `27.9326` edge `0.5625` maxDD `-6.0681`
- `market_context_high->metal_24h` score `1.4824` n `133` status `ready` deltaP `13.9659` edge `0.2395` maxDD `-2.3927`
- `market_context_high->crypto_major_1h` score `1.0513` n `133` status `ready` deltaP `13.1579` edge `0.044` maxDD `-1.5286`
- `market_context_high->crypto_major_4h` score `0.8297` n `133` status `ready` deltaP `13.4318` edge `0.1514` maxDD `-6.7444`
- `market_context_high->equity_4h` score `0.7787` n `133` status `ready` deltaP `2.7339` edge `0.2729` maxDD `-6.9701`
- `market_context_high->fx_24h` score `0.749` n `132` status `ready` deltaP `24.3137` edge `0.0427` maxDD `-3.0343`
- `market_context_high->equity_1h` score `0.6578` n `133` status `ready` deltaP `7.8958` edge `0.0881` maxDD `-4.2072`
- `market_context_high->crypto_alt_4h` score `0.6374` n `133` status `ready` deltaP `7.8947` edge `0.1122` maxDD `-3.9374`
- `market_context_high->index_1h` score `0.3446` n `133` status `ready` deltaP `8.3441` edge `0.0161` maxDD `-0.7743`
- `market_context_high->commodity_4h` score `0.2159` n `133` status `ready` deltaP `6.622` edge `0.0332` maxDD `-1.0817`
- `market_context_high->crypto_alt_1h` score `0.2072` n `133` status `ready` deltaP `4.428` edge `0.031` maxDD `-1.4603`
- `market_context_high->commodity_1h` score `-0.0175` n `133` status `ready` deltaP `5.0464` edge `0.0108` maxDD `-0.6722`
- `market_context_high->index_4h` score `-0.209` n `133` status `ready` deltaP `10.8643` edge `0.0466` maxDD `-1.3325`
- `market_context_high->fx_1h` score `-0.375` n `133` status `ready` deltaP `1.1245` edge `0.0` maxDD `-0.4331`
- `market_context_high->commodity_24h` score `-0.6646` n `132` status `ready` deltaP `10.3896` edge `0.0337` maxDD `-7.0012`
- `market_context_high->metal_1h` score `-0.9357` n `133` status `ready` deltaP `0.5189` edge `0.0189` maxDD `-0.6936`
- `market_context_high->fx_4h` score `-1.3461` n `133` status `ready` deltaP `-1.7153` edge `0.0017` maxDD `-1.6936`
- `market_context_high->metal_4h` score `-1.5644` n `133` status `ready` deltaP `0.2235` edge `0.0736` maxDD `-1.4368`
- `market_context_high->index_24h` score `-1.7678` n `132` status `ready` deltaP `-10.9624` edge `0.0567` maxDD `-2.1544`
- `market_context_high->unknown_1h` score `-2.0918` n `133` status `ready` deltaP `0.0732` edge `-0.1158` maxDD `-1.054`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
