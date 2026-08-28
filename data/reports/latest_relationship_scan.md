# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-28T09:07:25.694098+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11608`

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

- `news_risk_high->unknown_24h` score `53.2141` n `50` status `ready` deltaP `11.6118` edge `4.3571` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `29.9153` n `50` status `ready` deltaP `38.6343` edge `2.2795` maxDD `-2.8629`
- `news_risk_high->unknown_4h` score `12.7936` n `50` status `ready` deltaP `25.5549` edge `0.9057` maxDD `-0.1279`
- `news_risk_high->equity_24h` score `5.4103` n `50` status `ready` deltaP `30.1005` edge `0.343` maxDD `-4.7584`
- `news_risk_high->metal_24h` score `5.1912` n `50` status `ready` deltaP `48.26` edge `0.1151` maxDD `-0.0053`
- `news_risk_high->fx_4h` score `3.9321` n `50` status `ready` deltaP `45.811` edge `0.0313` maxDD `-0.0559`
- `market_context_high->unknown_24h` score `2.8078` n `134` status `ready` deltaP `5.6417` edge `0.2696` maxDD `-3.1917`
- `news_risk_high->unknown_1h` score `2.6984` n `52` status `ready` deltaP `15.3731` edge `0.158` maxDD `-0.8495`
- `news_risk_high->index_24h` score `2.5715` n `50` status `ready` deltaP `28.9012` edge `0.0367` maxDD `-0.2064`
- `market_context_high->unknown_4h` score `2.3506` n `148` status `ready` deltaP `18.7171` edge `0.1118` maxDD `-0.5894`
- `news_risk_high->crypto_major_24h` score `2.0289` n `50` status `ready` deltaP `18.3154` edge `0.0963` maxDD `-2.6128`
- `news_risk_high->equity_4h` score `1.7781` n `50` status `ready` deltaP `23.7134` edge `0.0664` maxDD `-2.105`
- `news_risk_high->fx_1h` score `1.5569` n `52` status `ready` deltaP `20.8544` edge `0.0077` maxDD `-0.0257`
- `news_risk_high->equity_1h` score `1.256` n `52` status `ready` deltaP `16.6628` edge `0.0218` maxDD `-0.2574`
- `market_context_high->unknown_1h` score `0.8593` n `148` status `ready` deltaP `8.8242` edge `0.0578` maxDD `-1.6015`
- `news_risk_high->commodity_1h` score `0.5264` n `52` status `ready` deltaP `14.5094` edge `0.0025` maxDD `-0.5397`
- `news_risk_high->metal_4h` score `0.3126` n `50` status `ready` deltaP `11.2744` edge `0.004` maxDD `-0.249`
- `market_context_high->metal_24h` score `0.218` n `134` status `ready` deltaP `14.4391` edge `0.0862` maxDD `-3.8102`
- `news_risk_high->index_4h` score `0.12` n `50` status `ready` deltaP `7.2378` edge `0.0014` maxDD `-0.1719`
- `news_risk_high->metal_1h` score `0.072` n `52` status `ready` deltaP `4.7444` edge `0.0002` maxDD `-0.1413`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
