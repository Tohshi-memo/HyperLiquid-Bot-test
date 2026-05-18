# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-18T13:37:19.062187+00:00`
- Price records: `672`
- Market context records: `1122`
- Flow alert records: `5134`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8723`

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

- `market_context_high->crypto_major_24h` score `18.8147` n `150` status `ready` deltaP `40.507` edge `1.3442` maxDD `-3.3749`
- `market_context_high->crypto_alt_24h` score `8.5302` n `150` status `ready` deltaP `16.868` edge `0.7218` maxDD `-9.5387`
- `market_context_high->equity_24h` score `6.7581` n `150` status `ready` deltaP `16.5208` edge `0.5027` maxDD `-3.6396`
- `market_context_high->metal_24h` score `5.5571` n `150` status `ready` deltaP `-1.8889` edge `0.6424` maxDD `-6.3373`
- `market_context_high->index_24h` score `5.3459` n `150` status `ready` deltaP `15.4791` edge `0.3731` maxDD `-2.1308`
- `market_context_high->equity_4h` score `1.5497` n `168` status `ready` deltaP `8.9649` edge `0.1357` maxDD `-3.6396`
- `market_context_high->index_4h` score `0.742` n `168` status `ready` deltaP `7.0702` edge `0.083` maxDD `-2.1308`
- `market_context_high->index_1h` score `0.3875` n `168` status `ready` deltaP `6.8969` edge `0.018` maxDD `-0.5353`
- `market_context_high->equity_1h` score `0.1973` n `168` status `ready` deltaP `2.4308` edge `0.038` maxDD `-1.3546`
- `market_context_high->fx_1h` score `0.1496` n `168` status `ready` deltaP `8.4652` edge `0.0016` maxDD `-0.3124`
- `market_context_high->crypto_major_1h` score `-0.0026` n `168` status `ready` deltaP `6.8328` edge `0.0308` maxDD `-4.1256`
- `market_context_high->crypto_major_4h` score `-0.0518` n `168` status `ready` deltaP `7.5421` edge `0.1352` maxDD `-8.3693`
- `market_context_high->metal_1h` score `-0.2652` n `168` status `ready` deltaP `6.8007` edge `-0.0064` maxDD `-2.2164`
- `market_context_high->crypto_alt_1h` score `-0.3233` n `168` status `ready` deltaP `2.6447` edge `0.0397` maxDD `-3.4088`
- `market_context_high->commodity_1h` score `-0.671` n `168` status `ready` deltaP `-1.3259` edge `0.0036` maxDD `-3.7959`
- `market_context_high->fx_4h` score `-0.7223` n `168` status `ready` deltaP `0.9364` edge `0.0008` maxDD `-1.6381`
- `market_context_high->crypto_alt_4h` score `-1.1071` n `168` status `ready` deltaP `4.9289` edge `0.1217` maxDD `-16.7194`
- `market_context_high->metal_4h` score `-2.501` n `168` status `ready` deltaP `5.9378` edge `-0.0526` maxDD `-9.2991`
- `market_context_high->commodity_4h` score `-3.1066` n `168` status `ready` deltaP `-10.9683` edge `-0.0084` maxDD `-13.0076`
- `market_context_high->unknown_4h` score `-3.4145` n `168` status `ready` deltaP `8.5511` edge `-0.2199` maxDD `-6.7322`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
