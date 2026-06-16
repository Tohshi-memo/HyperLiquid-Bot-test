# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-16T12:52:42.757517+00:00`
- Price records: `672`
- Market context records: `4093`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `10248`

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

- `risk_on_high->unknown_4h` score `144.6399` n `40` status `ready` deltaP `-8.811` edge `12.2937` maxDD `-10.864`
- `risk_on_and_context->unknown_4h` score `144.6399` n `40` status `ready` deltaP `-8.811` edge `12.2937` maxDD `-10.864`
- `market_context_high->unknown_1h` score `48.6324` n `177` status `ready` deltaP `2.199` edge `4.1958` maxDD `-9.6211`
- `market_context_high->unknown_24h` score `37.0421` n `144` status `ready` deltaP `-9.2396` edge `3.5513` maxDD `-24.2289`
- `market_context_high->unknown_4h` score `16.4596` n `173` status `ready` deltaP `-2.7272` edge `1.9321` maxDD `-35.7161`
- `risk_on_high->equity_4h` score `2.9793` n `40` status `ready` deltaP `36.5244` edge `0.0095` maxDD `-0.0446`
- `risk_on_and_context->equity_4h` score `2.9793` n `40` status `ready` deltaP `36.5244` edge `0.0095` maxDD `-0.0446`
- `market_context_high->equity_1h` score `0.6856` n `177` status `ready` deltaP `5.2945` edge `0.0778` maxDD `-2.144`
- `market_context_high->equity_4h` score `0.5132` n `173` status `ready` deltaP `13.0128` edge `0.1091` maxDD `-6.9137`
- `risk_on_high->equity_1h` score `0.4868` n `40` status `ready` deltaP `11.2126` edge `0.0049` maxDD `-0.7937`
- `risk_on_and_context->equity_1h` score `0.4868` n `40` status `ready` deltaP `11.2126` edge `0.0049` maxDD `-0.7937`
- `risk_on_high->fx_4h` score `0.165` n `40` status `ready` deltaP `11.4634` edge `0.0038` maxDD `-0.3925`
- `risk_on_and_context->fx_4h` score `0.165` n `40` status `ready` deltaP `11.4634` edge `0.0038` maxDD `-0.3925`
- `risk_on_high->fx_1h` score `0.0996` n `40` status `ready` deltaP `5.1497` edge `0.0014` maxDD `-0.1704`
- `risk_on_and_context->fx_1h` score `0.0996` n `40` status `ready` deltaP `5.1497` edge `0.0014` maxDD `-0.1704`
- `market_context_high->index_24h` score `0.0684` n `144` status `ready` deltaP `14.3847` edge `-0.0902` maxDD `0.0`
- `risk_on_high->crypto_major_1h` score `0.0011` n `40` status `ready` deltaP `10.6587` edge `-0.0167` maxDD `-2.3372`
- `risk_on_and_context->crypto_major_1h` score `0.0011` n `40` status `ready` deltaP `10.6587` edge `-0.0167` maxDD `-2.3372`
- `risk_on_high->crypto_major_4h` score `-0.0304` n `40` status `ready` deltaP `16.0976` edge `-0.0433` maxDD `-2.6576`
- `risk_on_and_context->crypto_major_4h` score `-0.0304` n `40` status `ready` deltaP `16.0976` edge `-0.0433` maxDD `-2.6576`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
