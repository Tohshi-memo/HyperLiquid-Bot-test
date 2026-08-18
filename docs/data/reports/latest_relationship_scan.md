# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-18T04:22:27.540096+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11837`

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

- `market_context_high->crypto_major_24h` score `3.46` n `73` status `ready` deltaP `9.7078` edge `0.3444` maxDD `-4.9964`
- `market_context_high->commodity_24h` score `0.8063` n `73` status `ready` deltaP `12.6469` edge `0.1662` maxDD `-4.666`
- `market_context_high->metal_24h` score `0.4085` n `73` status `ready` deltaP `4.8384` edge `0.072` maxDD `-1.9504`
- `market_context_high->commodity_4h` score `0.2943` n `102` status `ready` deltaP `9.8488` edge `0.0439` maxDD `-2.4692`
- `market_context_high->metal_4h` score `0.1712` n `102` status `ready` deltaP `10.1745` edge `0.0117` maxDD `-1.273`
- `market_context_high->crypto_major_4h` score `0.1144` n `102` status `ready` deltaP `6.3845` edge `0.0742` maxDD `-3.1677`
- `market_context_high->index_1h` score `0.04` n `104` status `ready` deltaP `6.6617` edge `0.0027` maxDD `-0.3584`
- `market_context_high->equity_1h` score `-0.1057` n `104` status `ready` deltaP `3.1956` edge `0.0254` maxDD `-1.8201`
- `market_context_high->unknown_1h` score `-0.197` n `104` status `ready` deltaP `6.2586` edge `-0.0332` maxDD `-0.6621`
- `market_context_high->fx_4h` score `-0.2273` n `102` status `ready` deltaP `4.5104` edge `0.0017` maxDD `-0.3904`
- `market_context_high->metal_1h` score `-0.5387` n `104` status `ready` deltaP `-1.3243` edge `-0.0032` maxDD `-1.2293`
- `market_context_high->fx_1h` score `-0.5774` n `104` status `ready` deltaP `-1.9864` edge `0.0013` maxDD `-0.2273`
- `market_context_high->commodity_1h` score `-0.6403` n `104` status `ready` deltaP `-3.4834` edge `0.0024` maxDD `-1.5684`
- `market_context_high->index_4h` score `-0.6838` n `102` status `ready` deltaP `-3.4583` edge `0.0007` maxDD `-0.5582`
- `market_context_high->crypto_alt_1h` score `-0.755` n `104` status `ready` deltaP `-2.4355` edge `0.0067` maxDD `-2.9807`
- `market_context_high->crypto_major_1h` score `-0.94` n `104` status `ready` deltaP `-3.4834` edge `-0.0021` maxDD `-3.6152`
- `market_context_high->crypto_alt_4h` score `-1.0135` n `102` status `ready` deltaP `4.5314` edge `0.0546` maxDD `-8.8459`
- `market_context_high->equity_4h` score `-1.1929` n `102` status `ready` deltaP `-6.0707` edge `-0.0047` maxDD `-3.9543`
- `market_context_high->index_24h` score `-1.4006` n `73` status `ready` deltaP `4.5321` edge `-0.071` maxDD `-2.4075`
- `market_context_high->unknown_24h` score `-1.4025` n `73` status `ready` deltaP `3.8152` edge `-0.0832` maxDD `-1.0624`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
