# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-25T04:22:28.722816+00:00`
- Price records: `672`
- Market context records: `7843`
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

- `market_context_high->equity_24h` score `10.197` n `132` status `ready` deltaP `28.5507` edge `0.7936` maxDD `-6.0681`
- `market_context_high->equity_4h` score `1.3031` n `133` status `ready` deltaP `5.3333` edge `0.3228` maxDD `-6.9701`
- `market_context_high->metal_24h` score `1.0988` n `133` status `ready` deltaP `10.0715` edge `0.2335` maxDD `-2.3927`
- `market_context_high->crypto_major_1h` score `1.0622` n `133` status `ready` deltaP `13.0082` edge `0.0459` maxDD `-1.5286`
- `market_context_high->crypto_major_4h` score `1.0385` n `133` status `ready` deltaP `13.4318` edge `0.1688` maxDD `-6.7444`
- `market_context_high->commodity_24h` score `1.0134` n `132` status `ready` deltaP `19.9052` edge `0.1101` maxDD `-7.0012`
- `market_context_high->fx_24h` score `0.832` n `132` status `ready` deltaP `25.2187` edge `0.0473` maxDD `-3.0343`
- `market_context_high->equity_1h` score `0.7286` n `133` status `ready` deltaP `7.8958` edge `0.094` maxDD `-4.2072`
- `market_context_high->crypto_alt_4h` score `0.6608` n `133` status `ready` deltaP `7.4374` edge `0.1172` maxDD `-3.9374`
- `market_context_high->commodity_4h` score `0.4832` n `133` status `ready` deltaP `8.7627` edge `0.0412` maxDD `-1.0817`
- `market_context_high->index_1h` score `0.3758` n `133` status `ready` deltaP `8.6444` edge `0.0167` maxDD `-0.7743`
- `market_context_high->crypto_alt_1h` score `0.2216` n `133` status `ready` deltaP `4.5777` edge `0.0312` maxDD `-1.4603`
- `market_context_high->commodity_1h` score `0.111` n `133` status `ready` deltaP `6.2476` edge `0.0135` maxDD `-0.6722`
- `market_context_high->index_4h` score `-0.0754` n `133` status `ready` deltaP `12.6992` edge `0.0515` maxDD `-1.3325`
- `market_context_high->fx_1h` score `-0.3726` n `133` status `ready` deltaP `1.1245` edge `0.0002` maxDD `-0.4331`
- `market_context_high->metal_1h` score `-0.7884` n `133` status `ready` deltaP `2.1656` edge `0.0202` maxDD `-0.6936`
- `market_context_high->index_24h` score `-1.2209` n `132` status `ready` deltaP `-5.1397` edge `0.088` maxDD `-2.1544`
- `market_context_high->metal_4h` score `-1.3481` n `133` status `ready` deltaP `2.3576` edge `0.0774` maxDD `-1.4368`
- `market_context_high->fx_4h` score `-1.4223` n `133` status `ready` deltaP `-3.0914` edge `0.0011` maxDD `-1.6936`
- `market_context_high->crypto_alt_24h` score `-1.9561` n `133` status `ready` deltaP `14.9164` edge `0.1793` maxDD `-28.3623`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
