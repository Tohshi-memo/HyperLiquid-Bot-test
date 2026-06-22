# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-22T06:22:31.846499+00:00`
- Price records: `672`
- Market context records: `4390`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11119`

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

- `risk_on_high->unknown_4h` score `132.8367` n `44` status `ready` deltaP `-0.6791` edge `11.2561` maxDD `-10.8809`
- `risk_on_and_context->unknown_4h` score `132.8367` n `44` status `ready` deltaP `-0.6791` edge `11.2561` maxDD `-10.8809`
- `market_context_high->unknown_1h` score `34.3486` n `219` status `ready` deltaP `2.5648` edge `2.9949` maxDD `-9.6361`
- `market_context_high->unknown_4h` score `11.4338` n `213` status `ready` deltaP `4.1545` edge `1.4681` maxDD `-35.7719`
- `risk_on_high->equity_4h` score `3.3622` n `44` status `ready` deltaP `35.6846` edge `0.047` maxDD `-0.044`
- `risk_on_and_context->equity_4h` score `3.3622` n `44` status `ready` deltaP `35.6846` edge `0.047` maxDD `-0.044`
- `risk_on_high->metal_24h` score `3.0191` n `44` status `ready` deltaP `-15.183` edge `0.5497` maxDD `-1.9133`
- `risk_on_and_context->metal_24h` score `3.0191` n `44` status `ready` deltaP `-15.183` edge `0.5497` maxDD `-1.9133`
- `risk_on_high->crypto_major_4h` score `1.9801` n `44` status `ready` deltaP `18.459` edge `0.1085` maxDD `-2.6576`
- `risk_on_and_context->crypto_major_4h` score `1.9801` n `44` status `ready` deltaP `18.459` edge `0.1085` maxDD `-2.6576`
- `risk_on_high->equity_24h` score `1.8093` n `44` status `ready` deltaP `20.4861` edge `0.0142` maxDD `0.0`
- `risk_on_and_context->equity_24h` score `1.8093` n `44` status `ready` deltaP `20.4861` edge `0.0142` maxDD `0.0`
- `risk_on_high->index_24h` score `1.3319` n `44` status `ready` deltaP `23.2639` edge `-0.0441` maxDD `0.0`
- `risk_on_and_context->index_24h` score `1.3319` n `44` status `ready` deltaP `23.2639` edge `-0.0441` maxDD `0.0`
- `risk_on_high->equity_1h` score `0.6264` n `47` status `ready` deltaP `11.4983` edge `0.0145` maxDD `-0.7834`
- `risk_on_and_context->equity_1h` score `0.6264` n `47` status `ready` deltaP `11.4983` edge `0.0145` maxDD `-0.7834`
- `risk_on_high->metal_4h` score `0.4039` n `44` status `ready` deltaP `6.4856` edge `0.0421` maxDD `-1.3516`
- `risk_on_and_context->metal_4h` score `0.4039` n `44` status `ready` deltaP `6.4856` edge `0.0421` maxDD `-1.3516`
- `risk_on_high->crypto_major_1h` score `0.4036` n `47` status `ready` deltaP `9.1891` edge `0.0447` maxDD `-2.3372`
- `risk_on_and_context->crypto_major_1h` score `0.4036` n `47` status `ready` deltaP `9.1891` edge `0.0447` maxDD `-2.3372`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
