# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-01T18:07:35.201838+00:00`
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

- `market_context_high->unknown_1h` score `335.4926` n `50` status `ready` deltaP `8.0299` edge `27.9091` maxDD `-0.0598`
- `market_context_high->unknown_4h` score `285.0244` n `50` status `ready` deltaP `6.8598` edge `23.7063` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `20.3786` n `110` status `ready` deltaP `35.3346` edge `1.4836` maxDD `-1.0093`
- `market_context_high->crypto_major_24h` score `10.1532` n `50` status `ready` deltaP `32.8681` edge `0.7686` maxDD `-9.3299`
- `market_context_high->crypto_major_4h` score `7.4914` n `50` status `ready` deltaP `20.1341` edge `0.5604` maxDD `-3.294`
- `market_context_high->crypto_alt_4h` score `5.2198` n `50` status `ready` deltaP `16.9512` edge `0.4513` maxDD `-7.6792`
- `market_context_high->crypto_alt_24h` score `5.1587` n `50` status `ready` deltaP `11.1528` edge `0.5265` maxDD `-11.6768`
- `news_risk_high->crypto_major_24h` score `5.0748` n `110` status `ready` deltaP `21.7772` edge `0.5931` maxDD `-15.8971`
- `market_context_high->equity_24h` score `3.9679` n `50` status `ready` deltaP `19.2153` edge `0.5668` maxDD `-11.8957`
- `news_risk_high->equity_4h` score `3.3032` n `123` status `ready` deltaP `26.5752` edge `0.1677` maxDD `-2.9013`
- `market_context_high->fx_4h` score `3.1648` n `50` status `ready` deltaP `35.4329` edge `0.041` maxDD `-0.0791`
- `market_context_high->crypto_major_1h` score `3.0371` n `50` status `ready` deltaP `14.7485` edge `0.1998` maxDD `-2.2692`
- `news_risk_high->equity_24h` score `3.0342` n `110` status `ready` deltaP `22.1244` edge `0.4764` maxDD `-9.4579`
- `market_context_high->crypto_alt_1h` score `2.9062` n `50` status `ready` deltaP `13.4551` edge `0.2188` maxDD `-3.6387`
- `news_risk_high->index_24h` score `2.522` n `110` status `ready` deltaP `24.7917` edge `0.0927` maxDD `-0.4916`
- `news_risk_high->metal_24h` score `2.291` n `110` status `ready` deltaP `26.9728` edge `0.2413` maxDD `-2.192`
- `market_context_high->fx_1h` score `1.5909` n `50` status `ready` deltaP `21.988` edge `0.0124` maxDD `-0.113`
- `market_context_high->index_24h` score `0.8987` n `50` status `ready` deltaP `14.7917` edge `0.0737` maxDD `-1.2338`
- `market_context_high->fx_24h` score `0.5149` n `50` status `ready` deltaP `14.4306` edge `0.0716` maxDD `-1.8102`
- `news_risk_high->equity_1h` score `0.3905` n `123` status `ready` deltaP `6.5698` edge `0.0424` maxDD `-0.9592`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
