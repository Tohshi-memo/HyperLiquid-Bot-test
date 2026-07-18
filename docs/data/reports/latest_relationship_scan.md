# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-18T22:37:31.799384+00:00`
- Price records: `672`
- Market context records: `7189`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11810`

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

- `risk_on_high->crypto_major_4h` score `6.2707` n `34` status `ready` deltaP `29.2145` edge `0.3661` maxDD `-0.7314`
- `risk_on_and_context->crypto_major_4h` score `6.2707` n `34` status `ready` deltaP `29.2145` edge `0.3661` maxDD `-0.7314`
- `risk_on_high->crypto_alt_4h` score `4.5566` n `34` status `ready` deltaP `18.9293` edge `0.2928` maxDD `-1.1423`
- `risk_on_and_context->crypto_alt_4h` score `4.5566` n `34` status `ready` deltaP `18.9293` edge `0.2928` maxDD `-1.1423`
- `risk_on_high->commodity_1h` score `2.0472` n `34` status `ready` deltaP `22.1293` edge `0.0381` maxDD `-0.2021`
- `risk_on_and_context->commodity_1h` score `2.0472` n `34` status `ready` deltaP `22.1293` edge `0.0381` maxDD `-0.2021`
- `risk_on_high->equity_4h` score `1.4397` n `34` status `ready` deltaP `8.3393` edge `0.1487` maxDD `-2.412`
- `risk_on_and_context->equity_4h` score `1.4397` n `34` status `ready` deltaP `8.3393` edge `0.1487` maxDD `-2.412`
- `risk_on_high->crypto_major_1h` score `0.4126` n `34` status `ready` deltaP `8.8235` edge `0.0231` maxDD `-0.9888`
- `risk_on_and_context->crypto_major_1h` score `0.4126` n `34` status `ready` deltaP `8.8235` edge `0.0231` maxDD `-0.9888`
- `risk_on_high->equity_1h` score `0.3898` n `34` status `ready` deltaP `4.2444` edge `0.0342` maxDD `-0.7345`
- `risk_on_and_context->equity_1h` score `0.3898` n `34` status `ready` deltaP `4.2444` edge `0.0342` maxDD `-0.7345`
- `risk_on_high->unknown_4h` score `-0.2893` n `34` status `ready` deltaP `4.2863` edge `-0.0058` maxDD `-1.4561`
- `risk_on_and_context->unknown_4h` score `-0.2893` n `34` status `ready` deltaP `4.2863` edge `-0.0058` maxDD `-1.4561`
- `market_context_high->fx_1h` score `-0.3146` n `178` status `ready` deltaP `3.2581` edge `0.001` maxDD `-0.5817`
- `market_context_high->crypto_major_1h` score `-0.5038` n `178` status `ready` deltaP `5.618` edge `0.039` maxDD `-7.6171`
- `market_context_high->crypto_alt_1h` score `-0.5783` n `178` status `ready` deltaP `0.6358` edge `0.0255` maxDD `-5.9775`
- `market_context_high->commodity_1h` score `-0.6046` n `178` status `ready` deltaP `-0.4087` edge `-0.0127` maxDD `-1.9668`
- `risk_on_high->commodity_4h` score `-0.7302` n `34` status `ready` deltaP `-0.6277` edge `-0.0139` maxDD `-0.7546`
- `risk_on_and_context->commodity_4h` score `-0.7302` n `34` status `ready` deltaP `-0.6277` edge `-0.0139` maxDD `-0.7546`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
