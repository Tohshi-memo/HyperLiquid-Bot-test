# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-25T02:22:29.067315+00:00`
- Price records: `672`
- Market context records: `7835`
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

- `market_context_high->equity_24h` score `9.8514` n `132` status `ready` deltaP `28.5507` edge `0.7648` maxDD `-6.0681`
- `market_context_high->equity_4h` score `1.3979` n `133` status `ready` deltaP `6.5565` edge `0.3268` maxDD `-6.9701`
- `market_context_high->metal_24h` score `1.2457` n `133` status `ready` deltaP `11.458` edge `0.2365` maxDD `-2.3927`
- `market_context_high->crypto_major_4h` score `1.1647` n `133` status `ready` deltaP `14.4989` edge `0.1722` maxDD `-6.7444`
- `market_context_high->crypto_major_1h` score `1.0717` n `133` status `ready` deltaP `13.1579` edge `0.0457` maxDD `-1.5286`
- `market_context_high->fx_24h` score `0.8288` n `132` status `ready` deltaP `25.2187` edge `0.0469` maxDD `-3.0343`
- `market_context_high->crypto_alt_4h` score `0.7818` n `133` status `ready` deltaP `8.1996` edge `0.1222` maxDD `-3.9374`
- `market_context_high->equity_1h` score `0.7778` n `133` status `ready` deltaP `8.3463` edge `0.0951` maxDD `-4.2072`
- `market_context_high->commodity_24h` score `0.7749` n `132` status `ready` deltaP `18.5139` edge `0.0995` maxDD `-7.0012`
- `market_context_high->commodity_4h` score `0.4541` n `133` status `ready` deltaP `8.6098` edge `0.0398` maxDD `-1.0817`
- `market_context_high->index_1h` score `0.3638` n `133` status `ready` deltaP `8.4943` edge `0.0167` maxDD `-0.7743`
- `market_context_high->crypto_alt_1h` score `0.2623` n `133` status `ready` deltaP `5.0268` edge `0.0316` maxDD `-1.4603`
- `market_context_high->commodity_1h` score `0.0533` n `133` status `ready` deltaP `5.647` edge `0.0127` maxDD `-0.6722`
- `market_context_high->index_4h` score `-0.0666` n `133` status `ready` deltaP `12.8521` edge `0.0516` maxDD `-1.3325`
- `market_context_high->fx_1h` score `-0.3726` n `133` status `ready` deltaP `1.1245` edge `0.0002` maxDD `-0.4331`
- `market_context_high->metal_1h` score `-0.8243` n `133` status `ready` deltaP `1.7165` edge `0.0202` maxDD `-0.6936`
- `market_context_high->index_24h` score `-1.2629` n `132` status `ready` deltaP `-5.6614` edge `0.0861` maxDD `-2.1544`
- `market_context_high->metal_4h` score `-1.4127` n `133` status `ready` deltaP `1.5954` edge `0.0771` maxDD `-1.4368`
- `market_context_high->fx_4h` score `-1.4159` n `133` status `ready` deltaP `-2.9385` edge `0.0009` maxDD `-1.6936`
- `market_context_high->crypto_alt_24h` score `-2.072` n `133` status `ready` deltaP `14.7431` edge `0.1656` maxDD `-28.3623`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
