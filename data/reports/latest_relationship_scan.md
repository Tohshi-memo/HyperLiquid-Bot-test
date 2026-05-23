# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-23T18:48:21.209069+00:00`
- Price records: `672`
- Market context records: `1657`
- Flow alert records: `6680`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8844`

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

- `market_context_high->metal_24h` score `9.8759` n `169` status `ready` deltaP `28.9337` edge `0.8727` maxDD `-12.7414`
- `market_context_high->crypto_alt_4h` score `4.3834` n `191` status `ready` deltaP `22.2907` edge `0.4831` maxDD `-16.3135`
- `market_context_high->index_24h` score `3.7923` n `169` status `ready` deltaP `20.5841` edge `0.3166` maxDD `-5.3574`
- `market_context_high->crypto_major_4h` score `2.5519` n `191` status `ready` deltaP `18.3214` edge `0.3614` maxDD `-13.3376`
- `market_context_high->equity_4h` score `1.882` n `191` status `ready` deltaP `12.5375` edge `0.1827` maxDD `-5.0894`
- `market_context_high->equity_24h` score `1.7633` n `169` status `ready` deltaP `19.9473` edge `0.5038` maxDD `-33.1875`
- `market_context_high->crypto_major_24h` score `0.8695` n `169` status `ready` deltaP `25.7468` edge `0.7594` maxDD `-62.3533`
- `market_context_high->crypto_alt_24h` score `0.6851` n `169` status `ready` deltaP `26.401` edge `1.062` maxDD `-88.8062`
- `market_context_high->crypto_alt_1h` score `0.5807` n `202` status `ready` deltaP `6.5038` edge `0.1074` maxDD `-4.1892`
- `market_context_high->equity_1h` score `-0.2297` n `202` status `ready` deltaP `1.9209` edge `0.0386` maxDD `-2.8014`
- `market_context_high->index_4h` score `-0.3758` n `191` status `ready` deltaP `1.3236` edge `0.0519` maxDD `-3.7119`
- `market_context_high->crypto_major_1h` score `-0.3959` n `202` status `ready` deltaP `2.659` edge `0.0589` maxDD `-5.5244`
- `market_context_high->index_1h` score `-0.4677` n `202` status `ready` deltaP `-0.8078` edge `0.0086` maxDD `-1.7205`
- `market_context_high->fx_24h` score `-0.4702` n `169` status `ready` deltaP `6.214` edge `0.0243` maxDD `-1.3925`
- `market_context_high->metal_1h` score `-0.7742` n `202` status `ready` deltaP `4.2939` edge `0.0057` maxDD `-6.3532`
- `market_context_high->fx_1h` score `-0.7941` n `202` status `ready` deltaP `0.0222` edge `-0.0031` maxDD `-0.3914`
- `market_context_high->commodity_1h` score `-1.0743` n `202` status `ready` deltaP `0.6329` edge `-0.0119` maxDD `-8.0707`
- `market_context_high->metal_4h` score `-1.3046` n `191` status `ready` deltaP `8.7699` edge `0.102` maxDD `-12.5349`
- `market_context_high->fx_4h` score `-1.9476` n `191` status `ready` deltaP `-8.4168` edge `-0.0133` maxDD `-1.4313`
- `market_context_high->unknown_4h` score `-3.9286` n `191` status `ready` deltaP `11.2107` edge `-0.175` maxDD `-11.1695`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
