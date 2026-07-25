# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-25T00:07:31.183803+00:00`
- Price records: `672`
- Market context records: `7825`
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

- `market_context_high->equity_24h` score `9.3354` n `132` status `ready` deltaP `28.5507` edge `0.7218` maxDD `-6.0681`
- `market_context_high->metal_24h` score `1.3909` n `133` status `ready` deltaP `13.0178` edge `0.2382` maxDD `-2.3927`
- `market_context_high->equity_4h` score `1.314` n `133` status `ready` deltaP `5.3333` edge `0.3242` maxDD `-6.9701`
- `market_context_high->crypto_major_4h` score `1.2374` n `133` status `ready` deltaP `15.1086` edge `0.1742` maxDD `-6.7444`
- `market_context_high->crypto_major_1h` score `1.0873` n `133` status `ready` deltaP `13.3076` edge `0.046` maxDD `-1.5286`
- `market_context_high->crypto_alt_4h` score `0.8895` n `133` status `ready` deltaP `8.9618` edge `0.1261` maxDD `-3.9374`
- `market_context_high->fx_24h` score `0.8296` n `132` status `ready` deltaP `25.2187` edge `0.047` maxDD `-3.0343`
- `market_context_high->equity_1h` score `0.7478` n `133` status `ready` deltaP `8.046` edge `0.0946` maxDD `-4.2072`
- `market_context_high->commodity_24h` score `0.5297` n `132` status `ready` deltaP `16.9486` edge `0.0895` maxDD `-7.0012`
- `market_context_high->commodity_4h` score `0.4359` n `133` status `ready` deltaP `8.4569` edge `0.0393` maxDD `-1.0817`
- `market_context_high->index_1h` score `0.3266` n `133` status `ready` deltaP `8.0438` edge `0.0166` maxDD `-0.7743`
- `market_context_high->crypto_alt_1h` score `0.2923` n `133` status `ready` deltaP `5.3262` edge `0.0321` maxDD `-1.4603`
- `market_context_high->commodity_1h` score `0.0665` n `133` status `ready` deltaP `5.7972` edge `0.0128` maxDD `-0.6722`
- `market_context_high->index_4h` score `-0.0721` n `133` status `ready` deltaP `12.8521` edge `0.0509` maxDD `-1.3325`
- `market_context_high->fx_1h` score `-0.399` n `133` status `ready` deltaP `0.8242` edge `0.0` maxDD `-0.4331`
- `market_context_high->metal_1h` score `-0.877` n `133` status `ready` deltaP `1.1177` edge `0.0198` maxDD `-0.6936`
- `market_context_high->fx_4h` score `-1.3484` n `133` status `ready` deltaP `-1.7153` edge `0.0014` maxDD `-1.6936`
- `market_context_high->index_24h` score `-1.3887` n `132` status `ready` deltaP `-7.2266` edge `0.0804` maxDD `-2.1544`
- `market_context_high->metal_4h` score `-1.4261` n `133` status `ready` deltaP `1.443` edge `0.077` maxDD `-1.4368`
- `market_context_high->crypto_alt_24h` score `-2.1399` n `133` status `ready` deltaP `14.7431` edge `0.1569` maxDD `-28.3623`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
