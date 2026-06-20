# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-20T10:52:27.720329+00:00`
- Price records: `672`
- Market context records: `4200`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `10050`

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

- `risk_on_high->unknown_4h` score `145.3374` n `40` status `ready` deltaP `-8.5061` edge `12.35` maxDD `-10.8809`
- `risk_on_and_context->unknown_4h` score `145.3374` n `40` status `ready` deltaP `-8.5061` edge `12.35` maxDD `-10.8809`
- `market_context_high->unknown_1h` score `32.6067` n `209` status `ready` deltaP `1.4813` edge `2.8653` maxDD `-9.6361`
- `market_context_high->unknown_4h` score `10.3382` n `202` status `ready` deltaP `-3.1348` edge `1.4254` maxDD `-35.7719`
- `market_context_high->unknown_24h` score `8.317` n `198` status `ready` deltaP `-12.5476` edge `1.1801` maxDD `-24.2693`
- `risk_on_high->commodity_24h` score `2.3734` n `40` status `ready` deltaP `4.5645` edge `0.3955` maxDD `-12.9187`
- `risk_on_and_context->commodity_24h` score `2.3734` n `40` status `ready` deltaP `4.5645` edge `0.3955` maxDD `-12.9187`
- `risk_on_high->equity_4h` score `2.2237` n `40` status `ready` deltaP `32.1037` edge `-0.024` maxDD `-0.044`
- `risk_on_and_context->equity_4h` score `2.2237` n `40` status `ready` deltaP `32.1037` edge `-0.024` maxDD `-0.044`
- `risk_on_high->crypto_major_4h` score `0.7954` n `40` status `ready` deltaP `14.4207` edge `0.0367` maxDD `-2.6576`
- `risk_on_and_context->crypto_major_4h` score `0.7954` n `40` status `ready` deltaP `14.4207` edge `0.0367` maxDD `-2.6576`
- `risk_on_high->metal_4h` score `0.1677` n `40` status `ready` deltaP `8.9634` edge `-0.0047` maxDD `-1.3516`
- `risk_on_and_context->metal_4h` score `0.1677` n `40` status `ready` deltaP `8.9634` edge `-0.0047` maxDD `-1.3516`
- `risk_on_high->equity_1h` score `0.095` n `40` status `ready` deltaP `9.4162` edge `-0.0159` maxDD `-0.7834`
- `risk_on_and_context->equity_1h` score `0.095` n `40` status `ready` deltaP `9.4162` edge `-0.0159` maxDD `-0.7834`
- `risk_on_high->fx_4h` score `0.0666` n `40` status `ready` deltaP `9.4817` edge `0.0044` maxDD `-0.3925`
- `risk_on_and_context->fx_4h` score `0.0666` n `40` status `ready` deltaP `9.4817` edge `0.0044` maxDD `-0.3925`
- `risk_on_high->fx_1h` score `0.0412` n `40` status `ready` deltaP `4.1018` edge `0.0009` maxDD `-0.1704`
- `risk_on_and_context->fx_1h` score `0.0412` n `40` status `ready` deltaP `4.1018` edge `0.0009` maxDD `-0.1704`
- `risk_on_high->crypto_major_1h` score `0.0013` n `40` status `ready` deltaP `8.8623` edge `-0.0047` maxDD `-2.3372`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
