# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-05T08:37:28.091096+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `10935`

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

- `risk_on_high->unknown_4h` score `20.6467` n `139` status `ready` deltaP `8.1429` edge `1.7281` maxDD `-2.2797`
- `risk_on_and_context->unknown_4h` score `20.6467` n `139` status `ready` deltaP `8.1429` edge `1.7281` maxDD `-2.2797`
- `market_context_high->unknown_4h` score `9.6288` n `228` status `ready` deltaP `8.673` edge `0.8176` maxDD `-2.8419`
- `news_risk_high->crypto_alt_24h` score `7.3163` n `37` status `ready` deltaP `25.1783` edge `0.4688` maxDD `-0.8236`
- `news_risk_high->commodity_24h` score `4.2454` n `37` status `ready` deltaP `24.1319` edge `0.1929` maxDD `0.0`
- `news_risk_high->crypto_major_4h` score `3.699` n `37` status `ready` deltaP `17.1803` edge `0.235` maxDD `-0.9693`
- `news_risk_high->metal_4h` score `2.1262` n `37` status `ready` deltaP `21.255` edge `0.0576` maxDD `-0.7692`
- `news_risk_high->commodity_4h` score `1.9178` n `37` status `ready` deltaP `11.5813` edge `0.1027` maxDD `-0.2737`
- `news_risk_high->equity_1h` score `1.6398` n `37` status `ready` deltaP `13.6835` edge `0.0845` maxDD `-0.7924`
- `news_risk_high->crypto_major_1h` score `1.2302` n `37` status `ready` deltaP `6.6152` edge `0.0767` maxDD `-0.4628`
- `news_risk_high->index_1h` score `1.2006` n `37` status `ready` deltaP `15.0227` edge `0.0133` maxDD `-0.0724`
- `news_risk_high->metal_1h` score `1.1963` n `37` status `ready` deltaP `14.2661` edge `0.0239` maxDD `-0.2118`
- `news_risk_high->crypto_alt_1h` score `0.8926` n `37` status `ready` deltaP `8.5775` edge `0.0437` maxDD `-0.7867`
- `news_risk_high->crypto_alt_4h` score `0.5903` n `37` status `ready` deltaP `6.3983` edge `0.0394` maxDD `-1.296`
- `news_risk_high->crypto_major_24h` score `0.4706` n `37` status `ready` deltaP `13.9734` edge `0.2448` maxDD `-18.2098`
- `news_risk_high->fx_24h` score `0.2836` n `37` status `ready` deltaP `12.8378` edge `0.0396` maxDD `-3.1244`
- `risk_on_high->metal_1h` score `0.0972` n `151` status `ready` deltaP `12.3151` edge `0.0016` maxDD `-1.699`
- `risk_on_and_context->metal_1h` score `0.0972` n `151` status `ready` deltaP `12.3151` edge `0.0016` maxDD `-1.699`
- `news_risk_high->commodity_1h` score `-0.0067` n `37` status `ready` deltaP `6.0245` edge `0.0036` maxDD `-0.9036`
- `market_context_high->equity_24h` score `-0.0503` n `192` status `ready` deltaP `15.7986` edge `0.3228` maxDD `-20.7654`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
