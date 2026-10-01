# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-01T10:37:34.882519+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `72`

- Symbol pattern count: `6886`

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

- `market_context_high->unknown_1h` score `324.298` n `50` status `ready` deltaP `7.1317` edge `26.9822` maxDD `-0.0598`
- `market_context_high->unknown_4h` score `281.1052` n `50` status `ready` deltaP `6.8598` edge `23.3797` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `20.6095` n `124` status `ready` deltaP `30.3315` edge `1.5362` maxDD `-1.0093`
- `market_context_high->crypto_major_24h` score `8.5221` n `50` status `ready` deltaP `30.0903` edge `0.6512` maxDD `-9.3299`
- `market_context_high->crypto_major_4h` score `6.8187` n `50` status `ready` deltaP `18.6098` edge `0.5145` maxDD `-3.294`
- `news_risk_high->equity_24h` score `6.1248` n `124` status `ready` deltaP `22.9782` edge `0.5921` maxDD `-9.4579`
- `news_risk_high->equity_4h` score `4.4805` n `124` status `ready` deltaP `29.6027` edge `0.2249` maxDD `-1.2436`
- `news_risk_high->crypto_major_24h` score `4.4092` n `124` status `ready` deltaP `22.2838` edge `0.7321` maxDD `-15.8971`
- `market_context_high->crypto_alt_4h` score `3.8815` n `50` status `ready` deltaP `13.9024` edge `0.3601` maxDD `-7.6792`
- `market_context_high->equity_24h` score `3.5085` n `50` status `ready` deltaP `16.7847` edge `0.5241` maxDD `-11.8957`
- `news_risk_high->crypto_alt_4h` score `3.4107` n `124` status `ready` deltaP `13.2572` edge `0.3965` maxDD `-10.7193`
- `market_context_high->fx_4h` score `2.9582` n `50` status `ready` deltaP `33.4512` edge `0.037` maxDD `-0.0791`
- `market_context_high->crypto_major_1h` score `2.9027` n `50` status `ready` deltaP `14.7485` edge `0.1886` maxDD `-2.2692`
- `news_risk_high->index_24h` score `2.6373` n `124` status `ready` deltaP `24.7928` edge `0.1023` maxDD `-0.4916`
- `market_context_high->crypto_alt_1h` score `2.6099` n `50` status `ready` deltaP `12.5569` edge `0.2001` maxDD `-3.6387`
- `news_risk_high->metal_24h` score `2.3449` n `124` status `ready` deltaP `27.425` edge `0.2452` maxDD `-2.192`
- `market_context_high->crypto_alt_24h` score `1.8728` n `50` status `ready` deltaP `5.9444` edge `0.2874` maxDD `-11.6768`
- `market_context_high->fx_1h` score `1.4699` n `50` status `ready` deltaP `20.6407` edge `0.0113` maxDD `-0.113`
- `market_context_high->fx_24h` score `0.7337` n `50` status `ready` deltaP `17.0347` edge `0.0823` maxDD `-1.8102`
- `market_context_high->index_24h` score `0.6963` n `50` status `ready` deltaP `12.5347` edge `0.0628` maxDD `-1.2338`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
