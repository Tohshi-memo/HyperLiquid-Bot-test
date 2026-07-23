# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-23T21:52:23.626949+00:00`
- Price records: `672`
- Market context records: `7711`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `14676`

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

- `market_context_high->equity_24h` score `3.6099` n `132` status `ready` deltaP `19.396` edge `0.3057` maxDD `-6.0681`
- `market_context_high->crypto_major_4h` score `1.1934` n `133` status `ready` deltaP `15.4135` edge `0.1685` maxDD `-6.7444`
- `market_context_high->crypto_major_1h` score `1.1245` n `133` status `ready` deltaP `13.4573` edge `0.0481` maxDD `-1.5286`
- `market_context_high->crypto_alt_4h` score `0.7657` n `133` status `ready` deltaP `8.8093` edge `0.1168` maxDD `-3.9374`
- `market_context_high->equity_4h` score `0.7391` n `133` status `ready` deltaP `2.8868` edge `0.2668` maxDD `-6.9701`
- `market_context_high->equity_1h` score `0.6747` n `133` status `ready` deltaP `8.9469` edge `0.0825` maxDD `-4.2072`
- `market_context_high->index_1h` score `0.4227` n `133` status `ready` deltaP `9.3952` edge `0.0156` maxDD `-0.7743`
- `market_context_high->crypto_alt_1h` score `0.1797` n `133` status `ready` deltaP `3.8292` edge `0.0327` maxDD `-1.4603`
- `market_context_high->fx_24h` score `0.0092` n `132` status `ready` deltaP `12.8155` edge `0.0245` maxDD `-3.0343`
- `market_context_high->index_4h` score `-0.1652` n `133` status `ready` deltaP `11.7818` edge `0.0461` maxDD `-1.3325`
- `market_context_high->commodity_1h` score `-0.2036` n `133` status `ready` deltaP `3.3948` edge `0.0063` maxDD `-0.6722`
- `market_context_high->commodity_4h` score `-0.214` n `133` status `ready` deltaP `4.0227` edge `0.0147` maxDD `-1.0817`
- `market_context_high->metal_24h` score `-0.4875` n `133` status `ready` deltaP `3.202` edge `0.1471` maxDD `-2.3927`
- `market_context_high->fx_1h` score `-0.5179` n `133` status `ready` deltaP `-0.5272` edge `-0.0009` maxDD `-0.4331`
- `market_context_high->metal_1h` score `-0.8662` n `133` status `ready` deltaP `1.2674` edge `0.0197` maxDD `-0.6936`
- `market_context_high->metal_4h` score `-1.4247` n `133` status `ready` deltaP `1.5954` edge `0.0761` maxDD `-1.4368`
- `market_context_high->fx_4h` score `-1.5695` n `133` status `ready` deltaP `-5.2321` edge `-0.0035` maxDD `-1.6936`
- `market_context_high->commodity_24h` score `-1.7549` n `132` status `ready` deltaP `5.6858` edge `-0.0258` maxDD `-7.0012`
- `market_context_high->unknown_1h` score `-2.1373` n `133` status `ready` deltaP `-0.825` edge `-0.1136` maxDD `-1.054`
- `market_context_high->index_24h` score `-2.5895` n `132` status `ready` deltaP `-18.4537` edge `0.0013` maxDD `-2.1544`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
