# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-26T22:22:01.341811+00:00`
- Price records: `672`
- Market context records: `4871`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `72`

- Symbol pattern count: `7594`

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

- `market_context_high->unknown_1h` score `15.3282` n `110` status `ready` deltaP `10.3212` edge `1.2503` maxDD `-1.674`
- `market_context_high->unknown_4h` score `9.7046` n `110` status `ready` deltaP `23.4673` edge `0.7054` maxDD `-1.917`
- `market_context_high->crypto_alt_4h` score `6.446` n `110` status `ready` deltaP `21.2084` edge `0.531` maxDD `-7.8181`
- `market_context_high->crypto_major_4h` score `6.1542` n `110` status `ready` deltaP `18.3398` edge `0.513` maxDD `-7.1265`
- `market_context_high->unknown_24h` score `5.2662` n `91` status `ready` deltaP `25.8166` edge `0.301` maxDD `-1.4072`
- `market_context_high->metal_4h` score `1.2778` n `110` status `ready` deltaP `9.5871` edge `0.1088` maxDD `-1.9651`
- `market_context_high->equity_4h` score `0.8828` n `110` status `ready` deltaP `12.439` edge `0.1684` maxDD `-6.3852`
- `market_context_high->index_4h` score `0.536` n `110` status `ready` deltaP `11.2306` edge `0.0401` maxDD `-0.7006`
- `market_context_high->crypto_major_1h` score `0.4703` n `110` status `ready` deltaP `6.4698` edge `0.121` maxDD `-5.6406`
- `market_context_high->crypto_alt_1h` score `0.4316` n `110` status `ready` deltaP `8.1709` edge `0.1031` maxDD `-5.5126`
- `market_context_high->equity_1h` score `0.2137` n `110` status `ready` deltaP `4.2352` edge `0.0589` maxDD `-2.779`
- `market_context_high->metal_1h` score `-0.1503` n `110` status `ready` deltaP `1.1431` edge `0.0311` maxDD `-1.3057`
- `market_context_high->commodity_1h` score `-0.209` n `110` status `ready` deltaP `3.5819` edge `0.0153` maxDD `-1.278`
- `market_context_high->index_1h` score `-0.4876` n `110` status `ready` deltaP `0.3103` edge `0.0109` maxDD `-0.7054`
- `market_context_high->fx_4h` score `-0.6245` n `110` status `ready` deltaP `1.6768` edge `0.0058` maxDD `-1.0967`
- `market_context_high->commodity_4h` score `-0.895` n `110` status `ready` deltaP `5.9673` edge `0.0043` maxDD `-4.4933`
- `market_context_high->fx_1h` score `-1.3741` n `110` status `ready` deltaP `-7.3163` edge `-0.0044` maxDD `-0.5734`
- `market_context_high->fx_24h` score `-1.8428` n `91` status `ready` deltaP `-6.3359` edge `-0.0103` maxDD `-2.749`
- `market_context_high->index_24h` score `-4.6908` n `91` status `ready` deltaP `-7.1448` edge `-0.1452` maxDD `-24.6845`
- `market_context_high->commodity_24h` score `-5.1903` n `91` status `ready` deltaP `12.0688` edge `-0.0021` maxDD `-27.5371`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
