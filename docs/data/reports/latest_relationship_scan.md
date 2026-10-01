# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-01T14:07:30.975907+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `72`

- Symbol pattern count: `7070`

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

- `market_context_high->unknown_1h` score `335.7063` n `50` status `ready` deltaP `7.7305` edge `27.9289` maxDD `-0.0598`
- `market_context_high->unknown_4h` score `282.6196` n `50` status `ready` deltaP `6.8598` edge `23.5059` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `19.1103` n `114` status `ready` deltaP `32.6206` edge `1.396` maxDD `-1.0093`
- `market_context_high->crypto_major_24h` score `9.6478` n `50` status `ready` deltaP `31.3056` edge `0.7369` maxDD `-9.3299`
- `market_context_high->crypto_major_4h` score `7.2265` n `50` status `ready` deltaP `19.372` edge `0.5434` maxDD `-3.294`
- `market_context_high->crypto_alt_4h` score `4.8874` n `50` status `ready` deltaP `16.0366` edge `0.4297` maxDD `-7.6792`
- `news_risk_high->crypto_major_24h` score `4.7819` n `114` status `ready` deltaP `21.2354` edge `0.5723` maxDD `-15.8971`
- `market_context_high->crypto_alt_24h` score `3.8817` n `50` status `ready` deltaP `8.375` edge `0.4386` maxDD `-11.6768`
- `market_context_high->equity_24h` score `3.8415` n `50` status `ready` deltaP `18.0` edge `0.5587` maxDD `-11.8957`
- `news_risk_high->equity_4h` score `3.6188` n `126` status `ready` deltaP `26.9575` edge `0.1797` maxDD `-1.9613`
- `news_risk_high->equity_24h` score `3.1271` n `114` status `ready` deltaP `21.9298` edge `0.4896` maxDD `-9.4579`
- `market_context_high->fx_4h` score `3.0654` n `50` status `ready` deltaP `34.6707` edge `0.0378` maxDD `-0.0791`
- `market_context_high->crypto_major_1h` score `2.9891` n `50` status `ready` deltaP `14.7485` edge `0.1958` maxDD `-2.2692`
- `market_context_high->crypto_alt_1h` score `2.8834` n `50` status `ready` deltaP `13.4551` edge `0.2169` maxDD `-3.6387`
- `news_risk_high->index_24h` score `2.3935` n `114` status `ready` deltaP `23.4101` edge `0.0912` maxDD `-0.4916`
- `news_risk_high->metal_24h` score `2.2511` n `114` status `ready` deltaP `26.3249` edge `0.2405` maxDD `-2.192`
- `market_context_high->fx_1h` score `1.4831` n `50` status `ready` deltaP `20.7904` edge `0.0114` maxDD `-0.113`
- `news_risk_high->equity_1h` score `0.8244` n `127` status `ready` deltaP `8.2736` edge `0.0672` maxDD `-0.9592`
- `market_context_high->index_24h` score `0.7335` n `50` status `ready` deltaP `12.7083` edge `0.0664` maxDD `-1.2338`
- `market_context_high->fx_24h` score `0.5574` n `50` status `ready` deltaP `14.6042` edge `0.0759` maxDD `-1.8102`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
