# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-01T21:37:32.543049+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `72`

- Symbol pattern count: `6814`

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

- `market_context_high->unknown_1h` score `337.8901` n `50` status `ready` deltaP `8.6287` edge `28.1049` maxDD `-0.0598`
- `market_context_high->unknown_4h` score `286.6576` n `50` status `ready` deltaP `6.8598` edge `23.8424` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `20.3387` n `96` status `ready` deltaP `36.1111` edge `1.4751` maxDD `-1.0093`
- `market_context_high->crypto_major_24h` score `10.3769` n `50` status `ready` deltaP `33.9097` edge `0.7803` maxDD `-9.3299`
- `market_context_high->crypto_major_4h` score `7.2329` n `50` status `ready` deltaP `18.7622` edge `0.548` maxDD `-3.294`
- `market_context_high->crypto_alt_24h` score `5.8444` n `50` status `ready` deltaP `12.1944` edge `0.5767` maxDD `-11.6768`
- `market_context_high->crypto_alt_4h` score `5.0246` n `50` status `ready` deltaP `16.3415` edge `0.4391` maxDD `-7.6792`
- `news_risk_high->crypto_major_24h` score `4.6471` n `96` status `ready` deltaP `18.5764` edge `0.5788` maxDD `-15.8971`
- `market_context_high->equity_24h` score `3.7927` n `50` status `ready` deltaP `19.0417` edge `0.5455` maxDD `-11.8957`
- `news_risk_high->equity_4h` score `3.2098` n `109` status `ready` deltaP `27.0726` edge `0.1566` maxDD `-2.9013`
- `market_context_high->fx_4h` score `3.088` n `50` status `ready` deltaP `34.5183` edge `0.0407` maxDD `-0.0791`
- `market_context_high->crypto_major_1h` score `3.0215` n `50` status `ready` deltaP `14.5988` edge `0.1995` maxDD `-2.2692`
- `market_context_high->crypto_alt_1h` score `2.9602` n `50` status `ready` deltaP `13.7545` edge `0.2213` maxDD `-3.6387`
- `news_risk_high->equity_24h` score `2.6334` n `96` status `ready` deltaP `18.75` edge `0.4475` maxDD `-9.4579`
- `news_risk_high->index_24h` score `2.0523` n `96` status `ready` deltaP `21.875` edge `0.073` maxDD `-0.4916`
- `news_risk_high->metal_24h` score `1.9997` n `96` status `ready` deltaP `22.9167` edge `0.231` maxDD `-2.192`
- `news_risk_high->commodity_24h` score `1.8294` n `96` status `ready` deltaP `22.0486` edge `0.1212` maxDD `-4.259`
- `market_context_high->fx_1h` score `1.4891` n `50` status `ready` deltaP `20.7904` edge `0.0119` maxDD `-0.113`
- `market_context_high->index_24h` score `0.9081` n `50` status `ready` deltaP `14.7917` edge `0.0749` maxDD `-1.2338`
- `news_risk_high->equity_1h` score `0.5549` n `109` status `ready` deltaP `7.8751` edge `0.0474` maxDD `-0.9592`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
