# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-25T07:34:58.230348+00:00`
- Price records: `672`
- Market context records: `7856`
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

- `market_context_high->equity_24h` score `10.779` n `132` status `ready` deltaP `28.5507` edge `0.8421` maxDD `-6.0681`
- `market_context_high->commodity_24h` score `1.3472` n `132` status `ready` deltaP `21.9921` edge `0.124` maxDD `-7.0012`
- `market_context_high->equity_4h` score `1.1807` n `133` status `ready` deltaP `3.8042` edge `0.3173` maxDD `-6.9701`
- `market_context_high->crypto_major_1h` score `1.0514` n `133` status `ready` deltaP `12.8585` edge `0.046` maxDD `-1.5286`
- `market_context_high->crypto_major_4h` score `1.0325` n `133` status `ready` deltaP `13.4318` edge `0.1683` maxDD `-6.7444`
- `market_context_high->metal_24h` score `0.9067` n `133` status `ready` deltaP `8.1651` edge `0.2302` maxDD `-2.3927`
- `market_context_high->fx_24h` score `0.839` n `132` status `ready` deltaP `25.2187` edge `0.0482` maxDD `-3.0343`
- `market_context_high->equity_1h` score `0.6806` n `133` status `ready` deltaP `7.4454` edge `0.093` maxDD `-4.2072`
- `market_context_high->commodity_4h` score `0.6098` n `133` status `ready` deltaP `9.986` edge `0.0436` maxDD `-1.0817`
- `market_context_high->crypto_alt_4h` score `0.6042` n `133` status `ready` deltaP `7.2849` edge `0.1135` maxDD `-3.9374`
- `market_context_high->index_1h` score `0.3746` n `133` status `ready` deltaP `8.6444` edge `0.0166` maxDD `-0.7743`
- `market_context_high->crypto_alt_1h` score `0.2108` n `133` status `ready` deltaP `4.428` edge `0.0313` maxDD `-1.4603`
- `market_context_high->commodity_1h` score `0.0846` n `133` status `ready` deltaP `5.9473` edge `0.0133` maxDD `-0.6722`
- `market_context_high->index_4h` score `-0.1285` n `133` status `ready` deltaP `11.7818` edge `0.0508` maxDD `-1.3325`
- `market_context_high->fx_1h` score `-0.3858` n `133` status `ready` deltaP `0.9743` edge `0.0001` maxDD `-0.4331`
- `market_context_high->metal_1h` score `-0.7896` n `133` status `ready` deltaP `2.1656` edge `0.0201` maxDD `-0.6936`
- `market_context_high->index_24h` score `-1.1924` n `132` status `ready` deltaP `-4.9658` edge `0.0905` maxDD `-2.1544`
- `market_context_high->metal_4h` score `-1.208` n `133` status `ready` deltaP `4.0344` edge `0.0779` maxDD `-1.4368`
- `market_context_high->fx_4h` score `-1.3889` n `133` status `ready` deltaP `-2.4798` edge `0.0013` maxDD `-1.6936`
- `market_context_high->crypto_alt_24h` score `-1.6512` n `133` status `ready` deltaP `16.1296` edge `0.2103` maxDD `-28.3623`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
