# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-30T10:22:30.875902+00:00`
- Price records: `672`
- Market context records: `5239`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `5602`

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

- `market_context_high->unknown_24h` score `23.6351` n `129` status `ready` deltaP `31.795` edge `1.7766` maxDD `-0.8515`
- `market_context_high->crypto_major_24h` score `12.9825` n `129` status `ready` deltaP `33.1113` edge `1.2273` maxDD `-22.6266`
- `market_context_high->crypto_alt_24h` score `6.4841` n `129` status `ready` deltaP `21.4955` edge `0.7524` maxDD `-23.4292`
- `market_context_high->crypto_alt_4h` score `4.1919` n `155` status `ready` deltaP `14.1513` edge `0.4149` maxDD `-9.46`
- `market_context_high->crypto_major_4h` score `4.0446` n `155` status `ready` deltaP `14.9843` edge `0.4664` maxDD `-14.0065`
- `market_context_high->unknown_4h` score `2.2288` n `155` status `ready` deltaP `17.2875` edge `0.1727` maxDD `-5.5109`
- `market_context_high->unknown_1h` score `1.7866` n `155` status `ready` deltaP `7.9399` edge `0.1601` maxDD `-2.7986`
- `market_context_high->equity_24h` score `1.4237` n `129` status `ready` deltaP `17.8981` edge `0.5622` maxDD `-40.0306`
- `market_context_high->fx_24h` score `0.5947` n `129` status `ready` deltaP `13.5134` edge `0.049` maxDD `-0.8294`
- `market_context_high->crypto_alt_1h` score `0.4616` n `155` status `ready` deltaP `4.6533` edge `0.1036` maxDD `-5.0257`
- `market_context_high->crypto_major_1h` score `0.4133` n `155` status `ready` deltaP `6.553` edge `0.1153` maxDD `-6.9639`
- `market_context_high->equity_4h` score `0.2037` n `155` status `ready` deltaP `6.6355` edge `0.1366` maxDD `-7.4425`
- `market_context_high->index_24h` score `-0.1183` n `129` status `ready` deltaP `17.7648` edge `0.0299` maxDD `-7.413`
- `market_context_high->equity_1h` score `-0.1767` n `155` status `ready` deltaP `5.3699` edge `0.046` maxDD `-5.0555`
- `market_context_high->metal_1h` score `-0.1893` n `155` status `ready` deltaP `3.6623` edge `0.0105` maxDD `-2.0682`
- `market_context_high->index_1h` score `-0.2326` n `155` status `ready` deltaP `3.3881` edge `0.0084` maxDD `-1.0296`
- `market_context_high->fx_1h` score `-0.311` n `155` status `ready` deltaP `0.9108` edge `-0.0007` maxDD `-0.6194`
- `market_context_high->commodity_1h` score `-0.6748` n `155` status `ready` deltaP `-0.4723` edge `-0.0025` maxDD `-2.4692`
- `market_context_high->fx_4h` score `-0.7655` n `155` status `ready` deltaP `0.4425` edge `0.0023` maxDD `-1.6047`
- `market_context_high->index_4h` score `-0.8667` n `155` status `ready` deltaP `3.4667` edge `0.0164` maxDD `-2.9391`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
