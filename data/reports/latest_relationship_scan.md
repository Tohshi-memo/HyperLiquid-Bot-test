# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-07T05:22:31.027958+00:00`
- Price records: `672`
- Market context records: `5950`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11220`

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

- `news_risk_high->fx_24h` score `6.8806` n `30` status `ready` deltaP `62.8472` edge `0.1544` maxDD `0.0`
- `news_risk_high->commodity_24h` score `5.4644` n `30` status `ready` deltaP `39.2709` edge `0.2141` maxDD `-0.3101`
- `news_risk_high->fx_4h` score `3.7906` n `30` status `ready` deltaP `39.2378` edge `0.0589` maxDD `-0.0345`
- `news_risk_high->fx_1h` score `2.0933` n `30` status `ready` deltaP `25.2794` edge `0.0198` maxDD `-0.1113`
- `market_context_high->equity_4h` score `1.6335` n `221` status `ready` deltaP `10.5852` edge `0.175` maxDD `-4.0887`
- `news_risk_high->crypto_major_1h` score `0.9315` n `30` status `ready` deltaP `11.2375` edge `0.0912` maxDD `-2.0691`
- `news_risk_high->crypto_alt_1h` score `0.2886` n `30` status `ready` deltaP `6.2176` edge `0.0417` maxDD `-1.6923`
- `news_risk_high->index_24h` score `-0.2038` n `30` status `ready` deltaP `6.9791` edge `0.0145` maxDD `-2.3058`
- `news_risk_high->metal_1h` score `-0.3768` n `30` status `ready` deltaP `2.4351` edge `-0.0279` maxDD `-1.2643`
- `market_context_high->equity_1h` score `-0.3971` n `231` status `ready` deltaP `4.7153` edge `0.0305` maxDD `-4.3608`
- `market_context_high->metal_1h` score `-0.4051` n `231` status `ready` deltaP `2.3486` edge `-0.0005` maxDD `-2.0339`
- `market_context_high->index_1h` score `-0.6622` n `231` status `ready` deltaP `0.3823` edge `0.0039` maxDD `-1.3078`
- `market_context_high->commodity_1h` score `-0.6936` n `231` status `ready` deltaP `-4.3796` edge `-0.004` maxDD `-1.4578`
- `market_context_high->equity_24h` score `-0.751` n `213` status `ready` deltaP `19.4004` edge `0.282` maxDD `-31.2762`
- `market_context_high->fx_1h` score `-0.7641` n `231` status `ready` deltaP `-1.7336` edge `-0.001` maxDD `-0.756`
- `news_risk_high->index_1h` score `-1.0462` n `30` status `ready` deltaP `-9.4012` edge `-0.02` maxDD `-1.1161`
- `market_context_high->crypto_major_1h` score `-1.1551` n `231` status `ready` deltaP `1.5839` edge `0.0181` maxDD `-9.807`
- `market_context_high->crypto_alt_1h` score `-1.1627` n `231` status `ready` deltaP `1.499` edge `0.0162` maxDD `-9.3536`
- `market_context_high->metal_4h` score `-1.5677` n `221` status `ready` deltaP `-1.794` edge `-0.0258` maxDD `-5.725`
- `market_context_high->index_4h` score `-1.6646` n `221` status `ready` deltaP `1.3974` edge `0.0207` maxDD `-3.165`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
