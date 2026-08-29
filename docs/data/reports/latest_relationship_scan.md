# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-29T19:52:28.188662+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11384`

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

- `news_risk_high->unknown_24h` score `29.3431` n `57` status `ready` deltaP `2.33` edge `2.5271` maxDD `-4.1232`
- `market_context_high->unknown_24h` score `11.5963` n `104` status `ready` deltaP `20.9535` edge `0.8999` maxDD `-3.1917`
- `risk_on_high->crypto_alt_4h` score `11.5009` n `36` status `ready` deltaP `44.292` edge `0.669` maxDD `-0.1367`
- `risk_on_and_context->crypto_alt_4h` score `11.5009` n `36` status `ready` deltaP `44.292` edge `0.669` maxDD `-0.1367`
- `news_risk_high->crypto_alt_24h` score `10.4325` n `57` status `ready` deltaP `28.39` edge `1.4858` maxDD `-22.3391`
- `risk_on_high->crypto_major_4h` score `7.9454` n `36` status `ready` deltaP `39.2277` edge `0.4282` maxDD `-1.208`
- `risk_on_and_context->crypto_major_4h` score `7.9454` n `36` status `ready` deltaP `39.2277` edge `0.4282` maxDD `-1.208`
- `news_risk_high->unknown_4h` score `6.0823` n `66` status `ready` deltaP `7.0446` edge `0.5189` maxDD `-1.7205`
- `market_context_high->metal_24h` score `4.6934` n `104` status `ready` deltaP `34.415` edge `0.2636` maxDD `-3.1535`
- `risk_on_high->metal_4h` score `3.0385` n `36` status `ready` deltaP `33.435` edge `0.0389` maxDD `-0.0208`
- `risk_on_and_context->metal_4h` score `3.0385` n `36` status `ready` deltaP `33.435` edge `0.0389` maxDD `-0.0208`
- `news_risk_high->unknown_1h` score `2.6047` n `66` status `ready` deltaP `-0.322` edge `0.2549` maxDD `-0.8558`
- `news_risk_high->fx_4h` score `2.2707` n `66` status `ready` deltaP `33.5505` edge `0.0205` maxDD `-0.3953`
- `market_context_high->unknown_4h` score `2.0669` n `136` status `ready` deltaP `17.4947` edge `0.0988` maxDD `-0.7887`
- `risk_on_high->metal_1h` score `1.377` n `46` status `ready` deltaP `19.0445` edge `0.0092` maxDD `-0.0463`
- `risk_on_and_context->metal_1h` score `1.377` n `46` status `ready` deltaP `19.0445` edge `0.0092` maxDD `-0.0463`
- `risk_on_high->equity_4h` score `1.1914` n `36` status `ready` deltaP `9.4682` edge `0.0611` maxDD `-0.3281`
- `risk_on_and_context->equity_4h` score `1.1914` n `36` status `ready` deltaP `9.4682` edge `0.0611` maxDD `-0.3281`
- `market_context_high->crypto_major_4h` score `0.8271` n `136` status `ready` deltaP `21.8257` edge `0.2685` maxDD `-20.9394`
- `risk_on_high->index_4h` score `0.6726` n `36` status `ready` deltaP `12.5508` edge `0.0033` maxDD `-0.1405`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
