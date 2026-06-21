# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-21T06:52:25.247311+00:00`
- Price records: `672`
- Market context records: `4288`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `10690`

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

- `risk_on_high->unknown_4h` score `130.6216` n `44` status `ready` deltaP `-2.5084` edge `11.0837` maxDD `-10.8809`
- `risk_on_and_context->unknown_4h` score `130.6216` n `44` status `ready` deltaP `-2.5084` edge `11.0837` maxDD `-10.8809`
- `market_context_high->unknown_1h` score `27.9303` n `236` status `ready` deltaP `2.6059` edge `2.4681` maxDD `-9.6361`
- `market_context_high->unknown_4h` score `8.9782` n `236` status `ready` deltaP `0.5348` edge `1.2876` maxDD `-35.7719`
- `market_context_high->unknown_24h` score `8.1281` n `200` status `ready` deltaP `-7.6944` edge `1.132` maxDD `-24.2693`
- `risk_on_high->equity_4h` score `2.0511` n `44` status `ready` deltaP `31.4163` edge `-0.0338` maxDD `-0.044`
- `risk_on_and_context->equity_4h` score `2.0511` n `44` status `ready` deltaP `31.4163` edge `-0.0338` maxDD `-0.044`
- `risk_on_high->metal_24h` score `1.1459` n `40` status `ready` deltaP `-22.2569` edge `0.3567` maxDD `-1.9133`
- `risk_on_and_context->metal_24h` score `1.1459` n `40` status `ready` deltaP `-22.2569` edge `0.3567` maxDD `-1.9133`
- `risk_on_high->crypto_major_4h` score `0.973` n `44` status `ready` deltaP `15.4102` edge `0.0449` maxDD `-2.6576`
- `risk_on_and_context->crypto_major_4h` score `0.973` n `44` status `ready` deltaP `15.4102` edge `0.0449` maxDD `-2.6576`
- `risk_on_high->equity_24h` score `0.8037` n `40` status `ready` deltaP `22.9167` edge `-0.0858` maxDD `0.0`
- `risk_on_and_context->equity_24h` score `0.8037` n `40` status `ready` deltaP `22.9167` edge `-0.0858` maxDD `0.0`
- `risk_on_high->fx_1h` score `0.4207` n `44` status `ready` deltaP `8.1927` edge `0.0034` maxDD `-0.1704`
- `risk_on_and_context->fx_1h` score `0.4207` n `44` status `ready` deltaP `8.1927` edge `0.0034` maxDD `-0.1704`
- `risk_on_high->crypto_major_1h` score `0.1487` n `44` status `ready` deltaP `8.0975` edge `0.0193` maxDD `-2.3372`
- `risk_on_and_context->crypto_major_1h` score `0.1487` n `44` status `ready` deltaP `8.0975` edge `0.0193` maxDD `-2.3372`
- `risk_on_high->fx_4h` score `0.0281` n `44` status `ready` deltaP `8.786` edge `0.0041` maxDD `-0.3925`
- `risk_on_and_context->fx_4h` score `0.0281` n `44` status `ready` deltaP `8.786` edge `0.0041` maxDD `-0.3925`
- `risk_on_high->equity_1h` score `-0.0477` n `44` status `ready` deltaP `6.6277` edge `-0.0092` maxDD `-0.7834`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
