# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-01T13:33:58.081347+00:00`
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

- `market_context_high->unknown_1h` score `335.3427` n `50` status `ready` deltaP `7.7305` edge `27.8986` maxDD `-0.0598`
- `market_context_high->unknown_4h` score `281.3008` n `50` status `ready` deltaP `6.8598` edge `23.396` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `18.8941` n `114` status `ready` deltaP `32.2734` edge `1.3803` maxDD `-1.0093`
- `market_context_high->crypto_major_24h` score `9.542` n `50` status `ready` deltaP `30.9583` edge `0.7304` maxDD `-9.3299`
- `market_context_high->crypto_major_4h` score `7.2085` n `50` status `ready` deltaP `19.372` edge `0.5419` maxDD `-3.294`
- `market_context_high->crypto_alt_4h` score `4.7983` n `50` status `ready` deltaP `15.7317` edge `0.4243` maxDD `-7.6792`
- `news_risk_high->crypto_major_24h` score `4.6761` n `114` status `ready` deltaP `20.8881` edge `0.5658` maxDD `-15.8971`
- `news_risk_high->equity_4h` score `3.9183` n `124` status `ready` deltaP `27.9455` edge `0.1891` maxDD `-1.2436`
- `market_context_high->equity_24h` score `3.784` n `50` status `ready` deltaP `17.4792` edge `0.5548` maxDD `-11.8957`
- `market_context_high->crypto_alt_24h` score `3.6655` n `50` status `ready` deltaP `8.0278` edge `0.4229` maxDD `-11.6768`
- `news_risk_high->equity_24h` score `3.0696` n `114` status `ready` deltaP `21.409` edge `0.4857` maxDD `-9.4579`
- `market_context_high->fx_4h` score `3.0398` n `50` status `ready` deltaP `34.3659` edge `0.0377` maxDD `-0.0791`
- `market_context_high->crypto_major_1h` score `3.0275` n `50` status `ready` deltaP `15.0479` edge `0.197` maxDD `-2.2692`
- `market_context_high->crypto_alt_1h` score `2.8511` n `50` status `ready` deltaP `13.1557` edge `0.2162` maxDD `-3.6387`
- `news_risk_high->index_24h` score `2.3688` n `114` status `ready` deltaP `23.2365` edge `0.0903` maxDD `-0.4916`
- `news_risk_high->metal_24h` score `2.2366` n `114` status `ready` deltaP `26.1513` edge `0.2398` maxDD `-2.192`
- `market_context_high->fx_1h` score `1.4819` n `50` status `ready` deltaP `20.7904` edge `0.0113` maxDD `-0.113`
- `news_risk_high->equity_1h` score `0.81` n `127` status `ready` deltaP `8.2736` edge `0.066` maxDD `-0.9592`
- `market_context_high->index_24h` score `0.7174` n `50` status `ready` deltaP `12.5347` edge `0.0655` maxDD `-1.2338`
- `market_context_high->fx_24h` score `0.5833` n `50` status `ready` deltaP `14.9514` edge `0.0769` maxDD `-1.8102`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
