# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-02T01:37:30.698668+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `72`

- Symbol pattern count: `6602`

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

- `market_context_high->unknown_1h` score `338.6904` n `50` status `ready` deltaP `9.5269` edge `28.1656` maxDD `-0.0598`
- `market_context_high->unknown_4h` score `287.7811` n `50` status `ready` deltaP `8.9939` edge `23.9218` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `19.0077` n `80` status `ready` deltaP `38.2986` edge `1.3496` maxDD `-1.0093`
- `market_context_high->crypto_major_24h` score `10.9727` n `50` status `ready` deltaP `36.1667` edge `0.8149` maxDD `-9.3299`
- `market_context_high->crypto_major_4h` score `7.1799` n `50` status `ready` deltaP `18.6098` edge `0.5446` maxDD `-3.294`
- `market_context_high->crypto_alt_24h` score `7.134` n `50` status `ready` deltaP `14.7986` edge `0.6668` maxDD `-11.6768`
- `market_context_high->crypto_alt_4h` score `4.9078` n `50` status `ready` deltaP `16.0366` edge `0.4314` maxDD `-7.6792`
- `market_context_high->equity_24h` score `3.5339` n `50` status `ready` deltaP `18.1736` edge `0.5181` maxDD `-11.8957`
- `news_risk_high->crypto_alt_4h` score `3.2056` n `93` status `ready` deltaP `12.7033` edge `0.3168` maxDD `-6.4152`
- `news_risk_high->crypto_major_24h` score `3.0872` n `80` status `ready` deltaP `14.1667` edge `0.4782` maxDD `-15.8971`
- `market_context_high->crypto_major_1h` score `3.0743` n `50` status `ready` deltaP `15.0479` edge `0.2009` maxDD `-2.2692`
- `market_context_high->crypto_alt_1h` score `2.9614` n `50` status `ready` deltaP `13.7545` edge `0.2214` maxDD `-3.6387`
- `market_context_high->fx_4h` score `2.9033` n `50` status `ready` deltaP `32.689` edge `0.0375` maxDD `-0.0791`
- `news_risk_high->equity_24h` score `2.7353` n `80` status `ready` deltaP `17.6736` edge `0.4315` maxDD `-8.2254`
- `news_risk_high->equity_4h` score `2.6816` n `93` status `ready` deltaP `23.9051` edge `0.1337` maxDD `-2.9013`
- `news_risk_high->commodity_24h` score `1.6765` n `80` status `ready` deltaP `26.7361` edge `0.1491` maxDD `-3.9922`
- `news_risk_high->metal_24h` score `1.4589` n `80` status `ready` deltaP `14.9306` edge `0.2149` maxDD `-2.192`
- `market_context_high->fx_1h` score `1.446` n `50` status `ready` deltaP `20.3413` edge `0.0113` maxDD `-0.113`
- `news_risk_high->index_24h` score `1.322` n `80` status `ready` deltaP `17.2917` edge `0.0427` maxDD `-0.4916`
- `market_context_high->index_24h` score `0.9214` n `50` status `ready` deltaP `14.7917` edge `0.0766` maxDD `-1.2338`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
