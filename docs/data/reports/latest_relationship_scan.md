# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-25T02:03:39.135107+00:00`
- Price records: `672`
- Market context records: `7833`
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

- `market_context_high->equity_24h` score `9.7974` n `132` status `ready` deltaP `28.5507` edge `0.7603` maxDD `-6.0681`
- `market_context_high->equity_4h` score `1.3979` n `133` status `ready` deltaP `6.5565` edge `0.3268` maxDD `-6.9701`
- `market_context_high->metal_24h` score `1.2632` n `133` status `ready` deltaP `11.6313` edge `0.2368` maxDD `-2.3927`
- `market_context_high->crypto_major_4h` score `1.1828` n `133` status `ready` deltaP `14.6513` edge `0.1727` maxDD `-6.7444`
- `market_context_high->crypto_major_1h` score `1.0741` n `133` status `ready` deltaP `13.1579` edge `0.0459` maxDD `-1.5286`
- `market_context_high->fx_24h` score `0.8288` n `132` status `ready` deltaP `25.2187` edge `0.0469` maxDD `-3.0343`
- `market_context_high->crypto_alt_4h` score `0.8024` n `133` status `ready` deltaP `8.352` edge `0.1229` maxDD `-3.9374`
- `market_context_high->equity_1h` score `0.7778` n `133` status `ready` deltaP `8.3463` edge `0.0951` maxDD `-4.2072`
- `market_context_high->commodity_24h` score `0.7454` n `132` status `ready` deltaP `18.3399` edge `0.0982` maxDD `-7.0012`
- `market_context_high->commodity_4h` score `0.4517` n `133` status `ready` deltaP `8.6098` edge `0.0396` maxDD `-1.0817`
- `market_context_high->index_1h` score `0.3518` n `133` status `ready` deltaP `8.3441` edge `0.0167` maxDD `-0.7743`
- `market_context_high->crypto_alt_1h` score `0.2623` n `133` status `ready` deltaP `5.0268` edge `0.0316` maxDD `-1.4603`
- `market_context_high->commodity_1h` score `0.0389` n `133` status `ready` deltaP `5.4969` edge `0.0125` maxDD `-0.6722`
- `market_context_high->index_4h` score `-0.0674` n `133` status `ready` deltaP `12.8521` edge `0.0515` maxDD `-1.3325`
- `market_context_high->fx_1h` score `-0.3726` n `133` status `ready` deltaP `1.1245` edge `0.0002` maxDD `-0.4331`
- `market_context_high->metal_1h` score `-0.8243` n `133` status `ready` deltaP `1.7165` edge `0.0202` maxDD `-0.6936`
- `market_context_high->index_24h` score `-1.2758` n `132` status `ready` deltaP `-5.8353` edge `0.0856` maxDD `-2.1544`
- `market_context_high->fx_4h` score `-1.408` n `133` status `ready` deltaP `-2.7856` edge `0.0009` maxDD `-1.6936`
- `market_context_high->metal_4h` score `-1.4127` n `133` status `ready` deltaP `1.5954` edge `0.0771` maxDD `-1.4368`
- `market_context_high->crypto_alt_24h` score `-2.0837` n `133` status `ready` deltaP `14.7431` edge `0.1641` maxDD `-28.3623`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
