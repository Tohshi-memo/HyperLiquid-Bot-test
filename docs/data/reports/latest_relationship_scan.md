# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-01T04:22:29.511498+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `6373`

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

- `market_context_high->unknown_24h` score `5629.2155` n `65` status `ready` deltaP `-1.9631` edge `469.1393` maxDD `-0.9938`
- `market_context_high->unknown_4h` score `271.2506` n `65` status `ready` deltaP `2.8541` edge `22.5954` maxDD `-0.15`
- `news_risk_high->unknown_1h` score `81.6136` n `108` status `ready` deltaP `-5.0454` edge `6.8634` maxDD `-0.9571`
- `market_context_high->equity_24h` score `17.0986` n `65` status `ready` deltaP `33.2505` edge `1.302` maxDD `-4.5698`
- `news_risk_high->crypto_alt_24h` score `13.6963` n `96` status `ready` deltaP `32.2917` edge `1.0617` maxDD `-6.8493`
- `market_context_high->unknown_1h` score `7.5464` n `65` status `ready` deltaP `2.7039` edge `0.6219` maxDD `-0.2178`
- `market_context_high->index_24h` score `6.418` n `65` status `ready` deltaP `55.454` edge `0.1788` maxDD `-0.0926`
- `news_risk_high->crypto_alt_4h` score `5.3209` n `108` status `ready` deltaP `20.122` edge `0.4479` maxDD `-7.4246`
- `market_context_high->commodity_4h` score `2.8281` n `65` status `ready` deltaP `27.6712` edge `0.0846` maxDD `-0.3387`
- `market_context_high->commodity_24h` score `2.2179` n `65` status `ready` deltaP `33.9636` edge `0.1734` maxDD `-5.9052`
- `market_context_high->equity_4h` score `1.1471` n `65` status `ready` deltaP `-1.2265` edge `0.2343` maxDD `-2.9909`
- `market_context_high->metal_4h` score `1.1156` n `65` status `ready` deltaP `13.6585` edge `0.0444` maxDD `-0.7323`
- `news_risk_high->crypto_alt_1h` score `0.8433` n `108` status `ready` deltaP `8.8767` edge `0.1065` maxDD `-3.9659`
- `market_context_high->crypto_alt_24h` score `0.806` n `65` status `ready` deltaP `-10.0481` edge `0.3171` maxDD `-11.3026`
- `market_context_high->crypto_major_24h` score `0.806` n `65` status `ready` deltaP `4.0198` edge `0.1879` maxDD `-8.4691`
- `market_context_high->crypto_major_4h` score `0.6778` n `65` status `ready` deltaP `18.6351` edge `0.1215` maxDD `-9.0399`
- `market_context_high->fx_1h` score `0.6091` n `65` status `ready` deltaP `14.5071` edge `-0.0002` maxDD `-0.1407`
- `market_context_high->metal_1h` score `0.5274` n `65` status `ready` deltaP `7.7798` edge `0.0211` maxDD `-0.3209`
- `market_context_high->crypto_alt_4h` score `0.3507` n `65` status `ready` deltaP `12.8143` edge `0.1529` maxDD `-11.8023`
- `market_context_high->fx_4h` score `0.1426` n `65` status `ready` deltaP `7.4085` edge `0.0016` maxDD `-0.1285`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
