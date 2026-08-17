# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-17T17:51:43.008563+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11835`

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

- `risk_on_high->unknown_1h` score `7.2148` n `35` status `ready` deltaP `1.5911` edge `0.6301` maxDD `-0.8243`
- `risk_on_and_context->unknown_1h` score `7.2148` n `35` status `ready` deltaP `1.5911` edge `0.6301` maxDD `-0.8243`
- `market_context_high->crypto_major_24h` score `3.939` n `83` status `ready` deltaP `13.7613` edge `0.3573` maxDD `-4.9964`
- `market_context_high->equity_24h` score `2.2683` n `83` status `ready` deltaP `17.0139` edge `0.0756` maxDD `0.0`
- `market_context_high->index_24h` score `1.2703` n `83` status `ready` deltaP `18.9236` edge `-0.0203` maxDD `0.0`
- `risk_on_high->fx_4h` score `1.2047` n `35` status `ready` deltaP `16.5897` edge `0.0039` maxDD `-0.1285`
- `risk_on_and_context->fx_4h` score `1.2047` n `35` status `ready` deltaP `16.5897` edge `0.0039` maxDD `-0.1285`
- `risk_on_high->crypto_major_1h` score `0.9496` n `35` status `ready` deltaP `11.3601` edge `0.034` maxDD `-1.1144`
- `risk_on_and_context->crypto_major_1h` score `0.9496` n `35` status `ready` deltaP `11.3601` edge `0.034` maxDD `-1.1144`
- `risk_on_high->index_1h` score `0.789` n `35` status `ready` deltaP `13.6442` edge `0.0123` maxDD `-0.3343`
- `risk_on_and_context->index_1h` score `0.789` n `35` status `ready` deltaP `13.6442` edge `0.0123` maxDD `-0.3343`
- `risk_on_high->equity_1h` score `0.7406` n `35` status `ready` deltaP `12.4594` edge `0.033` maxDD `-1.6811`
- `risk_on_and_context->equity_1h` score `0.7406` n `35` status `ready` deltaP `12.4594` edge `0.033` maxDD `-1.6811`
- `market_context_high->commodity_4h` score `0.5236` n `132` status `ready` deltaP `12.2644` edge `0.0469` maxDD `-2.4692`
- `risk_on_high->commodity_4h` score `0.4599` n `35` status `ready` deltaP `2.9137` edge `0.0818` maxDD `-1.3651`
- `risk_on_and_context->commodity_4h` score `0.4599` n `35` status `ready` deltaP `2.9137` edge `0.0818` maxDD `-1.3651`
- `market_context_high->commodity_24h` score `0.2001` n `83` status `ready` deltaP `16.8277` edge `0.0968` maxDD `-4.666`
- `risk_on_high->fx_1h` score `0.0788` n `35` status `ready` deltaP `4.5851` edge `0.0023` maxDD `-0.1547`
- `risk_on_and_context->fx_1h` score `0.0788` n `35` status `ready` deltaP `4.5851` edge `0.0023` maxDD `-0.1547`
- `risk_on_high->crypto_major_4h` score `-0.0222` n `35` status `ready` deltaP `1.0845` edge `0.0611` maxDD `-2.0278`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
