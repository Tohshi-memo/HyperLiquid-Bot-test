# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-29T20:37:24.430361+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11420`

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

- `news_risk_high->unknown_24h` score `28.3334` n `54` status `ready` deltaP `0.868` edge `2.4527` maxDD `-4.1232`
- `market_context_high->unknown_24h` score `11.9239` n `104` status `ready` deltaP `20.9535` edge `0.9272` maxDD `-3.1917`
- `risk_on_high->crypto_alt_4h` score `10.3798` n `39` status `ready` deltaP `39.4387` edge `0.6121` maxDD `-0.1367`
- `risk_on_and_context->crypto_alt_4h` score `10.3798` n `39` status `ready` deltaP `39.4387` edge `0.6121` maxDD `-0.1367`
- `news_risk_high->crypto_alt_24h` score `9.9988` n `54` status `ready` deltaP `27.0255` edge `1.4393` maxDD `-22.3391`
- `risk_on_high->crypto_major_4h` score `7.6421` n `39` status `ready` deltaP `39.4114` edge `0.4017` maxDD `-1.208`
- `risk_on_and_context->crypto_major_4h` score `7.6421` n `39` status `ready` deltaP `39.4114` edge `0.4017` maxDD `-1.208`
- `news_risk_high->unknown_4h` score `6.428` n `63` status `ready` deltaP `5.9064` edge `0.5553` maxDD `-1.7205`
- `market_context_high->metal_24h` score `4.6886` n `104` status `ready` deltaP `34.415` edge `0.2632` maxDD `-3.1535`
- `risk_on_high->metal_4h` score `3.0716` n `39` status `ready` deltaP `33.9236` edge `0.0384` maxDD `-0.0208`
- `risk_on_and_context->metal_4h` score `3.0716` n `39` status `ready` deltaP `33.9236` edge `0.0384` maxDD `-0.0208`
- `news_risk_high->unknown_1h` score `2.6646` n `63` status `ready` deltaP `-2.1979` edge `0.2724` maxDD `-0.8558`
- `market_context_high->unknown_4h` score `1.823` n `139` status `ready` deltaP `16.7891` edge `0.087` maxDD `-1.0945`
- `risk_on_high->equity_4h` score `1.5349` n `39` status `ready` deltaP `12.246` edge `0.0712` maxDD `-0.3281`
- `risk_on_and_context->equity_4h` score `1.5349` n `39` status `ready` deltaP `12.246` edge `0.0712` maxDD `-0.3281`
- `news_risk_high->fx_4h` score `1.4229` n `63` status `ready` deltaP `32.7091` edge `0.0193` maxDD `-0.3953`
- `risk_on_high->metal_1h` score `1.3474` n `49` status `ready` deltaP `18.734` edge `0.0088` maxDD `-0.0463`
- `risk_on_and_context->metal_1h` score `1.3474` n `49` status `ready` deltaP `18.734` edge `0.0088` maxDD `-0.0463`
- `risk_on_high->index_4h` score `0.8883` n `39` status `ready` deltaP `14.9625` edge `0.0052` maxDD `-0.1405`
- `risk_on_and_context->index_4h` score `0.8883` n `39` status `ready` deltaP `14.9625` edge `0.0052` maxDD `-0.1405`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
