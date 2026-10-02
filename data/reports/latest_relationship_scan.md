# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-02T21:22:25.609277+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `4884`

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

- `market_context_high->unknown_1h` score `364.0115` n `50` status `ready` deltaP `10.4251` edge `30.2697` maxDD `-0.0597`
- `market_context_high->unknown_4h` score `291.6383` n `50` status `ready` deltaP `10.2134` edge `24.2351` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `16.5503` n `73` status `ready` deltaP `41.8784` edge `1.1209` maxDD `-1.005`
- `market_context_high->crypto_alt_24h` score `10.225` n `50` status `ready` deltaP `18.6181` edge `0.8983` maxDD `-11.6271`
- `market_context_high->crypto_major_24h` score `9.0594` n `50` status `ready` deltaP `31.8264` edge `0.6844` maxDD `-9.3299`
- `news_risk_high->equity_24h` score `8.6652` n `73` status `ready` deltaP `31.0169` edge `0.5638` maxDD `-2.8784`
- `market_context_high->crypto_major_4h` score `7.7771` n `50` status `ready` deltaP `19.2195` edge `0.5903` maxDD `-3.294`
- `market_context_high->crypto_alt_4h` score `6.1985` n `50` status `ready` deltaP `17.4085` edge `0.5294` maxDD `-7.6465`
- `news_risk_high->crypto_alt_4h` score `6.0195` n `116` status `ready` deltaP `23.2706` edge `0.4809` maxDD `-6.4195`
- `market_context_high->crypto_alt_1h` score `3.3249` n `50` status `ready` deltaP `15.2515` edge `0.2417` maxDD `-3.6376`
- `market_context_high->crypto_major_1h` score `3.1295` n `50` status `ready` deltaP `14.4491` edge `0.2095` maxDD `-2.2692`
- `market_context_high->fx_4h` score `2.7141` n `50` status `ready` deltaP `30.25` edge `0.038` maxDD `-0.0791`
- `news_risk_high->equity_4h` score `2.4901` n `116` status `ready` deltaP `21.946` edge `0.1308` maxDD `-2.9013`
- `news_risk_high->crypto_major_4h` score `1.6245` n `116` status `ready` deltaP `15.8747` edge `0.3334` maxDD `-10.477`
- `news_risk_high->crypto_major_24h` score `1.5534` n `73` status `ready` deltaP `5.9908` edge `0.4746` maxDD `-15.8971`
- `market_context_high->equity_24h` score `1.4589` n `50` status `ready` deltaP `7.2361` edge `0.325` maxDD `-11.8957`
- `market_context_high->fx_1h` score `1.434` n `50` status `ready` deltaP `20.1916` edge `0.0113` maxDD `-0.113`
- `news_risk_high->metal_24h` score `1.373` n `73` status `ready` deltaP `13.009` edge `0.2167` maxDD `-2.192`
- `news_risk_high->crypto_alt_1h` score `1.1774` n `116` status `ready` deltaP `6.1481` edge `0.1132` maxDD `-2.4854`
- `market_context_high->fx_24h` score `0.9131` n `50` status `ready` deltaP `19.1181` edge `0.0914` maxDD `-1.8102`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
