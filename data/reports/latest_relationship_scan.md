# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-23T19:22:25.783773+00:00`
- Price records: `672`
- Market context records: `7699`
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

- `market_context_high->equity_24h` score `3.6279` n `132` status `ready` deltaP `19.396` edge `0.3072` maxDD `-6.0681`
- `market_context_high->crypto_major_4h` score `1.3356` n `133` status `ready` deltaP `15.8708` edge `0.1773` maxDD `-6.7444`
- `market_context_high->crypto_major_1h` score `1.1113` n `133` status `ready` deltaP `13.3076` edge `0.048` maxDD `-1.5286`
- `market_context_high->equity_4h` score `0.8709` n `133` status `ready` deltaP `3.6513` edge `0.2786` maxDD `-6.9701`
- `market_context_high->crypto_alt_4h` score `0.8545` n `133` status `ready` deltaP `8.8093` edge `0.1242` maxDD `-3.9374`
- `market_context_high->equity_1h` score `0.6963` n `133` status `ready` deltaP `8.7968` edge `0.0853` maxDD `-4.2072`
- `market_context_high->index_1h` score `0.4046` n `133` status `ready` deltaP `9.0949` edge `0.0161` maxDD `-0.7743`
- `market_context_high->crypto_alt_1h` score `0.1629` n `133` status `ready` deltaP `3.6795` edge `0.0323` maxDD `-1.4603`
- `market_context_high->index_4h` score `-0.086` n `133` status `ready` deltaP `13.005` edge `0.0481` maxDD `-1.3325`
- `market_context_high->fx_24h` score `-0.1033` n `132` status `ready` deltaP `11.0733` edge `0.0217` maxDD `-3.0343`
- `market_context_high->commodity_1h` score `-0.2469` n `133` status `ready` deltaP `2.9443` edge `0.0057` maxDD `-0.6722`
- `market_context_high->commodity_4h` score `-0.3748` n `133` status `ready` deltaP `2.4936` edge `0.0115` maxDD `-1.0817`
- `market_context_high->fx_1h` score `-0.4939` n `133` status `ready` deltaP `-0.2269` edge `-0.0009` maxDD `-0.4331`
- `market_context_high->metal_24h` score `-0.6852` n `133` status `ready` deltaP `2.6812` edge `0.1341` maxDD `-2.3927`
- `market_context_high->metal_1h` score `-0.8004` n `133` status `ready` deltaP `2.0159` edge `0.0202` maxDD `-0.6936`
- `market_context_high->unknown_1h` score `-1.2398` n `133` status `ready` deltaP `-0.0765` edge `-0.0438` maxDD `-1.054`
- `market_context_high->metal_4h` score `-1.4223` n `133` status `ready` deltaP `1.5954` edge `0.0763` maxDD `-1.4368`
- `market_context_high->fx_4h` score `-1.5369` n `133` status `ready` deltaP `-4.6205` edge `-0.0034` maxDD `-1.6936`
- `market_context_high->commodity_24h` score `-1.7201` n `132` status `ready` deltaP `5.6858` edge `-0.0229` maxDD `-7.0012`
- `market_context_high->unknown_4h` score `-2.2519` n `133` status `ready` deltaP `15.3023` edge `-0.164` maxDD `-1.7206`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
