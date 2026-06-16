# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-16T15:22:40.977411+00:00`
- Price records: `672`
- Market context records: `4103`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `10424`

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

- `risk_on_high->unknown_4h` score `144.8019` n `40` status `ready` deltaP `-8.811` edge `12.3072` maxDD `-10.864`
- `risk_on_and_context->unknown_4h` score `144.8019` n `40` status `ready` deltaP `-8.811` edge `12.3072` maxDD `-10.864`
- `market_context_high->unknown_1h` score `45.0022` n `185` status `ready` deltaP `2.1072` edge `3.8939` maxDD `-9.6211`
- `market_context_high->unknown_24h` score `37.2781` n `144` status `ready` deltaP `-8.7197` edge `3.5675` maxDD `-24.2289`
- `market_context_high->unknown_4h` score `15.7586` n `177` status `ready` deltaP `-1.9042` edge `1.8682` maxDD `-35.7161`
- `risk_on_high->equity_4h` score `2.5255` n `40` status `ready` deltaP `36.372` edge `-0.0273` maxDD `-0.0446`
- `risk_on_and_context->equity_4h` score `2.5255` n `40` status `ready` deltaP `36.372` edge `-0.0273` maxDD `-0.0446`
- `risk_on_high->equity_1h` score `0.3128` n `40` status `ready` deltaP `10.9132` edge `-0.0076` maxDD `-0.7937`
- `risk_on_and_context->equity_1h` score `0.3128` n `40` status `ready` deltaP `10.9132` edge `-0.0076` maxDD `-0.7937`
- `risk_on_high->fx_4h` score `0.1373` n `40` status `ready` deltaP `11.0061` edge `0.0033` maxDD `-0.3925`
- `risk_on_and_context->fx_4h` score `0.1373` n `40` status `ready` deltaP `11.0061` edge `0.0033` maxDD `-0.3925`
- `risk_on_high->fx_1h` score `0.0731` n `40` status `ready` deltaP `4.7006` edge `0.001` maxDD `-0.1704`
- `risk_on_and_context->fx_1h` score `0.0731` n `40` status `ready` deltaP `4.7006` edge `0.001` maxDD `-0.1704`
- `risk_on_high->crypto_major_1h` score `-0.0067` n `40` status `ready` deltaP `10.509` edge `-0.0167` maxDD `-2.3372`
- `risk_on_and_context->crypto_major_1h` score `-0.0067` n `40` status `ready` deltaP `10.509` edge `-0.0167` maxDD `-2.3372`
- `risk_on_high->crypto_major_4h` score `-0.048` n `40` status `ready` deltaP `16.4024` edge `-0.0468` maxDD `-2.6576`
- `risk_on_and_context->crypto_major_4h` score `-0.048` n `40` status `ready` deltaP `16.4024` edge `-0.0468` maxDD `-2.6576`
- `market_context_high->equity_4h` score `-0.208` n `177` status `ready` deltaP `11.7534` edge `0.0574` maxDD `-6.9137`
- `market_context_high->fx_1h` score `-0.2939` n `185` status `ready` deltaP `1.5925` edge `0.0002` maxDD `-0.546`
- `market_context_high->index_24h` score `-0.3033` n `144` status `ready` deltaP `13.5182` edge `-0.1154` maxDD `0.0`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
