# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-24T23:22:28.941487+00:00`
- Price records: `672`
- Market context records: `7822`
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

- `market_context_high->equity_24h` score `9.1494` n `132` status `ready` deltaP `28.5507` edge `0.7063` maxDD `-6.0681`
- `market_context_high->metal_24h` score `1.4361` n `133` status `ready` deltaP `13.5378` edge `0.2385` maxDD `-2.3927`
- `market_context_high->equity_4h` score `1.2975` n `133` status `ready` deltaP `5.1804` edge `0.3231` maxDD `-6.9701`
- `market_context_high->crypto_major_4h` score `1.1852` n `133` status `ready` deltaP `14.6513` edge `0.1729` maxDD `-6.7444`
- `market_context_high->crypto_major_1h` score `1.0861` n `133` status `ready` deltaP `13.3076` edge `0.0459` maxDD `-1.5286`
- `market_context_high->crypto_alt_4h` score `0.8507` n `133` status `ready` deltaP `8.6569` edge `0.1249` maxDD `-3.9374`
- `market_context_high->fx_24h` score `0.8281` n `132` status `ready` deltaP `25.2187` edge `0.0468` maxDD `-3.0343`
- `market_context_high->equity_1h` score `0.743` n `133` status `ready` deltaP `8.046` edge `0.0942` maxDD `-4.2072`
- `market_context_high->commodity_4h` score `0.47` n `133` status `ready` deltaP `8.7627` edge `0.0401` maxDD `-1.0817`
- `market_context_high->commodity_24h` score `0.446` n `132` status `ready` deltaP `16.4269` edge `0.086` maxDD `-7.0012`
- `market_context_high->index_1h` score `0.3386` n `133` status `ready` deltaP `8.194` edge `0.0166` maxDD `-0.7743`
- `market_context_high->crypto_alt_1h` score `0.2575` n `133` status `ready` deltaP `5.0268` edge `0.0312` maxDD `-1.4603`
- `market_context_high->commodity_1h` score `0.0521` n `133` status `ready` deltaP `5.647` edge `0.0126` maxDD `-0.6722`
- `market_context_high->index_4h` score `-0.0816` n `133` status `ready` deltaP `12.6992` edge `0.0507` maxDD `-1.3325`
- `market_context_high->fx_1h` score `-0.3978` n `133` status `ready` deltaP `0.8242` edge `0.0001` maxDD `-0.4331`
- `market_context_high->metal_1h` score `-0.889` n `133` status `ready` deltaP `0.968` edge `0.0198` maxDD `-0.6936`
- `market_context_high->fx_4h` score `-1.3309` n `133` status `ready` deltaP `-1.4095` edge `0.0016` maxDD `-1.6936`
- `market_context_high->metal_4h` score `-1.4273` n `133` status `ready` deltaP `1.443` edge `0.0769` maxDD `-1.4368`
- `market_context_high->index_24h` score `-1.4361` n `132` status `ready` deltaP `-7.7484` edge `0.0778` maxDD `-2.1544`
- `market_context_high->crypto_alt_24h` score `-2.1679` n `133` status `ready` deltaP `14.7431` edge `0.1533` maxDD `-28.3623`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
