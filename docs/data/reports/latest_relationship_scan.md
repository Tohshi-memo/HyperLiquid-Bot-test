# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-02T08:23:03.831282+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `4814`

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

- `market_context_high->unknown_1h` score `340.7315` n `50` status `ready` deltaP `9.976` edge `28.3327` maxDD `-0.0598`
- `market_context_high->unknown_4h` score `287.2901` n `50` status `ready` deltaP `8.8415` edge `23.8819` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `14.1852` n `65` status `ready` deltaP `39.4578` edge `0.94` maxDD `-1.0093`
- `market_context_high->crypto_major_24h` score `10.9427` n `50` status `ready` deltaP `36.1667` edge `0.8124` maxDD `-9.3299`
- `news_risk_high->equity_24h` score `9.5944` n `65` status `ready` deltaP `36.6025` edge `0.604` maxDD `-2.8784`
- `market_context_high->crypto_alt_24h` score `8.9577` n `50` status `ready` deltaP `16.5347` edge `0.8072` maxDD `-11.6768`
- `market_context_high->crypto_major_4h` score `6.9313` n `50` status `ready` deltaP `17.5427` edge `0.531` maxDD `-3.294`
- `market_context_high->crypto_alt_4h` score `4.9229` n `50` status `ready` deltaP `15.5793` edge `0.4357` maxDD `-7.6792`
- `news_risk_high->crypto_alt_4h` score `4.2507` n `94` status `ready` deltaP `15.7921` edge `0.3833` maxDD `-6.4152`
- `market_context_high->equity_24h` score `2.9478` n `50` status `ready` deltaP `13.8333` edge `0.4719` maxDD `-11.8957`
- `market_context_high->fx_4h` score `2.9177` n `50` status `ready` deltaP `32.689` edge `0.0387` maxDD `-0.0791`
- `market_context_high->crypto_alt_1h` score `2.9145` n `50` status `ready` deltaP `13.9042` edge `0.2165` maxDD `-3.6387`
- `market_context_high->crypto_major_1h` score `2.8728` n `50` status `ready` deltaP `14.0` edge `0.1911` maxDD `-2.2692`
- `news_risk_high->equity_4h` score `2.2628` n `94` status `ready` deltaP `23.2453` edge `0.1032` maxDD `-2.9013`
- `market_context_high->fx_1h` score `1.4651` n `50` status `ready` deltaP `20.491` edge `0.0119` maxDD `-0.113`
- `news_risk_high->metal_24h` score `1.1743` n `65` status `ready` deltaP `5.7692` edge `0.1868` maxDD `-2.192`
- `market_context_high->index_24h` score `1.0076` n `50` status `ready` deltaP `16.1806` edge `0.0784` maxDD `-1.2338`
- `news_risk_high->crypto_alt_1h` score `0.8327` n `106` status `ready` deltaP `5.4514` edge `0.0893` maxDD `-2.4998`
- `news_risk_high->crypto_major_24h` score `0.6429` n `65` status `ready` deltaP `4.9359` edge `0.3649` maxDD `-15.8971`
- `news_risk_high->crypto_major_4h` score `0.5907` n `94` status `ready` deltaP `8.0533` edge `0.253` maxDD `-10.477`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
