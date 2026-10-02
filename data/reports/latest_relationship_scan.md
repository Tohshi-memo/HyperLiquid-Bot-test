# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-02T09:07:36.366700+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `4838`

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

- `market_context_high->unknown_1h` score `340.8455` n `50` status `ready` deltaP `10.2754` edge `28.3402` maxDD `-0.0598`
- `market_context_high->unknown_4h` score `287.5821` n `50` status `ready` deltaP `9.1463` edge `23.9042` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `14.7121` n `68` status `ready` deltaP `39.5935` edge `0.983` maxDD `-1.0093`
- `market_context_high->crypto_major_24h` score `10.7968` n `50` status `ready` deltaP `35.9931` edge `0.8014` maxDD `-9.3299`
- `news_risk_high->equity_24h` score `10.021` n `68` status `ready` deltaP `36.489` edge `0.6403` maxDD `-2.8784`
- `market_context_high->crypto_alt_24h` score `8.9985` n `50` status `ready` deltaP `16.5347` edge `0.8106` maxDD `-11.6768`
- `market_context_high->crypto_major_4h` score `6.9901` n `50` status `ready` deltaP `17.5427` edge `0.5359` maxDD `-3.294`
- `market_context_high->crypto_alt_4h` score `4.9589` n `50` status `ready` deltaP `15.5793` edge `0.4387` maxDD `-7.6792`
- `news_risk_high->crypto_alt_4h` score `4.346` n `97` status `ready` deltaP `16.7133` edge `0.3851` maxDD `-6.4152`
- `market_context_high->fx_4h` score `2.9371` n `50` status `ready` deltaP `32.8415` edge `0.0393` maxDD `-0.0791`
- `market_context_high->crypto_alt_1h` score `2.8822` n `50` status `ready` deltaP `13.7545` edge `0.2148` maxDD `-3.6387`
- `market_context_high->crypto_major_1h` score `2.8464` n `50` status `ready` deltaP `13.8503` edge `0.1899` maxDD `-2.2692`
- `market_context_high->equity_24h` score `2.8287` n `50` status `ready` deltaP `13.3125` edge `0.4601` maxDD `-11.8957`
- `news_risk_high->equity_4h` score `2.4032` n `97` status `ready` deltaP `23.5448` edge `0.1129` maxDD `-2.9013`
- `market_context_high->fx_1h` score `1.4771` n `50` status `ready` deltaP `20.6407` edge `0.0119` maxDD `-0.113`
- `news_risk_high->crypto_major_24h` score `1.459` n `68` status `ready` deltaP `6.9343` edge `0.4562` maxDD `-15.8971`
- `news_risk_high->crypto_alt_1h` score `1.0234` n `109` status `ready` deltaP `6.4701` edge `0.0984` maxDD `-2.4998`
- `news_risk_high->metal_24h` score `1.0111` n `68` status `ready` deltaP `8.8235` edge `0.1982` maxDD `-2.192`
- `market_context_high->index_24h` score `0.9786` n `50` status `ready` deltaP `15.8333` edge `0.077` maxDD `-1.2338`
- `news_risk_high->crypto_major_4h` score `0.6839` n `97` status `ready` deltaP `9.3365` edge `0.2564` maxDD `-10.477`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
