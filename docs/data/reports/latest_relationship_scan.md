# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-20T12:07:27.916518+00:00`
- Price records: `672`
- Market context records: `4206`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9632`

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

- `risk_on_high->unknown_4h` score `145.5784` n `40` status `ready` deltaP `-7.7439` edge `12.365` maxDD `-10.8809`
- `risk_on_and_context->unknown_4h` score `145.5784` n `40` status `ready` deltaP `-7.7439` edge `12.365` maxDD `-10.8809`
- `market_context_high->unknown_1h` score `32.7014` n `209` status `ready` deltaP `1.7807` edge `2.8712` maxDD `-9.6361`
- `market_context_high->unknown_4h` score `10.0967` n `204` status `ready` deltaP `-2.989` edge `1.4043` maxDD `-35.7719`
- `market_context_high->unknown_24h` score `8.0038` n `198` status `ready` deltaP `-12.3976` edge `1.153` maxDD `-24.2693`
- `risk_on_high->commodity_24h` score `2.4334` n `40` status `ready` deltaP `4.7297` edge `0.3994` maxDD `-12.9187`
- `risk_on_and_context->commodity_24h` score `2.4334` n `40` status `ready` deltaP `4.7297` edge `0.3994` maxDD `-12.9187`
- `risk_on_high->equity_4h` score `2.2061` n `40` status `ready` deltaP `32.4085` edge `-0.0275` maxDD `-0.044`
- `risk_on_and_context->equity_4h` score `2.2061` n `40` status `ready` deltaP `32.4085` edge `-0.0275` maxDD `-0.044`
- `risk_on_high->crypto_major_4h` score `0.698` n `40` status `ready` deltaP `14.2683` edge `0.0296` maxDD `-2.6576`
- `risk_on_and_context->crypto_major_4h` score `0.698` n `40` status `ready` deltaP `14.2683` edge `0.0296` maxDD `-2.6576`
- `risk_on_high->equity_1h` score `0.1705` n `40` status `ready` deltaP `9.7156` edge `-0.0116` maxDD `-0.7834`
- `risk_on_and_context->equity_1h` score `0.1705` n `40` status `ready` deltaP `9.7156` edge `-0.0116` maxDD `-0.7834`
- `risk_on_high->metal_4h` score `0.1333` n `40` status `ready` deltaP `8.9634` edge `-0.0091` maxDD `-1.3516`
- `risk_on_and_context->metal_4h` score `0.1333` n `40` status `ready` deltaP `8.9634` edge `-0.0091` maxDD `-1.3516`
- `risk_on_high->fx_4h` score `0.0279` n `40` status `ready` deltaP `8.872` edge `0.0035` maxDD `-0.3925`
- `risk_on_and_context->fx_4h` score `0.0279` n `40` status `ready` deltaP `8.872` edge `0.0035` maxDD `-0.3925`
- `risk_on_high->fx_1h` score `0.0085` n `40` status `ready` deltaP `3.503` edge `0.0007` maxDD `-0.1704`
- `risk_on_and_context->fx_1h` score `0.0085` n `40` status `ready` deltaP `3.503` edge `0.0007` maxDD `-0.1704`
- `risk_on_high->crypto_major_1h` score `0.0021` n `40` status `ready` deltaP `8.7126` edge `-0.0036` maxDD `-2.3372`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
