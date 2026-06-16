# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-16T14:52:38.551922+00:00`
- Price records: `672`
- Market context records: `4101`
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

- `risk_on_high->unknown_4h` score `144.7563` n `40` status `ready` deltaP `-8.811` edge `12.3034` maxDD `-10.864`
- `risk_on_and_context->unknown_4h` score `144.7563` n `40` status `ready` deltaP `-8.811` edge `12.3034` maxDD `-10.864`
- `market_context_high->unknown_1h` score `45.8375` n `183` status `ready` deltaP `2.1081` edge `3.9635` maxDD `-9.6211`
- `market_context_high->unknown_24h` score `37.2078` n `144` status `ready` deltaP `-8.893` edge `3.5628` maxDD `-24.2289`
- `market_context_high->unknown_4h` score `15.713` n `177` status `ready` deltaP `-1.9042` edge `1.8644` maxDD `-35.7161`
- `risk_on_high->equity_4h` score `2.5135` n `40` status `ready` deltaP `36.372` edge `-0.0283` maxDD `-0.0446`
- `risk_on_and_context->equity_4h` score `2.5135` n `40` status `ready` deltaP `36.372` edge `-0.0283` maxDD `-0.0446`
- `risk_on_high->equity_1h` score `0.3572` n `40` status `ready` deltaP `10.9132` edge `-0.0039` maxDD `-0.7937`
- `risk_on_and_context->equity_1h` score `0.3572` n `40` status `ready` deltaP `10.9132` edge `-0.0039` maxDD `-0.7937`
- `risk_on_high->fx_4h` score `0.1539` n `40` status `ready` deltaP `11.311` edge `0.0034` maxDD `-0.3925`
- `risk_on_and_context->fx_4h` score `0.1539` n `40` status `ready` deltaP `11.311` edge `0.0034` maxDD `-0.3925`
- `risk_on_high->fx_1h` score `0.0902` n `40` status `ready` deltaP `5.0` edge `0.0012` maxDD `-0.1704`
- `risk_on_and_context->fx_1h` score `0.0902` n `40` status `ready` deltaP `5.0` edge `0.0012` maxDD `-0.1704`
- `risk_on_high->crypto_major_1h` score `-0.0129` n `40` status `ready` deltaP `10.509` edge `-0.0175` maxDD `-2.3372`
- `risk_on_and_context->crypto_major_1h` score `-0.0129` n `40` status `ready` deltaP `10.509` edge `-0.0175` maxDD `-2.3372`
- `market_context_high->equity_1h` score `-0.1291` n `183` status `ready` deltaP `4.0689` edge `0.0492` maxDD `-4.6337`
- `risk_on_high->crypto_major_4h` score `-0.1372` n `40` status `ready` deltaP `16.0976` edge `-0.0522` maxDD `-2.6576`
- `risk_on_and_context->crypto_major_4h` score `-0.1372` n `40` status `ready` deltaP `16.0976` edge `-0.0522` maxDD `-2.6576`
- `market_context_high->equity_4h` score `-0.22` n `177` status `ready` deltaP `11.7534` edge `0.0564` maxDD `-6.9137`
- `market_context_high->index_24h` score `-0.3057` n `144` status `ready` deltaP `13.5182` edge `-0.1156` maxDD `0.0`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
