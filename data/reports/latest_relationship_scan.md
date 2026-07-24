# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-24T17:52:33.592229+00:00`
- Price records: `672`
- Market context records: `7797`
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

- `market_context_high->equity_24h` score `8.0094` n `132` status `ready` deltaP `28.5507` edge `0.6113` maxDD `-6.0681`
- `market_context_high->metal_24h` score `1.4584` n `133` status `ready` deltaP `13.7111` edge `0.2392` maxDD `-2.3927`
- `market_context_high->crypto_major_4h` score `1.2398` n `133` status `ready` deltaP `15.033` edge `0.1749` maxDD `-6.7444`
- `market_context_high->equity_4h` score `1.1802` n `133` status `ready` deltaP `4.036` edge `0.3157` maxDD `-6.9701`
- `market_context_high->crypto_major_1h` score `1.1053` n `133` status `ready` deltaP `13.4573` edge `0.0465` maxDD `-1.5286`
- `market_context_high->crypto_alt_4h` score `0.9167` n `133` status `ready` deltaP `8.7318` edge `0.1299` maxDD `-3.9374`
- `market_context_high->fx_24h` score `0.814` n `132` status `ready` deltaP `25.2187` edge `0.045` maxDD `-3.0343`
- `market_context_high->equity_1h` score `0.7814` n `133` status `ready` deltaP `8.1961` edge `0.0964` maxDD `-4.2072`
- `market_context_high->commodity_4h` score `0.4418` n `133` status `ready` deltaP `8.2454` edge `0.0412` maxDD `-1.0817`
- `market_context_high->index_1h` score `0.4034` n `133` status `ready` deltaP `8.9447` edge `0.017` maxDD `-0.7743`
- `market_context_high->crypto_alt_1h` score `0.2635` n `133` status `ready` deltaP `4.8771` edge `0.0327` maxDD `-1.4603`
- `market_context_high->commodity_1h` score `0.0617` n `133` status `ready` deltaP `5.647` edge `0.0134` maxDD `-0.6722`
- `market_context_high->index_4h` score `-0.1266` n `133` status `ready` deltaP `12.0129` edge `0.0495` maxDD `-1.3325`
- `market_context_high->commodity_24h` score `-0.2105` n `132` status `ready` deltaP `12.6008` edge `0.0568` maxDD `-7.0012`
- `market_context_high->fx_1h` score `-0.2957` n `133` status `ready` deltaP `2.0254` edge `0.0006` maxDD `-0.4331`
- `market_context_high->metal_1h` score `-0.871` n `133` status `ready` deltaP `1.2674` edge `0.0193` maxDD `-0.6936`
- `market_context_high->fx_4h` score `-1.3303` n `133` status `ready` deltaP `-1.5014` edge `0.0023` maxDD `-1.6936`
- `market_context_high->metal_4h` score `-1.5839` n `133` status `ready` deltaP `-0.0046` edge `0.0735` maxDD `-1.4368`
- `market_context_high->index_24h` score `-1.6451` n `132` status `ready` deltaP `-9.4875` edge `0.0626` maxDD `-2.1544`
- `market_context_high->crypto_alt_24h` score `-2.3091` n `133` status `ready` deltaP `14.7431` edge `0.1352` maxDD `-28.3623`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
