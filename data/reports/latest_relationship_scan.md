# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-02T19:22:32.972199+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `4930`

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

- `market_context_high->unknown_1h` score `366.2794` n `50` status `ready` deltaP `10.8743` edge `30.4557` maxDD `-0.0597`
- `market_context_high->unknown_4h` score `292.3009` n `50` status `ready` deltaP `10.3659` edge `24.2893` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `16.0211` n `73` status `ready` deltaP `40.6631` edge `1.0849` maxDD `-1.005`
- `market_context_high->crypto_alt_24h` score `9.6958` n `50` status `ready` deltaP `17.4028` edge `0.8623` maxDD `-11.6271`
- `market_context_high->crypto_major_24h` score `9.0054` n `50` status `ready` deltaP `31.8264` edge `0.6799` maxDD `-9.3299`
- `news_risk_high->equity_24h` score `8.8178` n `73` status `ready` deltaP `31.3641` edge `0.5742` maxDD `-2.8784`
- `market_context_high->crypto_major_4h` score `7.4085` n `50` status `ready` deltaP `18.1524` edge `0.5667` maxDD `-3.294`
- `market_context_high->crypto_alt_4h` score `5.5515` n `50` status `ready` deltaP `16.3415` edge `0.4826` maxDD `-7.6465`
- `news_risk_high->crypto_alt_4h` score `5.3726` n `116` status `ready` deltaP `22.2036` edge `0.4341` maxDD `-6.4195`
- `market_context_high->crypto_alt_1h` score `3.3501` n `50` status `ready` deltaP `15.2515` edge `0.2438` maxDD `-3.6376`
- `market_context_high->crypto_major_1h` score `3.1691` n `50` status `ready` deltaP `14.7485` edge `0.2108` maxDD `-2.2692`
- `market_context_high->fx_4h` score `2.7641` n `50` status `ready` deltaP `30.8598` edge `0.0381` maxDD `-0.0791`
- `news_risk_high->equity_4h` score `2.5107` n `116` status `ready` deltaP `22.0984` edge `0.1315` maxDD `-2.9013`
- `market_context_high->equity_24h` score `1.5581` n `50` status `ready` deltaP `7.5833` edge `0.3354` maxDD `-11.8957`
- `news_risk_high->crypto_major_24h` score `1.5183` n `73` status `ready` deltaP `5.9908` edge `0.4701` maxDD `-15.8971`
- `market_context_high->fx_1h` score `1.4711` n `50` status `ready` deltaP `20.6407` edge `0.0114` maxDD `-0.113`
- `news_risk_high->crypto_major_4h` score `1.3849` n `116` status `ready` deltaP `14.8076` edge `0.3098` maxDD `-10.477`
- `news_risk_high->metal_24h` score `1.3504` n `73` status `ready` deltaP `13.009` edge `0.2138` maxDD `-2.192`
- `news_risk_high->crypto_alt_1h` score `1.2026` n `116` status `ready` deltaP `6.1481` edge `0.1153` maxDD `-2.4854`
- `market_context_high->fx_24h` score `0.8245` n `50` status `ready` deltaP `17.7292` edge `0.0893` maxDD `-1.8102`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
