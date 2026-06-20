# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-20T03:37:28.354001+00:00`
- Price records: `672`
- Market context records: `4169`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `10140`

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

- `risk_on_high->unknown_4h` score `144.722` n `40` status `ready` deltaP `-10.1829` edge `12.3099` maxDD `-10.8809`
- `risk_on_and_context->unknown_4h` score `144.722` n `40` status `ready` deltaP `-10.1829` edge `12.3099` maxDD `-10.8809`
- `market_context_high->unknown_1h` score `35.3283` n `202` status `ready` deltaP `0.7914` edge `3.0967` maxDD `-9.6361`
- `market_context_high->unknown_4h` score `9.7229` n `202` status `ready` deltaP `-4.8116` edge `1.3853` maxDD `-35.7719`
- `market_context_high->unknown_24h` score `9.2112` n `198` status `ready` deltaP `-13.3701` edge `1.2601` maxDD `-24.2693`
- `risk_on_high->equity_4h` score `2.1081` n `40` status `ready` deltaP `32.7134` edge `-0.0377` maxDD `-0.044`
- `risk_on_and_context->equity_4h` score `2.1081` n `40` status `ready` deltaP `32.7134` edge `-0.0377` maxDD `-0.044`
- `risk_on_high->commodity_24h` score `1.5415` n `40` status `ready` deltaP `1.9968` edge `0.3433` maxDD `-12.9187`
- `risk_on_and_context->commodity_24h` score `1.5415` n `40` status `ready` deltaP `1.9968` edge `0.3433` maxDD `-12.9187`
- `risk_on_high->crypto_major_4h` score `0.7986` n `40` status `ready` deltaP `15.0305` edge `0.0329` maxDD `-2.6576`
- `risk_on_and_context->crypto_major_4h` score `0.7986` n `40` status `ready` deltaP `15.0305` edge `0.0329` maxDD `-2.6576`
- `risk_on_high->metal_4h` score `0.1549` n `40` status `ready` deltaP `9.5732` edge `-0.0104` maxDD `-1.3516`
- `risk_on_and_context->metal_4h` score `0.1549` n `40` status `ready` deltaP `9.5732` edge `-0.0104` maxDD `-1.3516`
- `risk_on_high->equity_1h` score `0.1237` n `40` status `ready` deltaP `10.015` edge `-0.0175` maxDD `-0.7834`
- `risk_on_and_context->equity_1h` score `0.1237` n `40` status `ready` deltaP `10.015` edge `-0.0175` maxDD `-0.7834`
- `risk_on_high->fx_4h` score `0.0857` n `40` status `ready` deltaP `9.939` edge `0.0038` maxDD `-0.3925`
- `risk_on_and_context->fx_4h` score `0.0857` n `40` status `ready` deltaP `9.939` edge `0.0038` maxDD `-0.3925`
- `risk_on_high->fx_1h` score `0.0575` n `40` status `ready` deltaP `4.4012` edge `0.001` maxDD `-0.1704`
- `risk_on_and_context->fx_1h` score `0.0575` n `40` status `ready` deltaP `4.4012` edge `0.001` maxDD `-0.1704`
- `risk_on_high->crypto_major_1h` score `0.0364` n `40` status `ready` deltaP `9.3114` edge `-0.0032` maxDD `-2.3372`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
