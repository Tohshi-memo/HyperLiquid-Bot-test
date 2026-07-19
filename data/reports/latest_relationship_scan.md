# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-19T09:37:23.379296+00:00`
- Price records: `672`
- Market context records: `7236`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `112`

- Symbol pattern count: `13702`

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

- `risk_on_high->crypto_major_4h` score `5.8399` n `34` status `ready` deltaP `26.4706` edge `0.3485` maxDD `-0.7314`
- `risk_on_and_context->crypto_major_4h` score `5.8399` n `34` status `ready` deltaP `26.4706` edge `0.3485` maxDD `-0.7314`
- `risk_on_high->crypto_alt_4h` score `4.2857` n `34` status `ready` deltaP `17.2525` edge `0.2814` maxDD `-1.1423`
- `risk_on_and_context->crypto_alt_4h` score `4.2857` n `34` status `ready` deltaP `17.2525` edge `0.2814` maxDD `-1.1423`
- `risk_on_high->commodity_1h` score `2.0832` n `34` status `ready` deltaP `22.279` edge `0.0401` maxDD `-0.2021`
- `risk_on_and_context->commodity_1h` score `2.0832` n `34` status `ready` deltaP `22.279` edge `0.0401` maxDD `-0.2021`
- `risk_on_high->equity_4h` score `1.0274` n `34` status `ready` deltaP `4.9856` edge `0.1367` maxDD `-2.412`
- `risk_on_and_context->equity_4h` score `1.0274` n `34` status `ready` deltaP `4.9856` edge `0.1367` maxDD `-2.412`
- `risk_on_high->crypto_major_1h` score `0.2715` n `34` status `ready` deltaP `7.6259` edge `0.013` maxDD `-0.9888`
- `risk_on_and_context->crypto_major_1h` score `0.2715` n `34` status `ready` deltaP `7.6259` edge `0.013` maxDD `-0.9888`
- `risk_on_high->equity_1h` score `0.2052` n `34` status `ready` deltaP `2.5977` edge `0.0298` maxDD `-0.7345`
- `risk_on_and_context->equity_1h` score `0.2052` n `34` status `ready` deltaP `2.5977` edge `0.0298` maxDD `-0.7345`
- `risk_on_high->unknown_4h` score `-0.1169` n `34` status `ready` deltaP `3.3716` edge `0.0224` maxDD `-1.4561`
- `risk_on_and_context->unknown_4h` score `-0.1169` n `34` status `ready` deltaP `3.3716` edge `0.0224` maxDD `-1.4561`
- `market_context_high->fx_1h` score `-0.2602` n `168` status `ready` deltaP `2.2313` edge `0.0007` maxDD `-0.5817`
- `risk_on_high->commodity_4h` score `-0.5834` n `34` status `ready` deltaP `0.5918` edge `-0.0098` maxDD `-0.7546`
- `risk_on_and_context->commodity_4h` score `-0.5834` n `34` status `ready` deltaP `0.5918` edge `-0.0098` maxDD `-0.7546`
- `market_context_high->commodity_1h` score `-0.6203` n `168` status `ready` deltaP `-0.6202` edge `-0.0133` maxDD `-1.9668`
- `market_context_high->crypto_alt_1h` score `-0.7208` n `168` status `ready` deltaP `-0.5881` edge `0.0154` maxDD `-5.9775`
- `market_context_high->crypto_major_1h` score `-0.7555` n `168` status `ready` deltaP `2.9691` edge `0.0244` maxDD `-7.6171`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
