# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-02T02:52:34.635418+00:00`
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

- `market_context_high->unknown_1h` score `338.8344` n `50` status `ready` deltaP `9.5269` edge `28.1776` maxDD `-0.0598`
- `market_context_high->unknown_4h` score `288.0043` n `50` status `ready` deltaP `8.9939` edge `23.9404` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `18.0561` n `75` status `ready` deltaP `38.4791` edge `1.2691` maxDD `-1.0093`
- `market_context_high->crypto_major_24h` score `11.0411` n `50` status `ready` deltaP `36.1667` edge `0.8206` maxDD `-9.3299`
- `market_context_high->crypto_alt_24h` score `7.4641` n `50` status `ready` deltaP `15.1458` edge `0.692` maxDD `-11.6768`
- `market_context_high->crypto_major_4h` score `7.0289` n `50` status `ready` deltaP `17.8476` edge `0.5371` maxDD `-3.294`
- `market_context_high->crypto_alt_4h` score `4.7801` n `50` status `ready` deltaP `15.5793` edge `0.4238` maxDD `-7.6792`
- `news_risk_high->crypto_alt_4h` score `3.5842` n `88` status `ready` deltaP `13.7611` edge `0.3413` maxDD `-6.4152`
- `market_context_high->equity_24h` score `3.4139` n `50` status `ready` deltaP `17.3056` edge `0.5085` maxDD `-11.8957`
- `news_risk_high->equity_24h` score `3.3617` n `75` status `ready` deltaP `21.3056` edge `0.4476` maxDD `-6.6918`
- `market_context_high->crypto_major_1h` score `2.9519` n `50` status `ready` deltaP `14.4491` edge `0.1947` maxDD `-2.2692`
- `market_context_high->fx_4h` score `2.8997` n `50` status `ready` deltaP `32.689` edge `0.0372` maxDD `-0.0791`
- `market_context_high->crypto_alt_1h` score `2.8163` n `50` status `ready` deltaP `13.1557` edge `0.2133` maxDD `-3.6387`
- `news_risk_high->equity_4h` score `2.4241` n `88` status `ready` deltaP `22.561` edge `0.1212` maxDD `-2.9013`
- `news_risk_high->crypto_major_24h` score `2.275` n `75` status `ready` deltaP `11.5` edge `0.4283` maxDD `-15.8971`
- `news_risk_high->commodity_24h` score `1.532` n `75` status `ready` deltaP `24.8264` edge `0.1433` maxDD `-3.9922`
- `market_context_high->fx_1h` score `1.4472` n `50` status `ready` deltaP `20.3413` edge `0.0114` maxDD `-0.113`
- `news_risk_high->metal_24h` score `1.2731` n `75` status `ready` deltaP `12.0486` edge `0.2103` maxDD `-2.192`
- `news_risk_high->index_24h` score `1.0997` n `75` status `ready` deltaP `15.4584` edge `0.0364` maxDD `-0.4916`
- `market_context_high->index_24h` score `0.9229` n `50` status `ready` deltaP `14.7917` edge `0.0768` maxDD `-1.2338`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
