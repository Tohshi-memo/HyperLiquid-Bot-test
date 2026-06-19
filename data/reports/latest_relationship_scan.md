# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-19T20:50:12.470326+00:00`
- Price records: `672`
- Market context records: `4138`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `10024`

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

- `risk_on_high->unknown_4h` score `144.7642` n `40` status `ready` deltaP `-10.0305` edge `12.3124` maxDD `-10.8809`
- `risk_on_and_context->unknown_4h` score `144.7642` n `40` status `ready` deltaP `-10.0305` edge `12.3124` maxDD `-10.8809`
- `market_context_high->unknown_1h` score `38.0522` n `202` status `ready` deltaP `1.2406` edge `3.3207` maxDD `-9.6361`
- `market_context_high->unknown_24h` score `12.3462` n `198` status `ready` deltaP `-11.7731` edge `1.5107` maxDD `-24.2693`
- `market_context_high->unknown_4h` score `10.2678` n `200` status `ready` deltaP `-4.0305` edge `1.4255` maxDD `-35.7719`
- `risk_on_high->equity_4h` score `2.6472` n `40` status `ready` deltaP `35.7622` edge `-0.0131` maxDD `-0.044`
- `risk_on_and_context->equity_4h` score `2.6472` n `40` status `ready` deltaP `35.7622` edge `-0.0131` maxDD `-0.044`
- `risk_on_high->crypto_major_4h` score `1.3571` n `40` status `ready` deltaP `17.3171` edge `0.0642` maxDD `-2.6576`
- `risk_on_and_context->crypto_major_4h` score `1.3571` n `40` status `ready` deltaP `17.3171` edge `0.0642` maxDD `-2.6576`
- `risk_on_high->metal_4h` score `0.2605` n `40` status `ready` deltaP `9.878` edge `0.0011` maxDD `-1.3516`
- `risk_on_and_context->metal_4h` score `0.2605` n `40` status `ready` deltaP `9.878` edge `0.0011` maxDD `-1.3516`
- `risk_on_high->equity_1h` score `0.2507` n `40` status `ready` deltaP `10.9132` edge `-0.0129` maxDD `-0.7834`
- `risk_on_and_context->equity_1h` score `0.2507` n `40` status `ready` deltaP `10.9132` edge `-0.0129` maxDD `-0.7834`
- `risk_on_high->commodity_24h` score `0.2237` n `40` status `ready` deltaP `-1.1868` edge `0.2547` maxDD `-12.9187`
- `risk_on_and_context->commodity_24h` score `0.2237` n `40` status `ready` deltaP `-1.1868` edge `0.2547` maxDD `-12.9187`
- `risk_on_high->crypto_major_1h` score `0.1782` n `40` status `ready` deltaP `10.6587` edge `0.006` maxDD `-2.3372`
- `risk_on_and_context->crypto_major_1h` score `0.1782` n `40` status `ready` deltaP `10.6587` edge `0.006` maxDD `-2.3372`
- `risk_on_high->fx_1h` score `0.0256` n `40` status `ready` deltaP `3.8024` edge `0.0009` maxDD `-0.1704`
- `risk_on_and_context->fx_1h` score `0.0256` n `40` status `ready` deltaP `3.8024` edge `0.0009` maxDD `-0.1704`
- `risk_on_high->fx_4h` score `0.0233` n `40` status `ready` deltaP `9.0244` edge `0.0019` maxDD `-0.3925`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
