# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-02T09:37:32.784964+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `4854`

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

- `market_context_high->unknown_1h` score `340.9102` n `50` status `ready` deltaP `10.4251` edge `28.3446` maxDD `-0.0598`
- `market_context_high->unknown_4h` score `287.8369` n `50` status `ready` deltaP `9.4512` edge `23.9234` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `14.9348` n `70` status `ready` deltaP `39.6776` edge `1.001` maxDD `-1.0093`
- `market_context_high->crypto_major_24h` score `10.6682` n `50` status `ready` deltaP `35.6458` edge `0.793` maxDD `-9.3299`
- `news_risk_high->equity_24h` score `10.2102` n `70` status `ready` deltaP `36.3939` edge `0.6567` maxDD `-2.8784`
- `market_context_high->crypto_alt_24h` score `9.0141` n `50` status `ready` deltaP `16.5347` edge `0.8119` maxDD `-11.6768`
- `market_context_high->crypto_major_4h` score `6.9949` n `50` status `ready` deltaP `17.5427` edge `0.5363` maxDD `-3.294`
- `market_context_high->crypto_alt_4h` score `4.9685` n `50` status `ready` deltaP `15.5793` edge `0.4395` maxDD `-7.6792`
- `news_risk_high->crypto_alt_4h` score `4.4046` n `99` status `ready` deltaP `17.2965` edge `0.3861` maxDD `-6.4152`
- `market_context_high->fx_4h` score `2.9383` n `50` status `ready` deltaP `32.8415` edge `0.0394` maxDD `-0.0791`
- `market_context_high->crypto_alt_1h` score `2.9181` n `50` status `ready` deltaP `14.0539` edge `0.2158` maxDD `-3.6387`
- `market_context_high->crypto_major_1h` score `2.8692` n `50` status `ready` deltaP `14.0` edge `0.1908` maxDD `-2.2692`
- `market_context_high->equity_24h` score `2.7514` n `50` status `ready` deltaP `12.9653` edge `0.4525` maxDD `-11.8957`
- `news_risk_high->equity_4h` score `2.4927` n `99` status `ready` deltaP `23.7189` edge `0.1192` maxDD `-2.9013`
- `news_risk_high->crypto_major_24h` score `1.8431` n `70` status `ready` deltaP `7.9315` edge `0.4988` maxDD `-15.8971`
- `market_context_high->fx_1h` score `1.4783` n `50` status `ready` deltaP `20.6407` edge `0.012` maxDD `-0.113`
- `news_risk_high->metal_24h` score `1.1523` n `70` status `ready` deltaP `10.7143` edge `0.2037` maxDD `-2.192`
- `market_context_high->index_24h` score `0.9536` n `50` status `ready` deltaP `15.4861` edge `0.0761` maxDD `-1.2338`
- `news_risk_high->crypto_alt_1h` score `0.8992` n `111` status `ready` deltaP `5.7116` edge `0.0931` maxDD `-2.4998`
- `news_risk_high->crypto_major_4h` score `0.7511` n `99` status `ready` deltaP `10.1488` edge `0.2596` maxDD `-10.477`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
