# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-02T03:37:33.999046+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `72`

- Symbol pattern count: `6630`

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

- `market_context_high->unknown_1h` score `338.8152` n `50` status `ready` deltaP `9.5269` edge `28.176` maxDD `-0.0598`
- `market_context_high->unknown_4h` score `288.0163` n `50` status `ready` deltaP `8.9939` edge `23.9414` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `17.2981` n `72` status `ready` deltaP `38.8889` edge `1.2032` maxDD `-1.0093`
- `market_context_high->crypto_major_24h` score `11.0783` n `50` status `ready` deltaP `36.1667` edge `0.8237` maxDD `-9.3299`
- `market_context_high->crypto_alt_24h` score `7.7374` n `50` status `ready` deltaP `15.6667` edge `0.7113` maxDD `-11.6768`
- `market_context_high->crypto_major_4h` score `6.9625` n `50` status `ready` deltaP `17.5427` edge `0.5336` maxDD `-3.294`
- `market_context_high->crypto_alt_4h` score `4.7657` n `50` status `ready` deltaP `15.5793` edge `0.4226` maxDD `-7.6792`
- `news_risk_high->equity_24h` score `3.8121` n `72` status `ready` deltaP `23.7847` edge `0.4622` maxDD `-5.5622`
- `news_risk_high->crypto_alt_4h` score `3.5634` n `87` status `ready` deltaP `13.3954` edge `0.342` maxDD `-6.4152`
- `market_context_high->equity_24h` score `3.3447` n `50` status `ready` deltaP `16.7847` edge `0.5031` maxDD `-11.8957`
- `market_context_high->crypto_major_1h` score `2.9136` n `50` status `ready` deltaP `14.1497` edge `0.1935` maxDD `-2.2692`
- `market_context_high->fx_4h` score `2.8985` n `50` status `ready` deltaP `32.689` edge `0.0371` maxDD `-0.0791`
- `market_context_high->crypto_alt_1h` score `2.8283` n `50` status `ready` deltaP `13.1557` edge `0.2143` maxDD `-3.6387`
- `news_risk_high->equity_4h` score `2.3303` n `87` status `ready` deltaP `22.2736` edge `0.1153` maxDD `-2.9013`
- `market_context_high->fx_1h` score `1.434` n `50` status `ready` deltaP `20.1916` edge `0.0113` maxDD `-0.113`
- `news_risk_high->commodity_24h` score `1.4223` n `72` status `ready` deltaP `23.4375` edge `0.1385` maxDD `-3.9922`
- `news_risk_high->metal_24h` score `1.1336` n `72` status `ready` deltaP `10.0694` edge `0.2056` maxDD `-2.192`
- `news_risk_high->crypto_major_24h` score `1.0681` n `72` status `ready` deltaP `9.7223` edge `0.3875` maxDD `-15.8971`
- `news_risk_high->index_24h` score `0.9515` n `72` status `ready` deltaP `14.2361` edge `0.0322` maxDD `-0.4916`
- `market_context_high->index_24h` score `0.9253` n `50` status `ready` deltaP `14.7917` edge `0.0771` maxDD `-1.2338`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
