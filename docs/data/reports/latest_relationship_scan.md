# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-30T13:37:36.388302+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `72`

- Symbol pattern count: `7492`

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

- `market_context_high->unknown_1h` score `311.0319` n `50` status `ready` deltaP `7.8802` edge `25.8717` maxDD `-0.0597`
- `market_context_high->unknown_4h` score `308.2977` n `47` status `ready` deltaP `8.2317` edge `25.6366` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `15.7783` n `135` status `ready` deltaP `26.2963` edge `1.1605` maxDD `-1.0093`
- `market_context_high->crypto_major_4h` score `7.0111` n `47` status `ready` deltaP `18.39` edge `0.532` maxDD `-3.294`
- `news_risk_high->equity_24h` score `6.6384` n `135` status `ready` deltaP `24.7338` edge `0.6232` maxDD `-9.4579`
- `news_risk_high->crypto_major_24h` score `6.096` n `135` status `ready` deltaP `23.4723` edge `0.6669` maxDD `-15.8971`
- `market_context_high->crypto_alt_4h` score `3.8049` n `47` status `ready` deltaP `14.1152` edge `0.3523` maxDD `-7.6792`
- `market_context_high->fx_4h` score `3.4512` n `47` status `ready` deltaP `38.7844` edge `0.0421` maxDD `-0.0449`
- `news_risk_high->index_24h` score `3.3031` n `135` status `ready` deltaP `30.9259` edge `0.1169` maxDD `-0.4916`
- `market_context_high->crypto_major_1h` score `3.0609` n `50` status `ready` deltaP `15.9461` edge `0.1938` maxDD `-2.2692`
- `news_risk_high->metal_24h` score `2.8457` n `135` status `ready` deltaP `22.581` edge `0.214` maxDD `-2.192`
- `market_context_high->crypto_alt_1h` score `2.7262` n `50` status `ready` deltaP `13.6048` edge `0.2028` maxDD `-3.6387`
- `news_risk_high->equity_4h` score `2.4219` n `135` status `ready` deltaP `27.037` edge `0.1817` maxDD `-9.143`
- `market_context_high->fx_1h` score `1.4627` n `50` status `ready` deltaP `20.491` edge `0.0117` maxDD `-0.113`
- `news_risk_high->equity_1h` score `0.7796` n `135` status `ready` deltaP `9.1018` edge `0.0666` maxDD `-1.6514`
- `news_risk_high->crypto_alt_1h` score `0.628` n `135` status `ready` deltaP `7.6048` edge `0.0927` maxDD `-4.2849`
- `news_risk_high->index_1h` score `0.4262` n `135` status `ready` deltaP `8.2191` edge `0.0095` maxDD `-0.302`
- `news_risk_high->crypto_alt_4h` score `0.1229` n `135` status `ready` deltaP `7.6061` edge `0.2255` maxDD `-15.9436`
- `market_context_high->equity_1h` score `-0.0079` n `50` status `ready` deltaP `1.1018` edge `0.0567` maxDD `-1.2043`
- `market_context_high->commodity_1h` score `-0.0633` n `50` status `ready` deltaP `8.2994` edge `-0.0088` maxDD `-2.3717`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
