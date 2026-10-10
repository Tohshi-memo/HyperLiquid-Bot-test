# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-10T20:07:30.738018+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `72`

- Symbol pattern count: `5538`

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

- `market_context_high->unknown_4h` score `40.4675` n `91` status `ready` deltaP `-6.7978` edge `3.4715` maxDD `-2.3109`
- `market_context_high->equity_24h` score `10.0667` n `91` status `ready` deltaP `38.5474` edge `0.6248` maxDD `-1.0977`
- `market_context_high->crypto_major_24h` score `9.3731` n `91` status `ready` deltaP `20.9707` edge `1.3767` maxDD `-17.8526`
- `market_context_high->crypto_major_4h` score `1.5355` n `91` status `ready` deltaP `18.1637` edge `0.2088` maxDD `-6.9761`
- `market_context_high->crypto_alt_24h` score `1.3327` n `91` status `ready` deltaP `10.1534` edge `0.7144` maxDD `-35.5652`
- `market_context_high->crypto_major_1h` score `0.2233` n `91` status `ready` deltaP `10.1435` edge `0.0499` maxDD `-3.7778`
- `market_context_high->fx_1h` score `0.1038` n `91` status `ready` deltaP `4.751` edge `0.0012` maxDD `-0.271`
- `market_context_high->fx_4h` score `-0.122` n `91` status `ready` deltaP `8.5215` edge `0.0077` maxDD `-0.3077`
- `market_context_high->index_24h` score `-0.184` n `91` status `ready` deltaP `11.4259` edge `0.0912` maxDD `-1.9432`
- `market_context_high->commodity_1h` score `-0.3207` n `91` status `ready` deltaP `1.0019` edge `0.0042` maxDD `-0.3417`
- `market_context_high->metal_1h` score `-0.3445` n `91` status `ready` deltaP `3.1487` edge `0.0015` maxDD `-0.7626`
- `market_context_high->metal_24h` score `-0.4374` n `91` status `ready` deltaP `5.403` edge `0.0564` maxDD `-3.5466`
- `market_context_high->commodity_4h` score `-0.6293` n `91` status `ready` deltaP `-1.0318` edge `-0.0038` maxDD `-1.6002`
- `market_context_high->equity_1h` score `-0.9461` n `91` status `ready` deltaP `-4.8874` edge `-0.0047` maxDD `-2.0542`
- `market_context_high->metal_4h` score `-0.9633` n `91` status `ready` deltaP `-5.4661` edge `0.0137` maxDD `-1.0609`
- `market_context_high->crypto_alt_4h` score `-0.9985` n `91` status `ready` deltaP `-6.4946` edge `0.1086` maxDD `-8.7986`
- `market_context_high->index_1h` score `-1.1306` n `91` status `ready` deltaP `-8.3915` edge `-0.0028` maxDD `-0.5627`
- `market_context_high->crypto_alt_1h` score `-1.2131` n `91` status `ready` deltaP `-2.5432` edge `0.0297` maxDD `-4.7735`
- `market_context_high->index_4h` score `-1.217` n `91` status `ready` deltaP `-9.6456` edge `0.0015` maxDD `-1.1242`
- `market_context_high->equity_4h` score `-1.2706` n `91` status `ready` deltaP `-3.7439` edge `0.009` maxDD `-5.4217`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
