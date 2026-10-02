# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-02T10:22:28.101534+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `4842`

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

- `market_context_high->unknown_1h` score `340.9978` n `50` status `ready` deltaP `10.4251` edge `28.3519` maxDD `-0.0598`
- `market_context_high->unknown_4h` score `288.4843` n `50` status `ready` deltaP `9.9085` edge `23.9743` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `15.5334` n `73` status `ready` deltaP `39.795` edge `1.0501` maxDD `-1.0093`
- `market_context_high->crypto_major_24h` score `10.5043` n `50` status `ready` deltaP `35.4722` edge `0.7805` maxDD `-9.3299`
- `news_risk_high->equity_24h` score `10.4811` n `73` status `ready` deltaP `36.2252` edge `0.6804` maxDD `-2.8784`
- `market_context_high->crypto_alt_24h` score `9.0297` n `50` status `ready` deltaP `16.5347` edge `0.8132` maxDD `-11.6768`
- `market_context_high->crypto_major_4h` score `6.9635` n `50` status `ready` deltaP `17.3902` edge `0.5347` maxDD `-3.294`
- `market_context_high->crypto_alt_4h` score `4.9141` n `50` status `ready` deltaP `15.2744` edge `0.437` maxDD `-7.6792`
- `news_risk_high->crypto_alt_4h` score `4.4348` n `102` status `ready` deltaP `17.8234` edge `0.3851` maxDD `-6.4152`
- `market_context_high->crypto_alt_1h` score `2.9877` n `50` status `ready` deltaP `14.3533` edge `0.2196` maxDD `-3.6387`
- `market_context_high->crypto_major_1h` score `2.9448` n `50` status `ready` deltaP `14.2994` edge `0.1951` maxDD `-2.2692`
- `market_context_high->fx_4h` score `2.9407` n `50` status `ready` deltaP `32.8415` edge `0.0396` maxDD `-0.0791`
- `market_context_high->equity_24h` score `2.6393` n `50` status `ready` deltaP `12.4444` edge `0.4416` maxDD `-11.8957`
- `news_risk_high->equity_4h` score `2.5648` n `102` status `ready` deltaP `23.9449` edge `0.1237` maxDD `-2.9013`
- `news_risk_high->crypto_major_24h` score `2.4926` n `73` status `ready` deltaP `9.6366` edge `0.5707` maxDD `-15.8971`
- `market_context_high->fx_1h` score `1.452` n `50` status `ready` deltaP `20.3413` edge `0.0118` maxDD `-0.113`
- `news_risk_high->metal_24h` score `1.309` n `73` status `ready` deltaP `13.009` edge `0.2085` maxDD `-2.192`
- `market_context_high->index_24h` score `0.936` n `50` status `ready` deltaP `15.3125` edge `0.075` maxDD `-1.2338`
- `news_risk_high->crypto_alt_1h` score `0.9243` n `113` status `ready` deltaP `5.8754` edge `0.0941` maxDD `-2.4998`
- `news_risk_high->index_24h` score `0.8366` n `73` status `ready` deltaP `15.1755` edge `0.0539` maxDD `-0.4916`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
