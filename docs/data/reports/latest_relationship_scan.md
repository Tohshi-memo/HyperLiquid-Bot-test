# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-19T16:52:29.325982+00:00`
- Price records: `672`
- Market context records: `4120`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `10016`

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

- `risk_on_high->unknown_4h` score `145.4536` n `40` status `ready` deltaP `-8.7182` edge `12.3611` maxDD `-10.8809`
- `risk_on_and_context->unknown_4h` score `145.4536` n `40` status `ready` deltaP `-8.7182` edge `12.3611` maxDD `-10.8809`
- `market_context_high->unknown_1h` score `39.6452` n `198` status `ready` deltaP `1.3974` edge `3.4524` maxDD `-9.6361`
- `market_context_high->unknown_24h` score `14.4676` n `198` status `ready` deltaP `-9.8247` edge `1.6745` maxDD `-24.2693`
- `market_context_high->unknown_4h` score `11.4441` n `198` status `ready` deltaP `-2.0768` edge `1.5105` maxDD `-35.7719`
- `risk_on_high->equity_4h` score `2.8116` n `40` status `ready` deltaP `36.6629` edge `-0.0054` maxDD `-0.044`
- `risk_on_and_context->equity_4h` score `2.8116` n `40` status `ready` deltaP `36.6629` edge `-0.0054` maxDD `-0.044`
- `risk_on_high->crypto_major_4h` score `1.6961` n `40` status `ready` deltaP `18.5389` edge `0.0843` maxDD `-2.6576`
- `risk_on_and_context->crypto_major_4h` score `1.6961` n `40` status `ready` deltaP `18.5389` edge `0.0843` maxDD `-2.6576`
- `risk_on_high->metal_4h` score `0.5237` n `40` status `ready` deltaP `11.4462` edge `0.0244` maxDD `-1.3516`
- `risk_on_and_context->metal_4h` score `0.5237` n `40` status `ready` deltaP `11.4462` edge `0.0244` maxDD `-1.3516`
- `risk_on_high->equity_1h` score `0.2552` n `40` status `ready` deltaP `10.8483` edge `-0.0121` maxDD `-0.7834`
- `risk_on_and_context->equity_1h` score `0.2552` n `40` status `ready` deltaP `10.8483` edge `-0.0121` maxDD `-0.7834`
- `risk_on_high->metal_24h` score `0.2337` n `40` status `ready` deltaP `-19.5329` edge `0.2216` maxDD `-1.9133`
- `risk_on_and_context->metal_24h` score `0.2337` n `40` status `ready` deltaP `-19.5329` edge `0.2216` maxDD `-1.9133`
- `risk_on_high->crypto_major_1h` score `0.2175` n `40` status `ready` deltaP `10.8894` edge `0.0095` maxDD `-2.3372`
- `risk_on_and_context->crypto_major_1h` score `0.2175` n `40` status `ready` deltaP `10.8894` edge `0.0095` maxDD `-2.3372`
- `risk_on_high->equity_24h` score `0.0794` n `40` status `ready` deltaP `29.148` edge `-0.1877` maxDD `0.0`
- `risk_on_and_context->equity_24h` score `0.0794` n `40` status `ready` deltaP `29.148` edge `-0.1877` maxDD `0.0`
- `risk_on_high->fx_4h` score `0.0793` n `40` status `ready` deltaP `9.9664` edge `0.0028` maxDD `-0.3925`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
