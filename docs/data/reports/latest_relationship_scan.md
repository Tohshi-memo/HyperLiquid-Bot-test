# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-01T19:01:15.576387+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `72`

- Symbol pattern count: `6812`

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

- `market_context_high->unknown_1h` score `340.2469` n `50` status `ready` deltaP `8.479` edge `28.3023` maxDD `-0.0598`
- `market_context_high->unknown_4h` score `285.526` n `50` status `ready` deltaP `6.8598` edge `23.7481` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `20.3085` n `106` status `ready` deltaP `35.6132` edge `1.4759` maxDD `-1.0093`
- `market_context_high->crypto_major_24h` score `10.1892` n `50` status `ready` deltaP `32.8681` edge `0.7716` maxDD `-9.3299`
- `market_context_high->crypto_major_4h` score `7.3707` n `50` status `ready` deltaP `19.5244` edge `0.5544` maxDD `-3.294`
- `market_context_high->crypto_alt_24h` score `5.3749` n `50` status `ready` deltaP `11.5` edge `0.5422` maxDD `-11.6768`
- `market_context_high->crypto_alt_4h` score `5.138` n `50` status `ready` deltaP `16.7988` edge `0.4455` maxDD `-7.6792`
- `news_risk_high->crypto_major_24h` score `4.9078` n `106` status `ready` deltaP `20.6794` edge `0.5865` maxDD `-15.8971`
- `market_context_high->equity_24h` score `3.916` n `50` status `ready` deltaP `19.0417` edge `0.5613` maxDD `-11.8957`
- `news_risk_high->equity_4h` score `3.3324` n `119` status `ready` deltaP `27.2404` edge `0.1657` maxDD `-2.9013`
- `market_context_high->fx_4h` score `3.1684` n `50` status `ready` deltaP `35.4329` edge `0.0413` maxDD `-0.0791`
- `market_context_high->crypto_major_1h` score `3.0335` n `50` status `ready` deltaP `14.5988` edge `0.2005` maxDD `-2.2692`
- `news_risk_high->equity_24h` score `2.9517` n `106` status `ready` deltaP `21.7964` edge `0.468` maxDD `-9.4579`
- `market_context_high->crypto_alt_1h` score `2.9458` n `50` status `ready` deltaP `13.6048` edge `0.2211` maxDD `-3.6387`
- `news_risk_high->index_24h` score `2.4112` n `106` status `ready` deltaP `24.037` edge `0.0885` maxDD `-0.4916`
- `news_risk_high->metal_24h` score `2.2191` n `106` status `ready` deltaP `25.95` edge `0.2389` maxDD `-2.192`
- `market_context_high->fx_1h` score `1.5765` n `50` status `ready` deltaP `21.8383` edge `0.0122` maxDD `-0.113`
- `market_context_high->index_24h` score `0.9026` n `50` status `ready` deltaP `14.7917` edge `0.0742` maxDD `-1.2338`
- `market_context_high->fx_24h` score `0.5063` n `50` status `ready` deltaP `14.4306` edge `0.0705` maxDD `-1.8102`
- `news_risk_high->equity_1h` score `0.4346` n `119` status `ready` deltaP `6.9114` edge `0.0438` maxDD `-0.9592`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
